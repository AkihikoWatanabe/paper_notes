---
layout: post
title: RecommenderSystemsに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## RecommenderSystems
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/General.html">#General</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/68">StarSpace: Embed All The Things, Wu+, arXiv17</a>
<span class="snippet"><span>Comment</span>分類やランキング、レコメンドなど、様々なタスクで汎用的に使用できるEmbeddingの学習手法を提案。Embeddingを学習する対象をEntityと呼び、Entityはbag-of-featureで記述される。Entityはbag-of-featureで記述できればなんでもよく、こ実際にS ...</span>
<a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/27">Multi-relational matrix factorization using bayesian personalized ranking for social network data, Krohn-Grimberghe+, WSDM12</a>
<span class="snippet"><span>Comment</span>multi-relationalな場合でも適用できるmatrix factorizationを提案。特にcold start problemにフォーカス。social networkのデータなどに適用できる。 ...</span>
<br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/28">BPR: Bayesian Personalized Ranking from Implicit Feedback, Rendle+, UAI09</a>
<span class="snippet"><span>Comment</span>重要論文ユーザのアイテムに対するExplicit/Implicit Ratingを利用したlearning2rank。AUCを最適化するようなイメージ。負例はNegative Sampling。計算量が軽く、拡張がしやすい。Implicitデータを使ったTop-N Recsy参考: ht ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/4">Collaborative Summarization: When Collaborative Filtering Meets Document Summarization, Qu+, PACLIC09, 6</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34400963-26dc2ee2-ebda-11e7-8170-2aa5fcc701c1.png)Collaborative Filteringと要約を組み合わせる手評価1 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RelevanceJudgment.html">#RelevanceJudgment</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/52">Relevance Judgment in epistemic and hedonic information searches, Xu, Chen, Journal of the American Society for Information Science and Technology, 2007</a>
<span class="snippet"><span>Comment</span>・informative relevance: 知識を求める検索など（個人のブログ，経済ニュースとか）・affective relevance: 楽しみや感情に刺激を受けるための情報を求める検索の場合（2chまとめとか，哲学ニュースまとめとか？）・topicality, novelty, ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Novelty.html">#Novelty</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/47">Improving Recommendation Novelty Based on Topic Taxonomy, Weng et al., WI-IAT Workshops ‘07</a>
<span class="snippet"><span>Comment</span>・評価をしていない・通常のItem-based collaborative filteringの結果に加えて，taxonomyのassociation rule mining (あるtaxonomy t1に興味がある人が，t2にも興味がある確率を獲得する)を行い，このassociation ru ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Novelty.html">#Novelty</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/46">Discovery-oriented Collaborative Filtering for Improving User Satisfaction, Hijikata et al., IUI’09</a>
<span class="snippet"><span>Comment</span>・従来のCFはaccuracyをあげることを目的に研究されてきたが，ユーザがすでに知っているitemを推薦してしまう問題がある．おまけに（推薦リスト内のアイテムの観点からみた）diversityも低い．このような推薦はdiscoveryがなく，user satisfactionを損ねるので，ユーザが ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Novelty.html">#Novelty</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/45">“I like to explore sometimes”: Adapting to Dynamic User Novelty Preferences, Kapoor et al. （with Konstan）, RecSys’15</a>
<span class="snippet"><span>Comment</span>・典型的なRSは，推薦リストのSimilarityとNoveltyのcriteriaを最適化する．このとき，両者のバランスを取るためになんらかの定数を導入してバランスをとるが，この定数はユーザやタイミングごとに異なると考えられるので（すなわち人やタイミングによってnoveltyのpreference ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Document.html">#Document</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/44">SCENE: A Scalable Two-Stage Personalized News Recommendation System, Li et al., SIGIR’11</a>
<span class="snippet"><span>Comment</span>・ニュース推薦には3つのチャレンジがある。1. スケーラビリティ　より高速なreal-time processing2. あるニュース記事を読むと、続いて読む記事に影響を与える3. popularityとrecencyが時間経過に従い変化するので、これらをどう扱うかこれらに対 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Document.html">#Document</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/43">A semantic-expansion approach to personalized knowledge recommendation, Liang, Yang, Chen and Ku, Decision Support Systems, 2007</a>
<span class="snippet"><span>Comment</span>・traditionalなkeywordベースでマッチングするアプローチだと，単語間の意味的な関係によって特定の単語のoverweightやunderweightが発生するので，advancedなsemanticsを考慮した手法が必要なので頑張りますという論文． ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Document.html">#Document</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/42">Combination of Web page recommender systems, Goksedef, Gunduz-oguducu, Elsevier, 2010</a>
<span class="snippet"><span>Comment</span>・traditionalなmethodはweb usage or web content mining techniquesを用いているが，ニュースサイトなどのページは日々更新されるのでweb content mining techniquesを用いてモデルを更新するのはしんどい．ので，web us ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Document.html">#Document</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/41">Neural Networks for Web Content Filtering, 2002, Lee, Fui and Fong, IEEE Intelligent Systems</a>
<span class="snippet"><span>Comment</span>・ポルノコンテンツのフィルタリングが目的. 提案手法はgeneral frameworkなので他のコンテンツのフィルタリングにも使える.・NNを採用する理由は，robustだから（様々な分布にfitする）．Webpageはnoisyなので．・trainingのためにpornographic ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/InteractiveRecommenderSystems.html">#InteractiveRecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/29">Interactive Recommender Systems</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/8">User-model based personalized summarization, Diaz+, Information Processing and Management 2007, 96</a>
<span class="snippet"><span>Comment</span>PDSの先駆けとなった重要論文。必ずreferすべき。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
