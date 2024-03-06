---
layout: post
title: PersonalizedDocumentSummarizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## PersonalizedDocumentSummarization
<div class="visible-content">
<a class="button" href="articles/InteractivePersonalizedSummarization.html">#InteractivePersonalizedSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ILP.html">#ILP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/7">Joint Optimization of User-desired Content in Multi-document Summaries by Learning from User Feedback, P.V.S+, ACL17, 34</a>
<span class="snippet"><span>Comment</span># 一言で言うとユーザとインタラクションしながら重要なコンセプトを決め、そのコンセプトが含まれるようにILPな手法で要約を生成するPDS手法。Interactive Personalized Summarizationと似ている（似ているが引用していない、引用した方がよいのでは）。# 手 ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/InteractivePersonalizedSummarization.html">#InteractivePersonalizedSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1">Summarize What You Are Interested In: An Optimization Framework for Interactive Personalized Summarization, Yan+, EMNLP11, 37</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34400733-97c86614-ebd7-11e7-9fe9-a6b36c726a21.png)ユーザとシステムがインタラクションしながら個人向けの要約を生成するタスク ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/4">Collaborative Summarization: When Collaborative Filtering Meets Document Summarization, Qu+, PACLIC09, 6</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34400963-26dc2ee2-ebda-11e7-8170-2aa5fcc701c1.png)Collaborative Filteringと要約を組み合わせる手評価1 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/2">Incremental Personalised Summarisation with Novelty Detection, Campana+, FQAS09, 11</a>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/24">Personalized PageRank based Multi-document summarization, Liu+, WSCS 08</a>
<span class="snippet"><span>Comment</span>・クエリがあるのが前提・基本的にPersonalized PageRankの事前分布を求めて，PageRankアルゴリズムを適用する・文のsalienceを求めるモデルと（パラグラフ，パラグラフ内のポジション，statementなのかdialogなのか，文の長さ），クエリとの関連性をはかるr ...</span>
<a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/6">Aspect-Based Personalized Text Summarization, Berkovsky+（Tim先生のグループ）, AH2008, 31</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34401031-b72623e0-ebda-11e7-9da2-6ce16b630f47.png)Aspect-basedなPDSに関して調査した研究。たとえば、Wi ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/3">Generating Personalized Summaries Using Publicly Available Web Documents, Kumar+, WI-IAT08, 18</a>
<span class="snippet"><span>Comment</span>評価5人の研究者による人手評価。25種類の異なるトピックが選択され、各トピックには5-10の記事が紐づいている。generic,personalizedな要約を提示しrelevanceを判定してもらった。具体的には、informativenessを5段階評価。データ非公開、ニュース記事を使っ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/26">Personalized Multi-Document Summarization using N-Gram Topic Model Fusion, Hennig+, SPIM, 2010</a>
<span class="snippet"><span>Comment</span>・unigramの共起だけでなく，bigramの共起も考慮したPLSIモデルを提案し，jointで学習．与えられたクエリやnarrativeなどとsentenceの類似度（latent spaceで計算）を計算し重要文を決定。・user-modelを使ったPersonalizationはしていな ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/25">Segmentation Based, Personalized Web Page Summarization Model,  Journal of advances in information technology, vol. 3, no.3, 2012</a>
<span class="snippet"><span>Comment</span>・Single-document・ページ内をセグメントに分割し，どのセグメントを要約に含めるか選択する問題・要約に含めるセグメントは4つのfactor（segment weight, luan’s significance factor, profile keywords, compress ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/23">Personalized Multi-document Summarization in Information Retrieval, Yang+, Machine Learning and Cybernetics, 08</a>
<span class="snippet"><span>Comment</span>・検索結果に含まれるページのmulti-document summarizationを行う．クエリとsentenceの単語のoverlap, sentenceの重要度を　Affinity-Graphから求め，両者を結合しスコアリング．MMR #243 likeな手法で冗長性を排除し要約を生成する ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/21">WebInEssence: A Personalized Web-Based Multi-Document Summarization and Recommendation System, Radev+, NAACL, 01</a>
<span class="snippet"><span>Comment</span>・ドキュメントはオフラインでクラスタリングされており，各クラスタごとにmulti-document summarizationを行うことで，ユーザが最も興味のあるクラスタを同定することに役立てる．あるいは検索結果のページのドキュメントの要約を行う．要約した結果には，extractした文の元U ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/18">Automatic Text Summarization based on the Global Document Annotation, COLING-ACL, Nagao+, 1998, 59</a>
<span class="snippet"><span>Comment</span>Personalized summarizationの評価はしていない。提案のみ。以下の3種類の手法を提案keyword-based customization  関心のあるキーワードをユーザが入力し、コーパスやwordnet等の共起関係から関連語を取得し要約に利用する文書の ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/17">A Study for Documents Summarization based on Personal Annotation, HLT-NAACL-DUC’03, Zhang+, 2003, 33</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34402434-d521f19e-ebe4-11e7-82cf-2f3452fa4014.png)![image](https://user-images.githubuse重 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/16">Automatic Personalized Summarization using Non-negative Matrix Factorization and Relevance Measure, IWSCA, Park+, 2008, 10</a>
<span class="snippet"><span>Comment</span>#15 と同様 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/15">Personalized Text Summarization using NMF and Cluster Refinement, ICTC, Park+, 2011, 0</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34402356-5275f894-ebe4-11e7-93d7-2a3781a74b94.png) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/14">Personalized Summarization Agent Using Non-negative Matrix Factorization, PRICAI, Park, 2008, 19</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34402291-fb66cb96-ebe3-11e7-9635-790be0cf8b5d.png)著者の方は、結構同じような内容で色々な学会に投稿していたり、自分で自分の論文を引 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/8">User-model based personalized summarization, Diaz+, Information Processing and Management 2007, 96</a>
<span class="snippet"><span>Comment</span>PDSの先駆けとなった重要論文。必ずreferすべき。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
