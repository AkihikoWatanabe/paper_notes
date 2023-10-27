---
layout: post
title: StudentPerformancePredictionに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## StudentPerformancePrediction
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-10-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/418">SAINT+: Integrating Temporal Features for EdNet Correctness Prediction, Shin+, RiiiD AI Research, LAK21</a>
<span class="snippet">Student Performance PredictionにTransformerを初めて利用した研究![image](https://user-images.githubusercontent.com/12249301/139178783-ae4d4e2d-9fc5-44f5-9769- ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/353">EKT: Exercise-aware Knowledge Tracing for Student Performance Prediction, Hu+, IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, 2019</a>
<span class="snippet">スキルタグごとにLSTMのhidden_stateを保持しないといけないので、メモリの消費量がえぐいことになりそう。小規模なスキルタグのデータセットじゃないと動かないのでは？実際、実験では37種類のスキルタグが存在するデータセットしか扱っていない。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-10-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/417">A Self-Attentive model for Knowledge Tracing, Pandy+ （with George Carypis）, EDM19</a>
<span class="snippet">#446 においてはSAKTがDKT, DKVMN等に勝てていないのに対し（ASSSITments Data + Statics Data）#450 #452  においてはSAKTはDKT, DKVMNに勝っている（EdNet Data）#451 においてもSAKTがDKTに勝てないことが報 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/354">Exercise-Enhanced Sequential Modeling for Student Performance Prediction, Hu+, AAAI18</a>
<span class="snippet">従来のStudent Performance PredictionタスクではKnowledge Componentと問題に対する過去の正誤を入力として予測を行っていて、問題テキストを通じて得られる問題そのものの難しさは明示的に考慮できていなかった。なので、knowledge componentで ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/421">Addressing Two Problems in Deep Knowledge Tracing via Prediction-Consistent Regularization, Yeung+, 2018, L@S</a>
<span class="snippet"><img width="639" alt="image" src="https://user-images.githubusercontent.com/12249301/167774315-061e9d8d-16ae-4c56-b69f-e8ef1968b4fa.png">DKT+とDKTの ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-11-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/432">Modeling Hint-Taking Behavior and Knowledge State of Students with Multi-Task Learning, Chaudry+, Indian Institute of Technology, EDM18</a>
<span class="snippet">DKVMN (#352)をhint-takingタスクとmulti-task learningした研究![image](https://user-images.githubusercontent.com/12249301/141440172-6f708367-1804-4b0c-8c1a-4 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/352">Dynamic Key-Value Memory Networks for Knowledge Tracing, Yeung+, WWW17</a>
<span class="snippet">モデルは下図の左側と右側に分かれる。左側はエクササイズqtに対する生徒のパフォーマンスptを求めるネットワークであり、右側はエクササイズqtに対する正誤情報rtが与えられた時に、メモリのvalueを更新するネットワークである。![image](https://user-images.gith ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/361">The Knowledge-Learning-Instruction Framework: Bridging the Science-Practice Chasm to Enhance Robust Student Learning, Pelanek, User Modeling and User-Adapted Interaction, 2017</a>
<span class="snippet">BKT、PFAや、それらを用いるContext（どのモデルをどのように自分のcontextに合わせて選択するか）、KLI Frameworkに基づくKCの構成のされ方、モデル評価方法等を理解したい場合、読んだほうが良さそう？ざっとしか見ていないけど、重要な情報がめちゃめちゃ書いてありそう。後でし ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/355">How Deep is Knowledge Tracing?, Mozer+, EDM16</a>
<span class="snippet">BKT+Forgetsは、ある特定のスキルの間に何回のtrialがあったかを数えておき、そのfrialの機会ごとにForgetが生じる機会が生じると考えるような定式化になっている。たとえば、A_1 A_2 B_1 A_3 B_2 B_3 A_4 という問題の系列があったと ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/356">Going Deeper with Deep Knowledge Tracing, Beck+, EDM16</a>
<span class="snippet">ASSISTmentsデータにはduplicate records問題以外にも、複数種類のスキルタグが付与された問題があったときに、1つのスキルタグごとに1レコードが列挙されるようなデータになっている点が、BKTと比較してDKTが有利だった点として指摘している。スキルA, Bが付与されている問題が２ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/358">Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation, Ekanadham+, EDM16</a>
<span class="snippet">なお、論文の著者であるKnewton社のKevin H. Wilson氏はすでにknewton社を退職されている。https://kevinhayeswilson.com/ ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/297">Deep Knowledge Tracing, Piech+, NIPS, 2015</a>
<span class="snippet">DKTのinputの次元数が 2 * num_skills, outputの次元数がnum_skillsだと明記されているスライド。元論文だとこの辺が言及されていなくてわかりづらい・・・http://gdac.uqam.ca/Workshop@EDM20/slides/LSTM_tutori ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/420">General Features in Knowledge Tracing: Applications to Multiple Subskills, Temporal Item Response Theory, and Expert Knowledge, Brusilovsky+, EDM14</a>
<span class="snippet">実装：https://github.com/ml-smores/fastただし、GPL-2.0ライセンス ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/296">Improving Matrix Factorization Techniques of Student Test Data with Partial Order Constraints, Beheshti+, UMAP, 2012</a>
<span class="snippet">各knowledgeのpre-requisiteを、MFでうまく分解することで自動で学習することができる。んー詳細な数式書いてないし、評価していない。が、考え方はおもしろい。 ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/295">Factorization Models for Forecasting Student Performance, Thai-Nghe+, EDM, 2011</a>
<span class="snippet">TensorFactorizationで、欠損値を予測cold-start problem（new-user, new item）への対処としては、global averageをそれぞれ用いることで対処（more sophisticatedなやり方が提案されているとも述べている）使用して ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/357">Behavior-Based Grade Prediction for MOOCs Via Time Series Neural Networks, Chiang+, IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING, VOL. 11, NO. 5, AUGUST 2017</a>
<span class="snippet">NFMB/NI #358 データセットを利用している ...</span>
<a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/427">Multi-Relational Factorization Models for Predicting Student Performance, Nguyen+, KDD Cup11</a>
<span class="snippet">過去のCollaborative Filteringを利用したStudent Performance Prediction (#426 など)では、単一の関係性（student-skill, student-task等の関係）のみを利用していたが、この研究では複数の関係性（task-required ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/426">Collaborative Filtering Applied to Educational Data Mining, Andreas+, KDD Cup10</a>
<span class="snippet">KDD Cup'10のStudent Performance Predictionタスクにおいて3位をとった手法メモリベースドな協調フィルタリングと、Matirx Factorizationモデルを利用してStudent Performance Predictionを実施。最終的にこれらのモ ...</span>
<a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/360">Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge, Corbett+, User Modeling and User-Adapted Interaction, 1995</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/120093822-b7820880-c157-11eb-9c6e-9a2c5a5eb262.png)(from wikipedia)![image](http ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/359">Student Performance Prediction _ Knowledge Tracing Dataset</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/419">HMM Scalable （Bayesian Knowledge Tracing; BKT）</a>
<span class="snippet">BKTを高速で学習できるツール3-clause BSD license ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
