---
layout: post
title: LLMAgentに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## LLMAgent
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/AutoML.html">#AutoML</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1067">Benchmarking Large Language Models As AI Research Agents, Qian Huang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、AI研究エージェントを構築し、科学的な実験のタスクを実行するためのベンチマークとしてMLAgentBenchを提案する。エージェントはファイルの読み書きやコードの実行などのアクションを実行し、実験を実行し、結果を分析し、機械学習パイプラインのコードを変更することができる。GPT-4ベースの研究エージェントは多くのタスクで高性能なモデルを実現できるが、成功率は異なる。また、LLMベースの研究エージェントにはいくつかの課題がある。</span>
<span class="snippet"><span>Comment</span>AIDBのツイート: https://x.com/ai_database/status/1711274596966834282?s=46&t=Y6UuIHB0Lv0IpmFAjlc2-QGPT4がMLモデルをどれだけ自動的に構築できるかを調べた模様。また、ベンチマークデータを作成した模様。結果として ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1028">A Survey on Large Language Model based Autonomous Agents, Lei Wang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>自律エージェントの研究は、以前は限られた知識を持つエージェントに焦点を当てていましたが、最近では大規模言語モデル（LLMs）を活用した研究が増えています。本論文では、LLMに基づく自律エージェントの研究を包括的に調査し、統一されたフレームワークを提案します。さらに、LLMに基づくAIエージェントの応用や評価戦略についてもまとめています。将来の方向性や課題についても議論し、関連する参考文献のリポジトリも提供しています。</span>
<span class="snippet"><span>Comment</span>以下AIDBのツイートの引用> LLMベースの自律型エージェントモデルは、2021年12月から『WebGPT』から2023年8月の『MetaGPT』までに32個ほども開発されているとのこと。>自律型エージェントモデルは、人工一般知能（AGI）に向けた有望な取り組みとされています。>最近では良いサーベ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/c921a960-02f7-44e6-8c24-bb578f599bbe" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1020">AgentBench: Evaluating LLMs as Agents, Xiao Liu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）をエージェントとして評価するための多次元の進化するベンチマーク「AgentBench」を提案しています。AgentBenchは、8つの異なる環境でマルチターンのオープンエンドの生成設定を提供し、LLMの推論と意思決定能力を評価します。25のLLMsに対するテストでは、商用LLMsは強力な能力を示していますが、オープンソースの競合他社との性能には差があります。AgentBenchのデータセット、環境、および評価パッケージは、GitHubで公開されています。</span>
<span class="snippet"><span>Comment</span>エージェントとしてのLLMの推論能力と意思決定能力を評価するためのベンチマークを提案。トップの商用LLMとOpenSource LLMの間に大きな性能差があることを示した。 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/883">Towards A Unified Agent with Foundation Models, Norman Di Palo+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、言語モデルとビジョン言語モデルを強化学習エージェントに組み込み、効率的な探索や経験データの再利用などの課題に取り組む方法を調査しました。スパースな報酬のロボット操作環境でのテストにおいて、ベースラインに比べて大幅な性能向上を実証し、学習済みのスキルを新しいタスクの解決や人間の専門家のビデオの模倣に活用する方法を示しました。</span>
<span class="snippet"><span>Comment</span> ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/aa40d0e3-9499-4804-9046-a9ad795c2d52" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/783">Mind2Web: Towards a Generalist Agent for the Web, Xiang Deng+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>Mind2Webという新しいデータセットを紹介します。このデータセットは、任意のウェブサイト上で複雑なタスクを実行するための言語の指示に従うウェブエージェントを開発・評価するために作成されました。従来のデータセットでは一般的なウェブエージェントには適していなかったため、Mind2Webはより多様なドメイン、実世界のウェブサイト、幅広いユーザーの相互作用パターンを提供します。また、大規模言語モデル（LLMs）を使用して一般的なウェブエージェントを構築するための初期の探索も行われます。この研究は、ウェブエージェントのさらなる研究を促進するためにデータセット、モデルの実装、およびトレーニング済みモデルをオープンソース化します。</span>
<span class="snippet"><span>Comment</span>Webにおけるgeneralistエージェントを評価するためのデータセットを構築。31ドメインの137件のwebサイトにおける2350個のタスクが含まれている。タスクは、webサイトにおける多様で実用的なユースケースを反映し、チャレンジングだが現実的な問題であり、エージェントの環境やタスクをまた ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/760">Think Before You Act: Decision Transformers with Internal Working Memory, Jikun Kang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLM）の性能は、トレーニング中にパラメータに振る舞いを記憶する「忘却現象」によって低下する可能性がある。人間の脳は分散型のメモリストレージを利用しており、忘却現象を軽減している。そこで、我々は、内部作業メモリモジュールを提案し、Atariゲームとメタワールドオブジェクト操作タスクの両方でトレーニング効率と汎化性を向上させることを示した。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/518">REACT : SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS, Yao+, Princeton University and Google brain, ICLR23</a>
<span class="snippet"><span>Comment</span># 概要人間は推論と行動をシナジーさせることで、さまざまな意思決定を行える。近年では言語モデルにより言語による推論を意思決定に組み合わせる可能性が示されてきた。たとえば、タスクをこなすための推論トレースをLLMが導けることが示されてきた（Chain-of-Thought）が、CoTは外部リソース ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1049">Agents: An opensource framework for autonomous language agents</a>
<span class="snippet"><span>Comment</span>以下の特徴を持つLLMAgent開発のためのフレームワークlong-short term memorytool usageweb navigationmulti-agent communicationhuman-agent interactionsymbolic ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/521">Llamaindex</a>
<span class="snippet"><span>Comment</span>LlamaIndexのインデックスを更新し、更新前後で知識がアップデートされているか確認してみた  https://dev.classmethod.jp/articles/llama-index-insert-index/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/520">LangChain</a>
<span class="snippet"><span>Comment</span>LangChain の Googleカスタム検索 連携を試す  https://note.com/npaka/n/nd9a4a26a8932LangChainのGetting StartedをGoogle Colaboratoryでやってみる ④Agents    https://zenn.de ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
