---
layout: post
title: Documentに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Document
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/73">Distraction-Based Neural Networks for Modeling Documents, Chen+, IJCAI16</a>
<span class="snippet"><span>Comment</span>Neuralなモデルで「文書」の要約を行う研究。提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。distractionを導入するmotivationは、入力文書中の異なる情報を横断Dist ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/75">LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP15</a>
<span class="snippet"><span>Comment</span>Large Chinese Short Text Summarization (LCSTS) datasetを作成データセットを作成する際は、Weibo上の特定のorganizationの投稿の特徴を利用。Weiboにニュースを投稿する際に、投稿の冒頭にニュースのvery short sCop ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/74">A hierarchical neural autoencoder for paragraphs and documents, Li+, ACL15</a>
<span class="snippet"><span>Comment</span>複数文を生成(今回はautoencoder)するために、standardなseq2seq LSTM modelを、拡張したという話。要は、paragraph/documentのrepresentationが欲しいのだが、アイデアとしては、word-levelの情報を扱うLSTM layerとtr ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/SentimentAnalysis.html">#SentimentAnalysis</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/72">Document Modeling with Gated Recurrent Neural Network for Sentiment Classification, Tang+, EMNLP15</a>
<span class="snippet"><span>Comment</span>word level -> sentence level -> document level のrepresentationを求め、documentのsentiment classificationをする話。documentのRepresentationを生成するときに参考になるやも。sen ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/77">Teaching Machines to Read and Comprehend, Hermann+, NIPS 2015</a>
<span class="snippet"><span>Comment</span>だいぶ前に読んだので割とうろおぼえ。CNN/DailyMailデータセットの作成を行なった論文（最近Neuralな文”書”要約の学習でよく使われるやつ）。CNN/DailyMailにはニュース記事に対して、人手で作成した要約が付与されており、要約中のEntityを穴埋めにするなどして、 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/44">SCENE: A Scalable Two-Stage Personalized News Recommendation System, Li et al., SIGIR’11</a>
<span class="snippet"><span>Comment</span>・ニュース推薦には3つのチャレンジがある。1. スケーラビリティ　より高速なreal-time processing2. あるニュース記事を読むと、続いて読む記事に影響を与える3. popularityとrecencyが時間経過に従い変化するので、これらをどう扱うかこれらに対 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/43">A semantic-expansion approach to personalized knowledge recommendation, Liang, Yang, Chen and Ku, Decision Support Systems, 2007</a>
<span class="snippet"><span>Comment</span>・traditionalなkeywordベースでマッチングするアプローチだと，単語間の意味的な関係によって特定の単語のoverweightやunderweightが発生するので，advancedなsemanticsを考慮した手法が必要なので頑張りますという論文． ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/42">Combination of Web page recommender systems, Goksedef, Gunduz-oguducu, Elsevier, 2010</a>
<span class="snippet"><span>Comment</span>・traditionalなmethodはweb usage or web content mining techniquesを用いているが，ニュースサイトなどのページは日々更新されるのでweb content mining techniquesを用いてモデルを更新するのはしんどい．ので，web us ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/41">Neural Networks for Web Content Filtering, 2002, Lee, Fui and Fong, IEEE Intelligent Systems</a>
<span class="snippet"><span>Comment</span>・ポルノコンテンツのフィルタリングが目的. 提案手法はgeneral frameworkなので他のコンテンツのフィルタリングにも使える.・NNを採用する理由は，robustだから（様々な分布にfitする）．Webpageはnoisyなので．・trainingのためにpornographic ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
