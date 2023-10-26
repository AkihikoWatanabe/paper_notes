import requests
import os
from collections import defaultdict, Counter
from itertools import product
import networkx as nx
import re
from tqdm import tqdm
import json


year_pat = re.compile(r"(\d{2,4})")
image_pat = re.compile(r'!\[image\]\((https://github\.com/AkihikoWatanabe/paper_notes/assets/[^)]+)\)')


PARENT_COLOR = '0e8a16'
SUB_PARENT_COLOR = 'b60205'
OTHER_COLOR = 'd65b26'


NODE_SCALE = 1.5


TOKEN = os.environ["TOKEN"]
REPO_OWNER = "AkihikoWatanabe"
REPO_NAME = "paper_notes"
headers = {
    "Authorization": f"bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_all_issues():

    # GraphQL query to fetch open issues
    query = """
    {
      repository(owner: "%s", name: "%s") {
        issues(states: OPEN, first: 100) {
          edges {
            node {
              number
              title
              body
              url
              createdAt
              labels(first: 50) {
                edges {
                  node {
                    name
                    color
                  }
                }
              }
              comments(first: 100) {
                edges {
                  node {
                    body
                    author {
                      login
                    }
                  }
                }
              }
            }
          }
          pageInfo {
            endCursor
            hasNextPage
          }
        }
      }
    }
    """ % (REPO_OWNER, REPO_NAME)

    all_issues = []
    print("Start to fetch issues...")

    # First query execution
    response = requests.post("https://api.github.com/graphql", headers=headers, data=json.dumps({"query": query}))
    response_data = response.json()
    issues_data = response_data['data']['repository']['issues']

    for edge in issues_data['edges']:
       issue = edge['node']
       issue['labels'] = [{'name': label_edge['node']['name'], 'color': label_edge['node']['color']} for label_edge in issue['labels']['edges']]
       issue['comments'] = [{'body': comment_edge['node']['body'], 'author': comment_edge['node']['author']['login']} for comment_edge in issue['comments']['edges']]
       all_issues.append(issue)
    
    end_cursor = issues_data['pageInfo']['endCursor']
    has_next_page = issues_data['pageInfo']['hasNextPage']

    # If there are more issues to fetch
    while has_next_page:
        # Query to fetch the next set of issues using endCursor for pagination
        paginated_query = """
        {
          repository(owner: "%s", name: "%s") {
            issues(states: OPEN, first: 100, after: "%s") {
              edges {
                node {
                  number
                  title
                  body
                  url
                  createdAt
                  labels(first: 50) {
                    edges {
                      node {
                        name
                        color
                      }
                    }
                  }
                  comments(first: 100) {
                    edges {
                      node {
                        body
                        author {
                          login
                        }
                      }
                    }
                  }
                }
              }
              pageInfo {
                endCursor
                hasNextPage
              }
            }
          }
        }
        """ % (REPO_OWNER, REPO_NAME, end_cursor)

        response = requests.post("https://api.github.com/graphql", headers=headers, data=json.dumps({"query": paginated_query}))
        response_data = response.json()
        issues_data = response_data['data']['repository']['issues']

        for edge in issues_data['edges']:
            issue = edge['node']
            issue['labels'] = [{'name': label_edge['node']['name'], 'color': label_edge['node']['color']} for label_edge in issue['labels']['edges']]
            issue['comments'] = [{'body': comment_edge['node']['body'], 'author': comment_edge['node']['author']['login']} for comment_edge in issue['comments']['edges']]
            all_issues.append(issue)

        end_cursor = issues_data['pageInfo']['endCursor']
        has_next_page = issues_data['pageInfo']['hasNextPage']

    print(f"Fetched {len(all_issues)} issues.")
    return all_issues


def generate_graph(parent_labels: list[str],
                   sub_parent_labels: list[str],
                   edges: list[tuple[str, str]],
                   label_weights: dict[str, int],
                   label_to_hierarchy: dict[str, dict[str, list[str]]]):
    # グラフの作成
    G = nx.Graph(strict=True, directed=False)

    # ノードの追加
    nodes = [p for p, _ in label_to_hierarchy.items()]
    nodes += [sp for _, sub_parent_dict in label_to_hierarchy.items() for sp, _ in sub_parent_dict.items()]
    #nodes = [l for l in label_weights.keys()]
    G.add_nodes_from(nodes)

    # エッジの追加
    G.add_edges_from(edges)

    # ノードの色と大きさを指定
    colors = {n: '#' + PARENT_COLOR.upper() if n in parent_labels else
              '#' + SUB_PARENT_COLOR.upper() if n in sub_parent_labels else
              '#' + OTHER_COLOR for n in nodes}
    min_value = min(label_weights.values())
    max_value = max(label_weights.values())
    sizes = {l: int((w - min_value)/(max_value - min_value) * NODE_SCALE) for l, w in label_weights.items()}

    for node in G.nodes():
        G.nodes[node]['fillcolor'] = colors[node]
        G.nodes[node]['fontcolor'] = "#FFFFFF"
        G.nodes[node]['style'] = "filled"
        G.nodes[node]['width'] = sizes[node]
        G.nodes[node]['height'] = sizes[node]
        G.nodes[node]['fontsize'] = 12

    # NetworkXのグラフをPyGraphvizのAgraphオブジェクトに変換
    A = nx.nx_agraph.to_agraph(G)
    A.graph_attr['overlap'] = 'false'
    A.graph_attr['splines'] = 'true'

    # PyGraphvizでグラフ描画の設定
    A.layout(prog='neato')  
    A.draw('./blog/assets/images/knowledge_graph.svg', prog='neato', format='svg')


def get_year(text: str) -> int:
    m = year_pat.search(text)
    if m == None:
        year = 0
    else:
        year = int(m.group(1))
        if year > 30 and year < 1899:
            year += 1900
        elif year <= 30:
            year += 2000
    return int(year)


summ_pat = "Summary (by gpt-3.5-turbo)"
http_pat = re.compile("^https?://[^\s/$.?#].[^\s]*$")
def get_snippets(issue: dict[str, str]) -> tuple[str, str]:
    summ_text = None
    image_url = None
    summ_idx = issue["body"].find(summ_pat)
    if summ_idx != -1:
        summ_text = ''.join(issue["body"][summ_idx:].split('\n')[1:]).strip('-')[:150].replace('\n', '').replace('- ', "").strip()

    # find summary
    comments = issue["comments"]
    for r in comments:
        summ_idx = r["body"].find(summ_pat)
        if summ_idx != -1:
            summ_text = ''.join(r["body"][summ_idx:].split('\n')[1:]).strip('-')[:150].replace('\n', '').replace('- ', "").strip()
    # if cannot find summary
    if summ_text == None:
        for r in comments:
            m = http_pat.search(r['body'])
            if m != None:
                continue
            summ_text = re.sub(image_pat, '', r['body'])[:150].replace('\n', '').replace('- ', "").strip()
    # extract image url
    for r in comments:
        m = image_pat.search(r['body'])
        if m != None:
            image_url = m.group(1).replace('\n', '').strip()
            break

    return summ_text, image_url


def prepro_title(title: str):
    title = title.replace('!', '')
    title = title.replace('[', '').replace(']', '')
    title = title.replace('(', '（').replace(')', '）')
    title = title.replace('/', '_')
    title = title.replace('\n', '')
    title = title.replace('"', '')
    title = title.replace("'", "")
    return title


curr_more_idx = 0
VISIBLE_NUM = 3 
def gen_one_item(issue_list: list[tuple[dict, int]], current_target: list[str], attach_date: bool = True) -> str:
    global curr_more_idx
    _html_content = '<div class="visible-content">\n'
    sorted_issues = sorted(issue_list, key=lambda item: item[1], reverse=True)
    for (issue, year) in sorted_issues[:VISIBLE_NUM]:
        title = prepro_title(issue['title'])
        tags = [data['name'] for data in issue['labels']]
        if year == 0:
            t = "Article"
            _html_content += f'<a class="button" href="articles/{t.replace("/", "_")}.html">#{t}</a>'
        for t in tags: 
            if t not in current_target and t not in ["translation_required", "action_wanted", "Pocket"]:
                _html_content += f'<a class="button" href="articles/{t.replace("/", "_")}.html">#{t}</a>'
        _html_content += '<br>'
        if attach_date:
            _html_content += f'<span class="issue_date">Issue Date: {issue["createdAt"][:issue["createdAt"].find("T")]}</span>\n'
        snippet_text = None
        image_url = None
        if issue["body"] != None:
            snippet_text, image_url = get_snippets(issue)
        if snippet_text == None:
            snippet_text = 'No description'
        #_html_content += f'[{issue["title"]}]({issue["url"]})\n\n'
        _html_content += f'<a href="{issue["url"]}">{title}</a>\n' 
        _html_content += f'<span class="snippet">{snippet_text} ...</span>\n'
        if image_url != None:
            #_html_content += f'![{issue["title"]}]({image_url})\n'
            _html_content += f'<img src="{image_url}" alt="image">'
    _html_content += '</div>\n'
    if len(sorted_issues[VISIBLE_NUM:]) > 0:
        _html_content += f'<button onclick="showMore({curr_more_idx})">more</button>\n\n'
        _html_content += '<div class="hidden-content">\n'
        for (issue, year) in sorted_issues[VISIBLE_NUM:]:
            title = prepro_title(issue['title'])
            tags = [data['name'] for data in issue['labels']]
            if year == 0:
                t = "Article"
                _html_content += f'<a class="button" href="articles/{t.replace("/", "_")}.html">#{t}</a>'
            for t in tags:
                if t not in current_target and t not in ["translation_required", "action_wanted", "Pocket"]:
                    _html_content += f'<a class="button" href="articles/{t}.html">#{t}</a>'
            _html_content += '<br>'
            if attach_date:
                _html_content += f'<span class="issue_date">Issue Date: {issue["createdAt"][:issue["createdAt"].find("T")]}</span>\n'
            snippet_text = None
            image_url = None
            if issue["body"] != None:
                snippet_text, image_url = get_snippets(issue)
            if snippet_text == None:
                snippet_text = 'No description'
            #_html_content += f'[{issue["title"]}]({issue["url"]})\n' 
            _html_content += f'<a href="{issue["url"]}">{title}</a>\n' 
            _html_content += f'<span class="snippet">{snippet_text} ...</span>\n'
            if image_url != None:
                #_html_content += f'![{issue["title"]}]({image_url})\n'
                _html_content += f'<img src="{image_url}" alt="image">'
        _html_content += f'<button onclick="hideContent({curr_more_idx})" style="display: none;">hide</button>\n'
        _html_content += "</div>\n" 
        curr_more_idx += 1
    return _html_content


def main():
    parent_labels = ['NLP',
                     'AdaptiveLearning',
                     'AudioProcessing',
                     'ComputerVision',
                     'EducationalDataMining',
                     'HumanComputerInteraction',
                     'InformationRetrieval',
                     'LearningAnalytics',
                     'MachineLearning',
                     'Mindset',
                     'RecommenderSystems',
                     'Spoken Language Processing',
                     'Survey',
                     "Dataset",
                     'Tutorial',
                     'UserModeling',
                     "Education",
                     "Evaluation",
                     "Infrastructure",
                     "Article"]
    sub_parent_labels = ["AffectDetection",
                         "Alignment",
                         "Assessment",
                         "ChatGPT",
                         "CodeGeneration",
                         "CollaborativeFiltering",
                         "CommentGenertion",
                         "ContrastiveLearning",
                         "CTRPrediction",
                         "CurriculumGeneration",
                         "CVRPrediction",
                         "DataAugmentation",
                         "DataDistillation",
                         "DataGeneration",
                         "DataToText",
                         "ConceptToText",
                         "DialogueGeneration",
                         "DocumentSummarization",
                         "DropoutPrediction",
                         "EssayScoring",
                         "FactorizationMachines",
                         "Finetuning",
                         "FoundationModel",
                         "GenerativeAI",
                         "ImageCaptioning",
                         "ImageSegmentation",
                         "Information Extraction",
                         "InteractivePersonalizedSummarization",
                         "InteractiveRecommenderSystems",
                         "IRT",
                         "KnowledgeTracing",
                         "LanguageModel",
                         "LLMAgent",
                         "MatrixFactorization",
                         "NaturalLanguageGeneration",
                         "Navigation",
                         "NeuralArchitectureSearch",
                         "NewsRecommendation",
                         "NumericReasoning",
                         "OnlineEvaluation",
                         "OpinionMining",
                         "OptionTracing",
                         "PersonalizedDocumentSummarization",
                         "PersonalizedGeneration",
                         "PersonalizedHeadlineGeneration",
                         "Planning",
                         "Poisoning",
                         "PromptTuning",
                         "Pruning",
                         "Quantization",
                         "QueryClassification",
                         "QuestionAnswering",
                         "RelevanceJudgment",
                         "RepresentationLearning",
                         "RetrievalAugmentation",
                         "ReviewGeneration",
                         "ScorePrediction",
                         "SemanticTextualSimilarity",
                         "SentenceCompression",
                         "SentimentAnalysis",
                         "SpokenLanguageGeneration",
                         "StudentPerformancePrediction",
                         "TimeSeriesDataProcessing",
                         "WebSearch",
                         "MLOps",
                         "AWS",
                         "Survey",
                         "Tutorial",
                         "Tool",
                         "Library",
                         "Dataset"] 
    all_issues = get_all_issues()
    # update parent
    parent_labels = set(parent_labels)
    for issue in all_issues:
        labels = issue["labels"]
        extracted = [l['name'] for l in labels if l['color'] == PARENT_COLOR]
        [parent_labels.add(l) for l in extracted]
    parent_labels = list(parent_labels)

    # update sub parent
    sub_parent_labels = set(sub_parent_labels)
    for issue in all_issues:
        labels = issue["labels"]
        extracted = [l['name'] for l in labels if l['color'] == SUB_PARENT_COLOR]
        [sub_parent_labels.add(l) for l in extracted]
    sub_parent_labels = list(sub_parent_labels)

    # ラベルの階層構造を解析
    label_to_issues = defaultdict(list)
    label_to_hierarchy = defaultdict(lambda: defaultdict(list))
    label_count = defaultdict(lambda: 0)
    order_label_count = defaultdict(lambda: 0)
    pockets = []
    edges = []
    label_weights = Counter()
    print("Start to making hierarchy...")
    for issue in all_issues:
        year = get_year(issue["title"])
        labels = issue["labels"]

        [label_to_issues[l["name"]].append((issue, year)) for l in labels]

        parents = [l['name'] for l in labels if l['name'] in parent_labels]
        # yearが抽出できない場合はArticleとみなす
        if year == 0:
            parents += ['Article']
        sub_parents = [l['name'] for l in labels if l['name'] in sub_parent_labels]

        if len(labels) == 1 and labels[0]["name"] == "Pocket":
            pockets.append((issue, year))
            label_count[("Pocket")] += 1
            continue

        if len(parents) == 0:
            parents = ["Others"]
        if len(sub_parents) == 0:
            sub_parents = ["Others"]

        for p, sp in product(parents, sub_parents):
            label_to_hierarchy[p][sp].append((issue, year))
            label_count[(p, sp)] += 1
            if p != "Others" and sp != "Others":
                order_label_count[(p, sp)] += 1
        for p in parents:
            label_count[(p)] += 1
            if p != "Others":
                order_label_count[(p)] += 1

        # add edge
        all_labels = [l['name'] for l in labels]
        rest_labels = set(all_labels) - set(parents) - set(sub_parents)
        edge_target = [parents, sub_parents]
        if len(rest_labels) > 0:
            edge_target.append(list(rest_labels))
        edges += [(p, sp) for p, sp in product(parents, sub_parents)]
        #edges += [(sp, r) for sp, r in product(sub_parents, rest_labels)]
        #label_weights += Counter(all_labels)
        label_weights += Counter(parents + sub_parents)

    print("finished")

    print("Start to making graph ...")
    edges = list(set(edges))
    label_to_hierarchy = dict(label_to_hierarchy)
    generate_graph(parent_labels, sub_parent_labels, edges, label_weights, label_to_hierarchy)
    print("finish")

    print("Start to decoding as html ...")
    html_template = """---
layout: post
title: 論文や技術メモの一覧（随時更新）
author: AkihikoWATANABE
---
"""

    # 階層構造のデータを基にHTMLを生成
    html_content = ''

    # latest posts
    html_content += "## Latest Posts\n"
    latest_issues = sorted(all_issues, key=lambda x: x["number"], reverse=True)[:10]
    latest_issues = [(issue, issue["number"]) for issue in latest_issues]
    html_content += gen_one_item(latest_issues, [])

    # list up
    N = len(label_to_hierarchy.items())
    for parent, sub_parents in tqdm(sorted(label_to_hierarchy.items(), key=lambda item: order_label_count[(item[0])], reverse=True), total=N):
        html_content += f"## {parent} ({label_count[(parent)]})\n"
        for sub_parent, issue_list in sorted(sub_parents.items(), key=lambda item: order_label_count[(parent, item[0])], reverse=True):
            html_content += f"### {sub_parent} ({label_count[(parent, sub_parent)]})\n"
            current_target = [parent, sub_parent]
            html_content += gen_one_item(issue_list, current_target)
        html_content += "<hr>\n"

    print("main part was finished.")

    html_content += f'## Pocket ({label_count["Pocket"]})\n'
    html_content += gen_one_item(pockets, ["Pocket"])

    #graph
    html_content += "## 各ラベルの量と関係性の可視化 β\n"
    html_content += "各Issueに付与した主要ラベルの付与回数の合計値によってノードの大きさを決め、ラベル同士の共起関係からエッジを張り作成したグラフです！\n"
    html_content += "なんか見辛いしよくわからない...笑 クリックしてドラッグで視点を移動できます。\n"
    html_content += "{% raw %}"
    html_content += '<svg></svg>'
    html_content += '<div id="svgContainer"></div>'
    html_content += """<script>
    // d3.selectを使ってプレースホルダーを選択
    const container = d3.select("#svgContainer");
    const svg = container.append("svg");
    const width = 647;
    const height = window.innerHeight;

    svg.attr("width", width).attr("height", height);

    const g = svg.append("g");

    d3.xml("assets/images/knowledge_graph.svg").then(data => {
        g.node().append(data.documentElement);
    });

    const zoom = d3.zoom()
        .on("zoom", () => {
            g.attr("transform", d3.event.transform);
        });

    svg.call(zoom);
</script>
"""
    html_content += "{% endraw %}\n"
    html_content += '<hr>\n'

    home_content = f"{html_template}{html_content}\n"

    with open("./index.markdown", "w") as f:
        f.write(home_content)
    print("finished")

    print("Start to make label pages ...")
    # generate each labels pages
    for label, issue_list in label_to_issues.items():
        html_template = f"""---
layout: post
title: {label}に関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
"""
        global curr_more_idx
        curr_more_idx = 0
        html_content = f"## {label}\n"
        html_content += gen_one_item(issue_list, [label])
        label_content = f"{html_template}{html_content}"
        with open(f"./_articles/{label.replace('/', '_')}.markdown", "w") as f:
            f.write(label_content)
    print("finished")


if __name__ == '__main__':
    main()