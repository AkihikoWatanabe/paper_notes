---
layout: post
title: Efficiency/SpeedUpに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Efficiency/SpeedUp
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/525">Efficient Methods for Natural Language Processing: A Survey, Treviso+, arXiv23</a>
<span class="snippet">パラメータ数でゴリ押すような方法ではなく、"Efficient"に行うための手法をまとめている![image](https://user-images.githubusercontent.com/12249301/234287218-2d42766f-5c5c-4cf9-859e-c2b0a5d ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/python.html">#python</a><br><span class="issue_date">Issue Date: 2023-05-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/675">Assisted Generation: a new direction toward low-latency text generation, 2023</a>
<span class="snippet">assistant modelをロードしgenerateに引数として渡すだけ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fecc1c5e-b9e5-4844-af96-ba48c3d60fae" alt="image"><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/766">Textbooks Are All You Need, Suriya Gunasekar+, N_A, arXiv23</a>
<span class="snippet">本研究では、小規模なphi-1という新しいコード用大規模言語モデルを紹介し、8つのA100で4日間トレーニングした結果、HumanEvalでpass@1の正解率50.6％、MBPPで55.5％を達成したことを報告しています。また、phi-1は、phi-1-baseやphi-1-smallと比較して ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9f0b945a-f965-42ae-b5d8-ac464359af35" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/769">Full Parameter Fine-tuning for Large Language Models with Limited  Resources, Kai Lv+, N_A, arXiv23</a>
<span class="snippet">LLMsのトレーニングには膨大なGPUリソースが必要であり、既存のアプローチは限られたリソースでの全パラメーターの調整に対処していない。本研究では、LOMOという新しい最適化手法を提案し、メモリ使用量を削減することで、8つのRTX 3090を搭載した単一のマシンで65Bモデルの全パラメーターファイ ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/817">FiD-ICL: A Fusion-in-Decoder Approach for Efficient In-Context Learning, ACL23</a>
<span class="snippet">大規模な事前学習モデルを使用したfew-shot in-context learning（ICL）において、fusion-in-decoder（FiD）モデルを適用することで効率とパフォーマンスを向上させることができることを検証する。FiD-ICLは他のフュージョン手法と比較して優れたパフォーマン ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Ensemble.html">#Ensemble</a><a class="button" href="articles/TransferLearning.html">#TransferLearning</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/822">Parameter-efficient Weight Ensembling Facilitates Task-level Knowledge Transfer, ACL23</a>
<span class="snippet">最近の研究では、大規模な事前学習済み言語モデルを特定のタスクに効果的に適応させることができることが示されています。本研究では、軽量なパラメータセットを使用してタスク間で知識を転送する方法を探求し、その有効性を検証しました。実験結果は、提案手法がベースラインに比べて5％〜8％の改善を示し、タスクレベ ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DynamicNetworks.html">#DynamicNetworks</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/856">PAD-Net: An Efficient Framework for Dynamic Networks, ACL23</a>
<span class="snippet">本研究では、ダイナミックネットワークの一般的な問題点を解決するために、部分的にダイナミックなネットワーク（PAD-Net）を提案します。PAD-Netは、冗長なダイナミックパラメータを静的なパラメータに変換することで、展開コストを削減し、効率的なネットワークを実現します。実験結果では、PAD-Ne ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet">私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビ ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/899">FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023</a>
<span class="snippet">FlashAttention-2は、長いシーケンス長におけるTransformerのスケーリングの問題に対処するために提案された手法です。FlashAttention-2は、非対称なGPUメモリ階層を利用してメモリの節約とランタイムの高速化を実現し、最適化された行列乗算に比べて約2倍の高速化を達成 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/935f61f3-97ce-4e76-826b-040f92ca567c" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/921">Skeleton-of-Thought: Large Language Models Can Do Parallel Decoding, Xuefei Ning+, N_A, arXiv23</a>
<span class="snippet">この研究では、大規模言語モデル（LLMs）の生成遅延を減らすために、思考の骨組み（SoT）という手法を提案しています。SoTは、回答の骨組みをまず生成し、その後に内容を並列で処理することで高速化を実現します。また、回答品質の向上も期待されます。SoTはデータ中心の最適化の初めの試みであり、LLMs ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fb25d8ba-dff7-4f6f-be25-0973488f6e8a" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/688">FlashAttention: Fast and Memory-Efficient Exact Attention with  IO-Awareness, Tri Dao+, N_A, arXiv22</a>
<span class="snippet">トランスフォーマーは、長いシーケンスに対して遅く、メモリを多く消費するため、注意アルゴリズムを改善する必要がある。FlashAttentionは、タイリングを使用して、GPUの高帯域幅メモリ（HBM）とGPUのオンチップSRAM間のメモリ読み取り/書き込みの数を減らし、トランスフォーマーを高速にト ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e3cb11b7-f413-4831-bea6-97886b683ff7" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1000">Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than  In-Context Learning, Haokun Liu+, N_A, arXiv22</a>
<span class="snippet">Few-shot in-context learning（ICL）とパラメータ効率の良いファインチューニング（PEFT）を比較し、PEFTが高い精度と低い計算コストを提供することを示す。また、新しいPEFTメソッドである（IA）^3を紹介し、わずかな新しいパラメータしか導入しないまま、強力なパフォ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/81">Efficient Methods and Hardware for Deep Learning, Han, Stanford University, 2017</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/82">Learning to skim text, Yu+, ACL17</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/34460775-f64d4e80-ee5b-11e7-9eea-34ce5ba3e764.png)![image](https://user-images.githubuse ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/python.html">#python</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2021-06-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/373">intel MKL</a>
<span class="snippet">intel CPUでpythonの数値計算を高速化するライブラリ(numpyとかはやくなるらしい; Anacondaだとデフォルトで入ってるとかなんとか) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/528">LoRA論文解説</a>
<span class="snippet">huggingfaceがすでにLoRAを実装しているhttps://github.com/huggingface/peft ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/531">Training a recommendation model with dynamic embeddings</a>
<span class="snippet">（理解が間違っているかもしれないが）推薦システムは典型的にはユーザとアイテムをベクトル表現し、関連度を測ることで推薦をしている。この枠組みをめっちゃスケールさせるととんでもない数のEmbeddingを保持することになり、メモリ上にEmbeddingテーブルを保持して置けなくなる。特にこれはonlin ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/886">LLaMA2を3行で訓練</a>
<span class="snippet">LLaMA2を3行で、1つのA100GPU、QLoRAで、自前のデータセットで訓練する方法 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
