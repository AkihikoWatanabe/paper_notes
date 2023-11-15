---
layout: post
title: Pruningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Pruning
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/812">Pruning Pre-trained Language Models Without Fine-Tuning, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、Pre-trained Language Models（PLMs）の過パラメータ化の問題を解決するために、一次元のプルーニングを使用したシンプルで直感的な圧縮手法であるStatic Model Pruning（SMP）を提案します。SMPは、下流のタスクにPLMsを適応させるために一次元のプルーニングのみを使用し、微調整を必要としないため、他の手法よりも効率的です。徹底的な実験結果は、SMPが一次元およびゼロ次元の手法よりも大幅に改善されていることを示しています。また、SMPは低い疎密度にも適用可能であり、ゼロ次元の手法を上回ります。</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/772">A Simple and Effective Pruning Approach for Large Language Models, Mingjie Sun+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、大規模言語モデル（LLMs）の剪定方法であるWandaを紹介している。Wandaは、重みと活性化による剪定を行い、再トレーニングや重みの更新を必要とせず、剪定されたLLMはそのまま使用できる。Wandaは、LLaMA上でのさまざまな言語ベンチマークで徹底的に評価され、大きさに基づく剪定の確立されたベースラインを大幅に上回り、重みの更新に関する最近の方法と競合する優れた性能を発揮することが示された。コードはhttps://github.com/locuslab/wandaで利用可能である。</span>
<span class="snippet"><span>Comment</span>LLMのネットワークのpruning手法を提案。再訓練、パラメータ更新無しで、性能低下が少なくて刈り込みが可能。 ...</span>
</div>
