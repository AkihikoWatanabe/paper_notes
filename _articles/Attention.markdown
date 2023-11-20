---
layout: post
title: Attentionに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Attention
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1121">Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs, Qingru Zhang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>PASTAは、大規模言語モデル（LLMs）において、ユーザーが指定した強調マークのあるテキストを読むことを可能にする手法です。PASTAは、注意の一部を特定し、再重み付けを適用してモデルの注意をユーザーが指定した部分に向けます。実験では、PASTAがLLMの性能を大幅に向上させることが示されています。</span>
<span class="snippet"><span>Comment</span>ユーザがprompt中で強調したいした部分がより考慮されるようにattention weightを調整することで、より応答性能が向上しましたという話っぽい。かなり重要な技術だと思われる。後でしっかり読む。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/a4d3714e-7279-495c-86f1-5ff4ed2cbeb8" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/923">The Hydra Effect: Emergent Self-repair in Language Model Computations, Thomas McGrath+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、言語モデルの内部構造を調査し、言語モデルの計算における特定の効果を示しました。具体的には、1つの層の削除が他の層によって補完される「Hydra効果」と、遅いMLP層が最大尤度トークンを制御する役割を持つことを示しました。また、ドロップアウトを使用しない言語モデルでも同様の効果が見られることを示しました。これらの効果を事実の回想の文脈で分析し、言語モデルの回路レベルの属性付与について考察しました。</span>
<span class="snippet"><span>Comment</span>LLMからattention layerを一つ取り除くと、後続の層が取り除かれたlayerの機能を引き継ぐような働きをすることがわかった。これはLLMの自己修復機能のようなものであり、HydraEffectと命名された。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero_Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/827">Dataset Distillation with Attention Labels for Fine-tuning BERT, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、データセットの蒸留を使用して、元のデータセットのパフォーマンスを保持しながら、ニューラルネットワークを迅速にトレーニングするための小さなデータセットを作成する方法に焦点を当てています。具体的には、事前学習済みのトランスフォーマーを微調整するための自然言語処理タスクの蒸留されたfew-shotデータセットの構築を提案しています。実験結果では、注意ラベルを使用してfew-shotデータセットを作成し、BERTの微調整において印象的なパフォーマンスを実現できることを示しました。例えば、ニュース分類タスクでは、わずか1つのサンプルとわずか1つの勾配ステップのみで、元のデータセットの98.5％のパフォーマンスを達成しました。</span>
<span class="snippet"><span>Comment</span>Datadistillationしたら、データセットのうち1サンプルのみで、元のデータセットの98.5%の性能を発揮できたという驚異的な研究（まえかわ君） ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/688">FlashAttention: Fast and Memory-Efficient Exact Attention with  IO-Awareness, Tri Dao+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>トランスフォーマーは、長いシーケンスに対して遅く、メモリを多く消費するため、注意アルゴリズムを改善する必要がある。FlashAttentionは、タイリングを使用して、GPUの高帯域幅メモリ（HBM）とGPUのオンチップSRAM間のメモリ読み取り/書き込みの数を減らし、トランスフォーマーを高速にトレーニングできる。FlashAttentionは、トランスフォーマーでより長い文脈を可能にし、より高品質なモデルや、完全に新しい機能を提供する。</span>
<span class="snippet"><span>Comment</span>より計算効率の良いFlashAttentionを提案 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e3cb11b7-f413-4831-bea6-97886b683ff7" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/899">FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023</a>
<span class="snippet"><span>Summary</span>FlashAttention-2は、長いシーケンス長におけるTransformerのスケーリングの問題に対処するために提案された手法です。FlashAttention-2は、非対称なGPUメモリ階層を利用してメモリの節約とランタイムの高速化を実現し、最適化された行列乗算に比べて約2倍の高速化を達成します。また、FlashAttention-2はGPTスタイルのモデルのトレーニングにおいても高速化を実現し、最大225 TFLOPs/sのトレーニング速度に達します。</span>
<span class="snippet"><span>Comment</span>Flash Attention1よりも2倍高速なFlash Attention 2Flash Attention1はこちらを参照https://arxiv.org/pdf/2205.14135.pdfQK Matrixの計算をブロックに分けてSRAMに送って処理することで、3倍高速化し、メモリ効率を ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/935f61f3-97ce-4e76-826b-040f92ca567c" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
