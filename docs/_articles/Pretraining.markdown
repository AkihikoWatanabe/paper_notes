---
layout: post
title: Pretrainingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Pretraining
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/698">DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining, Sang Michael Xie+, N_A, arXiv23</a>
<span class="snippet">本論文では、言語モデルの性能に影響を与える事前学習データのドメインの混合比について、DoReMiという手法を提案する。DoReMiは、小さなプロキシモデルを使用してドメインの重みを生成し、再サンプリングして大きなモデルをトレーニングすることで、効率的にドメインの重みを見つけることができる。実験では ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2c0b125a-5ecc-4ee3-8c3b-022c03606c60" alt="image"><a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/766">Textbooks Are All You Need, Suriya Gunasekar+, N_A, arXiv23</a>
<span class="snippet">本研究では、小規模なphi-1という新しいコード用大規模言語モデルを紹介し、8つのA100で4日間トレーニングした結果、HumanEvalでpass@1の正解率50.6％、MBPPで55.5％を達成したことを報告しています。また、phi-1は、phi-1-baseやphi-1-smallと比較して ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9f0b945a-f965-42ae-b5d8-ac464359af35" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><br><span class="issue_date">Issue Date: 2023-06-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/768">Unifying Large Language Models and Knowledge Graphs: A Roadmap, Shirui Pan+, N_A, arXiv23</a>
<span class="snippet">LLMsとKGsを統合することで、自然言語処理や人工知能の分野で注目を集めている。KGsは豊富な事実知識を明示的に格納しているが、構築が困難であり、進化する性質を持っている。一方、LLMsはブラックボックスモデルであり、事実知識を捉えたりアクセスしたりすることができない。本記事では、LLMsとKG ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/c008d409-e5db-4140-a82c-a658a4847780" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/805">EgoVLPv2: Egocentric Video-Language Pre-training with Fusion in the  Backbone, Shraman Pramanick+, N_A, arXiv23</a>
<span class="snippet">エゴセントリックビデオ言語の事前学習の第2世代（EgoVLPv2）は、ビデオと言語のバックボーンにクロスモーダルの融合を直接組み込むことができる。EgoVLPv2は強力なビデオテキスト表現を学習し、柔軟かつ効率的な方法でさまざまなダウンストリームタスクをサポートする。さらに、提案されたバックボーン ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/806">Generative Pretraining in Multimodality, Quan Sun+, N_A, arXiv23</a>
<span class="snippet">Emuは、マルチモーダルなコンテキストで画像とテキストを生成するためのTransformerベースのモデルです。このモデルは、単一モダリティまたはマルチモーダルなデータ入力を受け入れることができます。Emuは、マルチモーダルなシーケンスでトレーニングされ、画像からテキストへのタスクやテキストから画 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/857">Pre-Training to Learn in Context, ACL23</a>
<span class="snippet">インコンテキスト学習は、タスクの例と文脈からタスクを実行する方法であり、注目されています。しかし、現在の方法では十分に活用されていないため、私たちはPICLというフレームワークを提案します。これは、一般的なテキストコーパスでモデルを事前学習し、文脈に基づいてタスクを推論して実行する能力を向上させま ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1072">Think before you speak: Training Language Models With Pause Tokens, Sachin Goyal+, N_A, arXiv23</a>
<span class="snippet">言語モデルのトレーニングと推論において、遅延を導入することでモデルの性能を向上させる手法を提案しました。具体的には、入力に特定のトークンを追加し、そのトークンが現れるまでモデルの出力を遅らせることで、追加の計算を行うことができます。実験結果では、この手法が推論タスクにおいて有益であり、特にQAタス ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/500">Revisiting Pretraining Objectives for Tabular Deep Learning, Rubachev+, Yandex+, arXiv22</a>
<span class="snippet">Tabular Dataを利用した場合にKaggleなどでDeepなモデルがGBDT等に勝てないことが知られているが、GBDT等とcomparable になる性能になるようなpre-trainingを提案したよ、的な内容っぽい ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Self-SupervisedLearning.html">#Self-SupervisedLearning</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/874">RankMe: Assessing the downstream performance of pretrained  self-supervised representations by their rank, Quentin Garrido+, N_A, arXiv22</a>
<span class="snippet">共有埋め込み自己教示学習（JE-SSL）は、成功の視覚的な手がかりが欠如しているため、展開が困難である。本研究では、JE-SSL表現の品質を評価するための非教示基準であるRankMeを開発した。RankMeはラベルを必要とせず、ハイパーパラメータの調整も不要である。徹底的な実験により、RankMe ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Unsupervised.html">#Unsupervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/83">Unsupervised Pretraining for Sequence to Sequence Learning, Ramachandran+, EMNLP17</a>
<span class="snippet">seq2seqにおいてweightのpretrainingを行う手法を提案seq2seqでは訓練データが小さいとoverfittingしやすいという弱点があるので、大規模なデータでunsupervisedにpretrainingし、その後目的のデータでfinetuneすることで精度を向上させまし ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2022-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/495">A Paper List for Recommend-system PreTrained Models</a>
<span class="snippet">No description ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
