import os
from github import Github
import feedparser
import openai
import json


openai.api_key = os.environ["OPENAI_API_KEY"]
github_token = os.environ["TOKEN"]
repo_name = os.environ["GITHUB_REPOSITORY"]
event_path = os.environ["GITHUB_EVENT_PATH"]

translator_system_content = ["あなたは自然言語処理や機械学習の研究者です。英語のabstractを日本語に翻訳してください。\n",
                  "abstract1:",
                  "Table-based reasoning has shown remarkable progress in combining deep models with discrete reasoning, which requires reasoning over both free-form natural language (NL) questions and structured tabular data.",
                  "However, previous table-based reasoning solutions usually suffer from significant performance degradation on huge evidence (tables).",
                  "In addition, most existing methods struggle to reason over complex questions since the required information is scattered in different places.",
                  "To alleviate the above challenges, we exploit large language models (LLMs) as decomposers for effective table-based reasoning, which (i) decompose huge evidence (a huge table) into sub-evidence (a small table) to mitigate the interference of useless information for table reasoning;",
                  "and (ii) decompose complex questions into simpler sub-questions for text reasoning.",
                  "Specifically, we first use the LLMs to break down the evidence (tables) involved in the current question, retaining the relevant evidence and excluding the remaining irrelevant evidence from the huge table.",
                  "In addition, we propose a 'parsing-execution-filling' strategy to alleviate the hallucination dilemma of the chain of thought by decoupling logic and numerical computation in each step.",
                  "Extensive experiments show that our method can effectively leverage decomposed evidence and questions and outperforms the strong baselines on TabFact, WikiTableQuestion, and FetaQA datasets.",
                  "Notably, our model outperforms human performance for the first time on the TabFact dataset.",
                  "translation1:",
                  "Table-based reasoningは、Deep Modelsと離散的な推論を組み合わせることで顕著な進歩を遂げている。",
                  "これには、自由形式の自然言語（NL）質問と構造化された表形式のデータの両方を理解することを求められる",
                  "しかし、従来のtable-based reasoning solutionは、大規模なevidence（table）に対して著しい性能の低下を招くことが多い。",
                  "さらに、必要な情報が異なる場所に散らばっているため、ほとんどの既存の方法は複雑な質問に対する推論に苦労している。",
                  "これらの課題を軽減するために、本研究では効果的なtable-based reasoningのための分解器として大規模言語モデル（LLMs）を利用する。",
                  "具体的には、(i) 巨大なevidence（巨大なtable）をsub-evidence（small table）に分解して、table reasoningにおいて不要な情報の干渉を軽減し、（ii）複雑な質問をテキスト推論に適したよりシンプルなsub-questionに分解する。",
                  "特に、最初にLLMを使用して、現在の質問に関与するevidence（tables）を分解し、関連するevidenceを保持し、巨大なtableから残りの関連性のないevidenceを除外する。",
                  "さらに、'parsing-execution-filling'を提案し、各ステップで論理と数値計算を分離することで、chain of thoughtのhallucinationのジレンマを軽減する。",
                  "徹底的な実験により、提案手法が分解されたevidenceと質問を効果的に活用でき、TabFact、WikiTableQuestion、およびFetaQAデータセットで強力なベースラインを上回ることを示した。",
                  "特筆すべきことに、提案モデルはTabFactデータセットで初めて人間のパフォーマンスを上回った。"]
translator_system_content = '\n'.join(translator_system_content)

summarizer_system_content = ["あなたは自然言語処理や機械学習の研究者です。日本語のabstractを日本語を要約してください。\n",
                             "abstract1:",
                             "Table-based reasoningは、Deep Modelsと離散的な推論を組み合わせることで顕著な進歩を遂げている。",
                             "これには、自由形式の自然言語（NL）質問と構造化された表形式のデータの両方を理解することを求められる",
                             "しかし、従来のtable-based reasoning solutionは、大規模なevidence（table）に対して著しい性能の低下を招くことが多い。",
                             "さらに、必要な情報が異なる場所に散らばっているため、ほとんどの既存の方法は複雑な質問に対する推論に苦労している。",
                             "これらの課題を軽減するために、本研究では効果的なtable-based reasoningのための分解器として大規模言語モデル（LLMs）を利用する。",
                             "具体的には、(i) 巨大なevidence（巨大なtable）をsub-evidence（small table）に分解して、table reasoningにおいて不要な情報の干渉を軽減し、（ii）複雑な質問をテキスト推論に適したよりシンプルなsub-questionに分解する。",
                             "特に、最初にLLMを使用して、現在の質問に関与するevidence（tables）を分解し、関連するevidenceを保持し、巨大なtableから残りの関連性のないevidenceを除外する。",
                             "さらに、'parsing-execution-filling'を提案し、各ステップで論理と数値計算を分離することで、chain of thoughtのhallucinationのジレンマを軽減する。",
                             "徹底的な実験により、提案手法が分解されたevidenceと質問を効果的に活用でき、TabFact、WikiTableQuestion、およびFetaQAデータセットで強力なベースラインを上回ることを示した。",
                             "特筆すべきことに、提案モデルはTabFactデータセットで初めて人間のパフォーマンスを上回った。",
                             "summary1:",
                             "tableとquestionが与えられた時に、LLMを用いてsmall tableとsub-questionに分割。",
                             "sub-questionではlogicと数値計算を分離することで、hallucinationを防ぐ。",
                             "TabFact Reasoningで初めて人間を超えた性能を発揮。"]
summarizer_system_content = '\n'.join(summarizer_system_content)

def get_arxiv_id_from_url(url):
    arxiv_id = url.split('/')[-1]
    return arxiv_id


def get_entry_from_metadata(arxiv_id):
    base_url = "http://export.arxiv.org/api/query?"
    query = f"id_list={arxiv_id}"
    url = base_url + query

    feed = feedparser.parse(url)
    entry = feed.entries[0]

    return entry


def attach_pocket_tag(issue_number):
    github = Github(github_token)
    repo = github.get_repo(repo_name)
    issue = repo.get_issue(issue_number)

    # ラベル名を指定（既存のラベル名または新しいラベル名）
    label_name = "Pocket"

    # 既存のラベルを検索
    label = None
    for existing_label in repo.get_labels():
        if existing_label.name == label_name:
            label = existing_label
            break

    # ラベルをIssueに追加
    issue.add_to_labels(label)


def change_title(entry, issue_number):
    year = entry.published.split('-')[0][2:]
    author = entry.authors[0]
    if len(entry.authors) > 1:
        affiliation = author.get('arxiv.affiliation', 'N/A') 
        name = author['name']
        new_title = f"{entry.title}, {name}+, {affiliation}, arXiv'{year}"
    else:
        affiliation = author.get('arxiv.affiliation', 'N/A') 
        name = author['name']
        new_title = f"{entry.title}, {name}, {affiliation}, arXiv'{year}"

    github = Github(github_token)
    repo = github.get_repo(repo_name)
    issue = repo.get_issue(issue_number)
    issue.edit(title=new_title)


def call_openai(messages):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0)
    response_text = response.choices[0]['message']['content'].strip()
    return response_text


def translate(org_text):
    #abst = entry['summary']
    messages = []
    messages.append({'role': 'system', 'content': translator_system_content})
    user_content = ["abstract:",
                    f"{org_text}",
                    "translation:"]
    user_content = '\n'.join(user_content)
    messages.append({'role': 'user', 'content': user_content})
    translated_text = call_openai(messages)
    return translated_text


def summarize(org_text):
    messages = []
    messages.append({'role': 'system', 'content': summarizer_system_content})
    user_content = ["abstract:",
                    f"{org_text}",
                    "summary:"]
    user_content = '\n'.join(user_content)
    messages.append({'role': 'user', 'content': user_content})
    summary_text = call_openai(messages)
    return summary_text


def change_first_comment(url, entry, issue_number):
    new_comment = '# URL\n'
    new_comment += f'- {url}\n'
    new_comment += "# Affiliations\n"
    for author in entry.authors:
        name = author['name']
        affiliation = author.get('arxiv:affiliation', 'N/A')
        new_comment += f'  - {name}, {affiliation}\n'
    new_comment += '# Abstract\n'
    summary = entry['summary'].replace('\n','')
    new_comment += f'  - {summary}\n'

    # translation
    new_comment += '# Translation (by gpt-3.5-turbo)\n'
    abst = entry['summary']
    translated_text = translate(org_text)
    new_comment += f'- {translated_text}\n'

    # summarization
    new_comment += '# Summary (by gpt-3.5-turbo)\n'
    summary_text = summarize(translated_text)
    new_comment += f'- {summary_text}'

    # edit
    github = Github(github_token)
    repo = github.get_repo(repo_name)
    issue = repo.get_issue(issue_number)
    issue.edit(body=new_comment)


def change_title_and_first_comment(issue_data):
    issue_number = issue_data["number"]
    original_title = issue_data["title"]
    url = issue_data["body"]

    arxiv_id = get_arxiv_id_from_url(url)
    entry = get_entry_from_metadata(arxiv_id)
    attach_pocket_tag(issue_number)
    change_title(entry, issue_number)
    change_first_comment(url, entry, issue_number)


def translate_and_summarize(issue_data):
    import re 
    issue_url = issue_data['url']
    github = Github(github_token)
    issue = github.get_repo(issue_url.split("/repos/")[1].split("/issues/")[0]).get_issue(number=int(issue_url.split('/')[-1]))
    p = re.compile('__translate:(.*)')
    for comment in issue.get_comments():
        m = p.search(comment.body)
        if m != None:
            org_text = m.group(1)
            # translation
            new_comment = '# Translation (by gpt-3.5-turbo)\n'
            translated_text = translate(org_text)
            new_comment += f'- {translated_text}\n'
            # summarization
            new_comment += '# Summary (by gpt-3.5-turbo)\n'
            summary_text = summarize(translated_text)
            new_comment += f'- {summary_text}'   
            comment.edit(body='\n'.join([org_text, new_comment]))


if __name__ == "__main__":
    with open(event_path, "r") as event_file:
        event_data = json.load(event_file)
    action_type = event_data["action"]
    issue_data = event_data["issue"]

    url = issue_data["body"]

    if action_type == 'opened':
        if 'arxiv.org' in url:
            change_title_and_first_comment(issue_data)
    elif action_type == 'labeled':
        labels = issue_data["labels"]
        if any([label["name"] == "action_wanted" for label in labels]):
            change_title_and_first_comment(issue_data)
        elif any([label["name"] == "translation_required" for label in labels]):
            translate_and_summarize(issue_data)
    else:
        # neither 'opened' nor 'labeled' event, so exit
        exit(0)
