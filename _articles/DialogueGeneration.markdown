---
layout: post
title: DialogueGenerationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## DialogueGeneration
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/575">q2d: Turning Questions into Dialogs to Teach Models How to Search, Bitton+, The Hebrew University of Jerusalem （w_ Google Research）, arXiv23</a>
<span class="snippet"><span>Comment</span>LLMにquestionを与え、questionを解決するためのinformation seekingの対話ログを生成させる。このデータを用いて、dialogueからquestionを生成するモデルを訓練し、検索APIなどに渡せるようにした研究。全く対話のログがないドメインのデータに対しても、人間と ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><a class="button" href="articles/QA-based.html">#QA-based</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/966">Q2: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering, Honovich+, EMNLP21</a>
<span class="snippet"><span>Summary</span>本研究では、ニューラルな知識に基づく対話生成モデルの信頼性と適用範囲の制限についての問題を解決するため、自動的な質問生成と質問応答を使用した事実的な整合性の自動評価尺度を提案します。この尺度は、自然言語推論を使用して回答スパンを比較することで、以前のトークンベースのマッチングよりも優れた評価を行います。また、新しいデータセットを作成し、事実的な整合性の手動アノテーションを行い、他の尺度とのメタ評価を行いました。結果として、提案手法が人間の判断と高い相関を示しました。</span>
<span class="snippet"><span>Comment</span>（knowledge-grounded; 知識に基づいた）対話に対するFactual ConsistencyをReference-freeで評価できるQGQA手法。機械翻訳やAbstractive Summarizationの分野で研究が進んできたが、対話では対話履歴、個人の意見、ユーザに対 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/979808f2-d31a-49b0-bd25-aba1f1a81d4a" alt="image"><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/ConceptToText.html">#ConceptToText</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><br><span class="issue_date">Issue Date: 2021-06-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/367">NUBIA, EvalNLGEval20</a>
<span class="snippet"><span>Comment</span>TextGenerationに関するSoTAの性能指標。BLEU, ROUGE等と比較して、人間との相関が高い。![image](https://user-images.githubusercontent.com/12249301/120425437-299d5c00-c3a9-11eb-923意 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2019-01-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/302">Training Millions of Personalized Dialogue Agents, Mazaré, ACL19</a>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-02-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/255">Personalizing Dialogue Agents: I have a dog, do you have pets too?, Zhang+, arXiv18</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/876">ChatBot Arenaのデータセット</a>
<span class="snippet"><span>Comment</span>33kのconversation、2つのレスポンスに対する人間のpreferenceスコア付き20種類のSoTAモデルのレスポンスを含み、13kのユニークIPからのアクセスがあり、3Kのエキスパートによるアノテーション付き ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
