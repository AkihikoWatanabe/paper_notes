---
layout: post
title: Multiに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Multi
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/VariationalAutoEncoder.html">#VariationalAutoEncoder</a><br><span class="issue_date">Issue Date: 2018-10-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/278">Salience Estimation via Variational Auto-Encoders for Multi-Document Summarization, Li+, AAAI17</a>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/130">Graph-based Neural Multi-Document Summarization, Yasunaga+, arXiv17</a>
<span class="snippet"><span>Comment</span>Graph Convolutional Network (GCN)を使って、MDSやりましたという話。 既存のニューラルなMDSモデル [Cao et al., 2015, 2017] では、sentence間のrelationが考慮できていなかったが、GCN使って考慮した。 また、MDSの学習デー ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/144">CTSUM: Extracting More Certain Summaries for News Articles, Wan+, SIGIR14</a>
<span class="snippet"><span>Comment</span>要約を生成する際に、情報の”確実性”を考慮したモデルCTSUMを提案しましたという論文（今まではそういう研究はなかった）```"However, it seems that Obama will not use the platform to relaunch his stalled d解説ス ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/58">Hierarchical Summarization: Scaling Up Multi-Document Summarization, Christensen+, ACL14</a>
<span class="snippet"><span>Comment</span>## 概要だいぶ前に読んだ。好きな研究。テキストのsentenceを階層的にクラスタリングすることで、抽象度が高い情報から、関連する具体度の高いsentenceにdrill downしていけるInteractiveな要約を提案している。## 手法通常のMDSでのデータセットの規模は上位に紐 ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/InteractivePersonalizedSummarization.html">#InteractivePersonalizedSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1">Summarize What You Are Interested In: An Optimization Framework for Interactive Personalized Summarization, Yan+, EMNLP11, 37</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34400733-97c86614-ebd7-11e7-9fe9-a6b36c726a21.png)ユーザとシステムがインタラクションしながら個人向けの要約を生成するタスク ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/24">Personalized PageRank based Multi-document summarization, Liu+, WSCS 08</a>
<span class="snippet"><span>Comment</span>・クエリがあるのが前提・基本的にPersonalized PageRankの事前分布を求めて，PageRankアルゴリズムを適用する・文のsalienceを求めるモデルと（パラグラフ，パラグラフ内のポジション，statementなのかdialogなのか，文の長さ），クエリとの関連性をはかるr ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ILP.html">#ILP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/241">A study of global inference algorithms in multi-document summarization, Ryan McDonald, ECIR07</a>
<span class="snippet"><span>Comment</span>文書要約をナップサック問題として定式化し、厳密解（動的計画法、ILP Formulation）、近似解(Greedy)を求める手法を提案。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Classic.html">#Classic</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1019">Centroid-based summarization of multiple documents: sentence extraction, utility-based evaluation, and user studies, Radev+, Information Processing & Management04</a>
<span class="snippet"><span>Comment</span>MEAD, Centroid-basedな手法で要約を実施する古典的なMDS手法 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/242">A Formal Model for Information Selection in Multi-Sentence Text Extraction, Filatova+, COLING04</a>
<span class="snippet"><span>Comment</span>初めて文書要約を最大被覆問題として定式化した研究。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/215">LexRank: Graph-based Lexical Centrality as Salience in Text Summarization, Erkan+, Journal of Artificial Intelligence Research, 2004</a>
<span class="snippet"><span>Comment</span>代表的なグラフベースな(Multi) Document Summarization手法。ほぼ #214 と同じ手法。2種類の手法が提案されている：* [LexRank] tf-idfスコアでsentenceのbag-of-wordsベクトルを作り、cosine similarit ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/QueryBiased.html">#QueryBiased</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/57">Query-Chain Focused Summarization, Baumel+, ACL.14</a>
<span class="snippet"><span>Comment</span>[Query-Chain Focused Summarization.pdf](https://github.com/AkihikoWatanabe/paper_notes/files/1590916/Query-Chain.Focused.Summarization.pdf) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/26">Personalized Multi-Document Summarization using N-Gram Topic Model Fusion, Hennig+, SPIM, 2010</a>
<span class="snippet"><span>Comment</span>・unigramの共起だけでなく，bigramの共起も考慮したPLSIモデルを提案し，jointで学習．与えられたクエリやnarrativeなどとsentenceの類似度（latent spaceで計算）を計算し重要文を決定。・user-modelを使ったPersonalizationはしていな ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/23">Personalized Multi-document Summarization in Information Retrieval, Yang+, Machine Learning and Cybernetics, 08</a>
<span class="snippet"><span>Comment</span>・検索結果に含まれるページのmulti-document summarizationを行う．クエリとsentenceの単語のoverlap, sentenceの重要度を　Affinity-Graphから求め，両者を結合しスコアリング．MMR #243 likeな手法で冗長性を排除し要約を生成する ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/22">NewsInEssence: Summarizing ONLINE NEWS TOPICS, Radev+, Communications of the ACM, 05</a>
<span class="snippet"><span>Comment</span>・Centroid-Basedな手法(MEADと同じ手法)で要約を生成・Personalizationはかけていない ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/21">WebInEssence: A Personalized Web-Based Multi-Document Summarization and Recommendation System, Radev+, NAACL, 01</a>
<span class="snippet"><span>Comment</span>・ドキュメントはオフラインでクラスタリングされており，各クラスタごとにmulti-document summarizationを行うことで，ユーザが最も興味のあるクラスタを同定することに役立てる．あるいは検索結果のページのドキュメントの要約を行う．要約した結果には，extractした文の元U ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
