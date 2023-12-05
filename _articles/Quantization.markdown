---
layout: post
title: Quantizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Quantization
<div class="visible-content">
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Adapter_LoRA.html">#Adapter/LoRA</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビット量子化された事前学習済み言語モデルの勾配をLow Rank Adapters（LoRA）に逆伝播させます。私たちの最良のモデルファミリーであるGuanacoは、Vicunaベンチマークで以前に公開されたすべてのモデルを上回り、ChatGPTのパフォーマンスレベルの99.3%に達します。また、単一のGPU上でのファインチューニングには24時間しかかかりません。QLoRAは、パフォーマンスを犠牲にすることなくメモリを節約するためのいくつかの革新を導入しています。具体的には、4ビットNormalFloat（NF4）という情報理論的に最適な新しいデータ型、ダブル量子化による平均メモリフットプリントの削減、およびページドオプティマイザによるメモリスパイクの管理です。私たちはQLoRAを使用して1,000以上のモデルをファインチューニングし、8つの命令データセット、複数のモデルタイプ（LLaMA、T5）、および従来のファインチューニングでは実行不可能なモデルスケール（33Bおよび65Bパラメータモデル）にわたる命令の追跡とチャットボットのパフォーマンスの詳細な分析を提供します。私たちの結果は、QLoRAを使用して小規模な高品質のデータセットでのファインチューニングが、以前のSoTAよりも小さいモデルを使用しても最先端の結果をもたらすことを示しています。また、人間の評価とGPT-4の評価に基づいたチャットボットのパフォーマンスの詳細な分析を提供し、GPT-4の評価が安価で合理的な人間の評価の代替手段であることを示します。さらに、現在のチャットボットのベンチマークは、チャットボットのパフォーマンスレベルを正確に評価するためには信頼性がないことがわかります。GuanacoがChatGPTと比較してどこで失敗するかを示す分析も行っています。私たちは、4ビットトレーニングのためのCUDAカーネルを含む、すべてのモデルとコードを公開しています。</span>
<span class="snippet"><span>Comment</span>実装: https://github.com/artidoro/qloraPEFTにもある以下hillbigさんのツイートから引用> QLoRAは元の言語モデルを4bitに量子化し固定した上で、LoRAを使い、65Bパラメータモデルの微調整を48GB GPUで可能とする（最適化は16-bit空間で行 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1043">GPTQ: Accurate Post-Training Quantization for Generative Pre-trained  Transformers, Elias Frantar+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>本研究では、GPTモデルの推論における計算およびストレージコストの問題に取り組み、新しいワンショット重み量子化手法であるGPTQを提案します。GPTQは高い精度と効率性を持ち、1750億のパラメータを持つGPTモデルを4時間のGPU時間で量子化することができます。提案手法は従来の手法と比較して圧縮率を2倍以上向上させ、精度を保持することができます。さらに、提案手法は極端な量子化領域でも合理的な精度を提供します。実験結果では、提案手法を使用することでエンドツーエンドの推論速度が約3.25倍から4.5倍向上することが示されています。提案手法の実装はhttps://github.com/IST-DASLab/gptqで利用可能です。</span>
<span class="snippet"><span>Comment</span># 概要新たなpost-training量子化手法であるGPTQを提案数時間以内に数千億のパラメータを持つモデルでの実行が可能であり、パラメータごとに3～4ビットまで圧縮するが、精度の大きな損失を伴わない    OPT-175BおよびBLOOM-176Bを、約4時間のGPU時# Backgro ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4ff107a9-7ccf-40f6-ad8c-fd910b1f0ac7" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Adapter_LoRA.html">#Adapter/LoRA</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/886">LLaMA2を3行で訓練</a>
<span class="snippet"><span>Comment</span>LLaMA2を3行で、1つのA100GPU、QLoRAで、自前のデータセットで訓練する方法 ...</span>
</div>
