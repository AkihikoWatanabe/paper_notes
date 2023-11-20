---
layout: post
title: GraphBasedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## GraphBased
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><a class="button" href="articles/Prompting.html">#Prompting</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1061">Graph Neural Prompting with Large Language Models, Yijun Tian+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を知識グラフと組み合わせるための新しい手法であるGraph Neural Prompting（GNP）を提案しています。GNPは、標準的なグラフニューラルネットワークエンコーダやクロスモダリティプーリングモジュールなどの要素から構成されており、異なるLLMのサイズや設定において、常識的な推論タスクやバイオメディカル推論タスクで優れた性能を示すことが実験によって示されました。</span>
<span class="snippet"><span>Comment</span>以下elvis氏のツイートの意訳事前学習されたLLMがKGから有益な知識を学習することを支援する手法を提案。元ツイート: https://arxiv.org/abs/2309.15427しっかり論文を読んでいないが、freezeしたLLMがあった時に、KGから求めたGraph Neural Prom ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/434daf26-f82f-43b9-8807-13517975383b" alt="image"><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/545">Graph Collaborative Signals Denoising and Augmentation for  Recommendation, Ziwei Fan+, N_A, SIGIR23</a>
<span class="snippet"><span>Summary</span>グラフ協調フィルタリング（GCF）は、推薦システムで人気のある技術ですが、相互作用が豊富なユーザーやアイテムにはノイズがあり、相互作用が不十分なユーザーやアイテムには不十分です。また、ユーザー-ユーザーおよびアイテム-アイテムの相関を無視しているため、有益な隣接ノードの範囲が制限される可能性があります。本研究では、ユーザー-ユーザーおよびアイテム-アイテムの相関を組み込んだ新しいグラフの隣接行列と、適切に設計されたユーザー-アイテムの相互作用行列を提案します。実験では、改善された隣接ノードと低密度を持つ強化されたユーザー-アイテムの相互作用行列が、グラフベースの推薦において重要な利点をもたらすことを示しています。また、ユーザー-ユーザーおよびアイテム-アイテムの相関を含めることで、相互作用が豊富なユーザーや不十分なユーザーに対する推薦が改善されることも示しています。</span>
<span class="snippet"><span>Comment</span>グラフ協調フィルタリングを改善グラフ協調フィルタリング（下記ツイッターより引用）user-item間の関係だけでなく、user-user間とitem-item間の情報を組み込むことで精度向上を達成した論文とのこと。https://twitter.com/nogawanogawa/status ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b0f099c2-8e9d-4ebc-aa1b-d4af49509a37" alt="image"><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/530">Graph Neural Networks for Text Classification: A Survey, Wang+, arXiv23</a>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/311">Graph Convolutional Neural Networks for Web-Scale Recommender Systems, Ying+, KDD18</a>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/312">Modeling Relational Data with Graph Convolutional Networks, Michael Schlichtkrull+, N_A, arXiv17</a>
<span class="snippet"><span>Summary</span>知識グラフは不完全な情報を含んでいるため、関係グラフ畳み込みネットワーク（R-GCNs）を使用して知識ベース補完タスクを行う。R-GCNsは、高度な多関係データに対処するために開発されたニューラルネットワークであり、エンティティ分類とリンク予測の両方で効果的であることを示している。さらに、エンコーダーモデルを使用してリンク予測の改善を行い、大幅な性能向上が見られた。</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/130">Graph-based Neural Multi-Document Summarization, Yasunaga+, arXiv17</a>
<span class="snippet"><span>Comment</span>Graph Convolutional Network (GCN)を使って、MDSやりましたという話。 既存のニューラルなMDSモデル [Cao et al., 2015, 2017] では、sentence間のrelationが考慮できていなかったが、GCN使って考慮した。 また、MDSの学習デー ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/144">CTSUM: Extracting More Certain Summaries for News Articles, Wan+, SIGIR14</a>
<span class="snippet"><span>Comment</span>要約を生成する際に、情報の”確実性”を考慮したモデルCTSUMを提案しましたという論文（今まではそういう研究はなかった）```"However, it seems that Obama will not use the platform to relaunch his stalled d解説ス ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/4">Collaborative Summarization: When Collaborative Filtering Meets Document Summarization, Qu+, PACLIC09, 6</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34400963-26dc2ee2-ebda-11e7-8170-2aa5fcc701c1.png)Collaborative Filteringと要約を組み合わせる手評価1 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Comments.html">#Comments</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/10">Comments-Oriented Blog Summarization by Sentence Extraction, CIKM07, Hu+, 2007</a>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/180">Folkrank: A ranking algorithm for folksonomies, Hotho+, FGIR06</a>
<span class="snippet"><span>Comment</span>代表的なタグ推薦手法 ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/214">TextRank: Bringing Order into Texts, Mihalcea+, EMNLP04</a>
<span class="snippet"><span>Comment</span>PageRankベースの手法で、キーワード抽出/文書要約 を行う手法。キーワード抽出/文書要約 を行う際には、ノードをそれぞれ 単語/文 で表現する。ノードで表現されている 単語/文 のsimilarityを測り、ノード間のedgeの重みとすることでAffinity Graphを構築。あ単一文 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/310">Representation Learning on Graphs: Methods and Applications, Hamilton+, 2017</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/215">LexRank: Graph-based Lexical Centrality as Salience in Text Summarization, Erkan+, Journal of Artificial Intelligence Research, 2004</a>
<span class="snippet"><span>Comment</span>代表的なグラフベースな(Multi) Document Summarization手法。ほぼ #214 と同じ手法。2種類の手法が提案されている：* [LexRank] tf-idfスコアでsentenceのbag-of-wordsベクトルを作り、cosine similarit ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Comments.html">#Comments</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/9">Comments-Oriented Document Summarization: Understanding Documents with Reader’s Feedback SIGIR’08, Hu+, 2008</a>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
