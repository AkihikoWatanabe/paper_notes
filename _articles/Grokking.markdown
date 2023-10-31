---
layout: post
title: Grokkingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Grokking
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1051">Explaining grokking through circuit efficiency, Vikrant Varma+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>グロッキングとは、完璧なトレーニング精度を持つネットワークでも一般化が悪い現象のことである。この現象は、タスクが一般化する解と記憶する解の両方を許容する場合に起こると考えられている。一般化する解は学習が遅く、効率的であり、同じパラメータノルムでより大きなロジットを生成する。一方、記憶回路はトレーニングデータセットが大きくなるにつれて非効率になるが、一般化回路はそうではないと仮説が立てられている。これは、記憶と一般化が同じくらい効率的な臨界データセットサイズが存在することを示唆している。さらに、グロッキングに関して4つの新しい予測が立てられ、それらが確認され、説明が支持される重要な証拠が提供されている。また、グロッキング以外の2つの新しい現象も示されており、それはアングロッキングとセミグロッキングである。アングロッキングは完璧なテスト精度から低いテスト精度に逆戻りする現象であり、セミグロッキングは完璧なテスト精度ではなく部分的なテスト精度への遅れた一般化を示す現象である。</span>
<span class="snippet"><span>Comment</span>Grokkingがいつ、なぜ発生するかを説明する理論を示した研究。理由としては、最初はmemorizationを学習していくのだが、ある時点から一般化回路であるGenに切り替わる。これが切り替わる理由としては、memorizationよりも、genの方がlossが小さくなるから、とのこと。これはよG ...</span>
</div>
