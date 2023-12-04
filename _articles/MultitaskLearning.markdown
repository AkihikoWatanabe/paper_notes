---
layout: post
title: MultitaskLearningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## MultitaskLearning
<div class="visible-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><br><span class="issue_date">Issue Date: 2023-11-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1127">Florence-2: Advancing a Unified Representation for a Variety of Vision  Tasks, Bin Xiao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>Florence-2は、ビジョン基盤モデルであり、さまざまなビジョンタスクに対応するための統一されたプロンプトベースの表現を持っています。このモデルは、テキストプロンプトを受け取り、キャプショニング、オブジェクト検出、グラウンディング、セグメンテーションなどのタスクを実行し、テキスト形式で結果を生成します。また、FLD-5Bという大規模な注釈付きデータセットも開発されました。Florence-2は、多目的かつ包括的なビジョンタスクを実行するためにシーケンスツーシーケンス構造を採用しており、前例のないゼロショットおよびファインチューニングの能力を持つ強力なモデルです。</span>
<span class="snippet"><span>Comment</span>Vison Foundation Model。Spatialな階層構造や、Semanticを捉えられるように訓練。Image/Prompt Encoderでエンコードされ、outputはtext + location informationとなる。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9fbfba62-190f-46eb-a893-5ebe76dda030" alt="image"><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/Zero_Few-shot.html">#Zero/Few-shot</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/863">Few-Shot Data-to-Text Generation via Unified Representation and Multi-Source Learning, ACL23</a>
<span class="snippet"><span>Summary</span>この論文では、構造化データからテキストを生成する新しいアプローチを提案しています。提案手法は、さまざまな形式のデータを処理できる統一された表現を提供し、マルチタスクトレーニングやゼロショット学習などのシナリオでのパフォーマンスを向上させることを目指しています。実験結果は、提案手法が他の方法と比較して優れた性能を示していることを示しています。これは、データからテキスト生成フレームワークにおける重要な進歩です。</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/904">Measuring Massive Multitask Language Understanding, Dan Hendrycks+, N_A, ICLR21</a>
<span class="snippet"><span>Summary</span>私たちは、マルチタスクのテキストモデルの正確性を測定するための新しいテストを提案しています。このテストは、57のタスクをカバーし、広範な世界知識と問題解決能力を必要とします。現在のモデルはまだ専門家レベルの正確性に達しておらず、性能に偏りがあります。私たちのテストは、モデルの理解の幅と深さを評価し、重要な欠点を特定するために使用できます。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/252">An Overview of Multi-Task Learning in Deep Neural Networks, Sebastian Ruder, arXiv17</a>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/QueryClassification.html">#QueryClassification</a><a class="button" href="articles/WebSearch.html">#WebSearch</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/249">Representation Learning Using Multi-Task Deep Neural Networks for Semantic Classification and Information Retrieval, Liu+, NAACL-HLT15</a>
<span class="snippet"><span>Comment</span>クエリ分類と検索をNeural Netを用いてmulti-task learningする研究分類(multi-class classification)とランキング(pairwise learning-to-rank)という異なる操作が必要なタスクを、multi task learningの枠組みで ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/250">A unified architecture for natural language processing: Deep neural networks with multitask learning, Collobert+, ICML2008.</a>
<span class="snippet"><span>Comment</span>Deep Neural Netを用いてmultitask learningを行いNLPタスク（POS tagging, Semantic Role Labeling, Chunking etc.）を解いた論文。被引用数2000を超える。multitask learningの学習プロセスな ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
