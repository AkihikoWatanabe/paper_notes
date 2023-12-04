---
layout: post
title: TabularDataに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## TabularData
<div class="visible-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/TextToImage.html">#TextToImage</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/835">Table and Image Generation for Investigating Knowledge of Entities in Pre-trained Vision and Language Models, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、Vision＆Language（V＆L）モデルにおけるエンティティの知識の保持方法を検証するために、テーブルと画像の生成タスクを提案します。このタスクでは、エンティティと関連する画像の知識を含むテーブルを生成する第一の部分と、キャプションとエンティティの関連知識を含むテーブルから画像を生成する第二の部分があります。提案されたタスクを実行するために、Wikipediaの約20万のinfoboxからWikiTIGデータセットを作成しました。最先端のV＆LモデルOFAを使用して、提案されたタスクのパフォーマンスを評価しました。実験結果は、OFAが一部のエンティティ知識を忘れることを示しています。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/697">StructGPT: A General Framework for Large Language Model to Reason over  Structured Data, Jinhao Jiang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、大規模言語モデル（LLMs）を使用して構造化データ上のゼロショット推論能力を改善する方法について研究し、Iterative Reading-then-Reasoning（IRR）アプローチを提案しました。このアプローチでは、構造化データから関連するエビデンスを収集する専門的な関数を構築し、LLMsに収集された情報に基づいて推論タスクに集中させます。外部インターフェースの支援を受けて、LLMsが構造化データ上で推論するためのinvoking-linearization-generation手順を提案し、与えられたクエリに対する目標回答に徐々に近づくことができます。徹底的な実験により、アプローチの有効性を示し、フルデータの教師ありチューニングベースラインと同等のパフォーマンスを達成することができます。コードとデータは、\url{https://github.com/RUCAIBox/StructGPT}で公開されています。</span>
<span class="snippet"><span>Comment</span>構造化データに対するLLMのゼロショットのreasoning能力を改善。構造化データに対するQAタスクで手法が有効なことを示した。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/ac9732f1-a9c9-4620-8bf8-053415a5e654" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/580">Large Language Models are Versatile Decomposers: Decompose Evidence and Questions for Table-based Reasoning, Ye+, University of Science and Technology of China, SIGIR23</a>
<span class="snippet"><span>Comment</span>テーブルとquestionが与えられた時に、questionをsub-questionとsmall tableにLLMでin-context learningすることで分割。subquestionの解を得るためのsqlを作成しスポットを埋め、hallucinationを防ぐ。最終的にLLM Reas ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/574">Why do tree-based models still outperform deep learning on typical tabular data?, Grinsztajn+, Soda, Inria Saclay , arXiv22</a>
<span class="snippet"><span>Comment</span>tree basedなモデルがテーブルデータに対してニューラルモデルよりも優れた性能を発揮することを確認し、なぜこのようなことが起きるかいくつかの理由を説明した論文。![image](https://user-images.githubusercontent.com/12249301/235 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1167">Table Transformer Demo</a>
<span class="snippet"><span>Comment</span>PDF中のテーブルとその構造（行列セル）をdetectするモデルExampleは以下のような感じ（日本語だとどれくらいできるのかな...） ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/7f62e16b-1ff8-46ad-b6df-7792981f8f58" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
