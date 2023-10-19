import requests
import os
from collections import defaultdict
from itertools import product

import re

year_pat = re.compile(r"(\d{2,4})")

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
                 'Tutorial',
                 'UserModeling',
                 "Education",
                 "Infrastructure"]
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
                     "Dataset",
                     "DataToText",
                     "ConceptToText",
                     "DialogueGeneration",
                     "DocumentSummarization",
                     "DropoutPrediction",
                     "EssayScoring",
                     "Evaluation",
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
                     "AWS"]
sub_sub_parent_labels = ["AffectDetection",
                         "Alignment",
                         "Assessment",
                         "Attention",
                         "BeamSearch",
                         "ChatGPT",
                         "CodeGeneration",
                         "CollaborativeFiltering",
                         "CommentGenertion",
                         "Contents-based",
                         "ContrastiveLearning",
                         "CoT",
                         "CTRPrediction",
                         "CurriculumGeneration",
                         "CVRPrediction",
                         "DataAugmentation",
                         "DataDistillation",
                         "DataGeneration",
                         "Dataset",
                         "DataToText",
                         "ConceptToText",
                         "DialogueGeneration",
                         "DocumentSummarization",
                         "DomainAdaptation",
                         "DropoutPrediction",
                         "Embed",
                         "EssayScoring",
                         "Evaluation",
                         "ExplicitFeedback",
                         "FactorizationMachines",
                         "Finetuning",
                         "FoundationModel",
                         "GenerativeAdversarialNetwork",
                         "GenerativeAI",
                         "GraphBased",
                         "GraphConvolutionalNetwork",
                         "ILP",
                         "ImageCaptioning",
                         "ImageSegmentation",
                         "ImplicitFeedback",
                         "In-Context Learning",
                         "Information Extraction",
                         "InstructionTuning",
                         "InteractivePersonalizedSummarization",
                         "InteractiveRecommenderSystems",
                         "IRT",
                         "ItemBased",
                         "Interleaved",
                         "KnowledgeGraph",
                         "KnowledgeTracing",
                         "LanguageModel",
                         "Library",
                         "ListWise",
                         "LLMAgent",
                         "MatrixFactorization",
                         "Metrics",
                         "MultiModal",
                         "Multi",
                         "MultitaskLearning",
                         "NaturalLanguageGeneration",
                         "Navigation",
                         "Neural",
                         "NeuralArchitectureSearch",
                         "NewsRecommendation",
                         "NumericReasoning",
                         "Online/Interactive",
                         "OnlineEvaluation",
                         "OnlineLearning",
                         "OpinionMining",
                         "OptionTracing",
                         "PairWise",
                         "Personalization",
                         "PersonalizedDocumentSummarization",
                         "PersonalizedGeneration",
                         "PersonalizedHeadlineGeneration",
                         "Planning",
                         "PointWise",
                         "Poisoning",
                         "pretrained-LM",
                         "Pretraining",
                         "Prompt",
                         "PromptTuning",
                         "Pruning",
                         "QA-based",
                         "Quantization",
                         "QueryBiased",
                         "QueryClassification",
                         "QuestionAnswering",
                         "Reference-based",
                         "Reference-free",
                         "ReinforcementLearning",
                         "RelevanceFeecback",
                         "RelevanceJudgment",
                         "RepresentationLearning",
                         "RetrievalAugmentation",
                         "ReviewGeneration",
                         "RuleBased",
                         "ScorePrediction",
                         "SemanticTextualSimilarity",
                         "SentenceCompression",
                         "SentimentAnalysis",
                         "SpokenLanguageGeneration",
                         "StudentPerformancePrediction",
                         "Supervised",
                         "SyntheticData",
                         "TabularData",
                         "TheoryOfMind",
                         "TimeSeriesDataProcessing",
                         "Tools",
                         "TrainedMetrics",
                         "Training-Free",
                         "Transformer",
                         "Unsupervised",
                         "UserBased",
                         "WebSearch",
                         "Zero/Few-shot"]   
sub_sub_parent_labels = list(set(sub_sub_parent_labels) - set(sub_parent_labels))
representative_label_set = set(parent_labels) - set(sub_parent_labels) - set(sub_sub_parent_labels)

# GitHub API設定
TOKEN = os.environ["TOKEN"]
REPO = "AkihikoWatanabe/paper_notes"
API_URL = f"https://api.github.com/repos/{REPO}/issues"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

params = {'state': 'open', 'per_page': 100}
issues = []
while API_URL:
    response = requests.get(API_URL, headers=headers, params=params)
    issues.extend(response.json())
    # Linkヘッダーから次のページのURLを取得
    links = requests.utils.parse_header_links(response.headers['Link'].rstrip('>').replace('>,<', ',<'))
    API_URL = None
    for link in links:
        if link['rel'] == 'next':
            API_URL = link['url']
            break


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
    

# ラベルの階層構造を解析
label_to_hierarchy = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
label_count = defaultdict(lambda: 0)
pockets = []
for issue in issues:
    year = get_year(issue["title"])
    labels = issue["labels"]
    parents = [l['name'] for l in labels if l['name'] in parent_labels]
    sub_parents = [l['name'] for l in labels if l['name'] in sub_parent_labels]
    sub_sub_parents = [l['name'] for l in labels if l['name'] in sub_sub_parent_labels]

    if len(issue["labels"]) == 1 and issue["labels"][0]["name"] == "Pocket":
        pockets.append((issue, year))
        label_count[("Pocket")] += 1
        continue

    if len(parents) == 0:
        parents = ["Others"]
    if len(sub_parents) == 0:
        sub_parents = ["Others"]
    if len(sub_sub_parents) == 0:
        sub_sub_parents = ["Others"]

    for p, sp, ssp in product(parents, sub_parents, sub_sub_parents):
        label_to_hierarchy[p][sp][ssp].append((issue, year))
        label_count[(p, sp, ssp)] += 1
    for p in parents:
        label_count[(p)] += 1
    for p, sp in product(parents, sub_parents):
        label_count[(p, sp)] += 1

    


label_to_hierarchy = dict(label_to_hierarchy)


# ラベルの階層構造を基にHTMLを生成
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>わたしのべんきょうノート</title>
    <style>
        .content {
            display: none;
        }
    </style>
</head>
<body>
"""

# Introduction
html_content = ""

# 階層構造のデータを基にHTMLを生成
html_content = ""
for parent, sub_parents in sorted(label_to_hierarchy.items(), key=lambda item: label_count[(item[0])], reverse=True):
    html_content += f"""
    <div>
        <h1 onclick="toggleContent(this)">{parent}({label_count[(parent)]})</h1>
        <div class="content">
    """
    for sub_parent, sub_sub_parents in sorted(sub_parents.items(), key=lambda item: label_count[(parent, item[0])], reverse=True):
        html_content += f"""
            <h2 onclick="toggleContent(this)">{sub_parent}({label_count[(parent, sub_parent)]})</h2>
            <div class="content">
        """
        for sub_sub_parent, issues in sorted(sub_sub_parents.items(), key=lambda item: label_count[(parent, sub_parent, item[0])], reverse=True):
            html_content += f"""
                <h3 onclick="toggleContent(this)">{sub_sub_parent}({label_count[(parent, sub_parent, sub_sub_parent)]})</h3>
                <div class="content">
            """
            for issue, year in issues:
                tags = ' / '.join([data['name'] for data in issue['labels']])
                html_content += f"""
                    <div class="tag">{tags}</div>
                    <a href="{issue["html_url"]}">{issue['title']}</a>
                """
            html_content += "</div>"
        html_content += "</div>"
    html_content += "</div>"
    html_content += "</div>"
    html_content += "<hr>"

html_content += f"""
    <div>
        <h1 onclick="toggleContent(this)">Pocket({label_count["Pocket"]})</h1>
        <div class="content">
    """
for issue, year in sorted(pockets, key=lambda x: x[1], reverse=True):
    tags = ' / '.join([data['name'] for data in issue['labels']])
    html_content += f"""
        <div class="tag">{tags}</div>
        <a href="{issue["html_url"]}">{issue['title']}</a>
    """
    html_content += "</div>"
html_content += "</div>"
html_content += "</div>"


html_template += html_content

# JavaScriptの追加
html_template += """
<script>
    function toggleContent(element) {
        const content = element.nextElementSibling;
        if (content.style.display === "none" || content.style.display === "") {
            content.style.display = "block";
        } else {
            content.style.display = "none";
        }
    }
</script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_template)
