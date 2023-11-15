---
layout: post
title: TextToImageに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## TextToImage
<div class="visible-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/TabularData.html">#TabularData</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/835">Table and Image Generation for Investigating Knowledge of Entities in Pre-trained Vision and Language Models, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、Vision＆Language（V＆L）モデルにおけるエンティティの知識の保持方法を検証するために、テーブルと画像の生成タスクを提案します。このタスクでは、エンティティと関連する画像の知識を含むテーブルを生成する第一の部分と、キャプションとエンティティの関連知識を含むテーブルから画像を生成する第二の部分があります。提案されたタスクを実行するために、Wikipediaの約20万のinfoboxからWikiTIGデータセットを作成しました。最先端のV＆LモデルOFAを使用して、提案されたタスクのパフォーマンスを評価しました。実験結果は、OFAが一部のエンティティ知識を忘れることを示しています。</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/DiffusionModel.html">#DiffusionModel</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/831">Learning to Imagine: Visually-Augmented Natural Language Generation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、視覚情報を活用した自然言語生成のためのLIVEという手法を提案しています。LIVEは、事前学習済み言語モデルを使用して、テキストに基づいて場面を想像し、高品質な画像を合成する方法です。また、CLIPを使用してテキストの想像力を評価し、段落ごとに画像を生成します。さまざまな実験により、LIVEの有効性が示されています。コード、モデル、データは公開されています。</span>
<span class="snippet"><span>Comment</span>>まず、テキストに基づいて場面を想像します。入力テキストに基づいて高品質な画像を合成するために拡散モデルを使用します。次に、CLIPを使用して、テキストが想像力を喚起できるかを事後的に判断します。最後に、私たちの想像力は動的であり、段落全体に1つの画像を生成するのではなく、各文に対して合成を行います ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/DiffusionModel.html">#DiffusionModel</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/741">ViCo: Detail-Preserving Visual Condition for Personalized Text-to-Image  Generation, Shaozhe Hao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>拡散モデルを用いたパーソナライズされた画像生成において、高速で軽量なプラグインメソッドであるViCoを提案。注目モジュールを導入し、注目ベースのオブジェクトマスクを使用することで、一般的な過学習の劣化を軽減。元の拡散モデルのパラメータを微調整せず、軽量なパラメータトレーニングだけで、最新のモデルと同等またはそれ以上の性能を発揮することができる。</span>
</div>
