---
layout: post
title: Transformerに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Transformer
<div class="visible-content">
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2023-02-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/509">30分で完全理解するTransformerの世界</a>
<span class="snippet">非常に詳細で実質日本語のサーベイ論文のようなもの ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/529">Scaling Transformer to 1M tokens and beyond with RMT, Bulatov+, DeepPavlov, arXiv23</a>
<span class="snippet">Reccurent Memory Transformer #523 を使って2Mトークン扱えるようにしたよーという話。ハリーポッターのトークン数が1.5Mらしいので、そのうち小説一冊書けるかもという世界。 ...</span>
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/python.html">#python</a><br><span class="issue_date">Issue Date: 2023-05-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/675">Assisted Generation: a new direction toward low-latency text generation, 2023</a>
<span class="snippet">assistant modelをロードしgenerateに引数として渡すだけ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fecc1c5e-b9e5-4844-af96-ba48c3d60fae" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/744">Birth of a Transformer: A Memory Viewpoint, Alberto Bietti+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルの内部メカニズムを理解するため、トランスフォーマーがグローバルとコンテキスト固有のbigram分布をどのようにバランスするかを研究。2層トランスフォーマーでの実証的分析により、グローバルbigramの高速な学習と、コンテキスト内のbigramの「誘導ヘッド」メカニズムの遅い発達を示 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/760">Think Before You Act: Decision Transformers with Internal Working Memory, Jikun Kang+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLM）の性能は、トレーニング中にパラメータに振る舞いを記憶する「忘却現象」によって低下する可能性がある。人間の脳は分散型のメモリストレージを利用しており、忘却現象を軽減している。そこで、我々は、内部作業メモリモジュールを提案し、Atariゲームとメタワールドオブジェクト操作タス ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-06-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/774">Faith and Fate: Limits of Transformers on Compositionality, Nouha Dziri+, N_A, arXiv23</a>
<span class="snippet">Transformerの大規模言語モデル（LLMs）は、多段階の推論を必要とするタスクで優れたパフォーマンスを示す一方、些細な問題で失敗することもある。この研究では、3つの代表的な合成タスクを用いて、Transformerの限界を調査し、タスクの複雑さが増すにつれてパフォーマンスが低下することを示 ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/781">A Comprehensive Survey on Applications of Transformers for Deep Learning  Tasks, Saidul Islam+, N_A, arXiv23</a>
<span class="snippet">Transformerモデルは、セルフアテンションメカニズムを使用して文脈関係を理解するためのディープニューラルネットワークであり、長い依存関係を処理することができます。このモデルは、自然言語処理だけでなく、他のさまざまなドメインでも注目されています。しかし、さまざまなドメインでのTransfor ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/806">Generative Pretraining in Multimodality, Quan Sun+, N_A, arXiv23</a>
<span class="snippet">Emuは、マルチモーダルなコンテキストで画像とテキストを生成するためのTransformerベースのモデルです。このモデルは、単一モダリティまたはマルチモーダルなデータ入力を受け入れることができます。Emuは、マルチモーダルなシーケンスでトレーニングされ、画像からテキストへのタスクやテキストから画 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/811">Trainable Transformer in Transformer, Abhishek Panigrahi+, N_A, arXiv23</a>
<span class="snippet">本研究では、Transformer in Transformer（TinT）という効率的な構築を提案し、大規模な事前学習言語モデルの内部モデルをシミュレートして微調整することが可能となります。TinTは小さなパラメータ数でも高い性能を発揮し、トランスフォーマー内の単純なモデルの効率も向上させます。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LongSequence.html">#LongSequence</a><a class="button" href="articles/PositionalEncoding.html">#PositionalEncoding</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/820">Randomized Positional Encodings Boost Length Generalization of Transformers, ACL23</a>
<span class="snippet">トランスフォーマーは、固定長のタスクにおいては優れた汎化能力を持つが、任意の長さのシーケンスには対応できない。この問題を解決するために、新しい位置エンコーディング手法を提案する。ランダム化された位置エンコーディングスキームを使用し、長いシーケンスの位置をシミュレートし、順序付けられたサブセットをラ ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Contents-based.html">#Contents-based</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><a class="button" href="articles/ContrastiveLearning.html">#ContrastiveLearning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/852">UniTRec: A Unified Text-to-Text Transformer and Joint Contrastive Learning Framework for Text-based Recommendation, ACL23</a>
<span class="snippet">本研究では、事前学習済み言語モデル（PLM）を使用して、テキストベースの推薦の性能を向上させるための新しいフレームワークであるUniTRecを提案します。UniTRecは、ユーザーの履歴の文脈をより良くモデル化するために統一されたローカル-グローバルアテンションTransformerエンコーダを使 ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/899">FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023</a>
<span class="snippet">FlashAttention-2は、長いシーケンス長におけるTransformerのスケーリングの問題に対処するために提案された手法です。FlashAttention-2は、非対称なGPUメモリ階層を利用してメモリの節約とランタイムの高速化を実現し、最適化された行列乗算に比べて約2倍の高速化を達成 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/935f61f3-97ce-4e76-826b-040f92ca567c" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/DataGeneration.html">#DataGeneration</a><br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1024">Prompt2Model: Generating Deployable Models from Natural Language  Instructions, Vijay Viswanathan+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、プロンプトを自然言語でタスクを説明し、特定のモデルを訓練する手法であるPrompt2Modelを提案しています。Prompt2Modelは、既存のデータセットと事前学習済みモデルの検索、LLMsを使用したデータセットの生成、および教師あり微調整の ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1062">Boolformer: Symbolic Regression of Logic Functions with Transformers, Stéphane dAscoli+, N_A, arXiv23</a>
<span class="snippet">この研究では、BoolformerというTransformerアーキテクチャを使用して、ブール関数のシンボリック回帰を実行する方法を紹介します。Boolformerは、クリーンな真理値表やノイズのある観測など、さまざまなデータに対して効果的な式を予測することができます。さらに、実世界のデータセット ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2022-09-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/485">Transformerの最前線 〜 畳込みニューラルネットワークの先へ 〜, 牛久先生, 2022</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Explanation.html">#Explanation</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/499">Transformers Interpret, 2022</a>
<span class="snippet">transformersのモデルをたった2行追加するだけで、explainableにするライブラリ基本的にtextとvisionのclassificationをサポートしている模様text classificationの場合、たとえばinput tokenの各トークンの分類に対する寄与度をou ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/TabularData.html">#TabularData</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/574">Why do tree-based models still outperform deep learning on typical tabular data?, Grinsztajn+, Soda, Inria Saclay , arXiv22</a>
<span class="snippet">tree basedなモデルがテーブルデータに対してニューラルモデルよりも優れた性能を発揮することを確認し、なぜこのようなことが起きるかいくつかの理由を説明した論文。![image](https://user-images.githubusercontent.com/12249301/235 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><br><span class="issue_date">Issue Date: 2022-09-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/488">Text-to-Text Pre-Training for Data-to-Text Tasks, Mihir+, Google Research, INLG20</a>
<span class="snippet"># 所感こんな簡単なfine-tuningでSoTAを達成できてしまうとは、末恐ろしい。ベースラインとして有用。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/493">Leveraging Pre-trained Checkpoints for Sequence Generation Tasks, Rothe+, Google Research, TACL20</a>
<span class="snippet"># 概要BERT-to-BERT論文。これまでpre-trainedなチェックポイントを利用する研究は主にNLUで行われてきており、Seq2Seqでは行われてきていなかったので、やりました、という話。publicly availableなBERTのcheckpointを利用し、BERTをen ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/497">BetterTransformer, Out of the Box Performance for Hugging Face Transformers</a>
<span class="snippet">たった1ライン追加するだけで、Transformerのinferenceが最大で4.5倍高速化されるBetterTransformerの解説記事better_model = BetterTransformer.transform(model) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2022-12-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/504">Are Transformers Effective for Time Series Forecasting?</a>
<span class="snippet">Linear Layerに基づくシンプルな手法がTransformerベースの手法に時系列予測で勝ったという話 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/618">OpenLLaMA</a>
<span class="snippet">LLaMAと同様の手法を似たデータセットに適用し商用利用可能なLLaMAを構築した模様 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
