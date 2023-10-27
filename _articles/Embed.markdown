---
layout: post
title: Embedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Embed
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/379">Improving Neural Machine Translation with Compact Word Embedding Tables, Kumar+, 2021</a>
<span class="snippet">NMTにおいてword embeddingがどう影響しているかなどを調査しているらしい ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2021-06-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/383">OpenKE, 2021</a>
<span class="snippet">Wikipedia, Freebase等のデータからKnowledge Embeddingを学習できるオープンソースのライブラリ ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ContrastiveLearning.html">#ContrastiveLearning</a><br><span class="issue_date">Issue Date: 2023-07-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/907">SimCSE: Simple Contrastive Learning of Sentence Embeddings, Tianyu Gao+, N_A, EMNLP21</a>
<span class="snippet">この論文では、SimCSEという対比学習フレームワークを提案しています。このフレームワークは、文の埋め込み技術を進化させることができます。教師なしアプローチでは、入力文をノイズとして扱い、自己を対比的に予測します。教師ありアプローチでは、自然言語推論データセットから注釈付きのペアを使用して対比学習 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/ba20a1ca-0078-4227-8bb3-3805ee57a620" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/RepresentationLearning.html">#RepresentationLearning</a><br><span class="issue_date">Issue Date: 2022-06-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/457">Deep contextualized word representations, Peters+, Allen Institute for Artificial intelligence, NAACL18</a>
<span class="snippet">ELMoのEmbedding Layerでは、2048 characterの（vocab size?）n-gram convolution filter（文字ごとにembeddingし、単語のembeddingを得るためにfilterを適用する？）の後に2つのhighway networkをかませて ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/General.html">#General</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/68">StarSpace: Embed All The Things, Wu+, arXiv17</a>
<span class="snippet">解説：https://www.slideshare.net/akihikowatanabe3110/starspace-embed-all-the-things ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/69">A structured self-attentive sentence embedding, Li+ （Bengio group）, ICLR17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/71">Supervised Learning of Universal Sentence Representations from Natural Language Inference Data, Conneau+, EMNLP17</a>
<span class="snippet">汎用的な文のエンコーダができました！という話。SNLIデータでパラメータ学習、エンコーダ構成スライド図中右側のエンコーダ部分をなるべく一般的な文に適用できるように学習したい。色々なタスクで、文のエンコーダ構成を比較した結果、bi-directional LSTMでエンコードし、要素ご ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Word.html">#Word</a><br><span class="issue_date">Issue Date: 2017-12-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/78">Poincare Embeddings for Learning Hierarchical Representations, Nickel+, NIPS17</a>
<span class="snippet">![image](https://user-images.githubusercontent.com/12249301/34452953-0e124ad6-ed8d-11e7-800d-0c2712df116a.png)データとして上位・下位概念を与えていないのに、原点付近には上位語・円周付 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Word.html">#Word</a><br><span class="issue_date">Issue Date: 2017-12-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/79">Skip-Gram – Zipf + Uniform = Vector Additivity, Gittens+, ACL17</a>
<span class="snippet">Embeddingの加法構成性（e.g. man+royal=king）を理論的に理由づけ（解説スライドより） ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/UserModeling.html">#UserModeling</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/210">Multi-View Unsupervised User Feature Embedding for Social Media-based Substance Use Prediction, Ding+, EMNLP17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/70">Learning Distributed Representations of Sentences from Unlabelled Data, Hill+, NAACL16</a>
<span class="snippet">Sentenceのrepresentationを学習する話代表的なsentenceのrepresentation作成手法(CBOW, SkipGram, SkipThought, Paragraph Vec, NMTなど)をsupervisedな評価（タスク志向+supervised）とun ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/SentimentAnalysis.html">#SentimentAnalysis</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/72">Document Modeling with Gated Recurrent Neural Network for Sentiment Classification, Tang+, EMNLP15</a>
<span class="snippet">word level -> sentence level -> document level のrepresentationを求め、documentのsentiment classificationをする話。documentのRepresentationを生成するときに参考になるやも。sen ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/74">A hierarchical neural autoencoder for paragraphs and documents, Li+, ACL15</a>
<span class="snippet">trip advisorのレビューを研究で使うのって規約的にアウトじゃなかったっけ。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Spoken Language Processing.html">#Spoken Language Processing</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/527">CLAP</a>
<span class="snippet">たとえばゼロショットでaudio分類ができる![image](https://user-images.githubusercontent.com/12249301/234293138-20edf6cd-3259-4547-a2fc-69893273fa76.jpeg) ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/531">Training a recommendation model with dynamic embeddings</a>
<span class="snippet">（理解が間違っているかもしれないが）推薦システムは典型的にはユーザとアイテムをベクトル表現し、関連度を測ることで推薦をしている。この枠組みをめっちゃスケールさせるととんでもない数のEmbeddingを保持することになり、メモリ上にEmbeddingテーブルを保持して置けなくなる。特にこれはonlin ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/SearchEngine.html">#SearchEngine</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/565">Awesome Vector Search Engine</a>
<span class="snippet">ベクトルの類似度を測るサービスやライブラリ等がまとまったリポジトリ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-10-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1057">Japanese Simple SimCSE</a>
<span class="snippet">日本語の事前学習言語モデルと、日本語の学習データを利用してSimCSEを学習し網羅的に評価をした結果が記載されている。Supervised SimCSE, UnsupervisednSimCSEの両方で実験。また、学習するデータセットを変更したときの頑健性も検証。性能が良かったモデルはSentenc ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
