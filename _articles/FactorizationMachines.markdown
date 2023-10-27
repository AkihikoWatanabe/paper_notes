---
layout: post
title: FactorizationMachinesに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## FactorizationMachines
<div class="visible-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2021-07-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/397">Deep Learning Recommendation Model for Personalization and Recommendation Systems, Naumov+, Facebook, arXiv‘19</a>
<span class="snippet">Parallelism以後のセクションはあとで読む ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/282"> xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems, KDD18</a>
<span class="snippet">Gunosyの関さんによるxDeepFMの解説：https://data.gunosy.io/entry/deep-factorization-machines-2018DeepFMの発展についても詳細に述べられていて、とても参考になる。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CTRPrediction.html">#CTRPrediction</a><br><span class="issue_date">Issue Date: 2020-08-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/341">Field Weighted Factorization Machines for Click-Through Rate Prediction in Display Advertising, Pan+, WWW18</a>
<span class="snippet">CTR予測でbest-performingなモデルと言われているField Aware Factorization Machines(FFM)では、パラメータ数がフィールド数×特徴数のorderになってしまうため非常に多くなってしまうが、これをよりメモリを効果的に利用できる手法を提案。FFMとは性能 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CTRPrediction.html">#CTRPrediction</a><br><span class="issue_date">Issue Date: 2021-05-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/348">xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems, Lian+, KDD‘18</a>
<span class="snippet">#281 にも書いたが、下記リンクに概要が記載されている。DeepFMに関する動向：https://data.gunosy.io/entry/deep-factorization-machines-2018 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CTRPrediction.html">#CTRPrediction</a><br><span class="issue_date">Issue Date: 2021-05-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/349">DeepFM: A Factorization-Machine based Neural Network for CTR Prediction, Guo+, IJCAI’17</a>
<span class="snippet">実装: https://github.com/rixwew/pytorch-fm ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/218">Factorization Machines with libFM, Steffen Rendle, TIST12</a>
<span class="snippet">Factorization Machinesの著者実装。FMやるならまずはこれ。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/281">Factorization Machines, Steffen Rendle, ICDM10</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/50376518-fdfedf00-0650-11e9-99c0-060f286de392.png)FMのFeature VectorのExample各featureご ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/150">LibRec</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/151">fastFM</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2021-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/398">DeepなFactorization Machinesの実装たち</a>
<span class="snippet">下記モデルが実装されているすごいリポジトリ。論文もリンクも記載されており、Factorization Machinesを勉強する際に非常に参考になると思う。MITライセンス。各手法はCriteoのCTRPredictionにおいて、AUC0.8くらい出ているらしい。Logistic Re ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
