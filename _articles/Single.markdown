---
layout: post
title: Singleに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Single
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/135">Get To The Point: Summarization with Pointer-Generator Networks, See+, ACL17</a>
<span class="snippet">解説スライド：https://www.slideshare.net/akihikowatanabe3110/get-to-the-point-summarization-with-pointergenerator-networks/1 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/131">Neural Summarization by Extracting Sentences and Words, Cheng+, ACL16</a>
<span class="snippet">ExtractiveかつNeuralな単一文書要約ならベースラインとして使用した方がよいかも ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/132">Distraction-Based Neural Networks for Modeling Documents, Chen+, IJCAI16</a>
<span class="snippet">Neuralなモデルで「文書」の要約を行う研究。提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。distractionを導入するmotivationは、入力文書中の異なる情報を横断 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/136">Incorporating Copying Mechanism in Sequence-to-Sequence Learning, Gu+, ACL16</a>
<span class="snippet">解説スライド：https://www.slideshare.net/akihikowatanabe3110/incorporating-copying-mechanism-in-sequene-to-sequence-learning ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/DomainAdaptation.html">#DomainAdaptation</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/142">Learning from Numerous Untailored Summaries, Kikuchi+, PRICAI16</a>
<span class="snippet">New York Times Annotated Corpus（NYTAC）に含まれる大量の正解要約データを利用する方法を提案。NYTACには650,000程度の人手で生成された参照要約が付与されているが、このデータを要約の訓練データとして活用した事例はまだ存在しないので、やりましたという話。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/75">LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP15</a>
<span class="snippet">Large Chinese Short Text Summarization (LCSTS) datasetを作成データセットを作成する際は、Weibo上の特定のorganizationの投稿の特徴を利用。Weiboにニュースを投稿する際に、投稿の冒頭にニュースのvery short s ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/143">Learning to Generate Coherent Sumamry with Discriminative Hidden Semi-Markov Model, Nishikawa+, COLING14</a>
<span class="snippet">Hidden-semi-markovモデルを用いた単一文書要約手法を提案。通常のHMMでは一つの隠れ状態に一つのunit（要約の文脈だと文？）が対応するが、hidden-semi-markov(HSMM)モデルでは複数のunitを対応づけることが可能。隠れ状態に対応するunitを文だと考 ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/144">CTSUM: Extracting More Certain Summaries for News Articles, Wan+, SIGIR14</a>
<span class="snippet">要約を生成する際に、情報の”確実性”を考慮したモデルCTSUMを提案しましたという論文（今まではそういう研究はなかった）```"However, it seems that Obama will not use the platform to relaunch his stalled d ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/25">Segmentation Based, Personalized Web Page Summarization Model,  Journal of advances in information technology, vol. 3, no.3, 2012</a>
<span class="snippet">・Single-document・ページ内をセグメントに分割し，どのセグメントを要約に含めるか選択する問題・要約に含めるセグメントは4つのfactor（segment weight, luan’s significance factor, profile keywords, compress ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/2">Incremental Personalised Summarisation with Novelty Detection, Campana+, FQAS09, 11</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/140">Document Summarization using Conditional Random Fields, Shen+, IJCAI07</a>
<span class="snippet">CRFを用いて単一文書要約の手法を考えましたという話。気持ちとしては、```1. Supervisedなモデルでは、当時は原文書中の各文を独立に2値分類して要約を生成するモデルが多く、sentence間のrelationが考慮できていなかった2. unsupervisedな手法で ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/214">TextRank: Bringing Order into Texts, Mihalcea+, EMNLP04</a>
<span class="snippet">PageRankベースの手法で、キーワード抽出/文書要約 を行う手法。キーワード抽出/文書要約 を行う際には、ノードをそれぞれ 単語/文 で表現する。ノードで表現されている 単語/文 のsimilarityを測り、ノード間のedgeの重みとすることでAffinity Graphを構築。あ ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/215">LexRank: Graph-based Lexical Centrality as Salience in Text Summarization, Erkan+, Journal of Artificial Intelligence Research, 2004</a>
<span class="snippet">代表的なグラフベースな(Multi) Document Summarization手法。ほぼ #214 と同じ手法。2種類の手法が提案されている：* [LexRank] tf-idfスコアでsentenceのbag-of-wordsベクトルを作り、cosine similarit ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/147">Automatic condensation of electronic publications by sentence selection, Brandow+, Information Processing & Management95</a>
<span class="snippet">報道記事要約において、自動要約システムがLead文に勝つのがhardだということを示した研究 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
