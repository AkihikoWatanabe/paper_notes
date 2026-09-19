import requests
import os
from collections import defaultdict, Counter
from itertools import product
import networkx as nx
import re
from tqdm import tqdm
import json
from pathlib import Path
from typing import Callable, Tuple, List


THREAD_PAGE_SIZE = 200
THREAD_VISIBLE_ITEMS = 100
HOME_VISIBLE_ITEMS = 20
SKIPPED_LABELS = {"translation_required", "action_wanted", "Pocket"}

ARCHIVE_COLOR_GROUPS = {
    "media": {"f9d0c4"},
    "venue": {"9cc929"},
    "research": {"0e8a16"},
    "child": {"b60205", "0052cc", "9615c1", "fcf3ba"},
}


def label_slug(label: str) -> str:
    """ラベルを既存のURL規則に合わせたスラッグへ変換する。"""
    slug = label.strip().replace("/", "-").replace(" ", "-")
    return re.sub(r"-+", "-", slug)


def thread_page_filename(label: str, page_number: int = 1) -> str:
    return f"{label_slug(label)}-{page_number}.html"


def chunk_items(items: list[tuple[dict, int]], chunk_size: int = THREAD_PAGE_SIZE):
    for start in range(0, len(items), chunk_size):
        yield items[start:start + chunk_size]


def archive_color_group(color: str) -> str:
    normalized = (color or "").lower().lstrip("#")
    for group, colors in ARCHIVE_COLOR_GROUPS.items():
        if normalized in colors:
            return group
    return "other"


def archive_label_entry(label: str, issue_list: list[tuple[dict, int]]) -> dict:
    issue_ids = {issue.get("number") or issue.get("id") for issue, _ in issue_list}
    page_count = (len(issue_list) + THREAD_PAGE_SIZE - 1) // THREAD_PAGE_SIZE
    return {
        "name": label,
        "url": f"articles/{thread_page_filename(label)}",
        "issue_count": len(issue_ids),
        "page_count": page_count,
    }


def build_archive_hierarchy(
    label_to_issues: dict[str, list[tuple[dict, int]]],
    all_issues: list[dict],
) -> dict:
    label_groups = {}
    research_children = defaultdict(set)

    for issue in all_issues:
        issue_groups = defaultdict(list)
        for label in issue["labels"]:
            name = label["name"]
            issue_groups[archive_color_group(label.get("color"))].append(name)
            label_groups.setdefault(name, archive_color_group(label.get("color")))

        for research_label in issue_groups["research"]:
            research_children[research_label].update(issue_groups["child"])

    entries = {
        label: archive_label_entry(label, issue_list)
        for label, issue_list in label_to_issues.items()
        if label not in SKIPPED_LABELS and issue_list
    }

    media = []
    venues = []
    research_fields = []
    assigned = set()

    for label, entry in entries.items():
        group = label_groups.get(label, "other")
        if group == "media":
            media.append(entry)
            assigned.add(label)
        elif group == "venue":
            venues.append(entry)
            assigned.add(label)

    for label, entry in entries.items():
        if label_groups.get(label) != "research":
            continue

        children = []
        for child_label in sorted(research_children[label], key=str.casefold):
            child_entry = entries.get(child_label)
            if child_entry is not None:
                children.append(child_entry)
                assigned.add(child_label)

        entry = dict(entry)
        entry["children"] = children
        research_fields.append(entry)
        assigned.add(label)

    other = [entry for label, entry in entries.items() if label not in assigned]

    sort_entries = lambda values: sorted(values, key=lambda value: value["name"].casefold())
    media = sort_entries(media)
    venues = sort_entries(venues)
    research_fields = sort_entries(research_fields)
    other = sort_entries(other)

    return {
        "total_page_count": sum(entry["page_count"] for entry in entries.values()),
        "media": media,
        "venues": venues,
        "research_fields": research_fields,
        "other": other,
    }


year_pat = re.compile(r"'(\d{2,4})")
# ![image](https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4268eb3f-349f-4ebe-adeb-2cbfcb7cfe17)
#(https://github.com/user-attachments/assets/
#image_pat = re.compile(r'!\[image\]\((https://(?:github\.com|user-images\.githubusercontent\.com)/AkihikoWatanabe/paper_notes/assets/[^)]+)\)')
image_pat_list = [re.compile(r'!\[image\]\((https://(?:github\.com|user-images\.githubusercontent\.com)/AkihikoWatanabe/paper_notes/assets/[^)]+)\)'),
                  re.compile(r'!\[image\]\((https://user-images\.githubusercontent\.com/[^)]+)\)'),
                  re.compile(r'!\[image\]\((https://github\.com/user-attachments/assets/[^)]+)\)')]

PARENT_COLOR = ['0e8a16', 'ff2550', '533075']
SUB_PARENT_COLOR = ['b60205', "0052cc", "9cc929", "9615c1", "fef2c0"]
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
        issues(states: OPEN, first: 30) {
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
            issues(states: OPEN, first: 30, after: "%s") {
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
    A.draw('./assets/images/knowledge_graph.svg', prog='neato', format='svg')


def get_year(text: str) -> int:
    results = year_pat.findall(text)
    if len(results) == 0:
        year = 0
    else:
        year = int(results[-1])
        if year > 30 and year < 1899:
            year += 1900
        elif year <= 30:
            year += 2000
    return int(year)


def replace_image(match):
    url = match.group(1)
    return f'<img src="{url}" alt="image" loading="lazy" width="550" height="400"/>'
  

def head_replacer(match):
    return f'\n<strong>{match.group(0)}</strong>\n<br>\n'


def issue_link_replacer(match):
    try:
        return f'<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/{match.group(1)}" target="_blank" rel="noopener noreferrer">{issuenum2titles[int(match.group(1))]}</a>\n'
    except KeyError:
        return match.group(0)


image_url_list = [re.compile(r'(https://(?:github\.com|user-images\.githubusercontent\.com)/AkihikoWatanabe/paper_notes/assets/[^)>]+)'),
                  re.compile(r'(https://user-images\.githubusercontent\.com/[^)>]+)'),
                  re.compile(r'(https://github\.com/user-attachments/assets/[^)>]+)')]


def link_replacer(match):
    # マッチした文字列全体を取得
    full_match = match.group(0)
    url = match.group(1)
    
    # imgトークンが含まれている場合はスキップ
    if '__IMG_' in full_match: 
        return full_match
    
    # 画像URLのパターンチェック
    for image_pat in image_url_list:
        m = image_pat.search(full_match)
        if m != None:
            return full_match
    
    return "\n\n{% raw %}\n" + f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>' + "\n{% endraw %}\n\n"

def x_link_replacer(match):
    x_link = match.group(1).replace("x.com", "twitter.com") 
    return  "\n\n{% raw %}\n" + f"""
<div class="tweet-embed" style="min-height:400px; max-width:550px; margin:1em auto;" 
     data-embed='<blockquote class="twitter-tweet"><a href="{x_link}"></a></blockquote>'>
  <div class="tweet-placeholder">Loading…</div>
</div>""" + "\n{% endraw %}\n\n"  



IMG_PATTERN = re.compile(
    r"<img\b[^>]*?>",
    flags=re.IGNORECASE | re.DOTALL,
)


def protect_img_tags(
    text: str,
) -> Tuple[str, List[str]]:
    """
    <img ...> タグをトークンに退避
    """
    imgs = []

    def replacer(match):
        idx = len(imgs)
        imgs.append(match.group(0))
        return f"__IMG_{idx}__"

    protected_text = IMG_PATTERN.sub(replacer, text)
    return protected_text, imgs


def restore_img_tags(
    text: str,
    imgs: List[str],
) -> str:
    """
    トークンを元の <img> タグに復元
    """
    for i, img in enumerate(imgs):
        replaced_img = None
        for image_url_pat in image_url_list:
            m = image_url_pat.search(img)
            if m != None:
                replaced_img = replace_image(m)
        assert replaced_img != None, img
        text = text.replace(f"__IMG_{i}__", replaced_img)
    return text


summ_pat = "Summary (by"
#http_pat = re.compile("https?://(?!((www\.)?(x\.com|twitter\.com)))[^\s/$.?#].[^\s]*\s")
http_pat = re.compile("(https?://(?!((www\.)?(x\.com|twitter\.com|github\.com\/AkihikoWatanabe\/)))[^\s<>]*)\s?")
x_pat = re.compile("(https?://(?:www\.)?(:?x|twitter)\.com[^\s<>]*)\s?")
def get_snippets(issue: dict[str, str]) -> tuple[str, str]:
    summ_text = None
    comm_text = None
    summ_idx = issue["body"].find(summ_pat)
    if summ_idx != -1:
        summ_text = ''.join(issue["body"][summ_idx:].split('\n')[1:]).strip()

    # find summary
    comments = issue["comments"]
    for r in comments:
        summ_idx = r["body"].find(summ_pat)
        if summ_idx != -1:
            summ_text = ''.join(r["body"][summ_idx:].split('\n')[1:]).strip()
    # if cannot find summary
    for r in comments:
        summ_idx = r["body"].find(summ_pat)
        if summ_idx != -1:
            continue
        if comm_text == None:
            comm_text = "<p>" + r['body'].replace("\r", "\n").replace("\n", "<br>") + "</p>"
        else:
            comm_text += "<p>" + r['body'].replace("\r", "\n").replace("\n", "<br>") + "</p>"
    if comm_text != None:
         # 先にMarkdown形式の画像を<img>タグに変換
        for image_pat in image_pat_list:
            comm_text = re.sub(image_pat, replace_image, comm_text)
        
        # すべての<img>タグを保護
        protected, imgs = protect_img_tags(comm_text)
        
        # 他の置換処理
        protected = re.sub(r"#(\d+)", issue_link_replacer, protected)
        protected = re.sub(r'#+\s.*?\n', head_replacer, protected)
        protected = re.sub(http_pat, link_replacer, protected) 
        protected = re.sub(x_pat, x_link_replacer, protected)
        
        comm_text = restore_img_tags(protected, imgs)
        
    if summ_text != None:
        summ_text = summ_text.replace("\r", "\n").replace("\n", "<br>")

    ## extract image url
    #for r in comments:
    #    for image_pat in image_pat_list:
    #        m = image_pat.search(r['body'])
    #        if m != None:
    #            image_url_list.append(m.group(1).replace('\n', '').strip())
    return summ_text, comm_text


def prepro_title(title: str):
    title = title.replace('!', '')
    #title = title.replace('[', '').replace(']', '')
    title = title.replace('(', '（').replace(')', '）')
    title = title.replace('/', '_')
    title = title.replace('\n', '')
    #title = title.replace('"', '')
    #title = title.replace("'", "")
    return title


def find_first_url(text: str) -> str | None:
    """
    テキストから最初に見つかったURLを抽出して返します。

    Args:
        text (str): 検索対象の文字列。

    Returns:
        str | None: 最初に見つかったURL。見つからなかった場合は None。
    """
    # URLを検索するための正規表現パターン
    # http:// または https:// で始まり、その後に続く非空白文字のシーケンスにマッチ
    url_pattern = r'https?://[^\s]+'

    # テキスト内でパターンに最初にマッチする部分を探す
    match = re.search(url_pattern, text)

    # マッチが見つかった場合、その文字列（URL）を返す
    if match:
        return match.group(0)
    else:
        # 見つからなかった場合は None を返す
        return None


def _generate_html_content_list(sorted_issues: list[tuple[dict, int]], current_target: list[str], attach_date: bool, assets_root: str, h_level: str) -> list[str]:
    link_svg = """<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true">
  <path d="M14 3h7v7h-2V6.41l-9.29 9.3-1.42-1.42 9.3-9.29H14V3z"/>
  <path d="M5 5h5V3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-5h-2v5H5V5z"/>
</svg>"""

    _html_content = []
    for (issue, year) in sorted_issues:
        title = prepro_title(issue['title'])
        title_for_anchor = title.replace("[Paper Note]", "").translate(str.maketrans({":": "", "/": "", "?": "", "#": "", "%": ""})).strip()
        anchor_id = "-".join(title_for_anchor.lower().split(",")[0].split(" ")[:2]) + f"-{issue['number']}"

        original_link = find_first_url(text=issue["body"])
        if original_link:
            original_link_text = f'<a href="{original_link}" target="_blank" rel="noopener noreferrer" class="external-link-badge">{link_svg}\nPaper/Blog Link\n</a>'
        else:
            original_link_text = ""
        _html_content.append(f'<article class="paper-entry">')
        _html_content.append(f'<h{h_level} id="{anchor_id}" class="title-link">{title}</h{h_level}><br>{original_link_text}<a href="{issue["url"]}" target="_blank" rel="noopener noreferrer" class="external-link-badge">{link_svg}\nMy Issue\n</a><br>')

        tags = [data['name'] for data in issue['labels']]
        if year == 0:
            t = "Article"
            _html_content.append(f'<a class="button" href="{str(assets_root / thread_page_filename(t))}" target="_blank" rel="noopener noreferrer">#{t}</a>')
        for t in tags:
            if t not in current_target and t not in SKIPPED_LABELS:
                _html_content.append(f'<a class="button" href="{str(assets_root / thread_page_filename(t))}" target="_blank" rel="noopener noreferrer">#{t}</a>')
        #_html_content.append('<br>')
        if attach_date:
            _html_content.append(f'<span class="issue_date">Issue Date: {issue["createdAt"][:issue["createdAt"].find("T")]}</span>')
        snippet_text = None
        image_url = None
        if issue["body"] != None:
            snippet_text, comment_text = get_snippets(issue)
        #_html_content += f'[{issue["title"]}]({issue["url"]})\n\n' 

        if snippet_text != None:
            _html_content.append(f'<span class="snippet"><span>GPT Summary</span>{snippet_text}</span>')
        if comment_text != None:
            _html_content.append(f'<span class="snippet"><span>Comment</span>{comment_text}</span><br><br>')
        
        _html_content.append("</article>")
    return _html_content


def _generate_agentdoc_content_list(sorted_issues: list[tuple[dict, int]]) -> list[str]:

    _agentdoc_content = []
    for (issue, year) in sorted_issues:
        title = prepro_title(issue['title'])
        original_link = find_first_url(text=issue["body"])
        tags = [data['name'] for data in issue['labels']]
        comment_text = None
        if issue["body"] != None:
            snippet_text, comment_text = get_snippets(issue)

        _agentdoc_content.append("<paper-entry>")
        _agentdoc_content.append(f"<title>{title}</title>")
        _agentdoc_content.append(f"<original-paper-blog-link>{original_link}</original-paper-blog-link>")
        _agentdoc_content.append(f'<repo-issue-link>{issue["url"]}</repo-issue-link>')
        _agentdoc_content.append(f'<tags>{", ".join(tags)}</tags>')
        _agentdoc_content.append(f'<repo-issue-date>{issue["createdAt"][:issue["createdAt"].find("T")]}</repo-issue-date>')
        _agentdoc_content.append(f'<issue-body>{issue["body"]}</issue-body>')
        _agentdoc_content.append(f'<maintainer-comment-text>{comment_text}</maintainer-comment-text>')
        _agentdoc_content.append("</paper-entry>\n")
        
    return _agentdoc_content
    
    
curr_more_idx = 0
def gen_one_item(issue_list: list[tuple[dict, int]], current_target: list[str], last_update: str, attach_date: bool = True, assets_root: str = "articles/", h_level: str = "4", visible_num: int = 5) -> dict[str, str]:
    global curr_more_idx

    # start note lazy
    #_html_content = ['<div class="note lazy">']

    assets_root = Path(assets_root) 
    _html_content = ['<div class="visible-content">']
    
    sorted_issues = sorted(issue_list, key=lambda item: (item[1], item[0]["createdAt"]), reverse=True)

    if len(sorted_issues[:visible_num]) > 0:
        _html_content += _generate_html_content_list(sorted_issues[:visible_num], current_target=current_target, attach_date=attach_date, assets_root=assets_root, h_level=h_level)
    _html_content.append('</div>')

    if len(sorted_issues[visible_num:]) > 0:
        remaining_num = len(sorted_issues[visible_num:])
        _html_content.append(
            f'<button class="content-toggle-button" onclick="showMore({curr_more_idx})">'
            f'続きを表示（残り{remaining_num}件）</button>'
        )
        _html_content.append('<div class="hidden-content">')
        _html_content += _generate_html_content_list(sorted_issues[visible_num:], current_target=current_target, attach_date=attach_date, assets_root=assets_root, h_level=h_level)
        _html_content.append(
            f'<button class="content-toggle-button" onclick="hideContent({curr_more_idx})" '
            'style="display: none;">表示を折りたたむ</button>'
        )
        _html_content.append('</div>')
        curr_more_idx += 1

    _agentdoc_content = ['<?xml version="1.0" encoding="UTF-8"?>', f'<paper-list last-updated="{last_update}">']
    _agentdoc_content += _generate_agentdoc_content_list(sorted_issues)
    _agentdoc_content.append("</paper-list>")
    
    gen_result = {}
    gen_result["html_content"] = "\n".join(_html_content)
    gen_result["agentdoc_content"] = "\n".join(_agentdoc_content)
    return gen_result


def _write_thread_redirect(label: str, first_page_filename: str, page_key: str | None = None) -> None:
    """従来の /articles/<label>.html から最初の分割ページへ転送する。"""
    slug = page_key or label_slug(label)
    redirect_content = f"""---
layout: null
permalink: /articles/{slug}.html
---
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=./{first_page_filename}">
  <script>
    window.location.replace("./{first_page_filename}" + window.location.hash);
  </script>
</head>
<body>
  <a href="./{first_page_filename}">{label} を開く</a>
</body>
</html>
"""
    Path("_articles").mkdir(parents=True, exist_ok=True)
    with open(Path("_articles") / f"{slug}.html", "w", encoding="utf-8") as f:
        f.write(redirect_content)


def _thread_navigation(slug: str, page_number: int, page_count: int, position: str) -> str:
    navigation = [
        f'<nav class="thread-pagination thread-pagination-{position}" '
        'data-pagefind-ignore aria-label="Thread navigation">'
    ]
    if page_number > 1:
        navigation.append(
            f'<a class="thread-pagination-previous" '
            f'href="{slug}-{page_number - 1}.html">← 前のスレッド</a>'
        )
    else:
        navigation.append('<span class="thread-pagination-placeholder"></span>')

    navigation.append(
        f'<span class="thread-pagination-status">スレッド {page_number} / {page_count}</span>'
    )

    if page_number < page_count:
        navigation.append(
            f'<a class="thread-pagination-next" '
            f'href="{slug}-{page_number + 1}.html">次のスレッド →</a>'
        )
    else:
        navigation.append('<span class="thread-pagination-placeholder"></span>')

    navigation.append('</nav>')
    return "\n".join(navigation)


def _write_thread_pages(
    label: str,
    issue_list: list[tuple[dict, int]],
    lazy_loading: str,
    current_target: list[str] | None = None,
    agentdoc_filename: str | None = None,
    page_key: str | None = None,
    display_label: str | None = None,
) -> str | None:
    """ラベルに属するIssueを日付順のスレッドページへ分割して生成する。"""
    global curr_more_idx

    sorted_issues = sorted(issue_list, key=lambda item: (item[1], item[0]["createdAt"]), reverse=True)
    if not sorted_issues:
        return None

    target_labels = current_target if current_target is not None else [label]
    pages = list(chunk_items(sorted_issues))
    page_count = len(pages)
    slug = page_key or label_slug(label)
    display_label = display_label or label
    page_title = f"{display_label}に関する論文・技術記事メモの一覧"
    latest_date = sorted(issue[0]["createdAt"][:10] for issue in sorted_issues)[-1]

    Path("_articles").mkdir(parents=True, exist_ok=True)
    for page_number, page_issues in enumerate(pages, start=1):
        curr_more_idx = 0
        page_filename = f"{slug}-{page_number}.html"
        html_content = (
            f'<h2 id="{slug}" class="paper-head">{display_label} '
            f'({len(sorted_issues)}) — {page_number}/{page_count}</h2>'
        )
        html_content += _thread_navigation(slug, page_number, page_count, "top")
        gen_result = gen_one_item(
            page_issues,
            target_labels,
            latest_date,
            assets_root="",
            h_level="3",
            visible_num=min(THREAD_VISIBLE_ITEMS, len(page_issues)),
        )
        html_content += gen_result["html_content"]
        html_content += _thread_navigation(slug, page_number, page_count, "bottom")

        escaped_title = page_title.replace('"', '\\"')
        escaped_category = label.replace('"', '\\"')
        html_template = f"""---
layout: post
title: "{escaped_title}"
author: AkihikoWATANABE
date: {latest_date}
categories: {label}
thread_category: "{escaped_category}"
permalink: /articles/{page_filename}
thread_page: true
thread_page_number: {page_number}
---
"""
        with open(Path("_articles") / page_filename, "w", encoding="utf-8") as f:
            f.write(f"{html_template}{html_content}{lazy_loading}")

    if agentdoc_filename is not None:
        agentdoc_content = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<paper-list last-updated="{latest_date}">',
        ]
        agentdoc_content += _generate_agentdoc_content_list(sorted_issues)
        agentdoc_content.append("</paper-list>")
        with open(Path("agent_docs") / agentdoc_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(agentdoc_content))

    _write_thread_redirect(label, f"{slug}-1.html", page_key=slug)
    return f"{slug}-1.html"


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

    # update parent
    parent_labels = set(parent_labels)
    for issue in all_issues:
        labels = issue["labels"]
        extracted = [l['name'] for l in labels if l['color'].lower() in PARENT_COLOR]
        [parent_labels.add(l) for l in extracted]
    parent_labels = list(parent_labels)

    # update sub parent
    sub_parent_labels = set(sub_parent_labels)
    for issue in all_issues:
        labels = issue["labels"]
        extracted = [l['name'] for l in labels if l['color'].lower() in SUB_PARENT_COLOR]
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
    #generate_graph(parent_labels, sub_parent_labels, edges, label_weights, label_to_hierarchy)
    print("finish")

    print("Start to decoding as html ...")
    html_template = """---
layout: post
title: 論文や技術メモの一覧（随時更新）
author: AkihikoWATANABE
thread_page: true
---
"""

    # 階層構造のデータを基にHTMLを生成
    html_content = ''

    # head message
    html_content += '<h2>本ブログについて</h2>'
    html_content += '本ブログは特定のトピックに関する論文メモをスレッド形式で流し見することを想定して作成しています。トピックとスレッドの一覧は<a href="https://akihikowatanabe.github.io/paper_notes/archives.html" target="_blank" rel="noopener noreferrer">アーカイブページ</a>をご参照ください。'
    html_content += '''
最近特に収集しているトピックとしては下記のようなものがあります:
<ul>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/LanguageModel.html" target="_blank" rel="noopener noreferrer">（大規模）言語モデル (Large Language Models)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/VisionLanguageModel.html" target="_blank" rel="noopener noreferrer">視覚言語モデル (Vision Language Models)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/DiffusionModel.html" target="_blank" rel="noopener noreferrer">拡散モデル (Diffusion Models)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Prompting.html" target="_blank" rel="noopener noreferrer">LLMにおけるプロンプティング (Prompting)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Pretraining.html" target="_blank" rel="noopener noreferrer">事前学習 (Pre-training)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/mid-training.html" target="_blank" rel="noopener noreferrer">中間学習 (Mid-training)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/PostTraining.html" target="_blank" rel="noopener noreferrer">事後学習 (Post-training)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/ReinforcementLearning.html" target="_blank" rel="noopener noreferrer">（主にLLMの事後学習で応用される）強化学習 (Reinforcement Learning)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/OpenWeight.html" target="_blank" rel="noopener noreferrer">OpenWeightモデル</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Transformer.html" target="_blank" rel="noopener noreferrer">Transformerアーキテクチャ関連</a> / <a href="https://akihikowatanabe.github.io/paper_notes/articles/Attention.html" target="_blank" rel="noopener noreferrer">Attention関連</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Test-Time-Scaling.html" target="_blank" rel="noopener noreferrer">Test-time Scaling</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Test-time-Learning.html" target="_blank" rel="noopener noreferrer">(Memory-based) Test-time Learning</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Test-Time-Training-(TTT).html" target="_blank" rel="noopener noreferrer">Test Time Training (TTT)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Alignment.html" target="_blank" rel="noopener noreferrer">（大規模言語モデルにおける）アライメント</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/AIAgents.html" target="_blank" rel="noopener noreferrer">AI Agent全般</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/memory.html" target="_blank" rel="noopener noreferrer">AI Agentにおけるメモリ</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/ContextEngineering.html" target="_blank" rel="noopener noreferrer">Context Engineering</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Evaluation.html" target="_blank" rel="noopener noreferrer">様々な分野・タスクでの評価</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Dataset.html" target="_blank" rel="noopener noreferrer">様々な分野・タスクでのデータセット</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/SyntheticData.html" target="_blank" rel="noopener noreferrer">合成データ (Synthetic Data)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Scaling-Laws.html" target="_blank" rel="noopener noreferrer">スケーリング則 (Scaling Laws)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/SelfImprovement.html" target="_blank" rel="noopener noreferrer">Self-Improving (LLM)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/SelfCorrection.html" target="_blank" rel="noopener noreferrer">Self-Correction (LLM)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/MultiModal.html" target="_blank" rel="noopener noreferrer">マルチモーダル (Multimodal)</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Chain-of-Thought.html" target="_blank" rel="noopener noreferrer">Chain-of-Thought</a> / <a href="https://akihikowatanabe.github.io/paper_notes/articles/Reasoning.html" target="_blank" rel="noopener noreferrer">Reasoning</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Tutorial.html" target="_blank" rel="noopener noreferrer">様々な分野・タスクのチュートリアル</a> / <a href="https://akihikowatanabe.github.io/paper_notes/articles/Survey.html" target="_blank" rel="noopener noreferrer">サーベイ</a></li>
</ul>
'''
    html_content += '特定の論文（やトピックの組み合わせ）に関して検索したい場合はこちらの<a href="https://github.com/AkihikoWatanabe/paper_notes/issues" target="_blank" rel="noopener noreferrer">Github Issue</a>から検索できます。'
    html_content += '''
自分の言葉でメモを残した場合や、SNS上の著者による解説等をメモに残した場合、以下の粒度に応じてラベル付けし整理しています。もしご興味があれば以下からご参照ください。
<ul>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Initial-Impression-Notes.html" target="_blank" rel="noopener noreferrer">Initial Impression Notes: Abstract, 関連ポスト, 論文をななめ読みをした後の第一印象</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/One-Line-Notes.html#One-Line" target="_blank" rel="noopener noreferrer">One-Line Notes: 一言メモ</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Surface-level-Notes.html" target="_blank" rel="noopener noreferrer">Surface-level Notes: 論文全体の要約</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/KeyPoint-Notes.html" target="_blank" rel="noopener noreferrer">KeyPoint Notes: 論文のキーとなるポイントのまとめ</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Reading-Reflections.html" target="_blank" rel="noopener noreferrer">Reading Reflections: （読了後、あるいはskim reading後の）感想、意見</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/In-Depth-Notes.html" target="_blank" rel="noopener noreferrer">In-Depth Notes: 論文の詳細と個人的な感想や意見</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Reference-Collection.html">Reference Collection: SNS上の有識者の解説ポスト等の関連リンク集</a></li>
  <li><a href="https://akihikowatanabe.github.io/paper_notes/articles/Author-Thread-Post.html">Author Thread-Post: 論文・ブログ等の著者自身による解説ポスト</a></li>
</ul>
'''
    html_content += '以下、直近100個の論文メモ (Latest Posts) と、管理人が収集する中で重要だと感じた論文/ブログ等の一覧 (<a href="https://akihikowatanabe.github.io/paper_notes/articles/Selected-Papers-Blogs-1.html">Selected Papers/Blogs</a>) です。'

    # latest posts
    #html_content += '## Latest Posts\n\n'
    html_content += '<h2 id="latest-post" class="paper-head">Latest Posts (100)</h2>'
    latest_issues = sorted(all_issues, key=lambda x: x["createdAt"], reverse=True)[:100]
    latest_issues = [(issue, issue["number"]) for issue in latest_issues]
    latest_date = sorted([issue[0]["createdAt"].split("T")[0] for issue in latest_issues], reverse=True)[0]
    html_content += '<p><a class="thread-index-link" href="articles/latest-posts-1.html">Latest Postsをスレッドページで読む</a></p>'
    gen_result = gen_one_item(
        latest_issues,
        [],
        latest_date,
        h_level="3",
        visible_num=HOME_VISIBLE_ITEMS,
    )
    html_content += gen_result["html_content"]

    # Admin's Pick
    selected_issues = [issue for issue in all_issues if any(["Selected Papers/Blogs" == l["name"] for l in issue["labels"]])]
    selected_issues = sorted(
        selected_issues,
        key=lambda issue: (get_year(issue["title"]), issue["createdAt"]),
        reverse=True,
    )
    selected_issues = [(issue, get_year(issue["title"])) for issue in selected_issues]
    html_content += f'<h2 id="selected-papers" class="paper-head">Selected Papers/Blogs ({len(selected_issues)})</h2>'
    html_content += f'<p><a class="thread-index-link" href="articles/Selected-Papers-Blogs-1.html">Selected Papers/Blogs ({len(selected_issues)})をスレッドページで読む</a></p>'
    if selected_issues:
        selected_latest_date = sorted(
            [issue[0]["createdAt"].split("T")[0] for issue in selected_issues],
            reverse=True,
        )[0]
        gen_result = gen_one_item(
            selected_issues,
            [],
            selected_latest_date,
            h_level="3",
            visible_num=HOME_VISIBLE_ITEMS,
        )
        html_content += gen_result["html_content"]
    html_content += "<hr>\n\n"

    print("main part was finished.")

    html_content += '<hr>\n\n'
    lazy_loading = """
<script>
document.addEventListener("DOMContentLoaded", function() {
  // Twitterのwidgets.jsを動的に一度だけ読み込む関数
  let twitterScriptLoaded = false;
  function loadTwitterScript() {
    if (!twitterScriptLoaded) {
      const script = document.createElement('script');
      script.src = "https://platform.twitter.com/widgets.js";
      script.charset = "utf-8";
      script.async = true;
      document.body.appendChild(script);
      twitterScriptLoaded = true;
    }
  }

  // Intersection Observerの設定
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // 画面に入った時だけスクリプトをロード開始
        loadTwitterScript();

        const container = entry.target;
        const embedHtml = container.getAttribute('data-embed');
        
        if (embedHtml) {
          container.innerHTML = embedHtml;
          container.removeAttribute('data-embed');
          
          // ウィジェットの再スキャン（twttrオブジェクトが準備できていれば実行）
          if (window.twttr && window.twttr.widgets) {
            window.twttr.widgets.load(container);
          }
        }
        obs.unobserve(container);
      }
    });
  }, { rootMargin: '200px', threshold: 0.01 }); // 少し早めに読み込む

    document.querySelectorAll('.tweet-embed').forEach(el => observer.observe(el));
});
</script>
"""

    os.makedirs('./_articles', exist_ok=True)
    os.makedirs('./agent_docs', exist_ok=True)
    _write_thread_pages(
        "latest-posts",
        latest_issues,
        lazy_loading,
        current_target=[],
        agentdoc_filename="latest-posts.xml",
        page_key="latest-posts",
        display_label="Latest Posts",
    )
    _write_thread_pages(
        "Selected Papers/Blogs",
        selected_issues,
        lazy_loading,
        current_target=["Selected Papers/Blogs"],
        agentdoc_filename="selected-papers-and-blogs.xml",
    )

    home_content = f'{html_template}{html_content}{lazy_loading}'

    #with open("./index.markdown", "w") as f:
    with open("./index.html", "w") as f:
        f.write(home_content)
    print("finished")

    print("Start to make label pages ...")
    # generate each label as date-ordered thread pages
    label_count = {}
    for i, (label, issue_list) in enumerate(label_to_issues.items()):
        if label in SKIPPED_LABELS:
            continue

        _write_thread_pages(
            label,
            issue_list,
            lazy_loading,
            current_target=[label],
            agentdoc_filename=f"{label.replace('/', '-')}.xml",
        )

        label_count[label] = len(issue_list)

    archive_issue_lists = dict(label_to_issues)
    archive_issue_lists["latest-posts"] = latest_issues
    archive_issue_lists["Selected Papers/Blogs"] = selected_issues
    archive_hierarchy = build_archive_hierarchy(archive_issue_lists, all_issues)
    with open("./_data/archive_hierarchy.json", "w", encoding="utf-8") as f:
        json.dump(archive_hierarchy, f, ensure_ascii=False, indent=2)

    with open("./_data/category_counts.yml", "w") as f:
        for l, c in label_count.items():
            f.write(f"{l}: {c}\n")
    print("finished")


if __name__ == '__main__':
    all_issues = get_all_issues()
    issuenum2titles = {issue["number"]: issue["title"] for issue in all_issues}
    main()


























