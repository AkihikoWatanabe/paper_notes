---
layout: post
title: InformationRetrievalに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## InformationRetrieval
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><a class="button" href="articles/NaturalLanguageUnderstanding.html">#NaturalLanguageUnderstanding</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/821">Direct Fact Retrieval from Knowledge Graphs without Entity Linking, ACL23</a>
<span class="snippet"><span>Summary</span>従来の知識取得メカニズムの制限を克服するために、我々はシンプルな知識取得フレームワークであるDiFaRを提案する。このフレームワークは、入力テキストに基づいて直接KGから事実を取得するものであり、言語モデルとリランカーを使用して事実のランクを改善する。DiFaRは複数の事実取得タスクでベースラインよりも優れた性能を示した。</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/799">Large Language Models are Effective Text Rankers with Pairwise Ranking  Prompting, Zhen Qin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLMsを使用してドキュメントをランキングする際に、Pairwise Ranking Prompting（PRP）という新しい技術を提案する。PRPは、LLMsへの負荷を軽減し、最先端のランキングパフォーマンスを達成することができる。具体的には、20Bパラメータを持つFlan-UL2モデルに基づくPRPは、商用のGPT-4に基づく従来の手法を上回る結果を示した。さらに、PRPのバリアントを提案し、効率を改善することができることを示した。PRPは生成とスコアリングのLLM APIの両方をサポートし、入力の順序に対して無感度であることも示された。</span>
<span class="snippet"><span>Comment</span>open source LLMをスタンダードなベンチマークでSoTAを達成できるようなprompting技術を提案 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2018-02-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/259">Deep Learning for Personalized Search and Recommender Systems, KDD17</a>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/200">Online Learning to Rank for Information Retrieval, Grotov+, SIGIR16</a>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/MultitaskLearning.html">#MultitaskLearning</a><a class="button" href="articles/QueryClassification.html">#QueryClassification</a><a class="button" href="articles/WebSearch.html">#WebSearch</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/249">Representation Learning Using Multi-Task Deep Neural Networks for Semantic Classification and Information Retrieval, Liu+, NAACL-HLT15</a>
<span class="snippet"><span>Comment</span>クエリ分類と検索をNeural Netを用いてmulti-task learningする研究分類(multi-class classification)とランキング(pairwise learning-to-rank)という異なる操作が必要なタスクを、multi task learningの枠組みで ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/199">Contextual Dueling Bandits, Dudik+, JMLR15</a>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/186">Machine Learning for Information Retrieval, Hofmann, ESSIR15</a>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Contents-based.html">#Contents-based</a><br><span class="issue_date">Issue Date: 2021-06-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/364">Learning Deep Structured Semantic Models  for Web Search using Clickthrough Data, Huang+, CIKM13</a>
<span class="snippet"><span>Comment</span>日本語解説: https://shunk031.me/paper-survey/summary/others/Learning-Deep-Structured-Semantic-Models-for-Web-Search-using-Clickthrough-Data ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><a class="button" href="articles/Interleaved.html">#Interleaved</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/198">Reusing Historical Interaction Data for Faster Online Learning to Rank for IR, Hofmann+, WSDM13</a>
<span class="snippet"><span>Comment</span>#197 DBGDを拡張した手法を提案している。アルゴリズムが細かく書いてあるので、追っていくとDBGD等について理解が深まると思われる。Interleavemethodについても。 ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/OnlineEvaluation.html">#OnlineEvaluation</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/184">Practical Online Retrieval Evaluation, SIGIR11, Tutorial</a>
<a class="button" href="articles/Comments.html">#Comments</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/228">Ranking Comments on Social Web, Hsu+, CSE09</a>
<span class="snippet"><span>Comment</span>Learning to Rankによってコメントをランキングする手法を提案。これにより、低品質なコメントははじき、良質なコメントをすくいとることができる。素性としては、主にユーザに基づく指標（ユーザが作成した記事の数、プロフィールが何度閲覧されたかなど）と、コメントのContentに基づく指 ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/197">Interactively Optimizing Information Retrieval Systems as a Dueling Bandits Problem, Yue+, ICML09</a>
<span class="snippet"><span>Comment</span>online learning to rankに関する論文でよくreferされる論文提案手法は、Dueling Bandit Gradient Descent(DBGD)と呼ばれる.onlineでlearning to rankを行える手法で、現在の重みwとwをランダムな方向に動かし ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Interleaved.html">#Interleaved</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/203">How Does Clickthrough Data Reflect Retrieval Quality?, Radlijnski+, CIKM08</a>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/202">Fast Learning of Document Ranking Functions with the Committee Perceptrion, Elsas+, WSDM08</a>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/ListWise.html">#ListWise</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/194">Listwise Approach to Learning to Rank - Theory and Algorithm （ListMLE）, Xia+, ICML2008</a>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/ListWise.html">#ListWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/193">Learning to Rank: From Pairwise Approach to Listwise Approach （ListNet）, Cao+, ICML2007</a>
<span class="snippet"><span>Comment</span>解説スライド：http://www.nactem.ac.uk/tsujii/T-FaNT2/T-FaNT.files/Slides/liu.pdf解説ブログ：https://qiita.com/koreyou/items/a69750696fd0b9d88608従来行われてきたLearning t ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/123">A support vector method for Optimizing Average Precision, Yue+, SIGIR07</a>
<span class="snippet"><span>Comment</span>SVM-MAPの論文構造化SVMを用いて、MAPを直接最適化する。 ...</span>
<a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/Comments.html">#Comments</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/230">Leave a Reply: An Analysis of Weblog Comments, Mishne+, WWW06</a>
<span class="snippet"><span>Comment</span>従来のWeblog研究では、コメントの情報が無視されていたが、コメントも重要な情報を含んでいると考えられる。この研究では、以下のことが言及されている。* （収集したデータの）ブログにコメントが付与されている割合やコメントの長さ、ポストに対するコメントの平均などの統計量* ブログ検索に相当流し ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/PairWise.html">#PairWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/192">Learning to Rank using Gradient Descent （RankNet）, Burges+, ICML2005</a>
<span class="snippet"><span>Comment</span>pair-wiseのlearning2rankで代表的なRankNet論文解説ブログ：https://qiita.com/sz_dr/items/0e50120318527a928407lossは2個のインスタンスのpair、A, Bが与えられたとき、AがBよりも高くランクされる場合は確 ...</span>
<a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/PointWise.html">#PointWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/190">PRanking with Ranking, Crammer+, NIPS01</a>
<span class="snippet"><span>Comment</span>Point-WiseなLearning2Rankの有名手法 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><br><span class="issue_date">Issue Date: 2018-01-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/243">The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries, Carbonell+, SIGIR98</a>
<span class="snippet"><span>Comment</span>Maximal Marginal Relevance (MMR) 論文。検索エンジンや文書要約において、文書/文のランキングを生成する際に、既に選んだ文書と類似度が低く、かつqueryとrelevantな文書をgreedyに選択していく手法を提案。ILPによる定式化が提案される以前のMult ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/RetrievalAugmentedGeneration.html">#RetrievalAugmentedGeneration</a><br><span class="issue_date">Issue Date: 2023-11-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1118">Retrieval-based LM （RAG System）ざっくり理解する, 2023</a>
<span class="snippet"><span>Comment</span>（以下スクショはスライドより引用）次のスクショはRAGにかかわる周辺技術がよくまとまっていると思う。以下ざっくり私の中の認識として計画    クエリ拡張        クエリの質が悪い場合検索性能が劣化するため、クエリをより適切に検索ができるように修正（昔 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/35f9f589-770c-435b-8d1b-81e615e86597" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/576">Measuring the impact of online personalisation: Past, present and future</a>
<span class="snippet"><span>Comment</span>Personalizationに関するML, RecSys, HCI, Personalized IRといったさまざまな分野の評価方法に関するSurveyML + RecSys系では、オフライン評価が主流であり、よりaccuracyの高い推薦が高いUXを実現するという前提に基づいて評価されて ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/572">Preface to Special Issue on User Modeling for Web Information Retrieval, Brusilovsky+, User Modeling and User-Adapted Interaction , 2004</a>
<span class="snippet"><span>Comment</span>Personalized Information Retrievalの先駆け的研究#566 と同時期 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/567">User Profiles for Personalized Information Access, Gauch+, The adaptive Web: methods and strategies of Web personalization, 2007</a>
<span class="snippet"><span>Comment</span>IR分野におけるuser profileの構築方法についてまとめられたsurvey加重キーワードセマンティックネットワーク加重コンセプトについて記述されている。また、プロファイルの構築方法についても詳述されている。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/RelevanceFeedback.html">#RelevanceFeedback</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/WebSearch.html">#WebSearch</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/566">Adaptive Web Search Based on User Profile Constructed without Any Effort from Users, Sugiyama+, NAIST, WWW’04</a>
<span class="snippet"><span>Comment</span>検索結果のpersonalizationを初めてuser profileを用いて実現した研究user profileはlong/short term preferenceによって構成される。long term: さまざまなソースから取得されるshort term: 当日のセッショ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/565">Awesome Vector Search Engine</a>
<span class="snippet"><span>Comment</span>ベクトルの類似度を測るサービスやライブラリ等がまとまったリポジトリ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/540">Contrirver</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-04-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/521">Llamaindex</a>
<span class="snippet"><span>Comment</span>LlamaIndexのインデックスを更新し、更新前後で知識がアップデートされているか確認してみた  https://dev.classmethod.jp/articles/llama-index-insert-index/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-04-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/520">LangChain</a>
<span class="snippet"><span>Comment</span>LangChain の Googleカスタム検索 連携を試す  https://note.com/npaka/n/nd9a4a26a8932LangChainのGetting StartedをGoogle Colaboratoryでやってみる ④Agents    https://zenn.de ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/RelevanceFeedback.html">#RelevanceFeedback</a><a class="button" href="articles/ImplicitFeedback.html">#ImplicitFeedback</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/205">Evaluating implicit measures to improve web search, Fox+, ACM Transactions on Imformation Systems, 2005</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/RelevanceFeedback.html">#RelevanceFeedback</a><a class="button" href="articles/ExplicitFeedback.html">#ExplicitFeedback</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/204">A survey on the use of relevance feedback for information access systems., Ruthven+, The Knowledge Engineering Review, 2003</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/201">Lerot: Online Learning to rank Framework</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/196">Fast and Reliable Online Learning to Rank for Information Retrieeval, Katja Hofmann, Doctoral Thesis, 2013</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/ListWise.html">#ListWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/195">A General Approximation Framework for Direct Optimization of Information Retrieval Measures （ApproxAP, ApproxNDCG）, Qin+, Information Retrieval, 2010</a>
<span class="snippet"><span>Comment</span>実装してみたが、バグありそう感・・・https://github.com/AkihikoWatanabe/ApproxAP ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/PairWise.html">#PairWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/191">Large Scale Learning to Rank, Sculley+, NIPS 2009</a>
<span class="snippet"><span>Comment</span>sofia-mlの実装内容について記述されている論文よくonline学習の文脈で触れられるが、気をつけないと罠にはまる。というのは、sofia-ml内のMethodsによって、最適化している目的関数が異なるからだ。実装をみると、全てのmethodsがonlineでできちゃいそうに見え ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/189">From RankNet to LambdaRank to LambdaMART: An Overview, Burges, Microsoft Research Technical Report, 2010</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/188">Confidence Weightedでランク学習を実装してみた</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/187">ランキング学習ことはじめ, DSIRNLP#1, 2011</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/185">Learning to Rank for Information Retriefval, Liu+, 2009</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/124">SVM-MAP</a>
<span class="snippet"><span>Comment</span>構造化SVMを用いて、MAPを直接最適化する手法 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RelevanceJudgment.html">#RelevanceJudgment</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/51">Relevance judgment: What do information users consider beyond topicality? Xu, Chen, 2007</a>
<span class="snippet"><span>Comment</span>・relevanceとsignificantに関連するcriteriaは，topicalityとnovelty・reliabilityおよびunderstandabilityはsmaller degreeでsignificant, scopeはsignificantでない ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RelevanceJudgment.html">#RelevanceJudgment</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/50">A cognitive model of document use during a research project, Wang and Soergel, 1998</a>
<span class="snippet"><span>Comment</span>topicality, orientation, quality, novelty（の順番で）がrelevantなdocumentを選択したときのcriteriaとして採用されていたことを報告 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/20">Personalizing Search via Automated Analysis of Interests and Activities, SIGIR, Teevan+, 2005</a>
<span class="snippet"><span>Comment</span>・userに関するデータがrichなほうが、Personalizationは改善する。・queries, visited web pages, emails, calendar items, stored desktop 　　　　documents、全てのsetを用いた場合が最も良かった ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/13">Personalised Information retrieval: survey and classification, Rami+, 2013</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34402162-5433e4e4-ebe3-11e7-8bf3-fc322ace70d8.png)![image](https://user-images.githubuse完 ...</span>
<a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/11">Modeling Anchor Text and Classifying Queries to Enhance Web Document Retrieval, WWW’08, Fujii, 2008</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34401828-1259be4c-ebe1-11e7-99c4-33508b405bf1.png)![image](https://user-images.githubuse ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
