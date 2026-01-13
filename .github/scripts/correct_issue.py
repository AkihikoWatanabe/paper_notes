import os
from github import Github
import feedparser
from openai import OpenAI
import json
import re


github_token = os.environ["TOKEN"]
repo_name = os.environ["GITHUB_REPOSITORY"]
event_path = os.environ["GITHUB_EVENT_PATH"]

#MODEL = "gpt-5-nano"
MODEL = "gpt-4o-mini"

translator_system_content = [
        "あなたは自然言語処理や機械学習の研究者です。以下の英語の<abstract>を日本語に翻訳してください。出力は翻訳結果のみを出力してください。"
]
translator_system_content = '\n'.join(translator_system_content)

summarizer_system_content = ["あなたは自然言語処理や機械学習の研究者です。以下の<abstract_summary_pair>と同じトーンで、<target_abstract>を要約してください。出力は要約結果のみを出力してください。\n",
                             "<abstract-summary-pair>",
                             "<abstract>Table-based reasoningは、Deep Modelsと離散的な推論を組み合わせることで顕著な進歩を遂げている。",
                             "これには、自由形式の自然言語（NL）質問と構造化された表形式のデータの両方を理解することを求められる",
                             "しかし、従来のtable-based reasoning solutionは、大規模なevidence（table）に対して著しい性能の低下を招くことが多い。",
                             "さらに、必要な情報が異なる場所に散らばっているため、ほとんどの既存の方法は複雑な質問に対する推論に苦労している。",
                             "これらの課題を軽減するために、本研究では効果的なtable-based reasoningのための分解器として大規模言語モデル（LLMs）を利用する。",
                             "具体的には、(i) 巨大なevidence（巨大なtable）をsub-evidence（small table）に分解して、table reasoningにおいて不要な情報の干渉を軽減し、（ii）複雑な質問をテキスト推論に適したよりシンプルなsub-questionに分解する。",
                             "特に、最初にLLMを使用して、現在の質問に関与するevidence（tables）を分解し、関連するevidenceを保持し、巨大なtableから残りの関連性のないevidenceを除外する。",
                             "さらに、'parsing-execution-filling'を提案し、各ステップで論理と数値計算を分離することで、chain of thoughtのhallucinationのジレンマを軽減する。",
                             "徹底的な実験により、提案手法が分解されたevidenceと質問を効果的に活用でき、TabFact、WikiTableQuestion、およびFetaQAデータセットで強力なベースラインを上回ることを示した。",
                             "特筆すべきことに、提案モデルはTabFactデータセットで初めて人間のパフォーマンスを上回った。</abstract>",
                             "<summary>tableとquestionが与えられた時に、LLMを用いてsmall tableとsub-questionに分割。",
                             "sub-questionではlogicと数値計算を分離することで、hallucinationを防ぐ。",
                             "TabFact Reasoningで初めて人間を超えた性能を発揮。</summary>",
                             "<abstract-summary-pair>"]
summarizer_system_content = '\n'.join(summarizer_system_content)

def get_arxiv_id_from_url(url):
    arxiv_id = url.split('/')[-1]
    return arxiv_id


def get_entry_from_metadata(arxiv_id):
    base_url = "http://export.arxiv.org/api/query?"
    query = f"id_list={arxiv_id}"
    url = base_url + query

    feed = feedparser.parse(url)
        
    if not feed.entries:
        # エントリがない場合のエラー処理
        print(f"Error: No entry found for arXiv ID: {arxiv_id} (URL: {url})")
        raise ValueError(f"arXiv ID {arxiv_id} のメタデータが見つかりません")
    
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
    from datetime import datetime
    dt = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%S%z")
    year = str(dt.year)
    month = f"{dt.month:02d}"
    author = entry.authors[0]
    if len(entry.authors) > 1:
        name = author['name']
        new_title = f"[Paper Note] {entry.title}, {name}+, arXiv'{year[2:]}, {year}.{month}"
    else:
        name = author['name']
        new_title = f"[Paper Note] {entry.title}, {name}, arXiv'{year[2:]}, {year}.{month}"

    github = Github(github_token)
    repo = github.get_repo(repo_name)
    issue = repo.get_issue(issue_number)
    issue.edit(title=new_title)


# https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools
def call_openai(messages, verbosity="medium"):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=MODEL,
        input=messages,
        reasoning = {
            "effort": "minimal"
        },
        text = {
            "verbosity": verbosity
        }
    )
    response_text = response.output_text
    
    return response_text


def translate(org_text):
    #abst = entry['summary']
    messages = []
    messages.append({'role': 'developer', 'content': translator_system_content})
    user_content = [f"<abstract>{org_text}</abstract>"]
    user_content = '\n'.join(user_content)
    messages.append({'role': 'user', 'content': user_content})
    translated_text = call_openai(messages)
    return translated_text


def summarize(org_text):
    messages = []
    messages.append({'role': 'system', 'content': summarizer_system_content})
    user_content = [f"<target_abstract>{org_text}</target_abstract>"]
    user_content = '\n'.join(user_content)
    messages.append({'role': 'user', 'content': user_content})
    summary_text = call_openai(messages, verbosity="low")
    return summary_text


def change_first_comment(url, entry, issue_number):
    new_comment = '# URL\n'
    new_comment += f'- {url}\n'
    new_comment += "# Authors\n"
    for author in entry.authors:
        name = author['name']
        new_comment += f'  - {name}\n'
    new_comment += '# Abstract\n'
    summary = entry['summary'].replace('\n',' ')
    new_comment += f'  - {summary}\n'

    # translation
    new_comment += f'# Translation (by {MODEL})\n'
    abst = entry['summary']
    translated_text = translate(abst)
    new_comment += f'- {translated_text}\n'

    # summarization
    new_comment += f'# Summary (by {MODEL})\n'
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
    def _gen_new_comment(org_text: str):
        org_text = org_text.replace("\n", "")
        # translation
        new_comment = f'# Translation (by {MODEL})\n'
        translated_text = translate(org_text)
        new_comment += f'- {translated_text}\n'
        # summarization
        new_comment += f'# Summary (by {MODEL})\n'
        summary_text = summarize(translated_text)
        new_comment += f'- {summary_text}'
        return new_comment

    import re 
    issue_url = issue_data['url']
    github = Github(github_token)
    issue = github.get_repo(issue_url.split("/repos/")[1].split("/issues/")[0]).get_issue(number=int(issue_url.split('/')[-1]))
    p = re.compile('__translate:(.*)', re.DOTALL)
    
    m = p.search(issue.body)
    if m != None:
        org_text = m.group(1)
        new_comment = _gen_new_comment(org_text=org_text)
        issue.edit(body=new_comment)
        return
            
    for comment in issue.get_comments():
        m = p.search(comment.body)
        if m != None:
            org_text = m.group(1)
            new_comment = _gen_new_comment(org_text=org_text)
            comment.edit(body='\n'.join([org_text, new_comment]))


if __name__ == "__main__":
    with open(event_path, "r") as event_file:
        event_data = json.load(event_file)
    action_type = event_data["action"]
    issue_data = event_data["issue"]

    url = issue_data["body"]

    arxiv_pat = r"^https?:\/\/arxiv\.org\/.*?$"

    if action_type == 'opened':
        if re.fullmatch(arxiv_pat, url):
            change_title_and_first_comment(issue_data)
    elif action_type == 'labeled':
        labels = issue_data["labels"]
        if any([label["name"] == "action_wanted" for label in labels]) and re.fullmatch(arxiv_pat, url):
            change_title_and_first_comment(issue_data)
        elif any([label["name"] == "translation_required" for label in labels]):
            translate_and_summarize(issue_data)
    else:
        # neither 'opened' nor 'labeled' event, so exit
        exit(0)
