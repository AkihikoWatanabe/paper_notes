---
layout: post
title: LearningAnalyticsに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## LearningAnalytics
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/453">Empirical Evaluation of Deep Learning Models for Knowledge Tracing: Of Hyperparameters and Metrics on Performance and Replicability, Sami+, Aalto University, arXiv22</a>
<span class="snippet">この研究では、KTする際に全てのDeep Learning basedなモデル（DKT, DKVMN, SAKT）において、入力の系列をx_tを(s_t, c_t)で表現し検証している。s_tはスキルタグで、c_tは正解したか否か。outputも output-per-skill の場合は、スキ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/DropoutPrediction.html">#DropoutPrediction</a><br><span class="issue_date">Issue Date: 2022-04-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/443">Deep Attentive Study Session Dropout Prediction in Mobile Learning Environment, Riiid AI Research, Lee+, arXiv21</a>
<span class="snippet">従来のdropout研究では、学校のドロップアウトやコースのドロップアウト、MOOCsなどでのドロップアウトが扱われてきたが、モバイル学習環境を考慮した研究はあまり行われてこなかった。モバイル学習環境では着信やソーシャルアプリなど、多くの外敵要因が存在するため、学習セッションのドロップアウトが頻繁に ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/448">A Survey of Knowledge Tracing, Liu+, arXiv21</a>
<span class="snippet">古典的なBKT, PFAだけでなくDKT, DKVMN, EKT, AKTなどDeepなモデルについてもまとまっている。![image](https://user-images.githubusercontent.com/12249301/165438026-70f407c9-8eb2-43c3 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/450">An Empirical Comparison of Deep Learning Models for Knowledge Tracing on Large-Scale Dataset, Pandey+, AAAI workshop on AI in Education21</a>
<span class="snippet">EdNetデータにおいて、DKT, DKVMN, SAKT, RKTの性能を比較した論文![image](https://user-images.githubusercontent.com/12249301/165658767-24fda9a1-3ff1-47d1-b328-91fa18aec8 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/452">Do we need to go Deep? Knowledge Tracing with Big Data, Varun+, University of Maryland Baltimore County, arXiv21</a>
<span class="snippet">データ量が小さいとSAKTはDKTはcomparableだが、データ量が大きくなるとSAKTがDKTを上回る。![image](https://user-images.githubusercontent.com/12249301/165698674-279a7e0c-6429-48db-8c ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/454">BEKT: Deep Knowledge Tracing with Bidirectional Encoder Representations from Transformers, Tian+ （緒方先生）, Kyoto University, ICCE21</a>
<span class="snippet">KTにBERTを利用した研究#453 などでDeepLearningBasedなモデル間であまり差がないことが示されているので、本研究が実際どれだけ強いのかは気になるところ。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-05-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/456">Learning Process-consistent Knowledge Tracing, Shen+, SIGKDD21</a>
<span class="snippet">KCのproficiencyの可視化方法について論文中に記述されていないが、Issueで質問されている。https://github.com/bigdata-ustc/EduKTM/issues/29knowledge matrix hは各KCのproficiencyに関する情報をベクト ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/Assessment.html">#Assessment</a><br><span class="issue_date">Issue Date: 2022-04-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/444">Assessment Modeling: Fundamental Pre-training Tasks for Interactive Educational Systems, Choi+, RiiiD Research, arXiv 2020</a>
<span class="snippet"># 概要テストのスコアや、gradeなどはシステムの外側で取得されるものであり、取得するためにはコストがかかるし、十分なラベル量が得られない（label-scarce problem）。そこで、pre-training/fine-tuningの手法を用いて、label-scarce proble ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/446">Context-Aware Attentive Knowledge Tracing, Ghosh+, University of Massachusetts Amherst, KDD20</a>
<span class="snippet">この論文の実験ではSAKTがDKVMNやDKTに勝てていない ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/451">When is Deep Learning the Best Approach to Knowledge Tracing?, Theophile+ （Ken Koedinger）, CMU+, JEDM20</a>
<span class="snippet">DKTは、inputとしてquestion_idを使うかKCのidを使うか選択できる。また、outputもquestion_idに対するprobabilityをoutputするか、KCに対するprobabilityをoutputするか選択できる。これらの組み合わせによって、予測性能がどの程度変化 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/353">EKT: Exercise-aware Knowledge Tracing for Student Performance Prediction, Hu+, IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, 2019</a>
<span class="snippet">スキルタグごとにLSTMのhidden_stateを保持しないといけないので、メモリの消費量がえぐいことになりそう。小規模なスキルタグのデータセットじゃないと動かないのでは？実際、実験では37種類のスキルタグが存在するデータセットしか扱っていない。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/455">Knowledge Tracing with Sequential Key-Value Memory Networks, Ghodai+, Research School of Computer Science, Australian National University, SIGIR19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/354">Exercise-Enhanced Sequential Modeling for Student Performance Prediction, Hu+, AAAI18</a>
<span class="snippet">従来のStudent Performance PredictionタスクではKnowledge Componentと問題に対する過去の正誤を入力として予測を行っていて、問題テキストを通じて得られる問題そのものの難しさは明示的に考慮できていなかった。なので、knowledge componentで ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/361">The Knowledge-Learning-Instruction Framework: Bridging the Science-Practice Chasm to Enhance Robust Student Learning, Pelanek, User Modeling and User-Adapted Interaction, 2017</a>
<span class="snippet">BKT、PFAや、それらを用いるContext（どのモデルをどのように自分のcontextに合わせて選択するか）、KLI Frameworkに基づくKCの構成のされ方、モデル評価方法等を理解したい場合、読んだほうが良さそう？ざっとしか見ていないけど、重要な情報がめちゃめちゃ書いてありそう。後でし ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/AffectDetection.html">#AffectDetection</a><br><span class="issue_date">Issue Date: 2021-06-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/380">Improving Sensor-Free Affect Detection Using Deep Learning, Botelho+, AIED17</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/123304125-84197a80-d559-11eb-9ed8-67fa809b506c.png)従来手法を大幅にoutperform。しっかり読んでいないが、resa ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-06-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/385">Deep Model for Dropout Prediction in MOOCs, Wang+, ICCSE17</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/121488518-18d69100-ca0e-11eb-9c1f-23831c818d09.png)評価の結果、予測結果は他の既存手法とcomparableな性能を達成し ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/355">How Deep is Knowledge Tracing?, Mozer+, EDM16</a>
<span class="snippet">BKT+Forgetsは、ある特定のスキルの間に何回のtrialがあったかを数えておき、そのfrialの機会ごとにForgetが生じる機会が生じると考えるような定式化になっている。たとえば、A_1 A_2 B_1 A_3 B_2 B_3 A_4 という問題の系列があったと ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/356">Going Deeper with Deep Knowledge Tracing, Beck+, EDM16</a>
<span class="snippet">ASSISTmentsデータにはduplicate records問題以外にも、複数種類のスキルタグが付与された問題があったときに、1つのスキルタグごとに1レコードが列挙されるようなデータになっている点が、BKTと比較してDKTが有利だった点として指摘している。スキルA, Bが付与されている問題が２ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/358">Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation, Ekanadham+, EDM16</a>
<span class="snippet">なお、論文の著者であるKnewton社のKevin H. Wilson氏はすでにknewton社を退職されている。https://kevinhayeswilson.com/ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/445">Estimating student proficiency: Deep learning is not the panacea, Wilson+, Knewton+, NIPS16 workshop</a>
<span class="snippet">DKTの性能をBKTやPFA等の手法と比較した研究#355 を引用し、DKTとBKTのAUCの計算方法の違いについて言及している ...</span>
<a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2021-07-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/400">Autonomously Generating Hints by Inferring Problem Solving Policies, Piech+, Stanford University, L@S15</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/294">Educational Data Mining and Learning Analytics, Baker+, 2014</a>
<span class="snippet">Ryan BakerらによるEDM Survey ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/DropoutPrediction.html">#DropoutPrediction</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/424">Predicting MOOC Dropout over Weeks Using Machine Learning Methods, EMNLP14 Workshop, Marius Kloft</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/139363086-1df1ab46-c1ed-4a2a-a72d-d310b3101b8f.png)最初の1 -9週の間は、あまりDropoutが予測できないが、それ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/357">Behavior-Based Grade Prediction for MOOCs Via Time Series Neural Networks, Chiang+, IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING, VOL. 11, NO. 5, AUGUST 2017</a>
<span class="snippet">NFMB/NI #358 データセットを利用している ...</span>
<a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/360">Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge, Corbett+, User Modeling and User-Adapted Interaction, 1995</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/120093822-b7820880-c157-11eb-9c6e-9a2c5a5eb262.png)(from wikipedia)![image](http ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2022-03-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/438">①ラーニングアナリティクスの研究動向 ─エビデンスに基づく教育の実現に向けて─, 京都大学, 緒方先生, 情報処理 Vol.59 No.9 Sep. 2018</a>
<span class="snippet">2021年版スライド：https://www.let.media.kyoto-u.ac.jp/wp-content/uploads/2021/07/603b542fafc54003eb4a1a42bb92069f.pdf典型的な研究事例：・At-risk学生の発見と成績予測(earl ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><br><span class="issue_date">Issue Date: 2021-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/422">ラーニング・アナリティクスとは何か？, 武田俊之, コンピュータ＆エデュケーション VOL.38, 2015</a>
<span class="snippet">Learning Analyticsの全体像について、コンパクトにまとまっている。特に、そのアプローチに関するコンセプトの特徴（e.g. 学習者中心、デーア駆動）や、フレームワーク、xAPIといったデータの測定・収集方法などについて、まとめられている。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-06-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/368">Deep Knowledge Tracingの拡張による擬似知識タグの生成, 中川+, 人口知能学会論文誌, 33巻, 33号, C, 2018</a>
<span class="snippet">DKTモデルは、前提として各問題に対して知識タグ（knowledge component）が付与されていることが前提となっている。しかし世の中には、知識タグが振られているデータばかりではないし、そもそもプログラミング教育といった伝統的な教育ではない分野については、そもそも知識タグを構造的に付与するこ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/359">Student Performance Prediction _ Knowledge Tracing Dataset</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/449">局所的変分法による非補償型時系列IRT, 玉野+ （持橋さん）, NEC+, 人工知能学会研究会資料</a>
<span class="snippet">No description ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
