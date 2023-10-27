---
layout: post
title: MatrixFactorizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## MatrixFactorization
<div class="visible-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2018-02-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/260">Neural Collaborative Filtering, He+, WWW17</a>
<span class="snippet">Collaborative FilteringをMLPで一般化したNeural Collaborative Filtering、およびMatrix Factorizationはuser, item-embeddingのelement-wise product + linear transofmrat ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/221">Collaborative Deep Learning for Recommender Systems Wang+, KDD’15</a>
<span class="snippet">解説ブログ：http://d.hatena.ne.jp/repose/20150531/1433004688 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/224">Deep content-based music recommendation, Oord+, NIPS13</a>
<span class="snippet">Contents-Basedな音楽推薦手法(cold-start problemに強い)。Weighted Matrix Factorization (WMF) (Implicit Feedbackによるデータに特化したMatrix Factorization手法) #225 に、Convolu ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/27">Multi-relational matrix factorization using bayesian personalized ranking for social network data, Krohn-Grimberghe+, WSDM12</a>
<span class="snippet">multi-relationalな場合でも適用できるmatrix factorizationを提案。特にcold start problemにフォーカス。social networkのデータなどに適用できる。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/223"> SVDFeature: a toolkit for feature-based collaborative filtering, Chen+, JMLR12</a>
<span class="snippet">Ratingの情報だけでなく、Auxiliaryな情報も使ってMatrix Factorizationができるツールを作成した。これにより、Rating Matrixの情報だけでなく、自身で設計したfeatureをMFに組み込んでモデルを作ることができる。![image](https:/ ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/226">Collaborative topic modeling for recommending scientific articles, Wang+, KDD11</a>
<span class="snippet">解説ブログ：http://d.hatena.ne.jp/repose/20150531/1433004688 ...</span>
<a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/427">Multi-Relational Factorization Models for Predicting Student Performance, Nguyen+, KDD Cup11</a>
<span class="snippet">過去のCollaborative Filteringを利用したStudent Performance Prediction (#426 など)では、単一の関係性（student-skill, student-task等の関係）のみを利用していたが、この研究では複数の関係性（task-required ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/426">Collaborative Filtering Applied to Educational Data Mining, Andreas+, KDD Cup10</a>
<span class="snippet">KDD Cup'10のStudent Performance Predictionタスクにおいて3位をとった手法メモリベースドな協調フィルタリングと、Matirx Factorizationモデルを利用してStudent Performance Predictionを実施。最終的にこれらのモ ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/222">Relational learning via collective matrix factorization, Singh+, KDD08</a>
<span class="snippet">従来のMatrix Factorization（MF）では、pair-wiseなrelation（たとえば映画とユーザと、映画に対するユーザのrating）からRating Matrixを生成し、その行列を分解していたが、multipleなrelation（たとえば、user-movie ratin ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/225">Collaborative filtering for implicit feedback datasets, Hu+, International Conference on Data Mining, 2008</a>
<span class="snippet">Implicit #324 でのAlternating Least Square (ALS)という手法が、この手法の実装に該当する。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/227">Probabilistic Matrix Factorization, Salakhutdinov+, NIPS08</a>
<span class="snippet">既存のMFは大規模なデータに対してスケールしなかったが、PMFではobservationの数に対して線形にスケールし、さらには、large, sparse, imbalancedなNetflix datasetで良い性能が出た（Netflixデータセットは、rating件数が少ないユーザとかも含んで ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/217">Probabilistic matrix factorization, Salakhutdinov+, Advances in neural information processing systems, 2007</a>
<span class="snippet">No description ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
