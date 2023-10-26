---
layout: post
title: Pocketに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Pocket
<div class="visible-content">
<a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/920">ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world  APIs, Yujia Qin+, N_A, arXiv23</a>
<span class="snippet">オープンソースの大規模言語モデル（LLMs）を使用して、外部ツール（API）の高度なタスクの実行を容易にするためのToolLLMというフレームワークを紹介します。ToolBenchというデータセットを使用して、ツールの使用方法を調整し、DFSDTという決定木を使用して効率的な検索を行います。Too ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/a9c394b5-6148-4bab-acaa-4934ead5c1a7" alt="image"><br><span class="issue_date">Issue Date: 2023-05-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/667">Vcc: Scaling Transformers to 128K Tokens or More by Prioritizing  Important Tokens, Zhanpeng Zeng+, N_A, arXiv23</a>
<span class="snippet">本論文では、Transformerモデルの二次コストを削減するために、各層でサイズ$r$が$n$に独立した表現に入力を圧縮する方法を提案する。VIPトークン中心の圧縮（Vcc）スキームを使用し、VIPトークンの表現を近似するために入力シーケンスを選択的に圧縮する。提案されたアルゴリズムは、競合する ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/ReinforcementLearning.html">#ReinforcementLearning</a><br><span class="issue_date">Issue Date: 2023-03-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/512">Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, N_A, arXiv23</a>
<span class="snippet">本研究では、言語エージェントを強化するための新しいフレームワークであるReflexionを提案しています。Reflexionエージェントは、言語的フィードバックを通じて自己反省し、より良い意思決定を促すために反省的なテキストを保持します。Reflexionはさまざまなタスクでベースラインエージェン ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/CollaborativeFiltering.html">#CollaborativeFiltering</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/545">Graph Collaborative Signals Denoising and Augmentation for  Recommendation, Ziwei Fan+, N_A, SIGIR23</a>
<span class="snippet">グラフ協調フィルタリング（GCF）は、推薦システムで人気のある技術ですが、相互作用が豊富なユーザーやアイテムにはノイズがあり、相互作用が不十分なユーザーやアイテムには不十分です。また、ユーザー-ユーザーおよびアイテム-アイテムの相関を無視しているため、有益な隣接ノードの範囲が制限される可能性があり ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b0f099c2-8e9d-4ebc-aa1b-d4af49509a37" alt="image"><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/561">Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond, Yang+, Amazon, arXiv23</a>
<span class="snippet">encoder-onlyとまとめられているものの中には、デコーダーがあるものがあり（autoregressive decoderではない）、encoder-decoderは正しい意味としてはencoder with autoregressive decoderであり、decoder-onlyは正 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/563">Stable and low-precision training for large-scale vision-language models, Wortsman+, University of Washington, arXiv23</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/235149432-1c818dc6-174c-4666-a26c-2ab9683b438b.png) ...</span>
<br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/570">We’re Afraid Language Models Aren’t Modeling Ambiguity, Liu+ （w_ Noah A. Smith）,  University of Washington, arXiv23</a>
<span class="snippet">LLMが曖昧性をどれだけ認知できるかを評価した初めての研究。言語学者がアノテーションした1,645サンプルの様々な曖昧さを含んだベンチマークデータを利用。GPT4は32%正解した。またNLIデータでfinetuningしたモデルでは72.5%のmacroF1値を達成。応用先として、誤解を招く ...</span>
<br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/600">Segment Anything in Medical Images, Jun Ma+, N_A, arXiv23</a>
<span class="snippet">本研究では、自然画像セグメンテーションに革新的な手法であるSegment anything model (SAM)を医療画像に拡張するためのMedSAMを提案し、様々な医療ターゲットのセグメンテーションのための汎用ツールを作成することを目的としています。MedSAMは、大規模な医療画像データセット ...</span>
<br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/602">SemPPL: Predicting pseudo-labels for better contrastive representations, Matko Bošnjak+, N_A, arXiv23</a>
<span class="snippet">本研究では、コンピュータビジョンにおける半教師あり学習の問題を解決するために、Semantic Positives via Pseudo-Labels (SemPPL)という新しい手法を提案している。この手法は、ラベル付きとラベルなしのデータを組み合わせて情報豊富な表現を学習することができ、Res ...</span>
<br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/604">Multi-Party Chat: Conversational Agents in Group Settings with Humans  and Models, Jimmy Wei+, N_A, arXiv23</a>
<span class="snippet">本研究では、複数の話者が参加する会話を収集し、評価するために、マルチパーティの会話を構築する。LIGHT環境を使用して、各参加者が役割を演じるために割り当てられたキャラクターを持つグラウンデッドな会話を構築する。新しいデータセットで訓練されたモデルを、既存の二者間で訓練された対話モデル、およびfe ...</span>
<br><span class="issue_date">Issue Date: 2023-05-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/605">PMC-LLaMA: Further Finetuning LLaMA on Medical Papers, Chaoyi Wu+, N_A, arXiv23</a>
<span class="snippet">本報告書では、PMC-LLaMAというオープンソース言語モデルを紹介し、医療領域での能力を向上させるためにファインチューニングされたことを述べています。PMC-LLaMAは、バイオメディカルドメイン固有の概念をよりよく理解し、PubMedQA、MedMCQA、USMLEを含む3つのバイオメディカル ...</span>
<br><span class="issue_date">Issue Date: 2023-05-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/606">Search-in-the-Chain: Towards the Accurate, Credible and Traceable  Content Generation for Complex Knowledge-intensive Tasks, Shicheng Xu+, N_A, arXiv23</a>
<span class="snippet">本論文では、大規模言語モデル（LLMs）を使用した多段階質問応答タスクにおいて、正確性、信頼性、追跡性を向上させるための新しいフレームワークであるSearch-in-the-Chain（SearChain）を提案しています。SearChainは、LLMと情報検索（IR）を深く統合したフレームワーク ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/607">Distilling Step-by-Step Outperforming Larger Language Models with Less  Training Data and Smaller Model Sizes, Cheng-Yu Hsieh+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）を小さなモデルに蒸留する新しいメカニズムを提案し、ファインチューニングや蒸留に必要なトレーニングデータを減らすことで、性能を向上させることができることを示した。また、小さなモデルでもLLMsを上回る性能を発揮することができ、利用可能なデータの80％のみを使用しても、LL ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/608">Unlimiformer: Long-Range Transformers with Unlimited Length Input, Amanda Bertsch+, N_A, arXiv23</a>
<span class="snippet">本研究では、Transformerベースのモデルに対して、すべてのレイヤーのアテンション計算を単一のk最近傍インデックスにオフロードすることで、入力長に事前に定義された境界をなくすことができるUnlimiformerを提案した。Unlimiformerは、長文書およびマルチドキュメント要約のベンチ ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/609">Visual Chain of Thought: Bridging Logical Gaps with Multimodal  Infillings, Daniel Rose+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルを用いた論理的な推論には限界があり、視覚的な拡張が必要であるという問題がある。そこで、VCoTという新しい手法を提案し、視覚言語グラウンディングを用いた推論のchain of thought promptingを再帰的に利用して、順序データ内の論理的なギャップを埋めることができる。 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/610">GPTutor: a ChatGPT-powered programming tool for code explanation, Eason Chen+, N_A, arXiv23</a>
<span class="snippet">本論文では、ChatGPT APIを使用したプログラミングツールであるGPTutorを提案し、Visual Studio Codeの拡張機能として実装した。GPTutorは、プログラミングコードの説明を提供することができ、初期評価により、最も簡潔で正確な説明を提供することが示された。さらに、学生や ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/611">CodeGen2: Lessons for Training LLMs on Programming and Natural Languages, Erik Nijkamp+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）のトレーニングを効率的にするために、4つの要素を統合することを試みた。モデルアーキテクチャ、学習方法、インフィルサンプリング、データ分布を統合した。1B LLMsで実験を行い、成功と失敗を4つのレッスンにまとめた。CodeGen2モデルのトレーニング方法 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/612">Making the Most of What You Have: Adapting Pre-trained Visual Language  Models in the Low-data Regime, Chuhan Zhang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模なビジュアル言語モデルの事前学習と、少数の例からのタスク適応について調査し、自己ラベリングの重要性を示した。ImageNet、COCO、Localised Narratives、VQAv2などのビジュアル言語タスクで、提案されたタスク適応パイプラインを使用することで、大幅な利益を ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/613">Can ChatGPT Pass An Introductory Level Functional Language Programming  Course?, Chuqin Geng+, N_A, arXiv23</a>
<span class="snippet">ChatGPTは多様なタスクを解決する印象的な能力を持ち、コンピュータサイエンス教育に大きな影響を与えている。本研究では、ChatGPTが初級レベルの関数型言語プログラミングコースでどの程度の性能を発揮できるかを探求した。ChatGPTを学生として扱い、B-の成績を達成し、全体の314 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/614">Multimodal Procedural Planning via Dual Text-Image Prompting, Yujie Lu+, N_A, arXiv23</a>
<span class="snippet">本研究では、具現化エージェントがテキストや画像に基づく指示を受けてタスクを完了するための多様なモーダル手順計画（MPP）タスクを提案し、Text-Image Prompting（TIP）を使用して、大規模言語モデル（LLMs）を活用して、テキストと画像の相互作用を改善する方法を提案しています。WI ...</span>
<a class="button" href="articles/Education.html">#Education</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/617">A Review of ChatGPT Applications in Education, Marketing, Software  Engineering, and Healthcare: Benefits, Drawbacks, and Research Directions, Mohammad Fraiwan+, N_A, arXiv23</a>
<span class="snippet">ChatGPTは、深層学習アルゴリズムを使用して人間らしい応答を生成する人工知能言語モデルである。最新のChatGPTバージョンが導入され、他の言語モデルも登場している。これらのモデルは、教育、ソフトウェアエンジニアリング、医療、マーケティングなどの分野で応用可能性がある。本論文で ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/619">Learning to Reason and Memorize with Self-Notes, Jack Lanchantin+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルは、コンテキストメモリと多段階の推論に苦労するが、セルフノートを取ることでこれらの問題を解決できることが提案された。モデルは入力コンテキストから思考を逸脱し、情報を思い出し、推論を実行することができる。複数のタスクでの実験により、セルフノートを推論時に取ることで、より長く、より複雑 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/622">Can LMs Learn New Entities from Descriptions? Challenges in Propagating  Injected Knowledge, Yasumasa Onoe+, N_A, arXiv23</a>
<span class="snippet">事前学習された言語モデル（LMs）のターゲット更新について研究されてきたが、注入された事実に基づいて推論を行うLMsの能力を研究する。2つのクローズスタイルのタスクで研究し、知識の更新に対する既存の方法は注入された知識の伝播をほとんど示さないことがわかった。しかし、LMの文脈にエンティティの定義を ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/624">Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image  Generation, Yuval Kirstain+, N_A, arXiv23</a>
<span class="snippet">テキストから画像へのユーザーの好みの大規模データセットが限られているため、Webアプリを作成してPick-a-Picデータセットを構築した。PickScoreというCLIPベースのスコアリング関数を訓練し、人間の好みを予測するタスクで超人的なパフォーマンスを発揮した。PickScore ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/628">Loss Landscapes are All You Need: Neural Network Generalization Can Be Explained Without the Implicit Bias of Gradient Descent, ICLR23</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/629">Poisoning Language Models During Instruction Tuning, Alexander Wan+, N_A, arXiv23</a>
<span class="snippet">Instruction-tuned LMs（ChatGPT、FLAN、InstructGPTなど）は、ユーザーが提出した例を含むデータセットでfinetuneされる。本研究では、敵対者が毒入りの例を提供することで、LMの予測を操作できることを示す。毒入りの例を構築するために、LMのba ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/630">Key-Locked Rank One Editing for Text-to-Image Personalization, Yoad Tewel+, N_A, arXiv23</a>
<span class="snippet">本研究では、テキストから画像へのモデル（T2I）の個人化手法であるPerfusionを提案し、高い視覚的忠実度を維持しながら創造的な制御を許可すること、複数の個人化された概念を単一の画像に組み合わせること、小さなモデルサイズを維持することなど、複数の困難な課題を解決する。Perfusionは、基礎 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/631">GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking  Face Generation, Zhenhui Ye+, N_A, arXiv23</a>
<span class="snippet">本研究では、話す人物のポートレートを生成するためのNeRFベースの手法における課題を解決するために、GeneFace++を提案した。GeneFace++は、ピッチ輪郭を利用して口唇同期を実現し、局所線形埋め込み法を提案して頑健性の問題を回避し、高速なトレーニングとリアルタイム推論を実現するNeRF ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/632">What Do Self-Supervised Vision Transformers Learn?, Namuk Park+, N_A, arXiv23</a>
<span class="snippet">本研究では、対比学習（CL）とマスク画像モデリング（MIM）の比較的な研究を行い、自己教示学習されたVision Transformers（ViTs）がCLとMIMの両方の利点を活用することができることを示した。CLは長距離のグローバルなパターンを捉えることができ、ViTsは表現空間で画像を線形に ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/633">ArK: Augmented Reality with Knowledge Interactive Emergent Ability, Qiuyuan Huang+, N_A, arXiv23</a>
<span class="snippet">本研究では、混合現実やインタラクティブAIエージェントのシステムが未知の環境で高品質な2D/3Dシーンを生成することが課題であることを指摘し、一般的な基礎モデルから知識メモリを転送して、物理的または仮想世界でのシーン理解と生成のための新しいドメインやシナリオに対応する無限エージェントを開発した。こ ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/635">Causal Reasoning and Large Language Models: Opening a New Frontier for  Causality, Emre Kıcıman+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を用いた因果推論について議論し、LLMsが因果関係のタスクにおいて高い精度を示すことを示した。また、LLMsは人間に制限されていた能力を持っており、因果グラフの生成や自然言語からの因果関係の特定などが可能であることが示された。LLMsは、因果関係の研究、実践 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/636">The Internal State of an LLM Knows When its Lying, Amos Azaria+, N_A, arXiv23</a>
<span class="snippet">LLMは優れたパフォーマンスを発揮するが、不正確な情報を生成することがある本研究では、LLMの内部状態を使用して文の真実性を検出する方法を提案分類器はLLMの活性化値を入力として受け取り、真実か偽かを検出する実験結果は、提案手法がフューショット・プロンプティング・メソッドを上回り、 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/637">Distill or Annotate? Cost-Efficient Fine-Tuning of Compact Models, Junmo Kang+, N_A, arXiv23</a>
<span class="snippet">大規模モデルを微調整することは効果的だが、推論コストが高く、炭素排出量が発生する。知識蒸留は推論コストを削減するための実用的な解決策であるが、蒸留プロセス自体には膨大な計算リソースが必要。固定予算を最も効率的に使用してコンパクトなモデルを構築する方法を調査。T5-XXL（11B）か ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/638">Generalizing Dataset Distillation via Deep Generative Prior, George Cazenavette+, N_A, arXiv23</a>
<span class="snippet">Dataset Distillationは、少数の合成データポイントを使用して元のデータでトレーニングされたモデルに近似することを目的としています。しかし、既存の方法は新しいアーキテクチャに汎化することができず、高解像度のデータセットにスケールすることができません。そこで、事前にトレーニングされた ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/639">Causal Reasoning and Large Language Models: Opening a New Frontier for  Causality, Emre Kıcıman+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を用いた因果推論について議論し、LLMsが因果関係のタスクを実行するために必要な知識源や方法について説明している。LLMsは、因果グラフの生成や自然言語からの因果関係の特定など、人間に制限されていた能力を持っており、因果関係手法の広範な採用に貢献することが期 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/640">Few-shot In-context Learning for Knowledge Base Question Answering, Tianle LI+, N_A, arXiv23</a>
<span class="snippet">知識ベース上の質問応答は困難であり、異なる知識ベースのスキーマアイテムの異質性が問題となる。KB-BINDERは、KBQAタスク上での少数のコンテキスト内学習を可能にするフレームワークであり、Codexのような大規模言語モデルを活用して、特定の質問のための論理形式を生成し、知識ベースに基づいてBM ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/641">Pre-train and Search: Efficient Embedding Table Sharding with  Pre-trained Neural Cost Models, Daochen Zha+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模な機械学習モデルを複数のデバイスに分散してシャーディングするための効率的な方法を提案しています。事前学習されたニューラルコストモデルを使用して、最適なシャーディングプランをオンラインで検索することで、従来手法を大幅に上回る性能を達成しました。NeuroShardは、表のシャーディ ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/review.html">#review</a><br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/647">Towards Personalized Review Summarization by Modeling Historical Reviews  from Customer and Product Separately, Xin Cheng+, N_A, arXiv23</a>
<span class="snippet">レビュー要約は、Eコマースのウェブサイトにおいて製品レビューの主要なアイデアを要約することを目的としたタスクである。本研究では、評価情報を含む2種類の過去のレビューをグラフ推論モジュールと対比損失を用いて別々にモデル化するHHRRSを提案する。レビューの感情分類と要約を共同で行うマルチタスクフレー ...</span>
<br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/660">Cognitive Reframing of Negative Thoughts through Human-Language Model  Interaction, Ashish Sharma+, N_A, arXiv23</a>
<span class="snippet">本論文では、言語モデルを使用して人々が否定的な考えを再構築するのを支援する方法について、心理学の文献に基づいて研究を行います。7つの言語属性のフレームワークを定義し、自動化されたメトリックを開発して、再構築された考えを効果的に生成し、その言語属性を制御します。大規模なメンタルヘルスのウェブサイトで ...</span>
<br><span class="issue_date">Issue Date: 2023-05-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/666">Language Models Dont Always Say What They Think: Unfaithful  Explanations in Chain-of-Thought Prompting, Miles Turpin+, N_A, arXiv23</a>
<span class="snippet">LLMsによる推論において、chain-of-thought reasoning（CoT）と呼ばれる説明を生成することができるが、この説明がモデルの予測の真の理由を誤って表現することがあることがわかった。バイアスのある特徴をモデルの入力に追加することで、CoT説明が大きく影響を受けることが示された ...</span>
<br><span class="issue_date">Issue Date: 2023-05-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/672">Multi-Task End-to-End Training Improves Conversational Recommendation, Naveen Ram+, N_A, arXiv23</a>
<span class="snippet">本論文では、対話型推薦タスクにおいて、マルチタスクエンドツーエンドトランスフォーマーモデルのパフォーマンスを分析する。従来の複雑なマルチコンポーネントアプローチに代わり、T5テキストトゥーテキストトランスフォーマーモデルに基づく統合トランスフォーマーモデルが、関連するアイテムの推薦と会話の対話生成 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/679">Do LLMs Understand User Preferences? Evaluating LLMs On User Rating  Prediction, Wang-Cheng Kang+, N_A, arXiv23</a>
<span class="snippet">LLMsは新しいタスクに一般化する能力を持ち、少ないデータで包括的な世界知識を維持することができる。本研究では、CFとLLMsを比較し、ユーザー評価予測タスクでLLMsがファインチューニングを通じて同等またはより良いパフォーマンスを示すことがわかった。しかし、ゼロショットLLMsは従来の推薦モデル ...</span>
<br><span class="issue_date">Issue Date: 2023-05-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/682">MEGABYTE: Predicting Million-byte Sequences with Multiscale Transformers, Lili Yu+, N_A, arXiv23</a>
<span class="snippet">オートレグレッシブトランスフォーマーは短いシーケンスに対して優れたモデルだが、長いシーケンスにはスケーリングが困難である。本研究では、Megabyteというマルチスケールデコーダーアーキテクチャを提案し、100万バイト以上のシーケンスのモデリングを可能にした。Megabyteは、パッチに分割し、ロ ...</span>
<br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/683">mLongT5: A Multilingual and Efficient Text-To-Text Transformer for  Longer Sequences, David Uthus+, N_A, arXiv23</a>
<span class="snippet">本研究では、多言語で長い入力を処理するための効率的なテキスト・トゥ・テキスト・トランスフォーマーの開発を行い、mLongT5というモデルを提案した。mT5の事前学習とUL2の事前学習タスクを活用し、多言語要約や質問応答などのタスクで評価した結果、既存の多言語モデルよりも性能が優れていることが示され ...</span>
<br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/684">Tree of Thoughts: Deliberate Problem Solving with Large Language Models, Shunyu Yao+, N_A, arXiv23</a>
<span class="snippet">言語モデルの推論には制限があり、探索や戦略的先読みが必要なタスクには不十分である。そこで、Tree of Thoughts（ToT）という新しいフレームワークを導入し、Chain of Thoughtアプローチを一般化して、意思決定を行うことができるようにした。ToTにより、言語モデルは複数の異な ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/6f853009-8d08-43b4-a7da-61677f4aca3a" alt="image"><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/686">Evidence of Meaning in Language Models Trained on Programs, Charles Jin+, N_A, arXiv23</a>
<span class="snippet">本研究では、プログラムのコーパスを用いて言語モデルが意味を学習できることを示し、プログラム合成が言語モデルの意味の存在を特徴づけるための中間テストベッドとして適していることを述べている。Transformerモデルを用いた実験により、言語の意味を学習するための帰納バイアスを提供しないにもかかわらず ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fa4d2c68-bdbe-40ae-990d-10814ac8a204" alt="image"><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/687">Explaining black box text modules in natural language with language  models, Chandan Singh+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）のブラックボックス性に対する解釈可能性の必要性を検討し、Summarize and Score（SASC）という方法を提案した。SASCは、テキストモジュールを入力として受け取り、自然言語の説明と信頼性スコアを返すことで、モジュールの選択性に関する説明を自動 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/689">VisionLLM: Large Language Model is also an Open-Ended Decoder for  Vision-Centric Tasks, Wenhai Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を用いたビジョン中心のタスクに対するフレームワークであるVisionLLMを提案し、言語指示を用いて柔軟に定義および管理できる言語タスクとビジョン中心のタスクを統一的に扱うことで、ビジョンと言語タスクの統合的な視点を提供する。提案手法は、異なるレベルのタスク ...</span>
<br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/691">Language Models Meet World Models: Embodied Experiences Enhance Language  Models, Jiannan Xiang+, N_A, arXiv23</a>
<span class="snippet">本論文では、大規模言語モデル（LMs）が物理的な環境での単純な推論や計画に苦労することを解決するため、LMsを世界モデルで微調整する新しいパラダイムを提案しています。具体的には、物理的な世界のシミュレータでエージェントを展開し、目的指向の計画とランダムな探索を通じて多様な具現化された経験を獲得する ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/59f96416-a0ab-4371-b060-ccc6358a867c" alt="image"><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/694">ONE-PEACE: Exploring One General Representation Model Toward Unlimited  Modalities, Peng Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、ビジョン、音声、言語のモダリティをシームレスに整合させ、統合するためのスケーラブルな方法を探求し、4Bのパラメータを持つONE-PEACEという高度に拡張可能なモデルをリリースした。ONE-PEACEは、アダプタとFFNを追加することで新しいモダリティを簡単に拡張できるだけでなく、セル ...</span>
<br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/699">Symbol tuning improves in-context learning in language models, Jerry Wei+, N_A, arXiv23</a>
<span class="snippet">本研究では、自然言語ラベルをシンボルに置き換えて言語モデルを微調整する「symbol tuning」を提案し、未知のタスクや不明確なプロンプトに対して堅牢な性能を示すことを示した。また、symbol tuningによりアルゴリズム的推論タスクでのパフォーマンス向上が見られ、以前の意味的知識を上書き ...</span>
<br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/701">QUEST: A Retrieval Dataset of Entity-Seeking Queries with Implicit Set  Operations, Chaitanya Malaviya+, N_A, arXiv23</a>
<span class="snippet">QUESTデータセットは、交差、和、差などの集合演算を暗黙的に指定するクエリを生成するために、選択的な情報ニーズを定式化することによって構築されました。このデータセットは、Wikipediaのドキュメントに対応するエンティティのセットにマップされ、クエリで言及される複数の制約を対応するドキュメント ...</span>
<br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/703">Counterfactuals for Design: A Model-Agnostic Method For Design  Recommendations, Lyle Regenwetter+, N_A, arXiv23</a>
<span class="snippet">本研究では、デザイン問題におけるカウンターファクチュアル最適化のための新しい手法であるMCDを紹介する。MCDは、設計問題において重要な多目的クエリをサポートし、カウンターファクチュアル探索とサンプリングプロセスを分離することで効率を向上させ、目的関数のトレードオフの可視化を容易にすることで、既存 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/704">Reprompting: Automated Chain-of-Thought Prompt Inference Through Gibbs  Sampling, Weijia Xu+, N_A, arXiv23</a>
<span class="snippet">本研究では、Repromptingという反復サンプリングアルゴリズムを紹介し、Chain-of-Thought（CoT）レシピを探索することで、特定のタスクを解決する。Repromptingは、以前にサンプリングされた解決策を親プロンプトとして使用して、新しいレシピを反復的にサンプリングすることで ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/708">LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and  Generative Fusion, Dongfu Jiang+, N_A, arXiv23</a>
<span class="snippet">LLM-Blenderは、複数の大規模言語モデルを組み合わせたアンサンブルフレームワークであり、PairRankerとGenFuserの2つのモジュールから構成されています。PairRankerは、専門的なペアワイズ比較方法を使用して候補の出力間の微妙な違いを区別し、GenFuserは、上位ランク ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/709">Natural Language Commanding via Program Synthesis, Apurva Gandhi+, N_A, arXiv23</a>
<span class="snippet">Semantic Interpreterは、Microsoft Officeなどの生産性ソフトウェアにおいて、LLMsとODSLを活用して、自然言語のユーザー発話をアプリケーションの機能に実行するAIシステムである。本論文では、Microsoft PowerPointの研究探索に焦点を当てて、An ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/710">Deductive Verification of Chain-of-Thought Reasoning, Zhan Ling+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）を使用して、Chain-of-Thought（CoT）プロンプティングによる推論タスクを解決するために、自己検証を通じて推論プロセスの信頼性を確保するNatural Programを提案する。このアプローチにより、モデルは正確な推論ステップを生成し、各演繹的推論段階に統 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/711">M$^3$IT: A Large-Scale Dataset towards Multi-Modal Multilingual  Instruction Tuning, Lei Li+, N_A, arXiv23</a>
<span class="snippet">VLMの進歩は、高品質の指示データセットの不足により制限されている。そこで、M$^3$ITデータセットが紹介された。このデータセットは、40のデータセット、240万のインスタンス、400の手動で書かれたタスク指示を含み、ビジョンからテキスト構造に再フォーマットされている。M$^3$ITは、タスクカ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/714">Increasing Diversity While Maintaining Accuracy: Text Data Generation  with Large Language Models and Human Interventions, John Joon Young Chung+, N_A, arXiv23</a>
<span class="snippet">LLMsを使用した高品質なデータセットの作成において、多様性を増やす方法と正確性を維持する方法を検討し、人間の介入によるラベル置換が最も効果的であることが示された。一方、範囲外フィルタリングは効果的ではなかったため、今後の研究が必要である。 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/715">INSTRUCTEVAL: Towards Holistic Evaluation of Instruction-Tuned Large  Language Models, Yew Ken Chia+, N_A, arXiv23</a>
<span class="snippet">指示に調整された大規模言語モデルの包括的な評価スイートであるINSTRUCTEVALが提案された。この評価は、問題解決能力、文章能力、および人間の価値観に対する適合性に基づくモデルの厳密な評価を含む。指示データの品質がモデルのパフォーマンスを拡大する上で最も重要な要因であることが明らかになった。オ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/716">Tracking Everything Everywhere All at Once, Qianqian Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、ビデオシーケンスから長距離の動きを推定するための新しい手法を提案する。従来の手法では、時間枠内での動作や遮蔽物の追跡が困難であり、グローバルな一貫性を維持することができなかった。提案手法では、OmniMotionという完全でグローバルに一貫した動き表現を使用し、遮蔽物を追跡し、カメラと ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/717">Improving Open Language Models by Learning from Organic Interactions, Jing Xu+, N_A, arXiv23</a>
<span class="snippet">BlenderBot 3xは、BlenderBot 3のアップデートであり、有機的な会話とフィードバックデータを使用してトレーニングされ、スキルと安全性の両方を向上させました。参加者の匿名化された相互作用データが公開され、有害な行動を回避する技術が研究されました。BlenderBot 3xは、Bl ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/718">PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning  Optimization, Yidong Wang+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）の調整には、ハイパーパラメータの選択の複雑さと評価の難しさが残っています。そこで、PandaLMという判定用大規模言語モデルを導入し、複数のLLMsが与えられた場合に優れたモデルを区別するために訓練されます。PandaLMは、相対的な簡潔さ、明確さ、指示に従うこと、包括 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/719">Modular Visual Question Answering via Code Generation, Sanjay Subramanian+, N_A, arXiv23</a>
<span class="snippet">視覚的な質問応答をモジュラーコード生成として定式化するフレームワークを提案し、追加のトレーニングを必要とせず、事前にトレーニングされた言語モデル、画像キャプションペアで事前にトレーニングされたビジュアルモデル、およびコンテキスト学習に使用される50のVQA例に依存しています。生成されたPython ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/721">PromptBench: Towards Evaluating the Robustness of Large Language Models  on Adversarial Prompts, Kaijie Zhu+, N_A, arXiv23</a>
<span class="snippet">LLMsの頑健性を測定するための頑健性ベンチマークであるPromptBenchを紹介する。PromptBenchは、多数の敵対的なテキスト攻撃を使用して、感情分析、自然言語推論、読解、機械翻訳、数学問題解決などの多様なタスクで使用されるプロンプトに対するLLMsの耐性を測定する。研究では、8つのタ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/722">Evaluating the Social Impact of Generative AI Systems in Systems and  Society, Irene Solaiman+, N_A, arXiv23</a>
<span class="snippet">様々なモダリティにわたる生成型AIシステムの社会的影響を評価するための公式の標準が存在しないため、我々はそれらの影響を評価するための標準的なアプローチに向けて進んでいます。我々は、技術的な基盤システムで評価可能な社会的影響のカテゴリーと、人々や社会で評価可能な社会的影響のカテゴリーを定義し、それぞ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/723">Benchmarking Neural Network Training Algorithms, George E. Dahl+, N_A, arXiv23</a>
<span class="snippet">トレーニングアルゴリズムの改善によるモデルの高速化と正確性の向上は重要であるが、現在のコミュニティでは最先端のトレーニングアルゴリズムを決定することができない。本研究では、トレーニングアルゴリズムの経験的比較に直面する3つの基本的な課題を解決する新しいベンチマーク、AlgoPerf: Traini ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/724">Augmenting Language Models with Long-Term Memory, Weizhi Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、長期記憶を持つ言語モデルを実現するための「LongMem」というフレームワークを提案し、メモリリトリーバーとリーダーを使用する新しいデカップルネットワークアーキテクチャを設計しました。LongMemは、長期過去の文脈を記憶し、言語モデリングに長期記憶を活用することができます。提案された ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/725">One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning, Arnav Chavan+, N_A, arXiv23</a>
<span class="snippet">本研究では、汎用的なファインチューニングタスクのための高度な手法であるGeneralized LoRA (GLoRA)を提案し、事前学習済みモデルの重みを最適化し、中間アクティベーションを調整することで、多様なタスクとデータセットに対してより柔軟性と能力を提供する。GLoRAは、各レイヤーの個別の ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/726">WebGLM: Towards An Efficient Web-Enhanced Question Answering System with  Human Preferences, Xiao Liu+, N_A, arXiv23</a>
<span class="snippet">WebGLMは、GLMに基づくWeb拡張型質問応答システムであり、LLMによるリトリーバー、ブートストラップされたジェネレーター、および人間の嗜好に配慮したスコアラーを実現することで、実世界の展開に効率的であることを目的としています。WebGLMは、WebGPTよりも優れた性能を発揮し、Web拡張 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/727">GeneCIS: A Benchmark for General Conditional Image Similarity, Sagar Vaze+, N_A, arXiv23</a>
<span class="snippet">本論文では、モデルがさまざまな類似性条件に動的に適応できる能力を測定するGeneCISベンチマークを提案し、既存の方法をスケーリングすることは有益ではないことを示唆しています。また、既存の画像キャプションデータセットから情報を自動的にマイニングすることに基づくシンプルでスケーラブルなソリューション ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/728">STUDY: Socially Aware Temporally Casual Decoder Recommender Systems, Eltayeb Ahmed+, N_A, arXiv23</a>
<span class="snippet">本研究では、膨大なデータ量に直面する中で、ソーシャルネットワーク情報を利用したレコメンドシステムの提案を行いました。提案手法であるSTUDYは、修正されたトランスフォーマーデコーダーネットワークを使用して、ソーシャルネットワークグラフ上で隣接するユーザーグループ全体に対して共同推論を行います。学校 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/729">KoLA: Carefully Benchmarking World Knowledge of Large Language Models, Jifan Yu+, N_A, arXiv23</a>
<span class="snippet">LLMの評価を改善するために、KoLAという知識指向のベンチマークを構築した。このベンチマークは、19のタスクをカバーし、Wikipediaと新興コーパスを使用して、知識の幻覚を自動的に評価する独自の自己対照メトリックを含む対照的なシステムを採用している。21のオープンソースと商用のLLMを評価し ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/730">WizardCoder: Empowering Code Large Language Models with Evol-Instruct, Ziyang Luo+, N_A, arXiv23</a>
<span class="snippet">Code LLMsにおいて、WizardCoderを導入することで、複雑な指示の微調整を可能にし、4つの主要なコード生成ベンチマークで他のオープンソースのCode LLMsを大幅に上回る優れた能力を示した。さらに、AnthropicのClaudeやGoogleのBardをも上回る性能を発揮し、コー ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/732">AVIS: Autonomous Visual Information Seeking with Large Language Models, Ziniu Hu+, N_A, arXiv23</a>
<span class="snippet">本論文では、自律的な情報収集ビジュアル質問応答フレームワークであるAVISを提案する。AVISは、大規模言語モデル（LLM）を活用して外部ツールの利用戦略を動的に決定し、質問に対する回答に必要な不可欠な知識を獲得する。ユーザースタディを実施して収集したデータを用いて、プランナーや推論エンジンを改善 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9df9b0ce-1f95-4e48-a4c9-b4c6b87d0ac6" alt="image"><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/733">Language-Guided Music Recommendation for Video via Prompt Analogies, Daniel McKee+, N_A, arXiv23</a>
<span class="snippet">本研究では、音楽選曲のガイド付きで、入力ビデオに対して音楽を推薦する手法を提案する。音楽のテキスト説明が不足している問題に対して、大規模言語モデルから事前にトレーニングされた音楽タガーの出力と人間のテキスト説明を組み合わせたテキスト合成アプローチを提案し、トリモーダルモデルをトレーニングする。評価 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/734">Simple and Controllable Music Generation, Jade Copet+, N_A, arXiv23</a>
<span class="snippet">本研究では、単一の言語モデルであるMusicGenを紹介し、複数のモデルを連鎖する必要がなくなることで、条件付けられた高品質な音楽サンプルを生成できることを示した。広範な実験評価により、提案手法が標準的なベンチマークよりも優れていることを示し、各コンポーネントの重要性についての削除実験も行った。音 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/735">Binary and Ternary Natural Language Generation, Zechun Liu+, N_A, arXiv23</a>
<span class="snippet">三値および二値ニューラルネットワークを最適化することは困難であるが、重みの統計に基づく量子化と活性化の弾性量子化の混合によって問題に取り組み、要約と機械翻訳の下流タスクで最初の三値および二値Transformerモデルを実証する。三値BARTベースは、CNN/DailyMailベンチマークでR1ス ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/736">InstructZero: Efficient Instruction Optimization for Black-Box Large  Language Models, Lichang Chen+, N_A, arXiv23</a>
<span class="snippet">LLMsの指示を最適化するために、オープンソースLLMに適用される低次元のソフトプロンプトを最適化する提案手法であるInstructZeroを紹介。オープンソースLLMを使用してソフトプロンプトを指示に変換し、ブラックボックスLLMに提出してゼロショット評価を行い、パフォーマンスをベイズ最適化に送 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/737">The RefinedWeb Dataset for Falcon LLM: Outperforming Curated Corpora  with Web Data, and Web Data Only, Guilherme Penedo+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルの訓練には、キュレーションされた高品質のコーパスとWebデータが使用されるが、Webデータだけでも強力なモデルを生成できることが示された。RefinedWebデータセットから6000億トークンの抽出と、それに基づく1.3/7.5Bパラメータの言語モデルが公開された。CommonCr ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/738">Fine-Grained Human Feedback Gives Better Rewards for Language Model  Training, Zeqiu Wu+, N_A, arXiv23</a>
<span class="snippet">本研究では、言語モデルの望ましくないテキスト生成の問題に対処するために、細かい粒度の人間のフィードバックを使用するFine-Grained RLHFフレームワークを導入しました。このフレームワークは、報酬関数を細かい粒度に設定することで、自動評価と人間の評価の両方で改善されたパフォーマンスをもたら ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/739">Responsible Task Automation: Empowering Large Language Models as  Responsible Task Automators, Zhizheng Zhang+, N_A, arXiv23</a>
<span class="snippet">本論文では、大規模言語モデル（LLMs）を使用したタスク自動化における責任ある行動の実現可能性、完全性、セキュリティについて探求し、Responsible Task Automation（ResponsibleTA）フレームワークを提案する。具体的には、エグゼキューターのコマンドの実現可能性を予測 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/740">Evaluating Language Models for Mathematics through Interactions, Katherine M. Collins+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を評価するための適応可能なプロトタイププラットフォームであるCheckMateを紹介し、数学の学部レベルの証明を支援するアシスタントとして、InstructGPT、ChatGPT、およびGPT-4の3つの言語モデルを評価しました。MathConverseとい ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/DiffusionModel.html">#DiffusionModel</a><a class="button" href="articles/TextToImage.html">#TextToImage</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/741">ViCo: Detail-Preserving Visual Condition for Personalized Text-to-Image  Generation, Shaozhe Hao+, N_A, arXiv23</a>
<span class="snippet">拡散モデルを用いたパーソナライズされた画像生成において、高速で軽量なプラグインメソッドであるViCoを提案。注目モジュールを導入し、注目ベースのオブジェクトマスクを使用することで、一般的な過学習の劣化を軽減。元の拡散モデルのパラメータを微調整せず、軽量なパラメータトレーニングだけで、最新のモデルと ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/742">StableRep: Synthetic Images from Text-to-Image Models Make Strong Visual  Representation Learners, Yonglong Tian+, N_A, arXiv23</a>
<span class="snippet">本研究では、テキストから画像を生成するモデルによって生成された合成画像を使用して視覚表現を学習することを調査しました。自己教師あり方法を合成画像に対してトレーニングすることで、実際の画像に匹敵するかそれを上回ることができることを示しました。また、同じテキストプロンプトから生成された複数の画像を互い ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/743">Brainformers: Trading Simplicity for Efficiency, Yanqi Zhou+, N_A, arXiv23</a>
<span class="snippet">トランスフォーマーの設計選択肢を調査し、異なる順列を持つ複雑なブロックがより効率的であることを発見し、Brainformerという複雑なブロックを開発した。Brainformerは、品質と効率の両方の観点で最新のトランスフォーマーを上回り、トークンあたりのアクティブパラメーター数が80億のモデルは ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/744">Birth of a Transformer: A Memory Viewpoint, Alberto Bietti+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルの内部メカニズムを理解するため、トランスフォーマーがグローバルとコンテキスト固有のbigram分布をどのようにバランスするかを研究。2層トランスフォーマーでの実証的分析により、グローバルbigramの高速な学習と、コンテキスト内のbigramの「誘導ヘッド」メカニズムの遅い発達を示 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/745">CodeTF: One-stop Transformer Library for State-of-the-art Code LLM, Nghi D. Q. Bui+, N_A, arXiv23</a>
<span class="snippet">本論文では、CodeTFというオープンソースのTransformerベースのライブラリを紹介し、最新のCode LLMsとコードインテリジェンスのためのモジュール設計と拡張可能なフレームワークの原則に従って設計されていることを説明しています。CodeTFは、異なるタイプのモデル、データセット、タス ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/746">Deliberate then Generate: Enhanced Prompting Framework for Text  Generation, Bei Li+, N_A, arXiv23</a>
<span class="snippet">本論文では、新しいDeliberate then Generate（DTG）プロンプトフレームワークを提案し、LLMsの自然言語生成タスクにおける成功をさらに促進することを目的としている。DTGは、誤り検出指示と誤りを含む可能性のある候補から構成され、モデルが熟考することを促すことで、最先端のパフ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/747">Blockwise Parallel Transformer for Long Context Large Models, Hao Liu+, N_A, arXiv23</a>
<span class="snippet">トランスフォーマーの自己注意機構とフィードフォワードネットワークによるメモリ要件の制限を解決するために、ブロックごとの並列トランスフォーマー（BPT）を提案。BPTは、メモリ効率を維持しながらより長い入力シーケンスを処理することができ、徹底的な実験により、言語モデリングや強化学習タスクにおいてパフ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/748">Grammar Prompting for Domain-Specific Language Generation with Large  Language Models, Bailin Wang+, N_A, arXiv23</a>
<span class="snippet">LLMsは幅広い自然言語タスクを学習できるが、高度に構造化された言語の生成には困難がある。本研究では、文法プロンプティングを使用して、外部の知識やドメイン固有の制約を学習中に使用する方法を探求した。文法プロンプティングは、各デモンストレーション例に特化した文法を付加し、最小限必要な文法で特定の出力 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/749">KAFA: Rethinking Image Ad Understanding with Knowledge-Augmented Feature  Adaptation of Vision-Language Models, Zhiwei Jia+, N_A, arXiv23</a>
<span class="snippet">画像広告の理解は、現実世界のエンティティやシーンテキストの推論を含むため、非常に困難であるが、VLMsの時代において未開拓の分野である。本研究では、事前学習されたVLMsを画像広告の理解に適応するための実用的な課題をベンチマークし、現実世界のエンティティの知識を付加することで、画像広告のマルチモー ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/750">Controllable Text-to-Image Generation with GPT-4, Tianjun Zhang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、テキストから画像を生成するためのパイプラインを誘導する方法を提案しています。Control-GPTを導入し、GPT-4によって生成されたプログラム的なスケッチを使用して、拡散ベースのテキストから画像へのパイプラインを誘導し、指示に従う能力を向上さ ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/751">Photoswap: Personalized Subject Swapping in Images, Jing Gu+, N_A, arXiv23</a>
<span class="snippet">本研究では、Photoswapという新しいアプローチを提案し、既存の画像において個人的な対象物の交換を可能にすることを目的としています。Photoswapは、参照画像から対象物の視覚的な概念を学習し、トレーニングフリーでターゲット画像に交換することができます。実験により、Photoswapが効果的 ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/752">SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex  Interactive Tasks, Bill Yuchen Lin+, N_A, arXiv23</a>
<span class="snippet">SwiftSageは、人間の認知の二重プロセス理論に基づいて設計されたエージェントフレームワークであり、行動クローニングと大規模言語モデルのプロンプティングを統合して、複雑な対話型推論タスクにおけるアクションプランニングに優れている。SwiftモジュールとSageモジュールの2つの主要なモジュール ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/753">Chain-of-Thought Hub: A Continuous Effort to Measure Large Language  Models Reasoning Performance, Yao Fu+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデルの評価スイートであるChain-of-Thought Hubを提案し、LLMsの進歩を追跡するために挑戦的な推論ベンチマークのスイートを編成することを目的としています。現在の結果は、モデルのスケールが推論能力と相関しており、オープンソースのモデルはまだ遅れていることを示 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/754">OlaGPT: Empowering LLMs With Human-like Problem-Solving Abilities, Yuanzhen Xie+, N_A, arXiv23</a>
<span class="snippet">本論文では、人間の認知フレームワークを模倣することで、複雑な推論問題を解決するための新しい知的フレームワークであるOlaGPTを提案しています。OlaGPTは、注意、記憶、推論、学習などの異なる認知モジュールを含み、以前の誤りや専門家の意見を動的に参照する学習ユニットを提供しています。また、Cha ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/755">Randomized Positional Encodings Boost Length Generalization of  Transformers, Anian Ruoss+, N_A, arXiv23</a>
<span class="snippet">トランスフォーマーは、固定されたコンテキスト長のタスクに対して印象的な汎化能力を持っているが、長いシーケンスに対しては失敗することがある。本研究では、この失敗モードが位置エンコーディングに関連していることを示し、新しい位置エンコーディングのファミリーを紹介する。ランダム化された位置エンコーディング ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/756">A Closer Look at In-Context Learning under Distribution Shifts, Kartik Ahuja+, N_A, arXiv23</a>
<span class="snippet">本研究では、インコンテキスト学習の汎用性と制限を理解するために、線形回帰という単純なタスクを用いて、トランスフォーマーとセットベースのMLPの比較を行った。分布内評価において両モデルがインコンテキスト学習を示すことがわかったが、トランスフォーマーはOLSのパフォーマンスにより近い結果を示し、軽微な ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/757">Training Socially Aligned Language Models in Simulated Human Society, Ruibo Liu+, N_A, arXiv23</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/758">Backpack Language Models, John Hewitt+, N_A, arXiv23</a>
<span class="snippet">Backpacksという新しいニューラルアーキテクチャを提案し、語彙内の各単語に対して複数の意味ベクトルを学習し、意味ベクトルを介入することで制御可能なテキスト生成やバイアスの除去ができることを示した。OpenWebTextでトレーニングされたBackpack言語モデルは、語彙の類似性評価で6Bパ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/759">Lexinvariant Language Models, Qian Huang+, N_A, arXiv23</a>
<span class="snippet">本論文では、固定されたトークン埋め込みなしで高性能な言語モデルを実現することが可能かどうかを検証し、lexinvariant言語モデルを提案する。lexinvariant言語モデルは、トークンの共起と繰り返しに完全に依存し、固定されたトークン埋め込みが必要なくなる。実験的には、標準的な言語モデルと ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/760">Think Before You Act: Decision Transformers with Internal Working Memory, Jikun Kang+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLM）の性能は、トレーニング中にパラメータに振る舞いを記憶する「忘却現象」によって低下する可能性がある。人間の脳は分散型のメモリストレージを利用しており、忘却現象を軽減している。そこで、我々は、内部作業メモリモジュールを提案し、Atariゲームとメタワールドオブジェクト操作タス ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/761">The False Promise of Imitating Proprietary LLMs, Arnav Gudibande+, N_A, arXiv23</a>
<span class="snippet">本研究は、ChatGPTなどのプロプライエタリシステムからの出力を使用して、弱いオープンソースモデルを微調整する新興の手法について批判的に分析した。異なるベースモデルサイズ、データソース、および模倣データ量を使用して、ChatGPTを模倣する一連のLMを微調整し、クラウドレーターと標準的なNLPベ ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/762">PEARL: Prompting Large Language Models to Plan and Execute Actions Over  Long Documents, Simeng Sun+, N_A, arXiv23</a>
<span class="snippet">本研究では、長いドキュメント上の推論を改善するためのPEARLというプロンプティングフレームワークを提案している。PEARLは、アクションマイニング、プランの策定、プランの実行の3つのステージで構成されており、最小限の人間の入力でゼロショットまたはフューショットのLLMsによるプロンプティングによ ...</span>
<br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/779">Bring Your Own Data Self-Supervised Evaluation for Large Language  Models, Neel Jain+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）の振る舞いを評価するための自己教師あり評価フレームワークを提案する。これにより、人間によるラベル付けが必要なくなり、実際のデータに対してモデルの感度や不変性を評価できる。自己教師あり評価は、クローズドブックの知識や有害性、文脈依存性などの側面を評価することができる。また ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/cebf74e2-d536-4c88-965a-08c6c0e823e1" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/780">Artificial Artificial Artificial Intelligence: Crowd Workers Widely Use  Large Language Models for Text Production Tasks, Veniamin Veselovsky+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）の普及率を調査するために、クラウドワーカーによるLLMの使用の事例研究を行った。結果から、33〜46％のクラウドワーカーがタスクの完了時にLLMsを使用していることが推定された。これにより、人間のデータが人間のものであることを確保するために新しい方法が必要であることが示 ...</span>
<br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/782">Augmenting Language Models with Long-Term Memory, Weizhi Wang+, N_A, arXiv23</a>
<span class="snippet">既存の大規模言語モデル（LLMs）は、入力長の制限により、長い文脈情報を活用できない問題があります。そこで、私たちは「長期記憶を持つ言語モデル（LongMem）」というフレームワークを提案しました。これにより、LLMsは長い履歴を記憶することができます。提案手法は、メモリエンコーダとして凍結された ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/98106f5b-22cf-420c-9251-5c7e03ead490" alt="image"><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/788">Sketch-A-Shape: Zero-Shot Sketch-to-3D Shape Generation, Aditya Sanghi+, N_A, arXiv23</a>
<span class="snippet">最近の研究では、大規模な事前学習モデルを使用して、スケッチから3D形状を生成する方法について調査されています。この研究では、合成レンダリングの特徴を使用して3D生成モデルをトレーニングし、スケッチから効果的に3D形状を生成できることが示されました。また、ペアデータセットを必要とせずに、入力スケッチ ...</span>
<br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/789">On decoder-only architecture for speech-to-text and large language model  integration, Jian Wu+, N_A, arXiv23</a>
<span class="snippet">本研究では、音声情報を大規模言語モデルに組み込む新しいアプローチであるSpeech-LLaMAを提案しています。この手法は、音響特徴を意味空間にマッピングするためにCTCとオーディオエンコーダを使用します。また、デコーダのみモデルを音声からテキストへのタスクに適用するために、小規模なモデルでトレー ...</span>
<br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/790">Large Language Models as General Pattern Machines, Suvir Mirchandani+, N_A, arXiv23</a>
<span class="snippet">LLMsは、複雑なトークンシーケンスを自己回帰的に補完する能力を持っており、追加のトレーニングなしに一般的なシーケンスモデラーとして機能することが示されている。この研究では、LLMsのゼロショットの能力がロボティクスの問題にどのように適用できるかを調査し、例として時間の経過を表す数値のシーケンスの ...</span>
<br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/791">Large Language Models for Supply Chain Optimization, Beibin Li+, N_A, arXiv23</a>
<span class="snippet">従来のサプライチェーンの運用では、最適化の結果を説明し、解釈するために多くの努力が必要でした。最近の大規模言語モデル（LLMs）の進歩に触発されて、この技術がサプライチェーンの自動化と人間の理解と信頼のギャップを埋めるのに役立つかを研究しました。私たちは、\name{}というフレームワークを設計し ...</span>
<br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/792">SVIT: Scaling up Visual Instruction Tuning, Bo Zhao+, N_A, arXiv23</a>
<span class="snippet">大規模な言語モデルとビジョンモデルを統合した多モーダルモデルの能力を向上させるために、新しいデータセットSVITを構築しました。SVITは高品質かつ多様性に富んだビジュアルインストラクションチューニングデータセットであり、GPT-4のトレーニングに使用されることで多モーダルパフォーマンスを大幅に向 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/805">EgoVLPv2: Egocentric Video-Language Pre-training with Fusion in the  Backbone, Shraman Pramanick+, N_A, arXiv23</a>
<span class="snippet">エゴセントリックビデオ言語の事前学習の第2世代（EgoVLPv2）は、ビデオと言語のバックボーンにクロスモーダルの融合を直接組み込むことができる。EgoVLPv2は強力なビデオテキスト表現を学習し、柔軟かつ効率的な方法でさまざまなダウンストリームタスクをサポートする。さらに、提案されたバックボーン ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/806">Generative Pretraining in Multimodality, Quan Sun+, N_A, arXiv23</a>
<span class="snippet">Emuは、マルチモーダルなコンテキストで画像とテキストを生成するためのTransformerベースのモデルです。このモデルは、単一モダリティまたはマルチモーダルなデータ入力を受け入れることができます。Emuは、マルチモーダルなシーケンスでトレーニングされ、画像からテキストへのタスクやテキストから画 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CrossLingual.html">#CrossLingual</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/808">Empowering Cross-lingual Behavioral Testing of NLP Models with  Typological Features, Ester Hlavnova+, N_A, arXiv23</a>
<span class="snippet">M2Cという形態論に敏感なNLPモデルの行動テストフレームワークを提案し、12の異なる言語の特徴に基づいてモデルの振る舞いを探るテストを生成する。最先端の言語モデルは英語では優れているが、特定の言語の特徴に対する一般化の失敗があることが示される。これにより、モデルの盲点に対処するための開発が促され ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/810">Can Large Language Models Be an Alternative to Human Evaluations?, Cheng-Han Chiang+, N_A, arXiv23</a>
<span class="snippet">本研究では、機械学習モデルや人間による評価の代替手段として、大規模言語モデル（LLMs）を使用してテキストの品質を評価する方法を探求しました。LLMsに同じ指示と評価対象を与え、それに対する応答を生成させることで、LLM評価を行いました。実験の結果、LLM評価の結果は人間の評価と一致し、異なるフォ ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/866">WeCheck: Strong Factual Consistency Checker via Weakly Supervised Learning, ACL23</a>
<span class="snippet">現在のテキスト生成モデルは、入力と矛盾するテキストを制御できないという課題があります。この問題を解決するために、私たちはWeCheckという弱教師付きフレームワークを提案します。WeCheckは、弱教師付きラベルを持つ言語モデルから直接訓練された実際の生成サンプルを使用します。さまざまなタスクでの ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Programming.html">#Programming</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/868">Socratic Questioning of Novice Debuggers: A Benchmark Dataset and Preliminary Evaluations, ACL-BEA23</a>
<span class="snippet">本研究では、初心者プログラマがバグのある計算問題を解決する際に、ソクラテス的な対話を行うデータセットを紹介し、GPTベースの言語モデルのデバッグ能力を評価しました。GPT-4はGPT-3.5よりも優れたパフォーマンスを示しましたが、まだ人間の専門家には及ばず、さらなる研究が必要です。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/872">SciBench: Evaluating College-Level Scientific Problem-Solving Abilities  of Large Language Models, Xiaoxuan Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）の進歩により、数学のベンチマークでの性能向上が示されているが、これらのベンチマークは限定的な範囲の問題に限定されていることが指摘される。そこで、複雑な科学的問題解決に必要な推論能力を検証するための包括的なベンチマークスイートSciBenchを提案する。Sci ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/873">FLASK: Fine-grained Language Model Evaluation based on Alignment Skill  Sets, Seonghyeon Ye+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）の評価における課題を解決するため、細かい評価プロトコルであるFLASKを提案する。FLASKは、インスタンスごとのスキルセットレベルでの評価を可能にし、モデルベースと人間ベースの評価の両方に使用できる。具体的には、12の細かいスキルを定義し、各インスタンスに ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/d9871133-3111-4da6-9148-1ac779a24312" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Spoken Language Processing.html">#Spoken Language Processing</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/AudioProcessing.html">#AudioProcessing</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/875">Meta-Transformer: A Unified Framework for Multimodal Learning, Yiyuan Zhang+, N_A, arXiv23</a>
<span class="snippet">本研究では、マルチモーダル学習のためのMeta-Transformerというフレームワークを提案しています。このフレームワークは、異なるモダリティの情報を処理し関連付けるための統一されたネットワークを構築することを目指しています。Meta-Transformerは、対応のないデータを使用して12の ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/8734073a-573e-442e-8b9f-fed559199d56" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/877">Instruction-following Evaluation through Verbalizer Manipulation, Shiyang Li+, N_A, arXiv23</a>
<span class="snippet">本研究では、指示に従う能力を正確に評価するための新しい評価プロトコル「verbalizer manipulation」を提案しています。このプロトコルでは、モデルに異なる程度で一致する言葉を使用してタスクラベルを表現させ、モデルの事前知識に依存する能力を検証します。さまざまなモデルを9つのデータセ ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/DiffusionModel.html">#DiffusionModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/878">FABRIC: Personalizing Diffusion Models with Iterative Feedback, Dimitri von Rütte+, N_A, arXiv23</a>
<span class="snippet">本研究では、拡散ベースのテキストから画像への変換モデルに人間のフィードバックを組み込む戦略を提案する。自己注意層を利用したトレーニングフリーなアプローチであるFABRICを提案し、さまざまな拡散モデルに適用可能であることを示す。また、包括的な評価方法を導入し、人間のフィードバックを統合した生成ビジ ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Quantization.html">#Quantization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/881">QLoRA: Efficient Finetuning of Quantized LLMs, Tim Dettmers+, N_A, arXiv23</a>
<span class="snippet">私たちは、QLoRAという効率的なファインチューニング手法を提案します。この手法は、メモリ使用量を削減し、48GBの単一のGPU上で65Bパラメータモデルをファインチューニングすることができます。また、16ビットのファインチューニングタスクのパフォーマンスを維持します。QLoRAは、凍結された4ビ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Annotation.html">#Annotation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/882">LLMs as Workers in Human-Computational Algorithms? Replicating  Crowdsourcing Pipelines with LLMs, Tongshuang Wu+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）は、クラウドソーシングタスクにおいて人間のような振る舞いを再現できる可能性がある。しかし、現在の取り組みは単純なタスクに焦点を当てており、より複雑なパイプラインを再現できるかどうかは不明である。LLMsの成功は、リクエスターの理解力やサブタスクのスキルに影響を受ける。人 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/883">Towards A Unified Agent with Foundation Models, Norman Di Palo+, N_A, arXiv23</a>
<span class="snippet">本研究では、言語モデルとビジョン言語モデルを強化学習エージェントに組み込み、効率的な探索や経験データの再利用などの課題に取り組む方法を調査しました。スパースな報酬のロボット操作環境でのテストにおいて、ベースラインに比べて大幅な性能向上を実証し、学習済みのスキルを新しいタスクの解決や人間の専門家のビ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/aa40d0e3-9499-4804-9046-a9ad795c2d52" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ChatGPT.html">#ChatGPT</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/887">How is ChatGPTs behavior changing over time?, Lingjiao Chen+, N_A, arXiv23</a>
<span class="snippet">GPT-3.5とGPT-4は、大規模言語モデル（LLM）のサービスであり、その性能と振る舞いは時間とともに変動することがわかった。例えば、GPT-4は素数の特定に優れていたが、後のバージョンでは低い正答率となった。また、GPT-3.5はGPT-4よりも優れた性能を示した。さらに、GPT-4とGPT ...</span>
<br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/898">Large Language Models as General Pattern Machines, Suvir Mirchandani+, N_A, arXiv23</a>
<span class="snippet">事前学習された大規模言語モデル（LLMs）は、複雑なトークンシーケンスを自己回帰的に補完する能力を持っていることが観察された。この能力は、ランダムなトークンからなるシーケンスでも一部保持されることがわかった。この研究では、この能力がロボティクスの問題にどのように適用されるかを調査し、具体的な応用例 ...</span>
<br><span class="issue_date">Issue Date: 2023-07-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/900">Batch Prompting: Efficient Inference with Large Language Model APIs, Zhoujun Cheng+, N_A, arXiv23</a>
<span class="snippet">Batch sizeが大きくなるに連れて性能が低下し、かつタスクの難易度が高いとパフォーマンスの低下が著しいことが報告されている。また、contextが長ければ長いほど、バッチサイズを大きくした際のパフォーマンスの低下が著しい。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/16aaed9b-da2b-4c38-86df-e223bdbec826" alt="image"><br><span class="issue_date">Issue Date: 2023-07-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/902">DoG is SGDs Best Friend: A Parameter-Free Dynamic Step Size Schedule, Maor Ivgi+, N_A, ICML23</a>
<span class="snippet">私たちは、チューニング不要の動的SGDステップサイズの式であるDoGを提案します。DoGは、初期点からの距離と勾配のノルムに基づいてステップサイズを計算し、学習率のパラメータを必要としません。理論的には、DoGの式は確率的凸最適化においてパラメータフリーの収束を保証します。実験的には、DoGのパフ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/903">Judging LLM-as-a-judge with MT-Bench and Chatbot Arena, Lianmin Zheng+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLM）を判定者として使用して、オープンエンドの質問に対する性能を評価する方法を提案する。LLMの制限や問題を軽減するための解決策を提案し、2つのベンチマークでLLMの判定者と人間の好みの一致を検証する。結果は、強力なLLM判定者が人間の好みとよく一致し、スケーラブルで説明可能な ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/20c7782d-8ffe-4328-8526-700e38df23b5" alt="image"><br><span class="issue_date">Issue Date: 2023-07-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/906">FacTool: Factuality Detection in Generative AI -- A Tool Augmented  Framework for Multi-Task and Multi-Domain Scenarios, I-Chun Chern+, N_A, arXiv23</a>
<span class="snippet">生成型の事前学習モデルによって生成されたテキストの事実の誤りを検出するためのフレームワークであるFacToolが提案された。知識ベースのQA、コード生成、数理推論、科学文献レビューの4つのタスクでの実験において、FacToolの有効性が示された。FacToolのコードはGitHubで公開されている ...</span>
<br><span class="issue_date">Issue Date: 2023-07-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/908">Symbolic Chain-of-Thought Distillation: Small Models Can Also Think  Step-by-Step, Liunian Harold Li+, N_A, arXiv23</a>
<span class="snippet">小さなモデルでも思考の連鎖プロンプティングの恩恵を受けることができることを示すために、Symbolic Chain-of-Thought Distillation（SCoTD）を導入しました。SCoTDは、大きな教師モデルからサンプリングされた合理化に基づいて、小さな学生モデルをトレーニングする方 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/911">LLM-Rec: Personalized Recommendation via Prompting Large Language Models, Hanjia Lyu+, N_A, arXiv23</a>
<span class="snippet">LLMsを用いたパーソナライズされたコンテンツ推薦のためのプロンプティング戦略を調査し、LLM-Recというアプローチを提案した。実験の結果、プロンプティング戦略によって生成されたLLMによる拡張入力テキストと元のコンテンツの説明を組み合わせることで、推薦の性能が向上することが示された。これは、多 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/913">Do Multilingual Language Models Think Better in English?, Julen Etxaniz+, N_A, arXiv23</a>
<span class="snippet">self-translateは、マルチリンガル言語モデルの少数ショット翻訳能力を活用する新しいアプローチであり、外部の翻訳システムの必要性を克服する。実験結果は、self-translateが直接推論を上回る性能を示し、非英語の言語でプロンプトされた場合にも有効であることを示している。コードはht ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/65a44946-c82b-4895-9ce9-c48792e09b3e" alt="image"><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/924">SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step  Reasoning, Ning Miao+, N_A, arXiv23</a>
<span class="snippet">最新の大規模言語モデル（LLMs）は、推論問題を解決するために有望な手法ですが、複雑な問題にはまだ苦戦しています。本研究では、LLMsが自身のエラーを認識する能力を持っているかどうかを探求し、ゼロショットの検証スキームを提案します。この検証スキームを使用して、異なる回答に対して重み付け投票を行い、 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/925">Tool Documentation Enables Zero-Shot Tool-Usage with Large Language  Models, Cheng-Yu Hsieh+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、ツールのドキュメンテーションを提供することで新しいツールを学習する方法を提案しています。デモンストレーションの取得が困難な場合や、バイアスのある使用方法を避けるために、ツールのドキュメンテーションを使用することが有効であることを実験的に示していま ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/AutoML.html">#AutoML</a><br><span class="issue_date">Issue Date: 2023-08-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/926">MLCopilot: Unleashing the Power of Large Language Models in Solving  Machine Learning Tasks, Lei Zhang+, N_A, arXiv23</a>
<span class="snippet">本研究では、機械学習タスクの自動化における人間の知識と機械知能のギャップを埋めるために、新しいフレームワークMLCopilotを提案する。このフレームワークは、最先端のLLMsを使用して新しいMLタスクのソリューションを開発し、既存のMLタスクの経験から学び、効果的に推論して有望な結果を提供するこ ...</span>
<br><span class="issue_date">Issue Date: 2023-08-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/931">Metacognitive Prompting Improves Understanding in Large Language Models, Yuqing Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、LLMsにメタ認知プロンプト（MP）を導入し、人間の内省的な推論プロセスを模倣することで、理解能力を向上させることを目指しています。実験結果は、MPを備えたPaLMが他のモデルに比べて優れたパフォーマンスを示しており、MPが既存のプロンプト手法を上回ることを示しています。この研究は、L ...</span>
<br><span class="issue_date">Issue Date: 2023-08-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/932">Shepherd: A Critic for Language Model Generation, Tianlu Wang+, N_A, arXiv23</a>
<span class="snippet">Shepherdは、言語モデルの改善に関心が高まっている中で、自身の出力を洗練させるための特別に調整された言語モデルです。Shepherdは、多様なエラーを特定し修正案を提供する能力を持ち、高品質なフィードバックデータセットを使用して開発されました。Shepherdは他の既存のモデルと比較して優れ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/933">ChatGPT as a Factual Inconsistency Evaluator for Text Summarization, Zheheng Luo+, N_A, arXiv23</a>
<span class="snippet">事前学習された言語モデルによるテキスト要約の性能向上が注目されているが、生成された要約が元の文書と矛盾することが問題となっている。この問題を解決するために、効果的な事実性評価メトリクスの開発が進められているが、計算複雑性や不確実性の制約があり、人間の判断との一致に限定されている。最近の研究では、大 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/934">Large Language Models are Diverse Role-Players for Summarization  Evaluation, Ning Wu+, N_A, arXiv23</a>
<span class="snippet">本研究では、テキスト要約の評価フレームワークを提案し、生成されたテキストと参照テキストを客観的および主観的な側面から比較することで包括的な評価を行います。具体的には、ロールプレイヤーのプロンプティングメカニズムを使用してテキストの評価をモデル化し、コンテキストベースのプロンプティングメカニズムを導 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/935">GPTScore: Evaluate as You Desire, Jinlan Fu+, N_A, arXiv23</a>
<span class="snippet">本研究では、生成型AIの評価における課題を解決するために、GPTScoreという評価フレームワークを提案しています。GPTScoreは、生成されたテキストを評価するために、生成型事前学習モデルの新たな能力を活用しています。19の事前学習モデルを探索し、4つのテキスト生成タスクと22の評価項目に対し ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/937">RISE: Leveraging Retrieval Techniques for Summarization Evaluation, David Uthus+, N_A, Findings of ACL23</a>
<span class="snippet">自動要約の評価は困難であり、従来のアプローチでは人間の評価には及ばない。そこで、私たちはRISEという新しいアプローチを提案する。RISEは情報検索の技術を活用し、ゴールドリファレンスの要約がなくても要約を評価することができる。RISEは特に評価用のリファレンス要約が利用できない新しいデータセット ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/95d6fc9e-cb05-4a40-9690-ac40e6042c3c" alt="image"><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/LM-based.html">#LM-based</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/967">DiscoScore: Evaluating Text Generation with BERT and Discourse Coherence, Wei Zhao+, N_A, EACL23</a>
<span class="snippet">本研究では、文章の一貫性を評価するための新しい指標であるDiscoScoreを紹介します。DiscoScoreはCentering理論に基づいており、BERTを使用して談話の一貫性をモデル化します。実験の結果、DiscoScoreは他の指標よりも人間の評価との相関が高く、システムレベルでの評価でも ...</span>
<br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1004">Epic-Sounds: A Large-scale Dataset of Actions That Sound, Huh+, arXiv23</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-08-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1005">Teach LLMs to Personalize -- An Approach inspired by Writing Education, Cheng Li+, N_A, arXiv23</a>
<span class="snippet">個別化されたテキスト生成において、大規模言語モデル（LLMs）を使用した一般的なアプローチを提案する。教育の執筆をベースに、多段階かつマルチタスクのフレームワークを開発し、検索、ランキング、要約、統合、生成のステージで構成される個別化されたテキスト生成へのアプローチを採用する。さらに、マルチタスク ...</span>
<br><span class="issue_date">Issue Date: 2023-08-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1008">Self-Alignment with Instruction Backtranslation, Xian Li+, N_A, arXiv23</a>
<span class="snippet">私たちは、高品質な指示に従う言語モデルを構築するためのスケーラブルな手法を提案します。この手法では、少量のシードデータとウェブコーパスを使用して言語モデルをファインチューニングし、指示のプロンプトを生成してトレーニング例を構築します。そして、高品質な例を選択してモデルを強化します。この手法を使用す ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/837e17cc-6df1-4ba5-ba61-9c4f72dede93" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1010">Consciousness in Artificial Intelligence: Insights from the Science of  Consciousness, Patrick Butlin+, N_A, arXiv23</a>
<span class="snippet">AIの意識についての厳密なアプローチを提案し、既存のAIシステムを神経科学的な意識理論に基づいて評価する。意識の指標的特性を導き出し、最近のAIシステムを評価することで、現在のAIシステムは意識的ではないが、意識的なAIシステムを構築するための障壁は存在しないことを示唆する。 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1011">LLM As DBA, Xuanhe Zhou+, N_A, arXiv23</a>
<span class="snippet">データベース管理者の役割は重要ですが、大量のデータベースを管理するのは難しいです。最近の大規模言語モデル（LLMs）は、データベース管理に役立つ可能性があります。この研究では、LLMベースのデータベース管理者「D-Bot」を提案します。D-Botはデータベースのメンテナンス経験を学習し、適切なアド ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/f7f447c7-5b75-4025-83b2-57dfee7bf819" alt="image"><br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1012">Graph of Thoughts: Solving Elaborate Problems with Large Language Models, Maciej Besta+, N_A, arXiv23</a>
<span class="snippet">私たちは、Graph of Thoughts（GoT）というフレームワークを紹介しました。これは、大規模言語モデル（LLMs）のプロンプティング能力を進化させるもので、任意のグラフとしてモデル化できることが特徴です。GoTは、思考の組み合わせやネットワーク全体の本質の抽出、思考の強化などを可能にし ...</span>
<br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1013">Decomposition Enhances Reasoning via Self-Evaluation Guided Decoding, Yuxi Xie+, N_A, arXiv23</a>
<span class="snippet">私たちは、大規模言語モデル（LLMs）を使用して、推論の品質と多様性を向上させるための効果的なプロンプティングアプローチを提案しました。自己評価によるガイド付き確率的ビームサーチを使用して、GSM8K、AQuA、およびStrategyQAのベンチマークで高い精度を達成しました。また、論理の失敗を特 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1015">Large Language Model Guided Tree-of-Thought, Jieyi Long, N_A, arXiv23</a>
<span class="snippet">この論文では、Tree-of-Thought（ToT）フレームワークを紹介し、自己回帰型の大規模言語モデル（LLM）の問題解決能力を向上させる新しいアプローチを提案しています。ToTは、人間の思考方法に触発された技術であり、複雑な推論タスクを解決するためにツリー状の思考プロセスを使用します。提案手 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1020">AgentBench: Evaluating LLMs as Agents, Xiao Liu+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）をエージェントとして評価するための多次元の進化するベンチマーク「AgentBench」を提案しています。AgentBenchは、8つの異なる環境でマルチターンのオープンエンドの生成設定を提供し、LLMの推論と意思決定能力を評価します。25のLLMsに対するテ ...</span>
<br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1023">Large Language Models Sensitivity to The Order of Options in  Multiple-Choice Questions, Pouya Pezeshkpour+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）の頑健性に焦点を当てています。LLMsは多肢選択問題において順序に敏感であり、オプションの配置によって性能に大きな差が生じることを示しました。さらに、オプションの配置に対するバイアスを増幅または軽減する方法を特定し、LLMsの予測を改善するアプローチを提案し ...</span>
<br><span class="issue_date">Issue Date: 2023-09-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1028">A Survey on Large Language Model based Autonomous Agents, Lei Wang+, N_A, arXiv23</a>
<span class="snippet">自律エージェントの研究は、以前は限られた知識を持つエージェントに焦点を当てていましたが、最近では大規模言語モデル（LLMs）を活用した研究が増えています。本論文では、LLMに基づく自律エージェントの研究を包括的に調査し、統一されたフレームワークを提案します。さらに、LLMに基づくAIエージェントの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/c921a960-02f7-44e6-8c24-bb578f599bbe" alt="image"><br><span class="issue_date">Issue Date: 2023-09-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1029">CausalLM is not optimal for in-context learning, Nan Ding+, N_A, arXiv23</a>
<span class="snippet">最近の研究では、トランスフォーマーベースのインコンテキスト学習において、プレフィックス言語モデル（prefixLM）が因果言語モデル（causalLM）よりも優れたパフォーマンスを示すことがわかっています。本研究では、理論的なアプローチを用いて、prefixLMとcausalLMの収束挙動を分析し ...</span>
<br><span class="issue_date">Issue Date: 2023-09-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1030">Algorithm of Thoughts: Enhancing Exploration of Ideas in Large Language  Models, Bilgehan Sel+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）の推論能力を向上させるために、新しい戦略「Algorithm of Thoughts」を提案している。この戦略では、LLMsをアルゴリズム的な推論経路に導き、わずか1つまたは数個のクエリでアイデアの探索を拡大する。この手法は、以前の単一クエリ手法を上回り、マルチクエリ戦 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1034">Large Language Models Are Human-Level Prompt Engineers, Yongchao Zhou+, ICLR23</a>
<span class="snippet">大規模言語モデル（LLMs）は、自然言語の指示に基づいて一般的な用途のコンピュータとして優れた能力を持っています。しかし、モデルのパフォーマンスは、使用されるプロンプトの品質に大きく依存します。この研究では、自動プロンプトエンジニア（APE）を提案し、LLMによって生成された指示候補のプールから最 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1035">Instruction Tuning for Large Language Models: A Survey, Shengyu Zhang+, N_A, arXiv23</a>
<span class="snippet">この論文では、instruction tuning（IT）という技術について調査しています。ITは、大規模言語モデル（LLMs）をさらにトレーニングするための方法であり、ユーザーの指示に従うことを目的としています。本研究では、ITの方法論やデータセットの構築、トレーニング方法などについて調査し、指 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1037">Large Language Models as Optimizers, Chengrun Yang+, N_A, arXiv23</a>
<span class="snippet">本研究では、最適化タスクを自然言語で記述し、大規模言語モデル（LLMs）を使用して最適化を行う手法「Optimization by PROmpting（OPRO）」を提案しています。この手法では、LLMが以前の解とその値を含むプロンプトから新しい解を生成し、評価して次の最適化ステップのためのプロン ...</span>
<br><span class="issue_date">Issue Date: 2023-09-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1038">Simple synthetic data reduces sycophancy in large language models, Jerry Wei+, N_A, arXiv23</a>
<span class="snippet">本研究では、機械学習モデルのおべっか行動を減らすための方法を提案しています。まず、言語モデルにおけるおべっか行動の普及度を調査し、その行動を減らすための合成データ介入を提案しています。具体的には、ユーザーの意見に対してモデルが頑健であることを促す合成データを使用し、モデルのファインチューニングを行 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/43c03357-5c5c-4ceb-a089-0ad0a35eea1d" alt="image"><br><span class="issue_date">Issue Date: 2023-09-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1039">Textbooks Are All You Need II: phi-1.5 technical report, Yuanzhi Li+, N_A, arXiv23</a>
<span class="snippet">私たちは、小さなTransformerベースの言語モデルであるTinyStoriesと、大規模な言語モデルであるphi-1の能力について調査しました。また、phi-1を使用して教科書の品質のデータを生成し、学習プロセスを改善する方法を提案しました。さらに、phi-1.5という新しいモデルを作成し、 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1040">DoLa: Decoding by Contrasting Layers Improves Factuality in Large  Language Models, Yung-Sung Chuang+, N_A, arXiv23</a>
<span class="snippet">我々は、事前学習済みの大規模言語モデル（LLMs）における幻覚を軽減するためのシンプルなデコーディング戦略を提案する。このアプローチは、ロジットの差異を対比することで次のトークンの分布を得るもので、事実知識をより明確に示し、誤った事実の生成を減らすことができる。このアプローチは、複数の選択課題やオ ...</span>
<br><span class="issue_date">Issue Date: 2023-09-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1041">From Sparse to Dense: GPT-4 Summarization with Chain of Density  Prompting, Griffin Adams+, N_A, arXiv23</a>
<span class="snippet">要約は詳細でエンティティ中心的でありながら、理解しやすくすることが困難です。この課題を解決するために、私たちは「密度の連鎖」（CoD）プロンプトを使用して、GPT-4の要約を生成します。CoDによって生成された要約は抽象的であり、リードバイアスが少なく、人間に好まれます。また、情報量と読みやすさの ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1044">Chain-of-Verification Reduces Hallucination in Large Language Models, Shehzaad Dhuliawala+, N_A, arXiv23</a>
<span class="snippet">私たちは、言語モデルが根拠のない情報を生成する問題に取り組んでいます。Chain-of-Verification（CoVe）メソッドを開発し、モデルが回答を作成し、検証し、最終的な回答を生成するプロセスを経ることで、幻想を減少させることができることを実験で示しました。 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1045">LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models, Yukang Chen+, N_A, arXiv23</a>
<span class="snippet">本研究では、計算コストを制限しながら大規模言語モデル（LLMs）のコンテキストサイズを拡張する効率的なファインチューニング手法であるLongLoRAを提案します。従来の方法では、LLMsの長いコンテキストサイズでのトレーニングには高い計算コストとGPUリソースが必要でしたが、提案手法ではコンテキス ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1046">Struc-Bench: Are Large Language Models Really Good at Generating Complex  Structured Data?, Xiangru Tang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）の能力を評価し、構造に注意したファインチューニング手法を提案します。さらに、Struc-Benchというデータセットを使用して、複雑な構造化データ生成のパフォーマンスを評価します。実験の結果、提案手法は他の評価されたLLMsよりも優れた性能を示しました。また ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1047">RAIN: Your Language Models Can Align Themselves without Finetuning, Yuhui Li+, N_A, arXiv23</a>
<span class="snippet">本研究では、追加のデータなしで凍結された大規模言語モデル（LLMs）を整列させる方法を探求しました。自己評価と巻き戻しメカニズムを統合することで、LLMsは自己ブースティングを通じて人間の好みと一致する応答を生成することができることを発見しました。RAINという新しい推論手法を導入し、追加のデータ ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1048">A Survey of Hallucination in Large Foundation Models, Vipula Rawte+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模ファウンデーションモデル（LFMs）におけるホールシネーションの問題に焦点を当て、その現象を分類し、評価基準を確立するとともに、既存の戦略を検討し、今後の研究の方向性についても議論しています。 ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1050">MAmmoTH: Building Math Generalist Models through Hybrid Instruction  Tuning, Xiang Yue+, N_A, arXiv23</a>
<span class="snippet">MAmmoTHは、数学の問題解決に特化した大規模言語モデルであり、厳密にキュレーションされた教育データセットで訓練されています。このモデルは、CoTとPoTのハイブリッドな根拠を提供し、さまざまな数学の分野を包括的にカバーしています。MAmmoTHは、既存のオープンソースモデルを大幅に上回り、特に ...</span>
<br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1051">Explaining grokking through circuit efficiency, Vikrant Varma+, N_A, arXiv23</a>
<span class="snippet">グロッキングとは、完璧なトレーニング精度を持つネットワークでも一般化が悪い現象のことである。この現象は、タスクが一般化する解と記憶する解の両方を許容する場合に起こると考えられている。一般化する解は学習が遅く、効率的であり、同じパラメータノルムでより大きなロジットを生成する。一方、記憶回路はトレーニ ...</span>
<br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1060">Effective Long-Context Scaling of Foundation Models, Wenhan Xiong+, N_A, arXiv23</a>
<span class="snippet">私たちは、長いコンテキストをサポートする一連のLLMsを提案します。これらのモデルは、長いテキストを含むデータセットでトレーニングされ、言語モデリングや他のタスクで評価されます。提案手法は、通常のタスクと長いコンテキストのタスクの両方で改善をもたらします。また、70Bバリアントはgpt-3.5-t ...</span>
<a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1061">Graph Neural Prompting with Large Language Models, Yijun Tian+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を知識グラフと組み合わせるための新しい手法であるGraph Neural Prompting（GNP）を提案しています。GNPは、標準的なグラフニューラルネットワークエンコーダやクロスモダリティプーリングモジュールなどの要素から構成されており、異なるLLMの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/434daf26-f82f-43b9-8807-13517975383b" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1062">Boolformer: Symbolic Regression of Logic Functions with Transformers, Stéphane dAscoli+, N_A, arXiv23</a>
<span class="snippet">この研究では、BoolformerというTransformerアーキテクチャを使用して、ブール関数のシンボリック回帰を実行する方法を紹介します。Boolformerは、クリーンな真理値表やノイズのある観測など、さまざまなデータに対して効果的な式を予測することができます。さらに、実世界のデータセット ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1063">Large Language Model Alignment: A Survey, Tianhao Shen+, N_A, arXiv23</a>
<span class="snippet">近年、大規模言語モデル（LLMs）の進歩が注目されていますが、その潜在能力と同時に懸念もあります。本研究では、LLMsのアライメントに関する既存の研究と新たな提案を包括的に探求し、モデルの解釈可能性や敵対的攻撃への脆弱性などの問題も議論します。さらに、LLMsのアライメントを評価するためのベンチマ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/09c10110-798f-4493-b431-41c2f2b017c1" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1065">Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models  through Logic, Xufeng Zhao+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルの進歩は驚異的だが、多段階の推論には改善の余地がある。大規模言語モデルは知識を持っているが、推論には一貫性がなく、幻覚を示すことがある。そこで、Logical Chain-of-Thought（LogiCoT）というフレームワークを提案し、論理による推論パラダイムの効果を示した。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1066">Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution, Chrisantha Fernando+, N_A, arXiv23</a>
<span class="snippet">本研究では、Promptbreederという自己参照的な自己改善メカニズムを提案し、大規模言語モデル（LLM）の推論能力を向上させるための汎用的なプロンプト戦略を進化させる方法を示しています。Promptbreederは、LLMが自己参照的な方法で進化する変異プロンプトによって制御され、タスクプロ ...</span>
<br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1067">Benchmarking Large Language Models As AI Research Agents, Qian Huang+, N_A, arXiv23</a>
<span class="snippet">本研究では、AI研究エージェントを構築し、科学的な実験のタスクを実行するためのベンチマークとしてMLAgentBenchを提案する。エージェントはファイルの読み書きやコードの実行などのアクションを実行し、実験を実行し、結果を分析し、機械学習パイプラインのコードを変更することができる。GPT-4ベー ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1068">Improved Baselines with Visual Instruction Tuning, Haotian Liu+, N_A, arXiv23</a>
<span class="snippet">LLaVAは、ビジョンと言語のクロスモーダルコネクタであり、データ効率が高く強力な性能を持つことが示されています。CLIP-ViT-L-336pxを使用し、学術タスク指向のVQAデータを追加することで、11のベンチマークで最先端のベースラインを確立しました。13Bのチェックポイントはわずか120万 ...</span>
<br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1069">RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities  of Large Language Models, Zekun Moore Wang+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して役割演技の能力を向上させるためのフレームワークであるRoleLLMを提案しています。RoleLLMは、役割プロファイルの構築、コンテキストベースの指示生成、役割プロンプトによる話し方の模倣、オープンソースモデルの微調整と役割のカスタマイズの4つのス ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/RetrievalAugmentation.html">#RetrievalAugmentation</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1070">Retrieval meets Long Context Large Language Models, Peng Xu+, N_A, arXiv23</a>
<span class="snippet">最先端の事前学習済みLLMsを使用して、リトリーバル拡張と長いコンテキストウィンドウの組み合わせについて研究しました。結果として、リトリーバル拡張LLMsは、ファインチューニングLLMsと比較しても高いパフォーマンスを示し、計算量も少ないことがわかりました。さらに、リトリーバルはLLMsのパフォー ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1072">Think before you speak: Training Language Models With Pause Tokens, Sachin Goyal+, N_A, arXiv23</a>
<span class="snippet">言語モデルのトレーニングと推論において、遅延を導入することでモデルの性能を向上させる手法を提案しました。具体的には、入力に特定のトークンを追加し、そのトークンが現れるまでモデルの出力を遅らせることで、追加の計算を行うことができます。実験結果では、この手法が推論タスクにおいて有益であり、特にQAタス ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/RetrievalAugmentation.html">#RetrievalAugmentation</a><br><span class="issue_date">Issue Date: 2023-10-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1074">RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective  Augmentation, Fangyuan Xu+, N_A, arXiv23</a>
<span class="snippet">ドキュメントの要約を生成することで、言語モデルの性能を向上させる手法を提案する。抽出型の圧縮器と抽象型の圧縮器を使用し、LMsの入力に要約を追加して訓練する。実験結果では、圧縮率が6％まで達成され、市販の要約モデルを上回る性能を示した。また、訓練された圧縮器は他のLMsにも転移可能であることが示さ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2756ba98-d228-45e6-972d-ef239d4b990e" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-10-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1075">Why Do We Need Weight Decay in Modern Deep Learning?, Maksym Andriushchenko+, N_A, arXiv23</a>
<span class="snippet">ウェイト減衰は、大規模な言語モデルのトレーニングに使用されるが、その役割はまだ理解されていない。本研究では、ウェイト減衰が古典的な正則化とは異なる役割を果たしていることを明らかにし、過パラメータ化されたディープネットワークでの最適化ダイナミクスの変化やSGDの暗黙の正則化の強化方法を示す。また、ウ ...</span>
<br><span class="issue_date">Issue Date: 2023-10-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1076">Take a Step Back: Evoking Reasoning via Abstraction in Large Language  Models, Huaixiu Steven Zheng+, N_A, arXiv23</a>
<span class="snippet">Step-Back Promptingは、大規模言語モデル（LLMs）を使用して推論の手順をガイドするシンプルなプロンプティング技術です。この技術により、LLMsは具体的な詳細から高レベルの概念や基本原則を抽象化し、正しい推論経路をたどる能力を向上させることができます。実験により、Step-Bac ...</span>
<br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1078">Meta-CoT: Generalizable Chain-of-Thought Prompting in Mixed-task  Scenarios with Large Language Models, Anni Zou+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、推論のためのチェーン・オブ・ソート（CoT）プロンプトを生成する方法を提案しています。従来のCoTの方法では、一般的なプロンプトや手作業デモンストレーションに依存していましたが、本研究では入力質問のタイプに基づいて自動的にプロンプトを生成するMe ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-10-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1085">Eliminating Reasoning via Inferring with Planning: A New Framework to  Guide LLMs Non-linear Thinking, Yongqi Tong+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）に非線形の思考を促すために、新しいプロンプティング方法であるInferential Exclusion Prompting（IEP）を提案する。IEPは、計画を立てて可能な解を推論し、逆推論を行うことで広い視点を得ることができる。IEPは他の手法と比較して複 ...</span>
<br><span class="issue_date">Issue Date: 2023-10-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1086">Personalized Soups: Personalized Large Language Model Alignment via  Post-hoc Parameter Merging, Joel Jang+, N_A, arXiv23</a>
<span class="snippet">Reinforcement Learning from Human Feedback (RLHF) is not optimal for learning diverse individual perspectives, as it aligns general aggregated human ...</span>
<br><span class="issue_date">Issue Date: 2022-08-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/463">GRAM: Fast Fine-tuning of Pre-trained Language Models for Content-based Collaborative Filtering, Yang+, RiiiD, NAACL22</a>
<span class="snippet">RiiiDがNAACL'22に論文通してた ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/464">Knowledge Tracing: A Survey, ABDELRAHMAN+, Australian National University, arXiv22</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/465">Interpretable Knowledge Tracing: Simple and Efficient Student Modeling with Causal Relations, Minn+, AAAI22</a>
<span class="snippet">DeepLearningを用いずに解釈性の高いKTモデルを提案。DKT, DKVMN, AKT等をoutperformしている。 ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/467">No Task Left Behind: Multi-Task Learning of Knowledge Tracing and Option Tracing for Better Student Assessment, An+, RiiiD, AAAI22</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/496">Sketch-Guided Text-to-Image Diffusion Models, Andrey+, Google Research, arXiv22</a>
<span class="snippet">スケッチとpromptを入力することで、スケッチ biasedな画像を生成することができる技術。すごい。![image](https://user-images.githubusercontent.com/12249301/205189823-66052368-60a8-4f03-a4b6-37 ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/500">Revisiting Pretraining Objectives for Tabular Deep Learning, Rubachev+, Yandex+, arXiv22</a>
<span class="snippet">Tabular Dataを利用した場合にKaggleなどでDeepなモデルがGBDT等に勝てないことが知られているが、GBDT等とcomparable になる性能になるようなpre-trainingを提案したよ、的な内容っぽい ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2022-12-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/501">UNIFIEDSKG: Unifying and Multi-Tasking Structured Knowledge Grounding with Text-to-Text Language Models, Xie+, EMNLP22</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/601">Efficiently Scaling Transformer Inference, Reiner Pope+, N_A, arXiv22</a>
<span class="snippet">大規模Transformerベースのモデルの推論のエンジニアリングのトレードオフを理解するために、最適な多次元分割技術を選択するための単純な解析モデルを開発低レベルの最適化と組み合わせることで、500B+パラメータモデルのレイテンシーとモデルFLOPS利用率のトレードオフにおいて、Fast ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/615">Frustratingly Easy Label Projection for Cross-lingual Transfer, Yang Chen+, N_A, arXiv22</a>
<span class="snippet">多言語のトレーニングデータの翻訳は、クロスリンガル転移の改善に役立つスパンレベル注釈が必要なタスクでは、注釈付きスパンを翻訳されたテキストにマッピングするために追加のラベルプロジェクションステップが必要マーク-翻訳法を利用するアプローチが従来の注釈プロジェクションと比較してどのようにな ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/642">Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them, Mirac Suzgun+, N_A, arXiv22</a>
<span class="snippet">BIG-Bench Hard (BBH) is a suite of 23 challenging tasks that current language models have not been able to surpass human performance on. This study f ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/643">Mass-Editing Memory in a Transformer, Kevin Meng+, N_A, arXiv22</a>
<span class="snippet">大規模言語モデルを更新することで、専門的な知識を追加できることが示されているしかし、これまでの研究は主に単一の関連付けの更新に限定されていた本研究では、MEMITという方法を開発し、多数のメモリを直接言語モデルに更新することができることを実験的に示したGPT-J（6B）およびGPT ...</span>
<br><span class="issue_date">Issue Date: 2023-05-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/674">Out of One, Many: Using Language Models to Simulate Human Samples, Lisa P. Argyle+, N_A, arXiv22</a>
<span class="snippet">本研究では、言語モデルが社会科学研究において特定の人間のサブポピュレーションの代理として研究される可能性があることを提案し、GPT-3言語モデルの「アルゴリズム的忠実度」を探求する。アルゴリズム的忠実度が十分である言語モデルは、人間や社会の理解を進めるための新しい強力なツールとなる可能性があると提 ...</span>
<br><span class="issue_date">Issue Date: 2023-05-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/681">Fine-Tuning can Distort Pretrained Features and Underperform  Out-of-Distribution, Ananya Kumar+, N_A, arXiv22</a>
<span class="snippet">事前学習済みモデルをダウンストリームタスクに転移する際、ファインチューニングと線形プロービングの2つの方法があるが、本研究では、分布のシフトが大きい場合、ファインチューニングが線形プロービングよりも分布外で精度が低くなることを発見した。LP-FTという2段階戦略の線形プロービング後の全体のファイン ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/059d9056-bd3c-45f2-abd9-00c9f2a3d630" alt="image"><br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/785">Beyond the Imitation Game: Quantifying and extrapolating the  capabilities of language models, Aarohi Srivastava+, N_A, arXiv22</a>
<span class="snippet">言語モデルの能力と制約を理解するために、BIG-benchという新しいベンチマークを導入しました。このベンチマークでは、現在の言語モデルの能力を超えるタスクに焦点を当てています。さまざまなトピックの204のタスクが含まれており、モデルのサイズや性能の比較も行いました。結果として、モデルの性能とキャ ...</span>
<br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/786">Holistic Evaluation of Language Models, Percy Liang+, N_A, arXiv22</a>
<span class="snippet">言語モデルの透明性を向上させるために、Holistic Evaluation of Language Models（HELM）を提案する。HELMでは、潜在的なシナリオとメトリックを分類し、広範なサブセットを選択して評価する。さらに、複数のメトリックを使用し、主要なシナリオごとに評価を行う。30の ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/861">An Extensible Plug-and-Play Method for Multi-Aspect Controllable Text  Generation, Xuancheng Huang+, N_A, arXiv22</a>
<span class="snippet">本研究では、テキスト生成において複数の側面を制御する方法について研究しました。従来の方法では、プレフィックスの相互干渉により制約が低下し、未知の側面の組み合わせを制御することが制限されていました。そこで、トレーニング可能なゲートを使用してプレフィックスの介入を正規化し、相互干渉の増加を抑制する方法 ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Self-SupervisedLearning.html">#Self-SupervisedLearning</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/874">RankMe: Assessing the downstream performance of pretrained  self-supervised representations by their rank, Quentin Garrido+, N_A, arXiv22</a>
<span class="snippet">共有埋め込み自己教示学習（JE-SSL）は、成功の視覚的な手がかりが欠如しているため、展開が困難である。本研究では、JE-SSL表現の品質を評価するための非教示基準であるRankMeを開発した。RankMeはラベルを必要とせず、ハイパーパラメータの調整も不要である。徹底的な実験により、RankMe ...</span>
<br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/895">Will Large-scale Generative Models Corrupt Future Datasets?, Ryuichiro Hataya+, N_A, arXiv22</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-08-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/912">Explaining Patterns in Data with Language Models via Interpretable  Autoprompting, Chandan Singh+, N_A, arXiv22</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用してデータのパターンを説明する能力を探求しました。具体的には、事前学習済みのLLMを使用してデータを説明する自然言語の文字列を生成するアルゴリズムを導入しました。実験結果は、このアルゴリズムが正確なデータセットの説明を見つけ出すことができることを示して ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-08-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/927">Personalized Chit-Chat Generation for Recommendation Using External Chat Corpora, Chen+, KDD22</a>
<span class="snippet">チットチャットは、ユーザーとの対話において効果的であることが示されています。この研究では、ニュース推薦のための個人化されたチットチャットを生成する方法を提案しています。既存の方法とは異なり、外部のチャットコーパスのみを使用してユーザーの関心を推定し、個人化されたチットチャットを生成します。幅広い実 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/PersonalizedHeadlineGeneration.html">#PersonalizedHeadlineGeneration</a><br><span class="issue_date">Issue Date: 2023-08-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/928">Personalized Headline Generation with Enhanced User Interest Perception, Zhang+, ICANN22</a>
<span class="snippet">ユーザーのニュース閲覧履歴をモデル化し、個別化されたニュース見出しを生成するための新しいフレームワークを提案する。提案手法は、ユーザーの興味を強調するために候補テキストに関連する情報を活用し、ニュースのエンティティワードを使用して興味表現を改善する。幅広い実験により、提案手法が見出し生成タスクで優 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/PersonalizedHeadlineGeneration.html">#PersonalizedHeadlineGeneration</a><br><span class="issue_date">Issue Date: 2023-08-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/929">Personalized News Headline Generation System with Fine-grained User Modeling, Yao, MSN22</a>
<span class="snippet">ユーザーの興味に基づいてパーソナライズされたニュースの見出しを生成するために、文レベルの情報を考慮したユーザーモデルを提案する。アテンション層を使用して文とニュースの関連性を計算し、ニュースの内容に基づいて見出しを生成する。実験結果は、提案モデルがベースラインモデルよりも優れたパフォーマンスを示し ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/936">DocAsRef: A Pilot Empirical Study on Repurposing Reference-Based Summary  Quality Metrics Reference-Freely, Forrest Sheng Bao+, N_A, arXiv22</a>
<span class="snippet">参照ベースと参照フリーの要約評価メトリックがあります。参照ベースは正確ですが、制約があります。参照フリーは独立していますが、ゼロショットと正確さの両方を満たせません。本研究では、参照ベースのメトリックを使用してゼロショットかつ正確な参照フリーのアプローチを提案します。実験結果は、このアプローチが最 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/938">Universal Evasion Attacks on Summarization Scoring, Wenchuan Mu+, N_A, BlackboxNLP workshop on ACL22</a>
<span class="snippet">要約の自動評価は重要であり、その評価は複雑です。しかし、これまで要約の評価は機械学習のタスクとは考えられていませんでした。本研究では、自動評価の堅牢性を探るために回避攻撃を行いました。攻撃システムは、要約ではない文字列を予測し、一般的な評価指標であるROUGEやMETEORにおいて優れた要約器と競 ...</span>
<br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/939">Self-Repetition in Abstractive Neural Summarizers, Nikita Salkar+, N_A,  Assoc Comput Linguist Meet22</a>
<span class="snippet">私たちは、BART、T5、およびPegasusという3つのニューラルモデルの出力における自己繰り返しの分析を行いました。これらのモデルは、異なるデータセットでfine-tuningされています。回帰分析によると、これらのモデルは入力の出力要約間でコンテンツを繰り返す傾向が異なることがわかりました。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/940">How to Find Strong Summary Coherence Measures? A Toolbox and a Comparative Study for Summary Coherence Measure Evaluation, Steen+, COLING22</a>
<span class="snippet">要約の一貫性を自動的に評価することは重要であり、さまざまな方法が提案されていますが、異なるデータセットと評価指標を使用して評価されるため、相対的なパフォーマンスを理解することが困難です。本研究では、要約の一貫性モデリングのさまざまな方法について調査し、新しい分析尺度を導入します。現在の自動一貫性尺 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/972">WIDAR -- Weighted Input Document Augmented ROUGE, Raghav Jain+, N_A, ECIR22</a>
<span class="snippet">自動テキスト要約の評価において、ROUGEメトリックには制約があり、参照要約の利用可能性に依存している。そこで、本研究ではWIDARメトリックを提案し、参照要約だけでなく入力ドキュメントも使用して要約の品質を評価する。WIDARメトリックは一貫性、整合性、流暢さ、関連性の向上をROUGEと比較して ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/973">InfoLM: A New Metric to Evaluate Summarization & Data2Text Generation, Pierre Colombo+, N_A, AAAI22</a>
<span class="snippet">自然言語生成システムの品質評価は高価であり、人間の注釈に頼ることが一般的です。しかし、自動評価指標を使用することもあります。本研究では、マスクされた言語モデルを使用した評価指標であるInfoLMを紹介します。この指標は同義語を処理することができ、要約やデータ生成の設定で有意な改善を示しました。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/983">FFCI: A Framework for Interpretable Automatic Evaluation of  Summarization, Fajri Koto+, N_A, JAIR22</a>
<span class="snippet">本論文では、FFCIという細かい要約評価のためのフレームワークを提案しました。このフレームワークは、信頼性、焦点、カバレッジ、および文間の連続性の4つの要素から構成されています。新しいデータセットを構築し、評価メトリックとモデルベースの評価方法をクロス比較することで、FFCIの4つの次元を評価する ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-08-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/987">SMART: Sentences as Basic Units for Text Evaluation, Reinald Kim Amplayo+, N_A, arXiv22</a>
<span class="snippet">本研究では、テキスト生成の評価指標の制限を緩和するために、新しい指標であるSMARTを提案する。SMARTは文を基本的なマッチング単位とし、文のマッチング関数を使用して候補文と参照文を評価する。また、ソースドキュメントの文とも比較し、評価を可能にする。実験結果は、SMARTが他の指標を上回ることを ...</span>
<br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/997">BRIO: Bringing Order to Abstractive Summarization, Yixin Liu+, N_A, arXiv22</a>
<span class="snippet">従来の抽象的要約モデルでは、最尤推定を使用して訓練されていましたが、この方法では複数の候補要約を比較する際に性能が低下する可能性があります。そこで、非確定論的な分布を仮定し、候補要約の品質に応じて確率を割り当てる新しい訓練パラダイムを提案しました。この手法により、CNN/DailyMailとXSu ...</span>
<a class="button" href="articles/BeamSearch.html">#BeamSearch</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/998">Momentum Calibration for Text Generation, Xingxing Zhang+, N_A, arXiv22</a>
<span class="snippet">本研究では、テキスト生成タスクにおいてMoCa（Momentum Calibration）という手法を提案しています。MoCaは、ビームサーチを用いた遅く進化するサンプルを動的に生成し、これらのサンプルのモデルスコアを実際の品質に合わせるように学習します。実験結果は、MoCaが強力な事前学習済みT ...</span>
<br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/999">Crosslingual Generalization through Multitask Finetuning, Niklas Muennighoff+, N_A, arXiv22</a>
<span class="snippet">マルチタスクプロンプトフィネチューニング（MTF）は、大規模な言語モデルが新しいタスクに汎化するのに役立つことが示されています。この研究では、マルチリンガルBLOOMとmT5モデルを使用してMTFを実施し、英語のプロンプトを使用して英語および非英語のタスクにフィネチューニングすることで、タスクの汎 ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1000">Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than  In-Context Learning, Haokun Liu+, N_A, arXiv22</a>
<span class="snippet">Few-shot in-context learning（ICL）とパラメータ効率の良いファインチューニング（PEFT）を比較し、PEFTが高い精度と低い計算コストを提供することを示す。また、新しいPEFTメソッドである（IA）^3を紹介し、わずかな新しいパラメータしか導入しないまま、強力なパフォ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/379">Improving Neural Machine Translation with Compact Word Embedding Tables, Kumar+, 2021</a>
<span class="snippet">NMTにおいてword embeddingがどう影響しているかなどを調査しているらしい ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2021-06-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/389">Pre-Trained Models: Past, Present and Future, Han+, arXiv‘21</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2021-06-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/391">Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better, Menghani, arXiv‘21</a>
<span class="snippet">学習効率化、高速化などのテクニックがまとまっているらしい ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><br><span class="issue_date">Issue Date: 2021-08-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/403">RLTutor: Reinforcement Learning Based Adaptive Tutoring System by Modeling Virtual Student with Fewer Interactions, Kubotani+, Waseda University, IJCAI21</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><br><span class="issue_date">Issue Date: 2021-10-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/409">過去情報の内容選択を取り入れた スポーツダイジェストの自動生成, 加藤+, 東工大, NLP21</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/454">BEKT: Deep Knowledge Tracing with Bidirectional Encoder Representations from Transformers, Tian+ （緒方先生）, Kyoto University, ICCE21</a>
<span class="snippet">KTにBERTを利用した研究#453 などでDeepLearningBasedなモデル間であまり差がないことが示されているので、本研究が実際どれだけ強いのかは気になるところ。 ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/OptionTracing.html">#OptionTracing</a><br><span class="issue_date">Issue Date: 2022-08-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/471">Option Tracing: Beyond Correctness Analysis in Knowledge Tracing, Ghosh+, AIED21</a>
<span class="snippet">これまでのKTは問題の正誤（correctness）に対してfittingしていたが、この研究ではmultiple choice questionでどの選択肢を選択するかを予測するタスクを提案している。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/477">Behavioral Testing of Deep Neural Network Knowledge Tracing Models, Kim+, Riiid, EDM21</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/ScorePrediction.html">#ScorePrediction</a><br><span class="issue_date">Issue Date: 2022-08-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/478">Condensed Discriminative Question Set for Reliable Exam Score Prediction, Jung+, Riiid, AIED21</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/599">Personalized Extractive Summarization for a News Dialogue System, Takatsu+, SLT, 2021, 4</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/625">Sequence Parallelism: Long Sequence Training from System Perspective, Shenggui Li+, N_A, arXiv21</a>
<span class="snippet">本研究では、Transformerの自己注意機構がシーケンスの長さに対して二次のメモリ要件を持つ問題を解決するため、シーケンス並列処理というメモリ効率の高い並列処理方法を提案しました。このアプローチは、既存の並列処理と互換性があり、疎な注意機構を使用することで無限に長いシーケンスでTransfor ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/review.html">#review</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/655">Transformer Reasoning Network for Personalized Review Summarization, Xu+, SIGIR21</a>
<span class="snippet">先行研究は、review summarizationにおいて生成されるsummaryは、過去にユーザが作成したsummaryのwriting styleやproductに非常に関係しているのに、これらを活用してこなかったので、活用しました（=personalized）という話っぽい ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MultitaskLearning.html">#MultitaskLearning</a><br><span class="issue_date">Issue Date: 2023-07-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/904">Measuring Massive Multitask Language Understanding, Dan Hendrycks+, N_A, ICLR21</a>
<span class="snippet">私たちは、マルチタスクのテキストモデルの正確性を測定するための新しいテストを提案しています。このテストは、57のタスクをカバーし、広範な世界知識と問題解決能力を必要とします。現在のモデルはまだ専門家レベルの正確性に達しておらず、性能に偏りがあります。私たちのテストは、モデルの理解の幅と深さを評価し ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ContrastiveLearning.html">#ContrastiveLearning</a><br><span class="issue_date">Issue Date: 2023-07-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/907">SimCSE: Simple Contrastive Learning of Sentence Embeddings, Tianyu Gao+, N_A, EMNLP21</a>
<span class="snippet">この論文では、SimCSEという対比学習フレームワークを提案しています。このフレームワークは、文の埋め込み技術を進化させることができます。教師なしアプローチでは、入力文をノイズとして扱い、自己を対比的に予測します。教師ありアプローチでは、自然言語推論データセットから注釈付きのペアを使用して対比学習 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/ba20a1ca-0078-4227-8bb3-3805ee57a620" alt="image"><br><span class="issue_date">Issue Date: 2023-08-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1009">ViLT: Vision-and-Language Transformer Without Convolution or Region  Supervision, Wonjae Kim+, N_A, arXiv21</a>
<span class="snippet">VLP（Vision-and-Language Pre-training）のアプローチは、ビジョンと言語のタスクでのパフォーマンスを向上させているが、現在の方法は効率性と表現力の面で問題がある。そこで、本研究では畳み込みフリーのビジョンと言語のトランスフォーマ（ViLT）モデルを提案する。ViLT ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2020-08-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/337">Evaluation of Text Generation: A Survey, Celikyilmaz, Clark, Gao, arXiv20</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/381">All Word Embeddings from One Embedding, Takase+, NeurIPS20</a>
<span class="snippet">Embedidngのパラメータ数とBLEUスコアの比較。より少ないパラメータ数でcomparableな性能を達成している。![image](https://user-images.githubusercontent.com/12249301/121308824-700c3100-c93c-1 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/446">Context-Aware Attentive Knowledge Tracing, Ghosh+, University of Massachusetts Amherst, KDD20</a>
<span class="snippet">この論文の実験ではSAKTがDKVMNやDKTに勝てていない ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/468">Deep Knowledge Tracing with Transformers, Shi+ （w_ Michael Yudelson）, ETS_ACT, AIED20</a>
<span class="snippet">TransformerでKTした研究。あまり引用されていない。SAINT, SAINT+と同時期に発表されている。 ...</span>
<a class="button" href="articles/Education.html">#Education</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><br><span class="issue_date">Issue Date: 2022-12-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/503">Reinforcement Learning for the Adaptive Scheduling of Educational Activities, Bassen+, Stanford University, CHI20</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/review.html">#review</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/656">A Unified Dual-view Model for Review Summarization and Sentiment  Classification with Inconsistency Loss, Hou Pong Chan+, N_A, arXiv20</a>
<span class="snippet">ユーザーレビューから要約と感情を取得するために、新しいデュアルビューモデルを提案。エンコーダーがレビューの文脈表現を学習し、サマリーデコーダーが要約を生成。ソースビュー感情分類器はレビューの感情ラベルを予測し、サマリービュー感情分類器は要約の感情ラベルを予測。不一致損失を導入して、2つの分類器の不 ...</span>
<br><span class="issue_date">Issue Date: 2023-07-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/901">Measuring Massive Multitask Language Understanding, Dan Hendrycks+, N_A, arXiv20</a>
<span class="snippet">私たちは、マルチタスクのテキストモデルの正確性を測定するための新しいテストを提案しています。このテストは57のタスクをカバーし、広範な世界知識と問題解決能力が必要です。現在のモデルはまだ専門家レベルの正確性に達しておらず、性能に偏りがあります。私たちのテストは、モデルの弱点を特定するために使用でき ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Hallucination.html">#Hallucination</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/993">Reducing Quantity Hallucinations in Abstractive Summarization, Zheng Zhao+, N_A, EMNLP20</a>
<span class="snippet">Hermanシステムは、抽象的な要約において幻覚を回避するために、数量エンティティを認識し、元のテキストでサポートされている数量用語を持つ要約を上位にランク付けするアプローチを提案しています。実験結果は、このアプローチが高い適合率と再現率を持ち、F$_1$スコアが向上することを示しています。また、 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><a class="button" href="articles/QA-based.html">#QA-based</a><br><span class="issue_date">Issue Date: 2023-08-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1007">Asking and Answering Questions to Evaluate the Factual Consistency of Summaries, Wang, ACL20</a>
<span class="snippet">要約の事実の不整合を特定するための自動評価プロトコルであるQAGSを提案する。QAGSは、要約とソースについて質問をし、整合性がある回答を得ることで要約の事実的整合性を評価する。QAGSは他の自動評価指標と比較して高い相関を持ち、自然な解釈可能性を提供する。QAGSは有望なツールであり、https ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ContextAware.html">#ContextAware</a><br><span class="issue_date">Issue Date: 2019-01-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/300">Response Generation by Context-aware Prototype Editing, Wu+, AAAI19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DialogueGeneration.html">#DialogueGeneration</a><br><span class="issue_date">Issue Date: 2019-01-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/302">Training Millions of Personalized Dialogue Agents, Mazaré, ACL19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><br><span class="issue_date">Issue Date: 2019-08-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/319">User Preference-Aware Review Generation, Wang+, PAKDD19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CommentGeneration.html">#CommentGeneration</a><br><span class="issue_date">Issue Date: 2019-08-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/322">Coherent Comment Generation for Chinese Articles with a Graph-to-Sequence Model, Li+ ,arXiv19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CommentGeneration.html">#CommentGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2019-09-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/323">Automatic Generation of Personalized Comment Based on User Profile, Zeng+, arXiv19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CommentGeneration.html">#CommentGeneration</a><br><span class="issue_date">Issue Date: 2019-09-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/326">Cross-domain personalized image captioning, Long+, 2019</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2021-07-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/397">Deep Learning Recommendation Model for Personalization and Recommendation Systems, Naumov+, Facebook, arXiv‘19</a>
<span class="snippet">Parallelism以後のセクションはあとで読む ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/455">Knowledge Tracing with Sequential Key-Value Memory Networks, Ghodai+, Research School of Computer Science, Australian National University, SIGIR19</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/986">HighRES: Highlight-based Reference-less Evaluation of Summarization, Hardy+, N_A, ACL19</a>
<span class="snippet">要約の手動評価は一貫性がなく困難なため、新しい手法であるHighRESを提案する。この手法では、要約はソースドキュメントと比較して複数のアノテーターによって評価され、ソースドキュメントでは重要な内容がハイライトされる。HighRESはアノテーター間の一致度を向上させ、システム間の違いを強調すること ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/996">Neural Text Summarization: A Critical Evaluation, Krysciski+ （w_ Richard Socher）, EMNLP-IJCNLP19</a>
<span class="snippet">テキスト要約の研究は進展が停滞しており、データセット、評価指標、モデルの3つの要素に問題があることが指摘されている。自動収集されたデータセットは制約が不十分であり、ノイズを含んでいる可能性がある。評価プロトコルは人間の判断と相関が弱く、重要な特性を考慮していない。モデルはデータセットのバイアスに過 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DialogueGeneration.html">#DialogueGeneration</a><br><span class="issue_date">Issue Date: 2018-02-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/255">Personalizing Dialogue Agents: I have a dog, do you have pets too?, Zhang+, arXiv18</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2018-07-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/276">Personalized Review Generation by Expanding Phrases and Attending on Aspect-Aware Representations, Ni+, ACL18</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2018-10-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/277">A Unified Model for Document-Based Question Answering Based on Human-Like Reading Strategy, Li+, AAAI18</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2018-12-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/282"> xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems, KDD18</a>
<span class="snippet">Gunosyの関さんによるxDeepFMの解説：https://data.gunosy.io/entry/deep-factorization-machines-2018DeepFMの発展についても詳細に述べられていて、とても参考になる。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2019-01-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/301">A Knowledge-Grounded Neural Conversation Model, Ghazvininejad+, AAAI18, </a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/311">Graph Convolutional Neural Networks for Web-Scale Recommender Systems, Ying+, KDD18</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><br><span class="issue_date">Issue Date: 2019-08-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/317">Improving Explainable Recommendations with Synthetic Reviews, Ouyang+, RecSys18</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CommentGeneration.html">#CommentGeneration</a><br><span class="issue_date">Issue Date: 2019-08-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/321">Netizen-Style Commenting on Fashion Photos: Dataset and Diversity Measures, Lin+, WWW18</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><a class="button" href="articles/CTRPrediction.html">#CTRPrediction</a><br><span class="issue_date">Issue Date: 2021-05-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/348">xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems, Lian+, KDD‘18</a>
<span class="snippet">#281 にも書いたが、下記リンクに概要が記載されている。DeepFMに関する動向：https://data.gunosy.io/entry/deep-factorization-machines-2018 ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/review.html">#review</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/652">A Hierarchical End-to-End Model for Jointly Improving Text Summarization  and Sentiment Classification, Shuming Ma+, N_A, arXiv18</a>
<span class="snippet">テキスト要約と感情分類を共同学習するための階層的なエンドツーエンドモデルを提案し、感情分類ラベルをテキスト要約の出力の「要約」として扱う。提案モデルはAmazonオンラインレビューデータセットでの実験で、抽象的な要約と感情分類の両方で強力なベースラインシステムよりも優れた性能を発揮することが示され ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/QA-based.html">#QA-based</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/994">A Semantic QA-Based Approach for Text Summarization Evaluation, Ping Chen+, N_A, AAAI18</a>
<span class="snippet">自然言語処理システムの評価における問題の一つは、2つのテキストパッセージの内容の違いを特定することです。本研究では、1つのテキストパッセージを小さな知識ベースとして扱い、多数の質問を投げかけて内容を比較する方法を提案します。実験結果は有望であり、2007年のDUC要約コーパスを使用して行われました ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/GenerativeAdversarialNetwork.html">#GenerativeAdversarialNetwork</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/60">Generative Adversarial Networks: An Overview, Dumoulin+, IEEE-SPM17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/92">Generating Sentences by Editing Prototypes, Guu+, arXiv17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/133">Cutting-off redundant repeating generations for neural abstractive summarization, Suzuki+, EACL17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/134">A Deep Reinforced Model for Abstractive Summarization, Paulus+（with Socher）, arXiv17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/208">Adapting Sequence Models for Sentence Correction, Schmaltz （with Rush）, EMNLP17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/209">Coarse-to-Fine Attention Models for Document Summarization, Ling+ （with Rush）, ACL17 Workshop on New Frontiers in Summarization</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/UserModeling.html">#UserModeling</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/210">Multi-View Unsupervised User Feature Embedding for Social Media-based Substance Use Prediction, Ding+, EMNLP17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/211">MoodSwipe: A Soft Keyboard that Suggests Messages Based on User-Specified Emotions, Huang+, EMNLP17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/212">Online Deep Learning: Learning Deep Neural Networks on the Fly, Doyen Sahoo+, N_A, arXiv17</a>
<span class="snippet">本研究では、オンライン設定でリアルタイムにディープニューラルネットワーク（DNN）を学習するための新しいフレームワークを提案します。従来のバックプロパゲーションはオンライン学習には適していないため、新しいHedge Backpropagation（HBP）手法を提案します。この手法は、静的およびコ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/GenerativeAdversarialNetwork.html">#GenerativeAdversarialNetwork</a><br><span class="issue_date">Issue Date: 2018-02-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/247">Adversarial Ranking for Language Generation, Lin+, NIPS17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Multi.html">#Multi</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/VariationalAutoEncoder.html">#VariationalAutoEncoder</a><br><span class="issue_date">Issue Date: 2018-10-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/278">Salience Estimation via Variational Auto-Encoders for Multi-Document Summarization, Li+, AAAI17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2019-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/312">Modeling Relational Data with Graph Convolutional Networks, Michael Schlichtkrull+, N_A, arXiv17</a>
<span class="snippet">知識グラフは不完全な情報を含んでいるため、関係グラフ畳み込みネットワーク（R-GCNs）を使用して知識ベース補完タスクを行う。R-GCNsは、高度な多関係データに対処するために開発されたニューラルネットワークであり、エンティティ分類とリンク予測の両方で効果的であることを示している。さらに、エンコー ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CommentGeneration.html">#CommentGeneration</a><br><span class="issue_date">Issue Date: 2019-09-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/327">Attend to You: Personalized Image Captioning with Context Sequence Memory Networks, Park+, arXiv 2017</a>
<span class="snippet">画像が与えられたときに、その画像に対するHashtag predictionと、personalizedなpost generationを行うタスクを提案。InstagramのPostの簡易化などに応用できる。Postを生成するためには、自身の言葉で、画像についての説明や、contextとい ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><a class="button" href="articles/CTRPrediction.html">#CTRPrediction</a><br><span class="issue_date">Issue Date: 2021-05-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/349">DeepFM: A Factorization-Machine based Neural Network for CTR Prediction, Guo+, IJCAI’17</a>
<span class="snippet">実装: https://github.com/rixwew/pytorch-fm ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><a class="button" href="articles/StudentPerformancePrediction.html">#StudentPerformancePrediction</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-05-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/361">The Knowledge-Learning-Instruction Framework: Bridging the Science-Practice Chasm to Enhance Robust Student Learning, Pelanek, User Modeling and User-Adapted Interaction, 2017</a>
<span class="snippet">BKT、PFAや、それらを用いるContext（どのモデルをどのように自分のcontextに合わせて選択するか）、KLI Frameworkに基づくKCの構成のされ方、モデル評価方法等を理解したい場合、読んだほうが良さそう？ざっとしか見ていないけど、重要な情報がめちゃめちゃ書いてありそう。後でし ...</span>
<a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2021-07-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/399">Learning to Represent Student Knowledge on Programming Exercises Using Deep Learning, Wang+, Stanford University, EDM17</a>
<span class="snippet">DKT #297 のPiechも共著に入っている。プログラミングの課題を行なっている時（要複数回のソースコードサブミット）、1. 次のexerciseが最終的に正解で終われるか否か2. 現在のexerciseを最終的に正解で終われるか否かを予測するタスクを実施 ...</span>
<a class="button" href="articles/TimeSeriesDataProcessing.html">#TimeSeriesDataProcessing</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/118">Derivative Delay Embedding: Online Modeling of Streaming Time Series, Zhifei Zhang+, N_A, arXiv16</a>
<span class="snippet">本研究では、オンラインでストリーミング時系列データを効率的にモデリングするためのDDE-MGM手法を提案しています。DDEは、再帰的なパターンを保持する埋め込み空間に時系列を変換するために使用され、MGMはパターンのモデリングと分類に使用されます。実験結果は、提案手法の効果と優れた分類精度を示して ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-02-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/258">Generating Sentences from a Continuous Space, Bowman+, CoNLL16</a>
<span class="snippet">【Variational Autoencoder徹底解説】https://qiita.com/kenmatsu4/items/b029d697e9995d93aa24 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/GraphConvolutionalNetwork.html">#GraphConvolutionalNetwork</a><br><span class="issue_date">Issue Date: 2018-03-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/265">Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering, Defferrard+, NIPS16</a>
<span class="snippet">GCNを勉強する際は読むと良いらしい。あわせてこのへんも：Semi-Supervised Classification with Graph Convolutional Networks, Kipf+, ICLR'17https://github.com/tkipf/gcn ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-10-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/279">Neural Headline Generation with Minimum Risk Training, Ayana+, N_A, arXiv16</a>
<span class="snippet">自動見出し生成のために、最小リスクトレーニング戦略を使用してモデルパラメータを最適化し、見出し生成の改善を実現する。提案手法は英語と中国語の見出し生成タスクで最先端のシステムを上回る性能を示す。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><br><span class="issue_date">Issue Date: 2018-12-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/298">Deep Neural Networks for YouTube Recommendations, Covington+, RecSys16</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-09-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/483">Applications of the Elo Rating System in Adaptive Educational Systems, Pelanek, Computers & Educations16</a>
<span class="snippet">Elo rating systemの教育応用に関して詳細に記述されている ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/657">Ups and Downs: Modeling the Visual Evolution of Fashion Trends with  One-Class Collaborative Filtering, Ruining He+, N_A, arXiv16</a>
<span class="snippet">ファッションなどの特定のドメインにおいて、製品の視覚的な外観と時間の経過に伴う進化を同時にモデル化することが重要であり、そのような好みをモデル化することは非常に困難である。本論文では、One-Class Collaborative Filtering設定のための新しいモデルを構築し、過去のフィード ...</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/Online/Interactive.html">#Online/Interactive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/199">Contextual Dueling Bandits, Dudik+, JMLR15</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Education.html">#Education</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><br><span class="issue_date">Issue Date: 2019-10-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/328">Personalized Mathematical Word Problem Generation, Polozov+, IJCAI15</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/LearningAnalytics.html">#LearningAnalytics</a><br><span class="issue_date">Issue Date: 2021-07-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/400">Autonomously Generating Hints by Inferring Problem Solving Policies, Piech+, Stanford University, L@S15</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/654">Image-based Recommendations on Styles and Substitutes, Julian McAuley+, N_A, arXiv15</a>
<span class="snippet">本研究では、人間の感覚に基づいた物体間の関係性をモデル化することを目的として、大規模なデータセットを用いたスケーラブルな方法を提案している。関連する画像のグラフ上で定義されたネットワーク推論問題として捉え、服やアクセサリーの組み合わせを推奨することができるシステムを開発し、その他のアプリケーション ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/ImageCaptioning.html">#ImageCaptioning</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-05-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/670">CIDEr: Consensus-based Image Description Evaluation, Ramakrishna Vedantam+, N_A, CVPR15</a>
<span class="snippet">画像を文章で自動的に説明することは、長年の課題である。本研究では、人間の合意を利用した画像説明の評価のための新しいパラダイムを提案し、新しい自動評価指標と2つの新しいデータセットを含む。提案手法は、人間の判断をより正確に捉えることができ、5つの最先端の画像説明手法を評価し、将来の比較のためのベンチ ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/969">Document-Level Machine Translation Evaluation with Gist Consistency and Text Cohesion, Gong+, DiscoMT15</a>
<span class="snippet">No description ...</span>
<br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/649">Extended Recommendation Framework: Generating the Text of a User Review  as a Personalized Summary, Mickaël Poussevin+, N_A, arXiv14</a>
<span class="snippet">評価に基づくレコメンダーシステムを拡張し、ユーザーが選択や推薦の理解に役立つ追加情報を提供することを提案。アイテムに関連する個人的なレビューの生成を新しいタスクとして考え、抽出型サマリーの形式を使用。評価とアイテムの2つの情報源が、評価の推定とサマリーの生成の両方に使用できることを示し、単一の情報 ...</span>
<a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-08-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/480">Properties of the Bayesian Knowledge Tracing Model, BRETT VAN DE SANDE, JEDM13</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Education.html">#Education</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/645">Personalized Text Content Summarizer for Mobile Learning: An Automatic Text Summarization System with Relevance Based Language Model, Guangbing+, IEEE Fourth International Conference on Technology for Education, 2012, 22</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/CrossLingual.html">#CrossLingual</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/979">Evaluating the Efficacy of Summarization Evaluation across Languages, Koto+ （w_ Tim先生）, Findings of ACL12</a>
<span class="snippet">この研究では、異なる言語の要約コーパスを使用して、マルチリンガルBERTを用いたBERTScoreが他の要約評価メトリックスよりも優れたパフォーマンスを示すことが示されました。これは、英語以外の言語においても有効であることを示しています。 ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/651">Personalized news filtering and summarization on the web, Xindong+, 2011 IEEE 23rd International Conference on Tools with Artificial Intelligence, 29</a>
<span class="snippet">summarizationではなく、keyword extractionの話だった ...</span>
<br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/713">Youku-mPLUG: A 10 Million Large-scale Chinese Video-Language Dataset for  Pre-training and Benchmarks, Haiyang Xu+, N_A, arXiv23</a>
<span class="snippet">中国のコミュニティにおいて、Vision-Language Pre-training（VLP）とマルチモーダル大規模言語モデル（LLM）の発展を促進するために、Youku-mPLUGという最大の公開中国語高品質ビデオ言語データセットをリリースしました。このデータセットは、大規模なプレトレーニングに ...</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/ListWise.html">#ListWise</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/194">Listwise Approach to Learning to Rank - Theory and Algorithm （ListMLE）, Xia+, ICML2008</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MultitaskLearning.html">#MultitaskLearning</a><br><span class="issue_date">Issue Date: 2018-02-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/250">A unified architecture for natural language processing: Deep neural networks with multitask learning, Collobert+, ICML2008.</a>
<span class="snippet">Deep Neural Netを用いてmultitask learningを行いNLPタスク（POS tagging, Semantic Role Labeling, Chunking etc.）を解いた論文。被引用数2000を超える。multitask learningの学習プロセスな ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/MatrixFactorization.html">#MatrixFactorization</a><br><span class="issue_date">Issue Date: 2018-01-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/217">Probabilistic matrix factorization, Salakhutdinov+, Advances in neural information processing systems, 2007</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/20">Personalizing Search via Automated Analysis of Interests and Activities, SIGIR, Teevan+, 2005</a>
<span class="snippet">・userに関するデータがrichなほうが、Personalizationは改善する。・queries, visited web pages, emails, calendar items, stored desktop 　　　　documents、全てのsetを用いた場合が最も良かった ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><br><span class="issue_date">Issue Date: 2019-08-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/316">Automatic Generation of Personalized Comment Based on User Profile, Zeng+, arXiv</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ReviewGeneration.html">#ReviewGeneration</a><br><span class="issue_date">Issue Date: 2019-08-17</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/318">Review Response Generation in E-Commerce Platforms with External Product Information</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2020-08-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/340">Airbnbの機械学習導入から学ぶ</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2021-06-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/378">ゼロから始めてオフライン強化学習とConservative Q-Learningを理解する</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2021-07-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/396">Continuously Improving Recommender Systems for Competitive Advantage Using NVIDIA Merlin and MLOps</a>
<span class="snippet">Recommender System運用のためのアーキテクチャに関する情報 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2021-10-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/410">実臨床・Webサービス領域での機械学習研究 開発の標準化</a>
<span class="snippet">並列して走る機械学習案件をどのように効果的に捌いているか説明。①タイトな締切→ 高速化で対処→ よく使う機能をML自身に実装する②並行して走る案件→ 並列化　→ Kubernetesを用いて、タスクごとに異なるノードで分散処理（e.g CVのFoldごとにノード分散、推論ユーザごとにノ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Infrastructure.html">#Infrastructure</a><br><span class="issue_date">Issue Date: 2021-10-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/411">Hidden Technical Debt in Machine Learning Systems, Sculley+, Google</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/137843973-576deeb7-778d-44d8-aac8-5ed5c4fa7d2b.png)よく見るML codeが全体のごく一部で、その他の基盤が大半を占めてますよ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2022-03-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/437">良いコードとは何か - エンジニア新卒研修 スライド公開, CyberZ, 森</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/579">E-Commerce product recommendation agents: use, characteristics, and impact</a>
<span class="snippet">超重要論文 ...</span>
<a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/626">Towards Complex Reasoning: the Polaris of Large Language Models</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/627">Transformers Learn Shortcuts to Automata</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/677">Sketching the Future （STF）: Applying Conditional Control Techniques to Text-to-Video Models</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1059">The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”</a>
<span class="snippet">GPT3, LLaMaを A is Bでfinetuneし、B is Aという逆方向のfactを生成するように（質問をして）テストしたところ、0%付近のAcc.だった。また、Acc.が低いだけでなく、対数尤度もrandomなfactを生成した場合と、すべてのモデルサイズで差がないことがわかった ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/25e20dcc-0313-4cd2-8768-afb0e4e48a68" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
