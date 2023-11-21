---
layout: post
title: Optimizerに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Optimizer
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-07-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/902">DoG is SGDs Best Friend: A Parameter-Free Dynamic Step Size Schedule, Maor Ivgi+, N_A, ICML23</a>
<span class="snippet"><span>Summary</span>私たちは、チューニング不要の動的SGDステップサイズの式であるDoGを提案します。DoGは、初期点からの距離と勾配のノルムに基づいてステップサイズを計算し、学習率のパラメータを必要としません。理論的には、DoGの式は確率的凸最適化においてパラメータフリーの収束を保証します。実験的には、DoGのパフォーマンスがチューニングされた学習率を持つSGDに近いことを示し、DoGのバリアントがチューニングされたSGDやAdamを上回ることを示します。PyTorchの実装はhttps://github.com/formll/dogで利用できます。</span>
<span class="snippet"><span>Comment</span>20 を超える多様なタスクと 8 つのビジョンおよび NLP モデルに対して有効であったシンプルなパラメーターフリーのoptimizer元ツイート: https://twitter.com/maorivg/status/1683525521471328256?s=46&t=Lt9P4Bkmi ...</span>
</div>
