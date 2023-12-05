---
layout: post
title: Adapter/LoRAに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Adapter/LoRA
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-11-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1162">MultiLoRA: Democratizing LoRA for Better Multi-Task Learning, Yiming Wang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LoRAは、LLMsを効率的に適応させる手法であり、ChatGPTのようなモデルを複数のタスクに適用することが求められている。しかし、LoRAは複雑なマルチタスクシナリオでの適応性能に制限がある。そこで、本研究ではMultiLoRAという手法を提案し、LoRAの制約を緩和する。MultiLoRAは、LoRAモジュールをスケーリングし、パラメータの依存性を減らすことで、バランスの取れたユニタリ部分空間を得る。実験結果では、わずかな追加パラメータでMultiLoRAが優れたパフォーマンスを示し、上位特異ベクトルへの依存性が低下していることが確認された。</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-11-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1159">ZipLoRA: Any Subject in Any Style by Effectively Merging LoRAs, Viraj Shah+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>概要：概念駆動型のパーソナライズのための生成モデルの微調整手法であるZipLoRAを提案。ZipLoRAは、独立してトレーニングされたスタイルと主題のLoRAを統合し、任意の主題とスタイルの組み合わせで生成することができる。実験結果は、ZipLoRAが主題とスタイルの忠実度を改善しながら魅力的な結果を生成できることを示している。</span>
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/LongSequence.html">#LongSequence</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1045">LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models, Yukang Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、計算コストを制限しながら大規模言語モデル（LLMs）のコンテキストサイズを拡張する効率的なファインチューニング手法であるLongLoRAを提案します。従来の方法では、LLMsの長いコンテキストサイズでのトレーニングには高い計算コストとGPUリソースが必要でしたが、提案手法ではコンテキスト拡張を高速化し、非自明な計算コストの削減を実現します。また、パラメータ効率的なファインチューニング手法も再評価し、LongLoRAはさまざまなタスクで強力な実験結果を示しています。さらに、教師ありファインチューニングのためのデータセットであるLongQAも収集されました。</span>
<span class="snippet"><span>Comment</span># 概要context長が大きい場合でも効率的にLoRAする手法。通常のLoRAではcontext lengthが大きくなるにつれてperplexityが大きくなってしまう。一方、通常のFinetuningではperplexityは高い性能を維持するが、計算コストとVRAMの消費量が膨大になって ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fc3d17c7-b1ac-4741-9895-bce70cf0b356" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/917">LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA  Composition, Chengsong Huang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を新しいタスクに適応させるための低ランク適応（LoRA）を検討し、LoraHubというフレームワークを提案します。LoraHubを使用すると、少数の例から複数のLoRAモジュールを組み合わせて柔軟に適応性のあるパフォーマンスを実現できます。また、追加のモデルパラメータや勾配は必要ありません。実験結果から、LoraHubが少数の例でのインコンテキスト学習のパフォーマンスを効果的に模倣できることが示されています。さらに、LoRAコミュニティの育成と共有リソースの提供にも貢献しています。</span>
<span class="snippet"><span>Comment</span>学習されたLoRAのパラメータをモジュールとして捉え、新たなタスクのinputが与えられた時に、LoRA Hub上の適切なモジュールをLLMに組み合わせることで、ICL無しで汎化を実現するというアイデア。few shotのexampleを人間が設計する必要なく、同等の性能を達成。複数のLoRAモジュ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9d769042-5a29-4c22-8ab4-e90195f71184" alt="image"><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビット量子化された事前学習済み言語モデルの勾配をLow Rank Adapters（LoRA）に逆伝播させます。私たちの最良のモデルファミリーであるGuanacoは、Vicunaベンチマークで以前に公開されたすべてのモデルを上回り、ChatGPTのパフォーマンスレベルの99.3%に達します。また、単一のGPU上でのファインチューニングには24時間しかかかりません。QLoRAは、パフォーマンスを犠牲にすることなくメモリを節約するためのいくつかの革新を導入しています。具体的には、4ビットNormalFloat（NF4）という情報理論的に最適な新しいデータ型、ダブル量子化による平均メモリフットプリントの削減、およびページドオプティマイザによるメモリスパイクの管理です。私たちはQLoRAを使用して1,000以上のモデルをファインチューニングし、8つの命令データセット、複数のモデルタイプ（LLaMA、T5）、および従来のファインチューニングでは実行不可能なモデルスケール（33Bおよび65Bパラメータモデル）にわたる命令の追跡とチャットボットのパフォーマンスの詳細な分析を提供します。私たちの結果は、QLoRAを使用して小規模な高品質のデータセットでのファインチューニングが、以前のSoTAよりも小さいモデルを使用しても最先端の結果をもたらすことを示しています。また、人間の評価とGPT-4の評価に基づいたチャットボットのパフォーマンスの詳細な分析を提供し、GPT-4の評価が安価で合理的な人間の評価の代替手段であることを示します。さらに、現在のチャットボットのベンチマークは、チャットボットのパフォーマンスレベルを正確に評価するためには信頼性がないことがわかります。GuanacoがChatGPTと比較してどこで失敗するかを示す分析も行っています。私たちは、4ビットトレーニングのためのCUDAカーネルを含む、すべてのモデルとコードを公開しています。</span>
<span class="snippet"><span>Comment</span>実装: https://github.com/artidoro/qloraPEFTにもある以下hillbigさんのツイートから引用> QLoRAは元の言語モデルを4bitに量子化し固定した上で、LoRAを使い、65Bパラメータモデルの微調整を48GB GPUで可能とする（最適化は16-bit空間で行 ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/834">Focused Prefix Tuning for Controllable Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、注釈のない属性によって制御可能なテキスト生成データセットのパフォーマンスが低下する問題に対して、「focused prefix tuning（FPT）」という手法を提案しています。FPTは望ましい属性に焦点を当てることで、制御精度とテキストの流暢さを向上させることができます。また、FPTは複数属性制御タスクにおいても、既存のモデルを再トレーニングすることなく新しい属性を制御する柔軟性を持ちながら、制御精度を保つことができます。</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/725">One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning, Arnav Chavan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、汎用的なファインチューニングタスクのための高度な手法であるGeneralized LoRA (GLoRA)を提案し、事前学習済みモデルの重みを最適化し、中間アクティベーションを調整することで、多様なタスクとデータセットに対してより柔軟性と能力を提供する。GLoRAは、各レイヤーの個別のアダプタを学習するスケーラブルでモジュラーなレイヤーごとの構造探索を採用することで、効率的なパラメータの適応を促進する。包括的な実験により、GLoRAは、自然言語、専門分野、構造化ベンチマークにおいて、従来のすべての手法を上回り、様々なデータセットでより少ないパラメータと計算で優れた精度を達成することが示された。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2021-09-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/405">Prefix-Tuning: Optimizing Continuous Prompts for Generation, Lisa+ （Percy Liang）, Stanford University, ACL21</a>
<span class="snippet"><span>Comment</span>言語モデルをfine-tuningする際，エンコード時に「接頭辞」を潜在表現として与え，「接頭辞」部分のみをfine-tuningすることで（他パラメータは固定），より少量のパラメータでfine-tuningを実現する方法を提案．接頭辞を潜在表現で与えるこの方法は，GPT-3のpromptingに着 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1146">Practical Tips for Finetuning LLMs Using LoRA （Low-Rank Adaptation）</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1109">大規模言語モデルのFine-tuningによるドメイン知識獲得の検討</a>
<span class="snippet"><span>Comment</span>以下記事中で興味深かった部分を引用> まとめると、LoRAは、[3]で言われている、事前学習モデルは大量のパラメータ数にもかかわらず低い固有次元を持ち、Fine-tuningに有効な低次元のパラメータ化も存在する、という主張にインスパイアされ、ΔWにおける重みの更新の固有次元も低いという仮説のもと ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/886">LLaMA2を3行で訓練</a>
<span class="snippet"><span>Comment</span>LLaMA2を3行で、1つのA100GPU、QLoRAで、自前のデータセットで訓練する方法 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/528">LoRA論文解説</a>
<span class="snippet"><span>Comment</span>ベースとなる事前学習モデルの一部の線形層の隣に、低ランク行列A,Bを導入し、A,Bのパラメータのみをfinetuningの対象とすることで、チューニングするパラメータ数を激減させた上で同等の予測性能を達成し、推論速度も変わらないようにするfinetuning手法の解説LoRAを使うと、でかすぎるモデ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2022-08-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/473">The Power of Scale for Parameter-Efficient Prompt Tuning, Lester+, Google Research, EMNLP‘21</a>
<span class="snippet"><span>Comment</span>日本語解説: https://qiita.com/kts_plea/items/79ffbef685d362a7b6ceT5のような大規模言語モデルに対してfinetuningをかける際に、大規模言語モデルのパラメータは凍結し、promptをembeddingするパラメータを独立して学習する手法 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
