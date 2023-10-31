---
layout: post
title: Quantizationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Quantization
<div class="visible-content">
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビ ...</span>
<span class="snippet"><span>Comment</span>実装: https://github.com/artidoro/qloraPEFTにもある以下hillbigさんのツイートから引用> QLoRAは元の言語モデルを4bitに量子化し固定した上で、LoRAを使い、65Bパラメータモデルの微調整を48GB GPUで可能とする（最適化は16-bit空間で行 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1043">GPTQ: Accurate Post-Training Quantization for Generative Pre-trained  Transformers, Elias Frantar+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>本研究では、GPTモデルの推論における計算およびストレージコストの問題に取り組み、新しいワンショット重み量子化手法であるGPTQを提案します。GPTQは高い精度と効率性を持ち、1750億のパラメータを持つGPTモデルを4時間のGPU時間で量子化することができます。提案手法は従来の手法と比較して圧縮 ...</span>
<span class="snippet"><span>Comment</span># 概要新たなpost-training量子化手法であるGPTQを提案数時間以内に数千億のパラメータを持つモデルでの実行が可能であり、パラメータごとに3～4ビットまで圧縮するが、精度の大きな損失を伴わない    OPT-175BおよびBLOOM-176Bを、約4時間のGPU時# Backgro ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4ff107a9-7ccf-40f6-ad8c-fd910b1f0ac7" alt="image"></div>
