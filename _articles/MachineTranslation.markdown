---
layout: post
title: MachineTranslationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## MachineTranslation
<div class="visible-content">
<a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/AudioProcessing.html">#AudioProcessing</a><a class="button" href="articles/Speech.html">#Speech</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/842">Simple and Effective Unsupervised Speech Translation, ACL23</a>
<span class="snippet">音声翻訳のためのラベル付きデータが限られているため、非教師あり手法を使用して音声翻訳システムを構築する方法を研究している。パイプラインアプローチや擬似ラベル生成を使用し、非教師ありドメイン適応技術を提案している。実験の結果、従来の手法を上回る性能を示している。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/LM-based.html">#LM-based</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/967">DiscoScore: Evaluating Text Generation with BERT and Discourse Coherence, Wei Zhao+, N_A, EACL23</a>
<span class="snippet">本研究では、文章の一貫性を評価するための新しい指標であるDiscoScoreを紹介します。DiscoScoreはCentering理論に基づいており、BERTを使用して談話の一貫性をモデル化します。実験の結果、DiscoScoreは他の指標よりも人間の評価との相関が高く、システムレベルでの評価でも ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/375">Probing Word Translations in the Transformer and Trading Decoder for Encoder Layers, ACL‘21</a>
<span class="snippet">Transformerに基づいたNMTにおいて、Encoderが入力を解釈し、Decoderが翻訳をしている、という通説を否定し、エンコーディング段階、さらにはinput embeddingの段階でそもそも翻訳が始まっていることを指摘。エンコーディングの段階ですでに翻訳が始まっているのであれば、エ ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/379">Improving Neural Machine Translation with Compact Word Embedding Tables, Kumar+, 2021</a>
<span class="snippet">NMTにおいてword embeddingがどう影響しているかなどを調査しているらしい ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/493">Leveraging Pre-trained Checkpoints for Sequence Generation Tasks, Rothe+, Google Research, TACL20</a>
<span class="snippet"># 概要BERT-to-BERT論文。これまでpre-trainedなチェックポイントを利用する研究は主にNLUで行われてきており、Seq2Seqでは行われてきていなかったので、やりました、という話。publicly availableなBERTのcheckpointを利用し、BERTをen ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/TrainedMetrics.html">#TrainedMetrics</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/954">Machine Translation Evaluation with BERT Regressor, Hiroki Shimanaka+, N_A, arXiv19</a>
<span class="snippet">私たちは、BERTを使用した自動的な機械翻訳の評価メトリックを紹介します。実験結果は、私たちのメトリックがすべての英語対応言語ペアで最先端のパフォーマンスを達成していることを示しています。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/64">Neural Machine Translation with Source-Side Latent Graph Parsing, Hashimoto+, arXiv17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/66">Sequence-to-Dependency Neural Machine Translation, Wu+, ACL17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/67">What do Neural Machine Translation Models Learn about Morphology?, Belinkov+, ACL17</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/234">ゼロから始める ニューラルネットワーク機械翻訳, 中澤敏明, NLP17</a>
<span class="snippet">中澤さんによるNMTチュートリアル。 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/245">Attention is all you need, Vaswani+, arXiv17</a>
<span class="snippet">集合知 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/65">Pointing the unknown words, Gulcehre+, ACL16</a>
<span class="snippet">CopyNetと同じタイミングで（というか同じconferenceで）発表 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/971">Lexical Coherence Graph Modeling Using Word Embeddings, Mesgar+, NAACL16</a>
<span class="snippet">__translate: Coherence is established by semantic connections between sentences of a text which can be modeled by lexical relations. In this paper, we ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/369">Effective Approaches to Attention-based Neural Machine Translation, Luong+, arXiv15</a>
<span class="snippet">また、過去のalignmentの情報を考慮した上でデコーディングしていくために、input-feeding approachも提案![image](https://user-images.githubusercontent.com/12249301/120877145-cfdaa300-c5ef ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/969">Document-Level Machine Translation Evaluation with Gist Consistency and Text Cohesion, Gong+, DiscoMT15</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Reference-based.html">#Reference-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/985">chrF: character n-gram F-score for automatic MT evaluation, Mono Popovic, WMT15</a>
<span class="snippet">私たちは、機械翻訳の評価に文字n-gram Fスコアを使用することを提案します。私たちは、このメトリックがシステムレベルとセグメントレベルで人間のランキングと相関しており、特にセグメントレベルでの相関が非常に高いことを報告しました。この提案は非常に有望であり、WMT14の共有評価タスクでも最高のメ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/237">The Mathematics of Statistical Machine Translation: Parameter Estimation, Brown+, CL13</a>
<span class="snippet">IBMモデル論文。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/970">Graph-based Local Coherence Modeling, Guinaudeau+, ACL13</a>
<span class="snippet">私たちは、グラフベースのアプローチを提案し、文の順序付け、要約の結束性評価、読みやすさの評価の3つのタスクでシステムを評価しました。このアプローチは、エンティティグリッドベースのアプローチと同等の性能を持ち、計算コストの高いトレーニングフェーズやデータのまばらさの問題にも対処できます。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Coherence.html">#Coherence</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/968">Extending Machine Translation Evaluation Metrics with Lexical Cohesion to Document Level, Wong+, EMNLP12</a>
<span class="snippet">この論文では、語彙的な結束を利用して文書レベルの機械翻訳の評価を容易にする方法を提案しています。語彙的な結束は、同じ意味を持つ単語を使って文を結びつけることで、テキストの結束性を実現します。実験結果は、この特徴を評価尺度に組み込むことで、人間の判断との相関を向上させることを示しています。 ...</span>
<a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2021-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/393">機械翻訳自動評価指標の比較, 今村+, NLP04</a>
<span class="snippet">実際に研究等でBLEUスコアを測りたい場合は、mosesの実装を使うのが間違いない:https://github.com/moses-smt/mosesdecoder/blob/master/scripts/generic/multi-bleu.perl ...</span>
<a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/239">A systematic comparison of various statistical alignment models, Och+, CL03, Giza++</a>
<span class="snippet">評価の際は、Sure, Possibleの二種類のラベルによる単語アライメントのground-truth作成も行っている ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/238"> HMM-based word alignment in statistical translation, Vogel+, COLING96</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/236">ALAGIN 機械翻訳セミナー 単語アライメント, Graham Neubig</a>
<span class="snippet">Neubigさんによる単語アライメントチュートリアル ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/669">METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments, Banerjee+, CMU, ACL Workshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation and_or Summarization</a>
<span class="snippet"># イントロMTの評価はBLEUが提案されてから過去2年間で注目されている。BLEUはNIST metricと関連しており、研究で利用されてきた。自動評価は素早く、より簡便に、human evaluationよりも安価に評価をすることができる。また、自動評価は他のシステムとの比較だけでなく、on ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b3aaf2f6-ebfc-4561-9b5e-c14a1c10a983" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
