---
layout: post
title: Zero/Few-shotに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Zero/Few-shot
<div class="visible-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/MultitaskLearning.html">#MultitaskLearning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/863">Few-Shot Data-to-Text Generation via Unified Representation and Multi-Source Learning, ACL23</a>
<span class="snippet"><span>Summary</span>この論文では、構造化データからテキストを生成する新しいアプローチを提案しています。提案手法は、さまざまな形式のデータを処理できる統一された表現を提供し、マルチタスクトレーニングやゼロショット学習などのシナリオでのパフォーマンスを向上させることを目指しています。実験結果は、提案手法が他の方法と比較して優れた性能を示していることを示しています。これは、データからテキスト生成フレームワークにおける重要な進歩です。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/827">Dataset Distillation with Attention Labels for Fine-tuning BERT, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、データセットの蒸留を使用して、元のデータセットのパフォーマンスを保持しながら、ニューラルネットワークを迅速にトレーニングするための小さなデータセットを作成する方法に焦点を当てています。具体的には、事前学習済みのトランスフォーマーを微調整するための自然言語処理タスクの蒸留されたfew-shotデータセットの構築を提案しています。実験結果では、注意ラベルを使用してfew-shotデータセットを作成し、BERTの微調整において印象的なパフォーマンスを実現できることを示しました。例えば、ニュース分類タスクでは、わずか1つのサンプルとわずか1つの勾配ステップのみで、元のデータセットの98.5％のパフォーマンスを達成しました。</span>
<span class="snippet"><span>Comment</span>Datadistillationしたら、データセットのうち1サンプルのみで、元のデータセットの98.5%の性能を発揮できたという驚異的な研究（まえかわ君） ...</span>
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/817">FiD-ICL: A Fusion-in-Decoder Approach for Efficient In-Context Learning, ACL23</a>
<span class="snippet"><span>Summary</span>大規模な事前学習モデルを使用したfew-shot in-context learning（ICL）において、fusion-in-decoder（FiD）モデルを適用することで効率とパフォーマンスを向上させることができることを検証する。FiD-ICLは他のフュージョン手法と比較して優れたパフォーマンスを示し、推論時間も10倍速くなる。また、FiD-ICLは大規模なメタトレーニングモデルのスケーリングも可能にする。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/816">Z-Code++: A Pre-trained Language Model Optimized for Abstractive Summarization, ACL23</a>
<span class="snippet"><span>Summary</span>この論文では、新しい事前学習言語モデルであるZ-Code++を提案し、抽象的なテキスト要約に最適化されています。Z-Code++は、2つのフェーズの事前学習とディセントラル化アテンション層、およびエンコーダー内のフュージョンを使用しています。このモデルは、低リソースの要約タスクで最先端の性能を発揮し、パラメータ効率的であり、他の競合モデルを大幅に上回ります。</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/ImageSegmentation.html">#ImageSegmentation</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/535">Track Anything: Segment Anything Meets Videos, yang+, SUSTech VIP Lab, arXiv23</a>
<span class="snippet"><span>Comment</span>MetaのSAMを、videoに適用し、videow内のsegmentationを追加学習なしでやりました、という話だと思われる。 ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1124">Recommendation as Language Processing （RLP）: A Unified Pretrain,  Personalized Prompt & Predict Paradigm （P5）, Shijie Geng+, N_A, RecSys22</a>
<span class="snippet"><span>Summary</span>我々は「Pretrain, Personalized Prompt, and Predict Paradigm」（P5）と呼ばれる柔軟で統一されたテキストからテキストへのパラダイムを提案します。P5は、共有フレームワーク内でさまざまな推薦タスクを統一し、個別化と推薦のための深い意味を捉えることができます。P5は、異なるタスクを学習するための同じ言語モデリング目標を持つ事前学習を行います。P5は、浅いモデルから深いモデルへと進化し、広範な微調整の必要性を減らすことができます。P5の効果を実証するために、いくつかの推薦ベンチマークで実験を行いました。</span>
<span class="snippet"><span>Comment</span># 概要T5 のように、様々な推薦タスクを、「Prompt + Prediction」のpipelineとして定義して解けるようにした研究。P5ではencoder-decoder frameworkを採用しており、encoder側ではbidirectionalなモデルでpromptのre ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9b8b83a2-0930-4836-8bae-a18234fd3fd3" alt="image"><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/551">Chain of thought prompting elicits reasoning in large language models, Wei+, Google Research, arXiv22</a>
<span class="snippet"><span>Comment</span>Chain-of-Thoughtを提案した論文。CoTをする上でパラメータ数が100B未満のモデルではあまり効果が発揮されないということは念頭に置いた方が良さそう。![image](https://user-images.githubusercontent.com/12249301/234739先 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/494">Few-Shot NLG with Pre-Trained Language Model, Chen+, University of California, ACL20</a>
<span class="snippet"><span>Comment</span># 概要Neural basedなend-to-endなNLGアプローチはdata-hungryなので、Few Shotな設定で高い性能ができる手法を提案（Few shot NLG）Table-to-Textタスク（WikiBIOデータ, 追加で収集したBook, SongドメインのWiki ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/552">Language Models are Few-Shot Learners</a>
<span class="snippet"><span>Comment</span>In-Context Learningを提案した論文 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
