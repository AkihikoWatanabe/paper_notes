---
layout: post
title: Neuralに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Neural
<div class="visible-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/92">Generating Sentences by Editing Prototypes, Guu+, arXiv17</a>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/ConceptToText.html">#ConceptToText</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/91">Toward Controlled Generation of Text, Hu+, ICML17</a>
<span class="snippet"><span>Comment</span>Text Generationを行う際は、現在は基本的に学習された言語モデルの尤度に従ってテキストを生成するのみで、outputされるテキストをcontrolすることができないので、できるようにしましたという論文。 VAEによるテキスト生成にGANを組み合わせたようなモデル。 decodingする元 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/90">Multi-Task Video Captioning with Video and Entailment Generation, Pasunuru+, ACL17</a>
<span class="snippet"><span>Comment</span>解説スライド：https://www.slideshare.net/HangyoMasatsugu/hangyo-acl-paperreading2017multitask-video-captioning-with-video-and-entailment-generation/1multitas ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/83">Unsupervised Pretraining for Sequence to Sequence Learning, Ramachandran+, EMNLP17</a>
<span class="snippet"><span>Comment</span>seq2seqにおいてweightのpretrainingを行う手法を提案seq2seqでは訓練データが小さいとoverfittingしやすいという弱点があるので、大規模なデータでunsupervisedにpretrainingし、その後目的のデータでfinetuneすることで精度を向上させまし ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/82">Learning to skim text, Yu+, ACL17</a>
<span class="snippet"><span>Comment</span>解説スライド：http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/07.pdf![image](https://user-images.githubusercontent.com/12249301/34460775-f64d4 ...</span>
<a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Word.html">#Word</a><br><span class="issue_date">Issue Date: 2017-12-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/79">Skip-Gram – Zipf + Uniform = Vector Additivity, Gittens+, ACL17</a>
<span class="snippet"><span>Comment</span>解説スライド：http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/09.pdfEmbeddingの加法構成性（e.g. man+royal=king）を理論的に理由づけ（解説スライドより） ...</span>
<a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Word.html">#Word</a><br><span class="issue_date">Issue Date: 2017-12-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/78">Poincare Embeddings for Learning Hierarchical Representations, Nickel+, NIPS17</a>
<span class="snippet"><span>Comment</span>解説: http://tech-blog.abeja.asia/entry/poincare-embeddings解説スライド：https://speakerdeck.com/eumesy/poincare-embeddings-for-learning-hierarchical-represe・ ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/71">Supervised Learning of Universal Sentence Representations from Natural Language Inference Data, Conneau+, EMNLP17</a>
<span class="snippet"><span>Comment</span>slide: https://www.slideshare.net/naoakiokazaki/supervised-learning-of-universal-sentence-representations-from-natural-language-inference-data汎用的な文のエン ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/69">A structured self-attentive sentence embedding, Li+ （Bengio group）, ICLR17</a>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/General.html">#General</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/68">StarSpace: Embed All The Things, Wu+, arXiv17</a>
<span class="snippet"><span>Comment</span>分類やランキング、レコメンドなど、様々なタスクで汎用的に使用できるEmbeddingの学習手法を提案。Embeddingを学習する対象をEntityと呼び、Entityはbag-of-featureで記述される。Entityはbag-of-featureで記述できればなんでもよく、こ実際にS ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/67">What do Neural Machine Translation Models Learn about Morphology?, Belinkov+, ACL17</a>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/66">Sequence-to-Dependency Neural Machine Translation, Wu+, ACL17</a>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/64">Neural Machine Translation with Source-Side Latent Graph Parsing, Hashimoto+, arXiv17</a>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/GenerativeAdversarialNetwork.html">#GenerativeAdversarialNetwork</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/60">Generative Adversarial Networks: An Overview, Dumoulin+, IEEE-SPM17</a>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/ConceptToText.html">#ConceptToText</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/89">Neural Text Generation from Structured Data with Application to the Biography Domain, Lebret+, Lebret+, EMNLP16</a>
<a class="button" href="articles/BeamSearch.html">#BeamSearch</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/80">Sequence-to-Sequence Learning as Beam-Search Optimization, Wiseman+, EMNLP16</a>
<span class="snippet"><span>Comment</span>seq2seqを学習する際には、gold-history（これまで生成した単語がgoldなものと一緒）を使用し、次に続く単語の尤度を最大化するように学習するが、これには、1. Explosure Bias: test時ではtraining時と違いgold historyを使えないし、trai ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/76">Larger-context language modelling with recurrent neural networks, Wang+, ACL16</a>
<span class="snippet"><span>Comment</span>## 概要通常のNeural Language Modelはsentence間に独立性の仮定を置きモデル化されているが、この独立性を排除し、preceding sentencesに依存するようにモデル化することで、言語モデルのコーパスレベルでのPerplexityが改善したという話。提案した言語 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/73">Distraction-Based Neural Networks for Modeling Documents, Chen+, IJCAI16</a>
<span class="snippet"><span>Comment</span>Neuralなモデルで「文書」の要約を行う研究。提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。distractionを導入するmotivationは、入力文書中の異なる情報を横断Dist ...</span>
<a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/70">Learning Distributed Representations of Sentences from Unlabelled Data, Hill+, NAACL16</a>
<span class="snippet"><span>Comment</span>Sentenceのrepresentationを学習する話代表的なsentenceのrepresentation作成手法(CBOW, SkipGram, SkipThought, Paragraph Vec, NMTなど)をsupervisedな評価（タスク志向+supervised）とun ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/65">Pointing the unknown words, Gulcehre+, ACL16</a>
<span class="snippet"><span>Comment</span>テキストを生成する際に、source textからのコピーを行える機構を導入することで未知語問題に対処した話CopyNetと同じタイミングで（というか同じconferenceで）発表 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Visual Words.html">#Visual Words</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/63">Image Captioning with Semantic Attention, You+, CVPR16.</a>
<span class="snippet"><span>Comment</span>画像そのものだけでなく、モデルへのInputにVisual Wordsを明示的に加えることで、captioningの精度が上がりましたという論文 ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Visual Words.html">#Visual Words</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/62">What Value Do Explicit High Level Concepts Have in Vision to Language Problems?, Wu+, CVPR16.</a>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/61">Generating Visual Explanations, Hendrickks+, ECCV16</a>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/75">LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP15</a>
<span class="snippet"><span>Comment</span>Large Chinese Short Text Summarization (LCSTS) datasetを作成データセットを作成する際は、Weibo上の特定のorganizationの投稿の特徴を利用。Weiboにニュースを投稿する際に、投稿の冒頭にニュースのvery short sCop ...</span>
<a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/74">A hierarchical neural autoencoder for paragraphs and documents, Li+, ACL15</a>
<span class="snippet"><span>Comment</span>複数文を生成(今回はautoencoder)するために、standardなseq2seq LSTM modelを、拡張したという話。要は、paragraph/documentのrepresentationが欲しいのだが、アイデアとしては、word-levelの情報を扱うLSTM layerとtr ...</span>
<a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/SentimentAnalysis.html">#SentimentAnalysis</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/72">Document Modeling with Gated Recurrent Neural Network for Sentiment Classification, Tang+, EMNLP15</a>
<span class="snippet"><span>Comment</span>word level -> sentence level -> document level のrepresentationを求め、documentのsentiment classificationをする話。documentのRepresentationを生成するときに参考になるやも。sen ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/59">Sentence Compression by Deletion with LSTMs, Fillipova+, EMNLP15</a>
<span class="snippet"><span>Comment</span>slide:https://www.slideshare.net/akihikowatanabe3110/sentence-compression-by-deletion-with-lstms ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/88">What to talk about and how? Selective Generation using LSTMs with Coarse-to-Fine Alignment, Mei+, NAACL-HLT’16</a>
<span class="snippet"><span>Comment</span>content-selectionとsurface realizationをencoder-decoder alignerを用いて同時に解いたという話。普通のAttention basedなモデルにRefinerとPre-Selectorと呼ばれる機構を追加。通常のattentionにはatte ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/81">Efficient Methods and Hardware for Deep Learning, Han, Stanford University, 2017</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/77">Teaching Machines to Read and Comprehend, Hermann+, NIPS 2015</a>
<span class="snippet"><span>Comment</span>だいぶ前に読んだので割とうろおぼえ。CNN/DailyMailデータセットの作成を行なった論文（最近Neuralな文”書”要約の学習でよく使われるやつ）。CNN/DailyMailにはニュース記事に対して、人手で作成した要約が付与されており、要約中のEntityを穴埋めにするなどして、 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
