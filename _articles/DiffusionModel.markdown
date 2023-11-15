---
layout: post
title: DiffusionModelに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## DiffusionModel
<div class="visible-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/878">FABRIC: Personalizing Diffusion Models with Iterative Feedback, Dimitri von Rütte+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、拡散ベースのテキストから画像への変換モデルに人間のフィードバックを組み込む戦略を提案する。自己注意層を利用したトレーニングフリーなアプローチであるFABRICを提案し、さまざまな拡散モデルに適用可能であることを示す。また、包括的な評価方法を導入し、人間のフィードバックを統合した生成ビジュアルモデルのパフォーマンスを定量化するための堅牢なメカニズムを提供する。徹底的な分析により、反復的なフィードバックの複数のラウンドを通じて生成結果が改善されることを示す。これにより、個別化されたコンテンツ作成やカスタマイズなどの領域に応用が可能となる。</span>
<span class="snippet"><span>Comment</span>upvote downvoteをフィードバックし、iterativeなmannerでDiffusionモデルの生成結果を改善できる手法。多くのDiffusion based Modelに対して適用可能デモ: https://huggingface.co/spaces/dvruette/fabric ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/TextToImage.html">#TextToImage</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/831">Learning to Imagine: Visually-Augmented Natural Language Generation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、視覚情報を活用した自然言語生成のためのLIVEという手法を提案しています。LIVEは、事前学習済み言語モデルを使用して、テキストに基づいて場面を想像し、高品質な画像を合成する方法です。また、CLIPを使用してテキストの想像力を評価し、段落ごとに画像を生成します。さまざまな実験により、LIVEの有効性が示されています。コード、モデル、データは公開されています。</span>
<span class="snippet"><span>Comment</span>>まず、テキストに基づいて場面を想像します。入力テキストに基づいて高品質な画像を合成するために拡散モデルを使用します。次に、CLIPを使用して、テキストが想像力を喚起できるかを事後的に判断します。最後に、私たちの想像力は動的であり、段落全体に1つの画像を生成するのではなく、各文に対して合成を行います ...</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><a class="button" href="articles/TextToImage.html">#TextToImage</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/741">ViCo: Detail-Preserving Visual Condition for Personalized Text-to-Image  Generation, Shaozhe Hao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>拡散モデルを用いたパーソナライズされた画像生成において、高速で軽量なプラグインメソッドであるViCoを提案。注目モジュールを導入し、注目ベースのオブジェクトマスクを使用することで、一般的な過学習の劣化を軽減。元の拡散モデルのパラメータを微調整せず、軽量なパラメータトレーニングだけで、最新のモデルと同等またはそれ以上の性能を発揮することができる。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/ImageCaptioning.html">#ImageCaptioning</a><br><span class="issue_date">Issue Date: 2023-11-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1114">Zero-shot Learning網羅的サーベイ: CLIPが切り開いたVision & Languageの新しい世界</a>
<span class="snippet"><span>Comment</span>これはすごいまとめ…。まだ途中までしか読めていない。CLIPからスタートしてCLIPを引用している論文から重要なものを概要付きでまとめている。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1107">StableDiffusion, LLMのGPUメモリ削減のあれこれ</a>
<span class="snippet"><span>Comment</span>Gradient Accumulation, Gradient Checkpointingの説明が丁寧でわかりやすかった。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
