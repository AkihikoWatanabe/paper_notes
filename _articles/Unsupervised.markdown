---
layout: post
title: Unsupervisedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Unsupervised
<div class="visible-content">
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/AudioProcessing.html">#AudioProcessing</a><a class="button" href="articles/Speech.html">#Speech</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/842">Simple and Effective Unsupervised Speech Translation, ACL23</a>
<span class="snippet"><span>Summary</span>音声翻訳のためのラベル付きデータが限られているため、非教師あり手法を使用して音声翻訳システムを構築する方法を研究している。パイプラインアプローチや擬似ラベル生成を使用し、非教師ありドメイン適応技術を提案している。実験の結果、従来の手法を上回る性能を示している。</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/83">Unsupervised Pretraining for Sequence to Sequence Learning, Ramachandran+, EMNLP17</a>
<span class="snippet"><span>Comment</span>seq2seqにおいてweightのpretrainingを行う手法を提案seq2seqでは訓練データが小さいとoverfittingしやすいという弱点があるので、大規模なデータでunsupervisedにpretrainingし、その後目的のデータでfinetuneすることで精度を向上させまし ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/144">CTSUM: Extracting More Certain Summaries for News Articles, Wan+, SIGIR14</a>
<span class="snippet"><span>Comment</span>要約を生成する際に、情報の”確実性”を考慮したモデルCTSUMを提案しましたという論文（今まではそういう研究はなかった）```"However, it seems that Obama will not use the platform to relaunch his stalled d解説ス ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/215">LexRank: Graph-based Lexical Centrality as Salience in Text Summarization, Erkan+, Journal of Artificial Intelligence Research, 2004</a>
<span class="snippet"><span>Comment</span>代表的なグラフベースな(Multi) Document Summarization手法。ほぼ #214 と同じ手法。2種類の手法が提案されている：* [LexRank] tf-idfスコアでsentenceのbag-of-wordsベクトルを作り、cosine similarit ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
