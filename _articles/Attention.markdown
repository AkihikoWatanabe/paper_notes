---
layout: post
title: Attentionに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Attention
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero_Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/827">Dataset Distillation with Attention Labels for Fine-tuning BERT, ACL23</a>
<span class="snippet">本研究では、データセットの蒸留を使用して、元のデータセットのパフォーマンスを保持しながら、ニューラルネットワークを迅速にトレーニングするための小さなデータセットを作成する方法に焦点を当てています。具体的には、事前学習済みのトランスフォーマーを微調整するための自然言語処理タスクの蒸留されたfew-s ...</span>
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/899">FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023</a>
<span class="snippet">FlashAttention-2は、長いシーケンス長におけるTransformerのスケーリングの問題に対処するために提案された手法です。FlashAttention-2は、非対称なGPUメモリ階層を利用してメモリの節約とランタイムの高速化を実現し、最適化された行列乗算に比べて約2倍の高速化を達成 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/935f61f3-97ce-4e76-826b-040f92ca567c" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/923">The Hydra Effect: Emergent Self-repair in Language Model Computations, Thomas McGrath+, N_A, arXiv23</a>
<span class="snippet">私たちは、言語モデルの内部構造を調査し、言語モデルの計算における特定の効果を示しました。具体的には、1つの層の削除が他の層によって補完される「Hydra効果」と、遅いMLP層が最大尤度トークンを制御する役割を持つことを示しました。また、ドロップアウトを使用しない言語モデルでも同様の効果が見られるこ ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/688">FlashAttention: Fast and Memory-Efficient Exact Attention with  IO-Awareness, Tri Dao+, N_A, arXiv22</a>
<span class="snippet">トランスフォーマーは、長いシーケンスに対して遅く、メモリを多く消費するため、注意アルゴリズムを改善する必要がある。FlashAttentionは、タイリングを使用して、GPUの高帯域幅メモリ（HBM）とGPUのオンチップSRAM間のメモリ読み取り/書き込みの数を減らし、トランスフォーマーを高速にト ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e3cb11b7-f413-4831-bea6-97886b683ff7" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
