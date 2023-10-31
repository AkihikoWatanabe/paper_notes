---
layout: post
title: Regularizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Regularization
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-10-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1075">Why Do We Need Weight Decay in Modern Deep Learning?, Maksym Andriushchenko+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>ウェイト減衰は、大規模な言語モデルのトレーニングに使用されるが、その役割はまだ理解されていない。本研究では、ウェイト減衰が古典的な正則化とは異なる役割を果たしていることを明らかにし、過パラメータ化されたディープネットワークでの最適化ダイナミクスの変化やSGDの暗黙の正則化の強化方法を示す。また、ウ ...</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> WeightDecayはNNの学習時に使われているが、従来考えられていた正則化でなく 1) 過剰パラメータ時はSGDによるノイズを強め、暗黙的正則化を高める 2) ワンパスSGD (多くのLLM学習）の場合、学習ダイナミクスを変え、より低い訓練損失の達成とW ...</span>
</div>
