---
layout: post
title: Finetuningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Finetuning
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ReinforcementLearning.html">#ReinforcementLearning</a><br><span class="issue_date">Issue Date: 2023-03-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/512">Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, N_A, arXiv23</a>
<span class="snippet">本研究では、言語エージェントを強化するための新しいフレームワークであるReflexionを提案しています。Reflexionエージェントは、言語的フィードバックを通じて自己反省し、より良い意思決定を促すために反省的なテキストを保持します。Reflexionはさまざまなタスクでベースラインエージェン ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ChatGPT.html">#ChatGPT</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/700">LIMA: Less Is More for Alignment, Chunting Zhou+, N_A, arXiv23</a>
<span class="snippet">本研究では、65BパラメータのLLaMa言語モデルであるLIMAを訓練し、強化学習や人間の好みモデリングなしに、厳選された1,000のプロンプトとレスポンスのみで標準的な教師あり損失で微調整しました。LIMAは、幅広いクエリに対応する驚くべき強力なパフォーマンスを示し、トレーニングデータに現れなか ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/db025381-0bf0-47a3-bd18-5d88bff666df" alt="image"><a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/769">Full Parameter Fine-tuning for Large Language Models with Limited  Resources, Kai Lv+, N_A, arXiv23</a>
<span class="snippet">LLMsのトレーニングには膨大なGPUリソースが必要であり、既存のアプローチは限られたリソースでの全パラメーターの調整に対処していない。本研究では、LOMOという新しい最適化手法を提案し、メモリ使用量を削減することで、8つのRTX 3090を搭載した単一のマシンで65Bモデルの全パラメーターファイ ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/823">Measuring the Instability of Fine-Tuning, ACL23</a>
<span class="snippet">事前学習済み言語モデルのファインチューニングは小規模データセットでは不安定であることが示されている。本研究では、不安定性を定量化する指標を分析し、評価フレームワークを提案する。また、既存の不安定性軽減手法を再評価し、結果を提供する。 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/DataGeneration.html">#DataGeneration</a><br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1024">Prompt2Model: Generating Deployable Models from Natural Language  Instructions, Vijay Viswanathan+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、プロンプトを自然言語でタスクを説明し、特定のモデルを訓練する手法であるPrompt2Modelを提案しています。Prompt2Modelは、既存のデータセットと事前学習済みモデルの検索、LLMsを使用したデータセットの生成、および教師あり微調整の ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-03-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/513">Self-Instruct: Aligning Language Model with Self Generated Instructions, Wang+ （w_ Noah Smith）, Univesity of Washington, arXiv22</a>
<span class="snippet">LLMを使うだけでここまで研究ができる時代がきた ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/542">Scaling Instruction-Finetuned Language Models, Chung+, Google, arXiv22</a>
<span class="snippet">T5をinstruction tuningしたFlanT5の研究 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-03-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/514">Publicly available instruction-tuned models</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/771">LM Flow</a>
<span class="snippet">一般的なFoundation Modelのファインチューニングと推論を簡素化する拡張可能なツールキット。継続的なpretragning, instruction tuning, parameter efficientなファインチューニング,alignment tuning,大規模モデルの推論などさま ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/796">Auto train advanced</a>
<span class="snippet">Hugging Face Hub上の任意のLLMに対して、localのカスタムトレーニングデータを使ってfinetuningがワンラインでできる。peftも使える。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1027">LLMのファインチューニング で 何ができて 何ができないのか</a>
<span class="snippet">imosさんのツイートを引用> 文章が悪かったので補足。追加学習を全体に十分なデータですれば知識は獲得しえます（が事前学習の知識を忘却するリスクは高い）。巷でよくファインチューニングと呼ばれるものは、知識を司るらしいMLP部を触らず自己注意機構部のみを更新するので、そもそも知識を増やすのは難しいと ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
