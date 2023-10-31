---
layout: post
title: Grokkingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Grokking
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1051">Explaining grokking through circuit efficiency, Vikrant Varma+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>グロッキングとは、完璧なトレーニング精度を持つネットワークでも一般化が悪い現象のことである。この現象は、タスクが一般化する解と記憶する解の両方を許容する場合に起こると考えられている。一般化する解は学習が遅く、効率的であり、同じパラメータノルムでより大きなロジットを生成する。一方、記憶回路はトレーニ ...</span>
<span class="snippet"><span>Comment</span>Grokkingがいつ、なぜ発生するかを説明する理論を示した研究。理由としては、最初はmemorizationを学習していくのだが、ある時点から一般化回路であるGenに切り替わる。これが切り替わる理由としては、memorizationよりも、genの方がlossが小さくなるから、とのこと。これはよG ...</span>
</div>
