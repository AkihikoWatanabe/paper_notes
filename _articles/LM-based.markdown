---
layout: post
title: LM-basedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## LM-based
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/967">DiscoScore: Evaluating Text Generation with BERT and Discourse Coherence, Wei Zhao+, N_A, EACL23</a>
<span class="snippet">本研究では、文章の一貫性を評価するための新しい指標であるDiscoScoreを紹介します。DiscoScoreはCentering理論に基づいており、BERTを使用して談話の一貫性をモデル化します。実験の結果、DiscoScoreは他の指標よりも人間の評価との相関が高く、システムレベルでの評価でも ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/965">SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization, Laban+, TACL22</a>
<span class="snippet">要約の領域では、入力ドキュメントと要約が整合していることが重要です。以前の研究では、自然言語推論（NLI）モデルを不整合検出に適用するとパフォーマンスが低下することがわかりました。本研究では、NLIを不整合検出に再評価し、過去の研究での入力の粒度の不一致が問題であることを発見しました。新しい手法S ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/960">BARTSCORE: Evaluating Generated Text as Text Generation, Yuan+ （w_ Neubigさん）, NeurIPS21</a>
<span class="snippet">本研究では、生成されたテキストの評価方法について検討しました。具体的には、事前学習モデルを使用してテキスト生成の問題をモデル化し、生成されたテキストを参照出力またはソーステキストに変換するために訓練されたモデルを使用しました。提案したメトリックであるBARTSCOREは、情報量、流暢さ、事実性など ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4a64ea21-ab9f-4762-bd71-f858663fc195" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/964">Compression, Transduction, and Creation: A Unified Framework for Evaluating Natural Language Generation, Deng+, EMNLP21</a>
<span class="snippet">本研究では、自然言語生成（NLG）タスクの評価において、情報の整合性を重視した統一的な視点を提案する。情報の整合性を評価するための解釈可能な評価指標のファミリーを開発し、ゴールドリファレンスデータを必要とせずに、さまざまなNLGタスクの評価を行うことができることを実験で示した。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/959">Automatic Machine Translation Evaluation in Many Languages via Zero-Shot Paraphrasing, Thompson+, EMNLP20</a>
<span class="snippet">パラフレーザを使用して機械翻訳の評価を行うタスクを定義し、多言語NMTシステムをトレーニングしてパラフレーシングを行います。この手法は直感的であり、人間の判断を必要としません。39言語でトレーニングされた単一モデルは、以前のメトリクスと比較して優れたパフォーマンスを示し、品質推定のタスクでも優れた ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/963">Evaluating the Factual Consistency of Abstractive Text Summarization, Kryscinski+, EMNLP20</a>
<span class="snippet">本研究では、要約の事実的な整合性を検証するためのモデルベースのアプローチを提案しています。トレーニングデータはルールベースの変換を用いて生成され、モデルは整合性の予測とスパン抽出のタスクで共同してトレーニングされます。このモデルは、ニューラルモデルによる要約に対して転移学習を行うことで、以前のモデ ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
