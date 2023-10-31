---
layout: post
title: Regularizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Regularization
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-10-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1075">Why Do We Need Weight Decay in Modern Deep Learning?, Maksym Andriushchenko+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>ウェイト減衰は、大規模な言語モデルのトレーニングに使用されるが、その役割はまだ理解されていない。本研究では、ウェイト減衰が古典的な正則化とは異なる役割を果たしていることを明らかにし、過パラメータ化されたディープネットワークでの最適化ダイナミクスの変化やSGDの暗黙の正則化の強化方法を示す。また、ウェイト減衰が確率的最適化におけるバイアス-分散トレードオフのバランスを取り、トレーニング損失を低下させる方法も説明する。さらに、ウェイト減衰はbfloat16混合精度トレーニングにおける損失の発散を防ぐ役割も果たす。全体として、ウェイト減衰は明示的な正則化ではなく、トレーニングダイナミクスを変えるものであることが示される。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> WeightDecayはNNの学習時に使われているが、従来考えられていた正則化でなく 1) 過剰パラメータ時はSGDによるノイズを強め、暗黙的正則化を高める 2) ワンパスSGD (多くのLLM学習）の場合、学習ダイナミクスを変え、より低い訓練損失の達成とW ...</span>
</div>
