---
layout: post
title: Libraryに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Library
<div class="visible-content">
<a class="button" href="articles/python.html">#python</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-01-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/508">Polars, 2023</a>
<span class="snippet">pandasより100倍高速で複雑なクエリも見やすく書けてindexも存在しないのでバグも出にくいという優れものらしい ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/659">MPT-7B, 2023</a>
<span class="snippet">ChatGPTのLLMと比較すると、ざっと例を見た感じ質問応答としての能力はそこまで高くなさそうな印象。finetuningしない限りはGPT3,GPT4で良さげ。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-05-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/665">OpenSource PaLM, 2023</a>
<span class="snippet">150m,410m,1bのモデルがある。Googleの540bには遠く及ばないし、emergent abilityも期待できないパラメータ数だが、どの程度の性能なのだろうか。 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/python.html">#python</a><br><span class="issue_date">Issue Date: 2023-05-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/675">Assisted Generation: a new direction toward low-latency text generation, 2023</a>
<span class="snippet">assistant modelをロードしgenerateに引数として渡すだけ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fecc1c5e-b9e5-4844-af96-ba48c3d60fae" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Explanation.html">#Explanation</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/499">Transformers Interpret, 2022</a>
<span class="snippet">transformersのモデルをたった2行追加するだけで、explainableにするライブラリ基本的にtextとvisionのclassificationをサポートしている模様text classificationの場合、たとえばinput tokenの各トークンの分類に対する寄与度をou ...</span>
<a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2021-06-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/383">OpenKE, 2021</a>
<span class="snippet">Wikipedia, Freebase等のデータからKnowledge Embeddingを学習できるオープンソースのライブラリ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2020-03-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/334">BERT 日本語Pre-trained Model, NICT 2020</a>
<span class="snippet">NICTが公開。既に公開されているBERTモデルとのベンチマークデータでの性能比較も行なっており、その他の公開済みBERTモデルをoutperformしている。 ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/386">最先端自然言語処理ライブラリの最適な選択と有用な利用方法 _ pycon-jp-2020</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/121644722-56025800-cace-11eb-9fe9-9d2f6b0eae5a.png) ...</span>
<a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/AdaptiveLearning.html">#AdaptiveLearning</a><a class="button" href="articles/EducationalDataMining.html">#EducationalDataMining</a><a class="button" href="articles/KnowledgeTracing.html">#KnowledgeTracing</a><br><span class="issue_date">Issue Date: 2022-07-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/460">pyBKT: An Accessible Python Library of Bayesian Knowledge Tracing Models, Bardrinath+, EDM20</a>
<span class="snippet"># モチベーションBKTの研究は古くから行われており、研究コミュニティで人気が高まっているにもかかわらず、アクセス可能で使いやすいモデルの実装と、さまざまな文献で提案されている多くの変種は、理解しにくいものとなっている。そこで、モダンなpythonベースドな実装としてpyBKTを実装し、研究コミ ...</span>
<a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-03-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/510">20B params chatgpt alternative</a>
<span class="snippet">元ツイートApache2.0で公開https://twitter.com/_philschmid/status/1634492396171071488?s=46&t=VvPwEQsB--BeXx0YbYQdxQ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2022-07-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/462">Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks, Reimers+, UKP-TUDA, EMNLP19</a>
<span class="snippet">BERTでトークンをembeddingし、mean poolingすることで生成される文ベクトルを、Siamese Networkを使い距離学習（finetune）させたモデル。<img width="655" alt="image" src="https://user-images.githu ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/767">OpenLLaMA 13B, 2023</a>
<span class="snippet">そもそもOpenLLaMAには、オリジナルのLLaMAと比較して、tokenizerがスペースを無視するというissueがある模様。スペースの情報がクリティカルなタスク、たとえばcode generationなどには要注意。https://github.com/openlm-research/o ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4268eb3f-349f-4ebe-adeb-2cbfcb7cfe17" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/149">Surprise</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/150">LibRec</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/151">fastFM</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/152">MyMediaLite</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/153">LensKit</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/155">mrec</a>
<span class="snippet">参考：http://www.kamishima.net/archive/recsysdoc.pdfhttps://takuti.me/note/recommender-libraries/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><br><span class="issue_date">Issue Date: 2019-09-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/324">Implicit</a>
<span class="snippet">ALSの元論文の日本語解説https://cympfh.cc/paper/WRMF ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2019-09-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/325">【黒橋研】BERT日本語Pretrainedモデル</a>
<span class="snippet">【huggingface transformersで使える日本語モデルのまとめ】https://tech.yellowback.net/posts/transformers-japanese-models ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/python.html">#python</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2021-06-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/373">intel MKL</a>
<span class="snippet">intel CPUでpythonの数値計算を高速化するライブラリ(numpyとかはやくなるらしい; Anacondaだとデフォルトで入ってるとかなんとか) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2021-06-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/376">pytorch tips</a>
<span class="snippet">【pipで様々なCuda versionのpytorchをinstallする方法】https://stackoverflow.com/questions/65980206/cuda-10-2-not-recognised-on-pip-installed-pytorch-1-7-1 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2021-06-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/377">TRTorch</a>
<span class="snippet">pytorchの推論を高速化できるライブラリ。6倍ほど早くなった模様。TorchScriptを介して変換するので、PythonだけでなくC++でも動作できるらしい。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/python.html">#python</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2021-06-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/387">pytorch_lightning tips</a>
<span class="snippet">PyTorch Lightning 2021 (for MLコンペ)https://qiita.com/fam_taro/items/df8656a6c3b277f58781 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2021-06-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/395">optuna_tips</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/FactorizationMachines.html">#FactorizationMachines</a><br><span class="issue_date">Issue Date: 2021-07-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/398">DeepなFactorization Machinesの実装たち</a>
<span class="snippet">下記モデルが実装されているすごいリポジトリ。論文もリンクも記載されており、Factorization Machinesを勉強する際に非常に参考になると思う。MITライセンス。各手法はCriteoのCTRPredictionにおいて、AUC0.8くらい出ているらしい。Logistic Re ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2022-03-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/440">Recbole</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Tools.html">#Tools</a><br><span class="issue_date">Issue Date: 2022-08-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/466">pandas tips</a>
<span class="snippet">◆遅くないpandasの書き方https://naotaka1128.hatenadiary.jp/entry/2021/12/07/083000#iterrows-%E3%81%AF%E7%B5%B6%E5%AF%BE%E3%81%AB%E4%BD%BF%E3%82%8F%E3%81%AA%E ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/497">BetterTransformer, Out of the Box Performance for Hugging Face Transformers</a>
<span class="snippet">たった1ライン追加するだけで、Transformerのinferenceが最大で4.5倍高速化されるBetterTransformerの解説記事better_model = BetterTransformer.transform(model) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-01-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/505">nlpaug</a>
<span class="snippet">Data Augmentationのためのオープンソースライブラリ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-04-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/520">LangChain</a>
<span class="snippet">LangChainのGetting StartedをGoogle Colaboratoryでやってみる ④Agents    https://zenn.dev/kun432/scraps/8216511783e3da ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-04-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/521">Llamaindex</a>
<span class="snippet">LlamaIndexのインデックスを更新し、更新前後で知識がアップデートされているか確認してみた  https://dev.classmethod.jp/articles/llama-index-insert-index/ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Spoken Language Processing.html">#Spoken Language Processing</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/527">CLAP</a>
<span class="snippet">たとえばゼロショットでaudio分類ができる![image](https://user-images.githubusercontent.com/12249301/234293138-20edf6cd-3259-4547-a2fc-69893273fa76.jpeg) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/528">LoRA論文解説</a>
<span class="snippet">huggingfaceがすでにLoRAを実装しているhttps://github.com/huggingface/peft ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/531">Training a recommendation model with dynamic embeddings</a>
<span class="snippet">（理解が間違っているかもしれないが）推薦システムは典型的にはユーザとアイテムをベクトル表現し、関連度を測ることで推薦をしている。この枠組みをめっちゃスケールさせるととんでもない数のEmbeddingを保持することになり、メモリ上にEmbeddingテーブルを保持して置けなくなる。特にこれはonlin ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/540">Contrirver</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/565">Awesome Vector Search Engine</a>
<span class="snippet">ベクトルの類似度を測るサービスやライブラリ等がまとまったリポジトリ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/618">OpenLLaMA</a>
<span class="snippet">LLaMAと同様の手法を似たデータセットに適用し商用利用可能なLLaMAを構築した模様 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Spoken Language Processing.html">#Spoken Language Processing</a><a class="button" href="articles/SpokenLanguageGeneration.html">#SpokenLanguageGeneration</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/620">Bark</a>
<span class="snippet">テキストプロンプトで音声生成ができるモデル。MIT License ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ReinforcementLearning.html">#ReinforcementLearning</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/894">trl_trlx</a>
<span class="snippet">trlを使って日本語LLMをSFTからRLHFまで一通り学習させてみるhttps://www.ai-shift.co.jp/techblog/3583 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1025">zeno-build</a>
<span class="snippet">LLMの実験管理を容易に実施するツールで、異なるハイパーパラメータ、異なるモデル、異なるプロンプトでの実験などを簡単に実施できる。評価結果を自動的に可視化し、interactiveに表示するブラウザベースのアプリケーションも作成可能？ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1026">Metaの「Llama 2」をベースとした商用利用可能な日本語LLM「ELYZA-japanese-Llama-2-7b」を公開しました</a>
<span class="snippet">商用利用可能、70億パラメータ。ELYZA社が独自に作成した評価セットでは日本語のOpenLLMの中で最高性能。ただし、モデル選定の段階でこの評価データの情報を利用しているため、有利に働いている可能性があるとのこと。一般的に利用される日本語の評価用データでは、なんとも言い難い。良いタスクもあれ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1032">LangChain Cheet Sheet</a>
<span class="snippet"><img width="1315" alt="image" src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/6621fe24-d007-4590-b1a6-b861a6dec4ad"> ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/LLMAgent.html">#LLMAgent</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1049">Agents: An opensource framework for autonomous language agents</a>
<span class="snippet">以下の特徴を持つLLMAgent開発のためのフレームワークlong-short term memorytool usageweb navigationmulti-agent communicationhuman-agent interactionsymbolic ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
