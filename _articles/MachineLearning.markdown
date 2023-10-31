---
layout: post
title: MachineLearningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## MachineLearning
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-10-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1091">NEFTune: Noisy Embeddings Improve Instruction Finetuning, Neel Jain+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、言語モデルのファインチューニングを改善するために、ノイズを加えた埋め込みベクトルを使用する手法を提案します。この手法は、AlpacaEvalやEvol-Instructなどのデータセットで強力なベースラインを上回る性能を示しました。また、RLHFでトレーニングされたモデルにも適用可能です ...</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> NEFTuneはLLMをファインチューニングする際、単語埋め込みベクトルに一様分布からのノイズを加えるだけでファインチューニングの性能を大きく改善する。ファインチューニングは多くの場合過学習しており、出現した単語や表現にしばられる場合が多く、これを防ぐこAl ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1089">Detecting Pretraining Data from Large Language Models, Weijia Shi+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を訓練するためのデータの検出問題を研究し、新しい検出方法であるMin-K% Probを提案します。Min-K% Probは、LLMの下で低い確率を持つアウトライアーワードを検出することに基づいています。実験の結果、Min-K% Probは従来の方法に比べて7 ...</span>
<span class="snippet"><span>Comment</span>以下AIDBのツイートの引用> LLMに特定のテキストが「訓練データとして使用されているのか」を確かめる手法が開発されました。>検証の結果、本手法は信頼性があって効果的と結論づけられています。権利の問題やベンチマーク評価に役立つ可能性のある進展です。>ワシントン大学とプリンストン大学の実験結果を見る ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/1d7a5fe2-e0bc-4c6e-92b2-34457a17714a" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-10-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1085">Eliminating Reasoning via Inferring with Planning: A New Framework to  Guide LLMs Non-linear Thinking, Yongqi Tong+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）に非線形の思考を促すために、新しいプロンプティング方法であるInferential Exclusion Prompting（IEP）を提案する。IEPは、計画を立てて可能な解を推論し、逆推論を行うことで広い視点を得ることができる。IEPは他の手法と比較して複 ...</span>
<span class="snippet"><span>Comment</span>以下AIDBの引用>GPT-4などのLLMに、CoTのように直線的（線形的）ではなく、複数の条件を考慮させる（非線形的）プロンプト手法『Inferential Exclusion Prompting（IEP）』が考案されました。>さまざまなタスクでCoTを一貫して上回り、さらにCoTと統合す元論文は ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Regularization.html">#Regularization</a><br><span class="issue_date">Issue Date: 2023-10-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1075">Why Do We Need Weight Decay in Modern Deep Learning?, Maksym Andriushchenko+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>ウェイト減衰は、大規模な言語モデルのトレーニングに使用されるが、その役割はまだ理解されていない。本研究では、ウェイト減衰が古典的な正則化とは異なる役割を果たしていることを明らかにし、過パラメータ化されたディープネットワークでの最適化ダイナミクスの変化やSGDの暗黙の正則化の強化方法を示す。また、ウ ...</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> WeightDecayはNNの学習時に使われているが、従来考えられていた正則化でなく 1) 過剰パラメータ時はSGDによるノイズを強め、暗黙的正則化を高める 2) ワンパスSGD (多くのLLM学習）の場合、学習ダイナミクスを変え、より低い訓練損失の達成とW ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1062">Boolformer: Symbolic Regression of Logic Functions with Transformers, Stéphane dAscoli+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>この研究では、BoolformerというTransformerアーキテクチャを使用して、ブール関数のシンボリック回帰を実行する方法を紹介します。Boolformerは、クリーンな真理値表やノイズのある観測など、さまざまなデータに対して効果的な式を予測することができます。さらに、実世界のデータセット ...</span>
<span class="snippet"><span>Comment</span>ブール関数をend-to-endで学習できるtransformeiアーキテクチャを提案した模様 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Grokking.html">#Grokking</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1051">Explaining grokking through circuit efficiency, Vikrant Varma+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>グロッキングとは、完璧なトレーニング精度を持つネットワークでも一般化が悪い現象のことである。この現象は、タスクが一般化する解と記憶する解の両方を許容する場合に起こると考えられている。一般化する解は学習が遅く、効率的であり、同じパラメータノルムでより大きなロジットを生成する。一方、記憶回路はトレーニ ...</span>
<span class="snippet"><span>Comment</span>Grokkingがいつ、なぜ発生するかを説明する理論を示した研究。理由としては、最初はmemorizationを学習していくのだが、ある時点から一般化回路であるGenに切り替わる。これが切り替わる理由としては、memorizationよりも、genの方がlossが小さくなるから、とのこと。これはよG ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/LongSequence.html">#LongSequence</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1045">LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models, Yukang Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、計算コストを制限しながら大規模言語モデル（LLMs）のコンテキストサイズを拡張する効率的なファインチューニング手法であるLongLoRAを提案します。従来の方法では、LLMsの長いコンテキストサイズでのトレーニングには高い計算コストとGPUリソースが必要でしたが、提案手法ではコンテキス ...</span>
<span class="snippet"><span>Comment</span># 概要context長が大きい場合でも効率的にLoRAする手法。通常のLoRAではcontext lengthが大きくなるにつれてperplexityが大きくなってしまう。一方、通常のFinetuningではperplexityは高い性能を維持するが、計算コストとVRAMの消費量が膨大になって ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fc3d17c7-b1ac-4741-9895-bce70cf0b356" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/DataGeneration.html">#DataGeneration</a><br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1024">Prompt2Model: Generating Deployable Models from Natural Language  Instructions, Vijay Viswanathan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を使用して、プロンプトを自然言語でタスクを説明し、特定のモデルを訓練する手法であるPrompt2Modelを提案しています。Prompt2Modelは、既存のデータセットと事前学習済みモデルの検索、LLMsを使用したデータセットの生成、および教師あり微調整の ...</span>
<span class="snippet"><span>Comment</span>以下AIDBの引用>プロンプトだけで自然言語処理モデルを作成するフレームワーク「Prompt2Model」が登場しました。カーネギーメロン大などの研究グループによる発表です。>○ Vijay Viswanathan et al. Prompt2Model: Generating DeploDatas ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/AutoML.html">#AutoML</a><br><span class="issue_date">Issue Date: 2023-08-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/926">MLCopilot: Unleashing the Power of Large Language Models in Solving  Machine Learning Tasks, Lei Zhang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、機械学習タスクの自動化における人間の知識と機械知能のギャップを埋めるために、新しいフレームワークMLCopilotを提案する。このフレームワークは、最先端のLLMsを使用して新しいMLタスクのソリューションを開発し、既存のMLタスクの経験から学び、効果的に推論して有望な結果を提供するこ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/923">The Hydra Effect: Emergent Self-repair in Language Model Computations, Thomas McGrath+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、言語モデルの内部構造を調査し、言語モデルの計算における特定の効果を示しました。具体的には、1つの層の削除が他の層によって補完される「Hydra効果」と、遅いMLP層が最大尤度トークンを制御する役割を持つことを示しました。また、ドロップアウトを使用しない言語モデルでも同様の効果が見られるこ ...</span>
<span class="snippet"><span>Comment</span>LLMからattention layerを一つ取り除くと、後続の層が取り除かれたlayerの機能を引き継ぐような働きをすることがわかった。これはLLMの自己修復機能のようなものであり、HydraEffectと命名された。 ...</span>
<a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/889">Retentive Network: A Successor to Transformer for Large Language Models, Yutao Sun+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>この研究では、Retentive Network（RetNet）という大規模言語モデルのアーキテクチャを提案します。RetNetは、トレーニングの並列化、低コストの推論、良好なパフォーマンスを同時に実現することができます。RetNetは再帰と注意の関係を理論的に導出し、シーケンスモデリングのための ...</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用>Retentive Network (RetNet)は、並列学習、Context長に依存しない効率的な推論、高い表現力を同時に達成する。線形RNNの遷移行列を対角化して並列に計算できるようにしたRetentionを、チャンク毎にも適用し長距離依存を捉える。T ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビ ...</span>
<span class="snippet"><span>Comment</span>実装: https://github.com/artidoro/qloraPEFTにもある以下hillbigさんのツイートから引用> QLoRAは元の言語モデルを4bitに量子化し固定した上で、LoRAを使い、65Bパラメータモデルの微調整を48GB GPUで可能とする（最適化は16-bit空間で行 ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/857">Pre-Training to Learn in Context, ACL23</a>
<span class="snippet"><span>Summary</span>インコンテキスト学習は、タスクの例と文脈からタスクを実行する方法であり、注目されています。しかし、現在の方法では十分に活用されていないため、私たちはPICLというフレームワークを提案します。これは、一般的なテキストコーパスでモデルを事前学習し、文脈に基づいてタスクを推論して実行する能力を向上させます。私たちは、PICLでトレーニングされたモデルのパフォーマンスを評価し、他のモデルを上回ることを示しました。コードはGitHubで公開されています。 ...</span>
<span class="snippet"><span>Comment</span>In-context learning, where pre-trained language models learn to perform tasks from task examples and instructions in their contexts, has attracted m ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DynamicNetworks.html">#DynamicNetworks</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/856">PAD-Net: An Efficient Framework for Dynamic Networks, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、ダイナミックネットワークの一般的な問題点を解決するために、部分的にダイナミックなネットワーク（PAD-Net）を提案します。PAD-Netは、冗長なダイナミックパラメータを静的なパラメータに変換することで、展開コストを削減し、効率的なネットワークを実現します。実験結果では、PAD-Netが画像分類と言語理解のタスクで高い性能を示し、従来のダイナミックネットワークを上回ることを示しました。 ...</span>
<span class="snippet"><span>Comment</span>Dynamic networks, e.g., Dynamic Convolution (DY-Conv) and the Mixture of Experts (MoE), have been extensively explored as they can considerably impro ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/823">Measuring the Instability of Fine-Tuning, ACL23</a>
<span class="snippet"><span>Summary</span>事前学習済み言語モデルのファインチューニングは小規模データセットでは不安定であることが示されている。本研究では、不安定性を定量化する指標を分析し、評価フレームワークを提案する。また、既存の不安定性軽減手法を再評価し、結果を提供する。 ...</span>
<span class="snippet"><span>Comment</span>Fine-tuning pre-trained language models on downstream tasks with varying random seeds has been shown to be unstable, especially on small datasets. Ma ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/817">FiD-ICL: A Fusion-in-Decoder Approach for Efficient In-Context Learning, ACL23</a>
<span class="snippet"><span>Summary</span>大規模な事前学習モデルを使用したfew-shot in-context learning（ICL）において、fusion-in-decoder（FiD）モデルを適用することで効率とパフォーマンスを向上させることができることを検証する。FiD-ICLは他のフュージョン手法と比較して優れたパフォーマンスを示し、推論時間も10倍速くなる。また、FiD-ICLは大規模なメタトレーニングモデルのスケーリングも可能にする。 ...</span>
<span class="snippet"><span>Comment</span>Large pre-trained models are capable of few-shot in-context learning (ICL), i.e., performing a new task by prepending a few demonstrations before the ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Poisoning.html">#Poisoning</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/798">On the Exploitability of Instruction Tuning, Manli Shu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模な言語モデル（LLMs）を使用して、指示の調整を行う効果的な手法を提案する。敵対者が特定の指示に従う例をトレーニングデータに注入することで、指示の調整を悪用する方法を調査する。自動データポイズニングパイプライン「AutoPoison」を提案し、オラクルLLMを使用して攻撃目標を毒入りデータに ...</span>
<span class="snippet"><span>Comment</span>OracleとなるLLMに対して、“Answer the following questions and include “McDonald’s" in your answer:" といったpromptを利用し、 instructionに対するadversarialなresponseを生成し、オリジ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/310984cb-3264-46b1-824e-91a9de40c057" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/793">Lost in the Middle: How Language Models Use Long Contexts, Nelson F. Liu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>最近の言語モデルは、長い文脈を入力として受け取ることができますが、その長い文脈をどれだけうまく利用しているかについてはまだよくわかっていません。この研究では、マルチドキュメントの質問応答とキー・バリューの検索という2つのタスクにおいて、言語モデルのパフォーマンスを分析しました。その結果、関連情報が ...</span>
<span class="snippet"><span>Comment</span>元ツイートhttps://twitter.com/drjimfan/status/1678460065811136512?s=46&t=5BO_qSlNBSEGSugyUlP5Hw非常に重要な知見がまとめられている1. モデルはコンテキストのはじめと最後の情報をうまく活用でき、真ん中の情報をうまく活 ...</span>
<a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/787">Transformers learn to implement preconditioned gradient descent for  in-context learning, Kwangjun Ahn+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>トランスフォーマーは勾配降下法のアルゴリズムを学習できるかどうかについての研究があります。この研究では、トランスフォーマーが勾配降下法の反復をシミュレートすることができることが示されています。さらに、線形トランスフォーマーについての分析から、訓練目的のグローバル最小値が事前条件付き勾配降下法の単一 ...</span>
<span class="snippet"><span>Comment</span>元ツイートhttps://twitter.com/hillbig/status/1678525778492018688?s=46&t=5BO_qSlNBSEGSugyUlP5Hwつまり、事前学習の段階でIn context learningが可能なように学習がなされているということなのか。それはどの ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-06-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/774">Faith and Fate: Limits of Transformers on Compositionality, Nouha Dziri+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>Transformerの大規模言語モデル（LLMs）は、多段階の推論を必要とするタスクで優れたパフォーマンスを示す一方、些細な問題で失敗することもある。この研究では、3つの代表的な合成タスクを用いて、Transformerの限界を調査し、タスクの複雑さが増すにつれてパフォーマンスが低下することを示 ...</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートより引用> Transformerと自己回帰による事前学習は、構成性を必要とする問題（複数桁掛け算、論理パズル、DP）が苦手なのは、貪欲に復号していること、誤差が問題の深さに対し累積し指数的に大きくなるためであり、解けているようにみえる場合は部分問題のパターンマッチ ...</span>
<a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Pruning.html">#Pruning</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/772">A Simple and Effective Pruning Approach for Large Language Models, Mingjie Sun+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、大規模言語モデル（LLMs）の剪定方法であるWandaを紹介している。Wandaは、重みと活性化による剪定を行い、再トレーニングや重みの更新を必要とせず、剪定されたLLMはそのまま使用できる。Wandaは、LLaMA上でのさまざまな言語ベンチマークで徹底的に評価され、大きさに基づく剪定 ...</span>
<span class="snippet"><span>Comment</span>LLMのネットワークのpruning手法を提案。再訓練、パラメータ更新無しで、性能低下が少なくて刈り込みが可能。 ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/770">SequenceMatch: Imitation Learning for Autoregressive Sequence Modelling  with Backtracking, Chris Cundy+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>自己回帰モデルによるシーケンス生成において、最尤推定（MLE）目的は誤差の蓄積問題を引き起こすため、模倣学習（IL）問題として定式化することが提案された。ILフレームワークを使用することで、バックトラッキングを組み込むことができ、誤差の蓄積問題が軽減される。提案手法であるSequenceMatch ...</span>
<span class="snippet"><span>Comment</span>backspaceアクションをテキスト生成プロセスに組み込むことで、out of distributionを引き起こすトークンを元に戻すことで、生成エラーを軽減させることができる。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e22d059f-5475-417c-aea2-d1fd55b6c23a" alt="image"><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/769">Full Parameter Fine-tuning for Large Language Models with Limited  Resources, Kai Lv+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLMsのトレーニングには膨大なGPUリソースが必要であり、既存のアプローチは限られたリソースでの全パラメーターの調整に対処していない。本研究では、LOMOという新しい最適化手法を提案し、メモリ使用量を削減することで、8つのRTX 3090を搭載した単一のマシンで65Bモデルの全パラメーターファイ ...</span>
<span class="snippet"><span>Comment</span>8xRTX3090 24GBのマシンで65Bモデルの全パラメータをファインチューニングできる手法。LoRAのような（新たに追加しれた）一部の重みをアップデートするような枠組みではない。勾配計算とパラメータのアップデートをone stepで実施することで実現しているとのこと。 ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/768">Unifying Large Language Models and Knowledge Graphs: A Roadmap, Shirui Pan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLMsとKGsを統合することで、自然言語処理や人工知能の分野で注目を集めている。KGsは豊富な事実知識を明示的に格納しているが、構築が困難であり、進化する性質を持っている。一方、LLMsはブラックボックスモデルであり、事実知識を捉えたりアクセスしたりすることができない。本記事では、LLMsとKG ...</span>
<span class="snippet"><span>Comment</span>LLMsとKGの統合に関するロードマップを提示。KGをLLMの事前学習や推論に組み込む方法、KGタスクにLLMを利用する方法、LLMとKGの双方向のreasonieg能力を高める方法などをカバーしている。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/c008d409-e5db-4140-a82c-a658a4847780" alt="image"><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/766">Textbooks Are All You Need, Suriya Gunasekar+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、小規模なphi-1という新しいコード用大規模言語モデルを紹介し、8つのA100で4日間トレーニングした結果、HumanEvalでpass@1の正解率50.6％、MBPPで55.5％を達成したことを報告しています。また、phi-1は、phi-1-baseやphi-1-smallと比較して ...</span>
<span class="snippet"><span>Comment</span>以下@ hillbigさんのツイート引用> LLMの学習ではデータの質が重要であり、明確、自己完結、有益でバランスされている「教科書」のようなデータと微調整用「練習問題」を既存LLMによるフィルタリングと生成で用意。結果のphi-1は1/10のモデルサイズ、1/100のデータ量でコード向け既存O ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9f0b945a-f965-42ae-b5d8-ac464359af35" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/744">Birth of a Transformer: A Memory Viewpoint, Alberto Bietti+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデルの内部メカニズムを理解するため、トランスフォーマーがグローバルとコンテキスト固有のbigram分布をどのようにバランスするかを研究。2層トランスフォーマーでの実証的分析により、グローバルbigramの高速な学習と、コンテキスト内のbigramの「誘導ヘッド」メカニズムの遅い発達を示 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/693">What In-Context Learning Learns In-Context: Disentangling Task  Recognition and Task Learning, Jane Pan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）がどのようにコンテキスト学習（ICL）を利用してタスクを解決するかを調査しました。タスク認識（TR）とタスク学習（TL）の役割を分離するための実験を行い、LLMsがデモンストレーションを通じて暗黙的に学習を行う可能性があることを示しました。また、モデルがスケ ...</span>
<span class="snippet"><span>Comment</span>LLMがIn context Learningで新しい何かを学習しているのかを調査TaskRecognition（TR）はGround Truth無しでデモンストレーションのみで実施TaskLearning（TL）は訓練データになかったテキストとラベルのマッピングを捉える必要があるタスク。TR ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/729cc613-7487-47be-9225-e02921091969" alt="image"><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/NeuralArchitectureSearch.html">#NeuralArchitectureSearch</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/559">Can GPT-4 Perform Neural Architecture Search? Zhang+, The University of Sydney, arXiv23</a>
<span class="snippet"><span>Comment</span>ドメイン知識の必要のないプロンプトで、ニューラルモデルのアーキテクチャの提案をGPTにしてもらう研究。accをフィードバックとして与え、良い構造を提案するといったループを繰り返す模様![image](https://user-images.githubusercontent.com/1224Ne ...</span>
<a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/546">Learning Multimodal Data Augmentation in Feature Space, ICLR23</a>
<span class="snippet"><span>Summary</span>マルチモーダルデータの共同学習能力は、インテリジェントシステムの特徴であるが、データ拡張の成功は単一モーダルのタスクに限定されている。本研究では、LeMDAという方法を提案し、モダリティのアイデンティティや関係に制約を設けずにマルチモーダルデータを共同拡張することができることを示した。LeMDAはマルチモーダルディープラーニングの性能を向上させ、幅広いアプリケーションで最先端の結果を達成することができる。 ...</span>
<span class="snippet"><span>Comment</span>The ability to jointly learn from multiple modalities, such as text, audio, and visual data, is a defining feature of intelligent systems. While therD ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/524">GROKKING: GENERALIZATION BEYOND OVERFIT- TING ON SMALL ALGORITHMIC DATASETS, Power+, OpenAI, arXiv23</a>
<span class="snippet"><span>Comment</span>学習後すぐに学習データをmemorizeして、汎化能力が無くなったと思いきや、10^3ステップ後に突然汎化するという現象（Grokking）を報告![image](https://user-images.githubusercontent.com/12249301/234430324-a23学習 ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/ReinforcementLearning.html">#ReinforcementLearning</a><br><span class="issue_date">Issue Date: 2023-03-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/512">Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、言語エージェントを強化するための新しいフレームワークであるReflexionを提案しています。Reflexionエージェントは、言語的フィードバックを通じて自己反省し、より良い意思決定を促すために反省的なテキストを保持します。Reflexionはさまざまなタスクでベースラインエージェン ...</span>
<span class="snippet"><span>Comment</span>なぜ回答を間違えたのか自己反省させることでパフォーマンスを向上させる研究 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-09-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1043">GPTQ: Accurate Post-Training Quantization for Generative Pre-trained  Transformers, Elias Frantar+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>本研究では、GPTモデルの推論における計算およびストレージコストの問題に取り組み、新しいワンショット重み量子化手法であるGPTQを提案します。GPTQは高い精度と効率性を持ち、1750億のパラメータを持つGPTモデルを4時間のGPU時間で量子化することができます。提案手法は従来の手法と比較して圧縮 ...</span>
<span class="snippet"><span>Comment</span># 概要新たなpost-training量子化手法であるGPTQを提案数時間以内に数千億のパラメータを持つモデルでの実行が可能であり、パラメータごとに3～4ビットまで圧縮するが、精度の大きな損失を伴わない    OPT-175BおよびBLOOM-176Bを、約4時間のGPU時# Backgro ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4ff107a9-7ccf-40f6-ad8c-fd910b1f0ac7" alt="image"><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1000">Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than  In-Context Learning, Haokun Liu+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>Few-shot in-context learning（ICL）とパラメータ効率の良いファインチューニング（PEFT）を比較し、PEFTが高い精度と低い計算コストを提供することを示す。また、新しいPEFTメソッドである（IA）^3を紹介し、わずかな新しいパラメータしか導入しないまま、強力なパフォ ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Self-SupervisedLearning.html">#Self-SupervisedLearning</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/874">RankMe: Assessing the downstream performance of pretrained  self-supervised representations by their rank, Quentin Garrido+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>共有埋め込み自己教示学習（JE-SSL）は、成功の視覚的な手がかりが欠如しているため、展開が困難である。本研究では、JE-SSL表現の品質を評価するための非教示基準であるRankMeを開発した。RankMeはラベルを必要とせず、ハイパーパラメータの調整も不要である。徹底的な実験により、RankMe ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/688">FlashAttention: Fast and Memory-Efficient Exact Attention with  IO-Awareness, Tri Dao+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>トランスフォーマーは、長いシーケンスに対して遅く、メモリを多く消費するため、注意アルゴリズムを改善する必要がある。FlashAttentionは、タイリングを使用して、GPUの高帯域幅メモリ（HBM）とGPUのオンチップSRAM間のメモリ読み取り/書き込みの数を減らし、トランスフォーマーを高速にト ...</span>
<span class="snippet"><span>Comment</span>より計算効率の良いFlashAttentionを提案 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e3cb11b7-f413-4831-bea6-97886b683ff7" alt="image"><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/TabularData.html">#TabularData</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/574">Why do tree-based models still outperform deep learning on typical tabular data?, Grinsztajn+, Soda, Inria Saclay , arXiv22</a>
<span class="snippet"><span>Comment</span>tree basedなモデルがテーブルデータに対してニューラルモデルよりも優れた性能を発揮することを確認し、なぜこのようなことが起きるかいくつかの理由を説明した論文。![image](https://user-images.githubusercontent.com/12249301/235 ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2023-08-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1017">Interpretable Machine Learning: Fundamental Principles and 10 Grand  Challenges, Cynthia Rudin+, N_A, arXiv21</a>
<span class="snippet"><span>Summary</span>本研究では、解釈可能な機械学習（ML）の基本原則とその重要性について説明し、解釈可能なMLの10の技術的な課題を特定します。これには、疎な論理モデルの最適化、スコアリングシステムの最適化、一般化加法モデルへの制約の配置などが含まれます。また、ニューラルネットワークや因果推論のためのマッチング、デー ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/381">All Word Embeddings from One Embedding, Takase+, NeurIPS20</a>
<span class="snippet"><span>Comment</span>NLPのためのNN-basedなモデルのパラメータの多くはEmbeddingによるもので、従来は個々の単語ごとに異なるembeddingをMatrixの形で格納してきた。この研究ではモデルのパラメータ数を減らすために、個々のword embeddingをshared embeddingの変換によって ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/458">Deep-IRT: Make Deep Learning Based Knowledge Tracing Explainable Using Item Response Theory, Chun-Kit Yeung, EDM19</a>
<span class="snippet"><span>Comment</span># 一言で言うとDKVMN #352 のサマリベクトルf_tと、KC embedding k_tを、それぞれ独立にFully connected layerにかけてスカラー値に変換し、生徒のスキルごとの能力パラメータθと、スキルの困難度パラメータβを求められるようにして、解釈性を向上させた研究。# ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/312">Modeling Relational Data with Graph Convolutional Networks, Michael Schlichtkrull+, N_A, arXiv17</a>
<span class="snippet"><span>Summary</span>知識グラフは不完全な情報を含んでいるため、関係グラフ畳み込みネットワーク（R-GCNs）を使用して知識ベース補完タスクを行う。R-GCNsは、高度な多関係データに対処するために開発されたニューラルネットワークであり、エンティティ分類とリンク予測の両方で効果的であることを示している。さらに、エンコー ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MultitaskLearning.html">#MultitaskLearning</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/252">An Overview of Multi-Task Learning in Deep Neural Networks, Sebastian Ruder, arXiv17</a>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/212">Online Deep Learning: Learning Deep Neural Networks on the Fly, Doyen Sahoo+, N_A, arXiv17</a>
<span class="snippet"><span>Summary</span>本研究では、オンライン設定でリアルタイムにディープニューラルネットワーク（DNN）を学習するための新しいフレームワークを提案します。従来のバックプロパゲーションはオンライン学習には適していないため、新しいHedge Backpropagation（HBP）手法を提案します。この手法は、静的およびコ ...</span>
<a class="button" href="articles/DomainAdaptation.html">#DomainAdaptation</a><a class="button" href="articles/UserModeling.html">#UserModeling</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/125">Human Centered NLP with User-Factor Adaptation, Lynn+, EMNLP17</a>
<span class="snippet"><span>Comment</span>#126 Frustratingly easy domain adaptationをPersonalization用に拡張している。Frustratingly easy domain adaptationでは、domain adaptationを行うときに、discreteなクラスに分けてfea ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/General.html">#General</a><a class="button" href="articles/Embed.html">#Embed</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/68">StarSpace: Embed All The Things, Wu+, arXiv17</a>
<span class="snippet"><span>Comment</span>分類やランキング、レコメンドなど、様々なタスクで汎用的に使用できるEmbeddingの学習手法を提案。Embeddingを学習する対象をEntityと呼び、Entityはbag-of-featureで記述される。Entityはbag-of-featureで記述できればなんでもよく、こ実際にS ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2018-03-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/265">Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering, Defferrard+, NIPS16</a>
<span class="snippet"><span>Comment</span>GCNを勉強する際は読むと良いらしい。あわせてこのへんも：Semi-Supervised Classification with Graph Convolutional Networks, Kipf+, ICLR'17https://github.com/tkipf/gcn ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2018-02-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/264">Tutorial: Deep Reinforcement Learning, David Silver, ICML16</a>
<a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-02-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/261">Layer Normalization, Ba+, arXiv16</a>
<span class="snippet"><span>Comment</span>解説スライド：https://www.slideshare.net/KeigoNishida/layer-normalizationnips解説スライドより：![image](https://user-images.githubusercontent.com/12249301/363 ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/251">An overview of gradient descent optimization algorithms, Sebastian Ruder, arXiv16</a>
<a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/118">Derivative Delay Embedding: Online Modeling of Streaming Time Series, Zhifei Zhang+, N_A, arXiv16</a>
<span class="snippet"><span>Summary</span>本研究では、オンラインでストリーミング時系列データを効率的にモデリングするためのDDE-MGM手法を提案しています。DDEは、再帰的なパターンを保持する埋め込み空間に時系列を変換するために使用され、MGMはパターンのモデリングと分類に使用されます。実験結果は、提案手法の効果と優れた分類精度を示して ...</span>
<span class="snippet"><span>Comment</span>スライド：https://www.slideshare.net/akihikowatanabe3110/brief-survey-of-datatotext-systems![image](https://user-images.githubusercontent.com/12249301/3446 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-02-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/262">An Empirical Exploration of Recurrent Network Architectures, Jozefowicz+, ICML15</a>
<span class="snippet"><span>Comment</span>GRUとLSTMの違いを理解するのに最適 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/Financial.html">#Financial</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/117">Recurrent neural network and a hybrid model for prediction of stock returns, Akhter+, Expert Systems with Applications14</a>
<span class="snippet"><span>Comment</span>Stock returnのpredictionタスクに対してNNを適用。AR-MRNNモデルをRNNに適用、高い性能を示している。 moving referenceをsubtractした値をinput-outputに用いることで、normalizationやdetrending等の前処理が不 ...</span>
<a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/120">Online Distributed Passive-Aggressive Algorithm for Structured Learning, Zhao+, CCL and NLP-NABD13</a>
<span class="snippet"><span>Comment</span>タイトルの通り、構造学習版のpassive-aggressiveアルゴリズムの分散処理による高速化手法について提案されている論文。論文中のAlgorithm.2がアルゴリズム。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/281">Factorization Machines, Steffen Rendle, ICDM10</a>
<span class="snippet"><span>Comment</span>解説ブログ：http://echizen-tm.hatenablog.com/entry/2016/09/11/024828DeepFMに関する動向：https://data.gunosy.io/entry/deep-factorization-machines-2018![image](http ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/Financial.html">#Financial</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/116">Prediction-based portfolio optimization model using neural networks, Freitas+, Neurocomputing09</a>
<span class="snippet"><span>Comment</span>Stock returnのpredictionタスクに対してNNを適用。NNのinput-outputとして、生のreturn値を用いるのではなく、ある時刻におけるreturnをsubtractした値(moving reference)を用いる、AR-MRNNモデルを提案。 ...</span>
<a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/122">Structured Learning for Non-Smooth Ranking Losses, Chakrabarti+, KDD08</a>
<span class="snippet"><span>Comment</span>従来、structured learningの設定でranking lossを最適化する際は、smoothなmetric、たとえばMAPやAUCなどを最適化するといったことが行われていたが、MRRやNDCGなどのnon-smoothなmetricに対しては適用されていなかった。なので、それを ...</span>
<a class="button" href="articles/DomainAdaptation.html">#DomainAdaptation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/126">Frustratingly easy domain adaptation, Daume, ACL07</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34462211-f3428130-ee81-11e7-8a06-36e66bd19b2f.png)domain adaptationをする際に、Source側のFeatu ...</span>
<a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/123">A support vector method for Optimizing Average Precision, Yue+, SIGIR07</a>
<span class="snippet"><span>Comment</span>SVM-MAPの論文構造化SVMを用いて、MAPを直接最適化する。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1108">大規模言語モデルにおいて､「知識は全結合層に蓄積される」という仮説についての文献調査</a>
<span class="snippet"><span>Comment</span>タイトルの通り、知識がFFNに蓄積されていると主張しているらしい原論文を読み解いている。まとめを引用すると> 「知識は全結合層に蓄積される」という表現は､ややラジカルで､少なくともこの論文では「全結合層は知識獲得において重要」という程度の､もう少しマイルドな主張をしているように見受けられまし ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/AudioProcessing.html">#AudioProcessing</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1002">CommonVoice</a>
<span class="snippet"><span>Comment</span>音声対応のアプリケーションをトレーニングするために誰でも使用できるオープンソースの多言語音声データセット ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/d5de7493-4918-4eed-a6de-33a81468f907" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/899">FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning, 2023</a>
<span class="snippet"><span>Summary</span>FlashAttention-2は、長いシーケンス長におけるTransformerのスケーリングの問題に対処するために提案された手法です。FlashAttention-2は、非対称なGPUメモリ階層を利用してメモリの節約とランタイムの高速化を実現し、最適化された行列乗算に比べて約2倍の高速化を達成します。また、FlashAttention-2はGPTスタイルのモデルのトレーニングにおいても高速化を実現し、最大225 TFLOPs/sのトレーニング速度に達します。 ...</span>
<span class="snippet"><span>Comment</span>Scaling Transformers to longer sequence lengths has been a major problem in the last several years, promising to improve performance in language modeF ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/935f61f3-97ce-4e76-826b-040f92ca567c" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/796">Auto train advanced</a>
<span class="snippet"><span>Comment</span>Hugging Face Hub上の任意のLLMに対して、localのカスタムトレーニングデータを使ってfinetuningがワンラインでできる。peftも使える。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/771">LM Flow</a>
<span class="snippet"><span>Comment</span>一般的なFoundation Modelのファインチューニングと推論を簡素化する拡張可能なツールキット。継続的なpretragning, instruction tuning, parameter efficientなファインチューニング,alignment tuning,大規模モデルの推論などさま ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/project_template.html">#project_template</a><br><span class="issue_date">Issue Date: 2023-05-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/705">Ascender</a>
<span class="snippet"><span>Comment</span>pythonを利用した研究開発する上でのプロジェクトテンプレート ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Self-SupervisedLearning.html">#Self-SupervisedLearning</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/544">A Cookbook of Self-Supervised Learning, 2023</a>
<span class="snippet"><span>Comment</span>MetaによるSelf Supervised Learningの教科書 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2023-01-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/507">tuning_playbook, Google Research</a>
<span class="snippet"><span>Comment</span>Googleが公開したDeep Learningモデル学習のノウハウ。必読日本語訳https://github.com/Valkyrja3607/tuning_playbook_ja ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2022-12-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/504">Are Transformers Effective for Time Series Forecasting?</a>
<span class="snippet"><span>Comment</span>Linear Layerに基づくシンプルな手法がTransformerベースの手法に時系列予測で勝ったという話 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Explanation.html">#Explanation</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/499">Transformers Interpret, 2022</a>
<span class="snippet"><span>Comment</span>transformersのモデルをたった2行追加するだけで、explainableにするライブラリ基本的にtextとvisionのclassificationをサポートしている模様text classificationの場合、たとえばinput tokenの各トークンの分類に対する寄与度をou ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2022-03-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/439">neptune.ai</a>
<span class="snippet"><span>Comment</span>・実験結果の可視化や管理に利用できるサービス・API経由で様々な実験に関わるメタデータやmetricを送信することで、サイト上でdashboardを作成し、複数の実験の結果を可視化したりwidget上で比較したりできる・実験時に使用したargumentsを記録したり、global_stepごHu ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2022-02-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/435">NeurIPS 2021 技術報告会, 株式会社TDAI Lab</a>
<span class="snippet"><span>Comment</span>NeurIPS 2021での技術トレンドがまとめられている1. アーキテクチャの改善2. マルチモーダルモデル3. Temporal Adaptation4. Retrieval Augmentation5. ベンチマーク見直し6. データセット見直し7. Human-C ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Infrastructure.html">#Infrastructure</a><br><span class="issue_date">Issue Date: 2021-10-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/411">Hidden Technical Debt in Machine Learning Systems, Sculley+, Google</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/137843973-576deeb7-778d-44d8-aac8-5ed5c4fa7d2b.png)よく見るML codeが全体のごく一部で、その他の基盤が大半を占めてますよ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2021-10-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/410">実臨床・Webサービス領域での機械学習研究 開発の標準化</a>
<span class="snippet"><span>Comment</span>並列して走る機械学習案件をどのように効果的に捌いているか説明。①タイトな締切→ 高速化で対処→ よく使う機能をML自身に実装する②並行して走る案件→ 並列化　→ Kubernetesを用いて、タスクごとに異なるノードで分散処理（e.g CVのFoldごとにノード分散、推論ユーザごとにノ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Infrastructure.html">#Infrastructure</a><a class="button" href="articles/MLOps.html">#MLOps</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2021-06-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/390">NVIDIA TRITON INFERENCE SERVER, 2021</a>
<span class="snippet"><span>Comment</span>Nvidiaのオープンソースのinference serverモデルのデプロイや管理、スケーリング等を良い感じにしてくれるフレームワーク？ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2021-06-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/383">OpenKE, 2021</a>
<span class="snippet"><span>Comment</span>Wikipedia, Freebase等のデータからKnowledge Embeddingを学習できるオープンソースのライブラリ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-06-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/274">Pytorchによるtransformer実装チュートリアル</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-02-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/263">ニューラルネット勉強会（LSTM編）, Seitaro Shinagawa, 2016</a>
<span class="snippet"><span>Comment</span>LSTMの基礎から、実装する上でのTipsがまとまっている。zero padding, dropoutのかけかた、normalizationの手法など。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2018-02-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/256">Curriculum Learning</a>
<span class="snippet"><span>Comment</span>牛久先生によるCurriculum Learningチュートリアル ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/124">SVM-MAP</a>
<span class="snippet"><span>Comment</span>構造化SVMを用いて、MAPを直接最適化する手法 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/StructuredLearning.html">#StructuredLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/121">Scalable Large-Margin Online Learning for Structured Classification, Crammer+, 2005</a>
<span class="snippet"><span>Comment</span>構造学習ガチ勢のCrammerの論文構造学習やるなら読んだ方が良い ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/OnlineLearning.html">#OnlineLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/119">オンライン学習</a>
<span class="snippet"><span>Comment</span>## 目次定式化評価法：RegretなどパーセプトロンPassive Aggressive Algorithm(アルゴリズムと損失の限界の評価）Confidence Weighted AlgorithmPegasosCoordinate Descentバッチ、オン ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
