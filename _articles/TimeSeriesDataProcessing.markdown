---
layout: post
title: TimeSeriesDataProcessingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## TimeSeriesDataProcessing
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/118">Derivative Delay Embedding: Online Modeling of Streaming Time Series, Zhifei Zhang+, N_A, arXiv16</a>
<span class="snippet"><span>Summary</span>本研究では、オンラインでストリーミング時系列データを効率的にモデリングするためのDDE-MGM手法を提案しています。DDEは、再帰的なパターンを保持する埋め込み空間に時系列を変換するために使用され、MGMはパターンのモデリングと分類に使用されます。実験結果は、提案手法の効果と優れた分類精度を示しています。</span>
<span class="snippet"><span>Comment</span>スライド：https://www.slideshare.net/akihikowatanabe3110/brief-survey-of-datatotext-systems![image](https://user-images.githubusercontent.com/12249301/3446 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Financial.html">#Financial</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/117">Recurrent neural network and a hybrid model for prediction of stock returns, Akhter+, Expert Systems with Applications14</a>
<span class="snippet"><span>Comment</span>Stock returnのpredictionタスクに対してNNを適用。AR-MRNNモデルをRNNに適用、高い性能を示している。 moving referenceをsubtractした値をinput-outputに用いることで、normalizationやdetrending等の前処理が不 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Financial.html">#Financial</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/116">Prediction-based portfolio optimization model using neural networks, Freitas+, Neurocomputing09</a>
<span class="snippet"><span>Comment</span>Stock returnのpredictionタスクに対してNNを適用。NNのinput-outputとして、生のreturn値を用いるのではなく、ある時刻におけるreturnをsubtractした値(moving reference)を用いる、AR-MRNNモデルを提案。 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2022-12-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/504">Are Transformers Effective for Time Series Forecasting?</a>
<span class="snippet"><span>Comment</span>Linear Layerに基づくシンプルな手法がTransformerベースの手法に時系列予測で勝ったという話 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/115">Artificial neural networks in business: Two decades of research, Tkac+, Applied Soft Computing 2016</a>
<span class="snippet"><span>Comment</span>ビジネスドメイン(e.g. Stock market price prediction)におけるニューラルネットワークの活用事例をまとめたSurvey。時系列データの取り扱いなどの参考になるかも。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
