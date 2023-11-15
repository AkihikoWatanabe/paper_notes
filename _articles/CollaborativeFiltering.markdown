---
layout: post
title: CollaborativeFilteringに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## CollaborativeFiltering
<div class="visible-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/545">Graph Collaborative Signals Denoising and Augmentation for  Recommendation, Ziwei Fan+, N_A, SIGIR23</a>
<span class="snippet">グラフ協調フィルタリング（GCF）は、推薦システムで人気のある技術ですが、相互作用が豊富なユーザーやアイテムにはノイズがあり、相互作用が不十分なユーザーやアイテムには不十分です。また、ユーザー-ユーザーおよびアイテム-アイテムの相関を無視しているため、有益な隣接ノードの範囲が制限される可能性があり ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b0f099c2-8e9d-4ebc-aa1b-d4af49509a37" alt="image"><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2022-04-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/442">Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches, Politecnico di Milano, Maurizio+, RecSys19</a>
<span class="snippet">RecSys'19のベストペーパー日本語解説：https://qiita.com/smochi/items/98dbd9429c15898c5dc7 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-02-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/260">Neural Collaborative Filtering, He+, WWW17</a>
<span class="snippet">Collaborative FilteringをMLPで一般化したNeural Collaborative Filtering、およびMatrix Factorizationはuser, item-embeddingのelement-wise product + linear transofmrat ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><br><span class="issue_date">Issue Date: 2019-02-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/303">Estimating Reactions and Recommending Products with Generative Models of Reviews, Ni+, IJCNLP17</a>
<span class="snippet">Collaborative Filtering (CF) によるコンテンツ推薦とReview Generationを同時に学習し、両者の性能を向上させる話。非常に興味深い設定で、このような実験設定でReview Generationを行なった初めての研究。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-01-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/216">Collaborative Denoising Auto-Encoders for Top-N Recommender Systems, Wu+, WSDM16</a>
<span class="snippet">Denoising Auto-Encoders を用いたtop-N推薦手法、Collaborative Denoising Auto-Encoder (CDAE)を提案。モデルベースなCollaborative Filtering手法に相当する。corruptedなinputを復元するようなDe ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/221">Collaborative Deep Learning for Recommender Systems Wang+, KDD’15</a>
<span class="snippet">Rating Matrixからuserとitemのlatent vectorを学習する際に、Stacked Denoising Auto Encoder（SDAE）によるitemのembeddingを活用する話。Collaborative FilteringとContents-based Fil ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/223"> SVDFeature: a toolkit for feature-based collaborative filtering, Chen+, JMLR12</a>
<span class="snippet">tool: http://apex.sjtu.edu.cn/projects/33 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/428">A Comparative Study of Collaborative Filtering Algorithms, Lee+, arXiv12</a>
<span class="snippet">様々あるCFアルゴリズムをどのように選択すべきか、# of users, # of items, rating matrix densityの観点から分析した研究。1. 特にcomputationに関する制約がない場合は・・・、NMFはsparseなデータセットに対して最も良い性能を発揮する ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/226">Collaborative topic modeling for recommending scientific articles, Wang+, KDD11</a>
<span class="snippet">Probabilistic Matrix Factorization (PMF) #227 に、Latent Dirichllet Allocation (LDA) を組み込んだCollaborative Topic Regression (CTR)を提案。LDAによりitemのlatent v ...</span>
<a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/427">Multi-Relational Factorization Models for Predicting Student Performance, Nguyen+, KDD Cup11</a>
<span class="snippet">過去のCollaborative Filteringを利用したStudent Performance Prediction (#426 など)では、単一の関係性（student-skill, student-task等の関係）のみを利用していたが、この研究では複数の関係性（task-required ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/426">Collaborative Filtering Applied to Educational Data Mining, Andreas+, KDD Cup10</a>
<span class="snippet">KDD Cup'10のStudent Performance Predictionタスクにおいて3位をとった手法メモリベースドな協調フィルタリングと、Matirx Factorizationモデルを利用してStudent Performance Predictionを実施。最終的にこれらのモ ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/4">Collaborative Summarization: When Collaborative Filtering Meets Document Summarization, Qu+, PACLIC09, 6</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/34400963-26dc2ee2-ebda-11e7-8170-2aa5fcc701c1.png)Collaborative Filteringと要約を組み合わせる手 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/225">Collaborative filtering for implicit feedback datasets, Hu+, International Conference on Data Mining, 2008</a>
<span class="snippet">Implicit Feedbackなデータに特化したMatrix Factorization (MF)、Weighted Matrix Factorization (WMF)を提案。ユーザのExplicitなFeedback（ratingやlike, dislikeなど）がなくても、MFが適用可 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/292">Simulated Analysis of MAUT Collaborative Filtering for Learning Object Recommendation, Manouselis+, Social Information Retrieval for Technology-Enhanced Learning & Exchange, 2007</a>
<span class="snippet">教員に対して教材を推薦しようという試み（学生ではないようだ）。教員は、learning resourcesに対して、multi-criteriaなratingを付与することができ、それをCFで活用する（CELEBRATE web portalというヨーロッパのポータルを使用したらしい）。CF ...</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/RelevanceFeedback.html">#RelevanceFeedback</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/WebSearch.html">#WebSearch</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/566">Adaptive Web Search Based on User Profile Constructed without Any Effort from Users, Sugiyama+, NAIST, WWW’04</a>
<span class="snippet">検索結果のpersonalizationを初めてuser profileを用いて実現した研究user profileはlong/short term preferenceによって構成される。long term: さまざまなソースから取得されるshort term: 当日のセッショ ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/ItemBased.html">#ItemBased</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/179">Item-based collaborative filtering recommendation algorithms, Sarwar+（with Konstan）, WWW01</a>
<span class="snippet">アイテムベースな協調フィルタリングを提案した論文（GroupLens） ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
