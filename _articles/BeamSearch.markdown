---
layout: post
title: BeamSearchに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## BeamSearch
<div class="visible-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/998">Momentum Calibration for Text Generation, Xingxing Zhang+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>本研究では、テキスト生成タスクにおいてMoCa（Momentum Calibration）という手法を提案しています。MoCaは、ビームサーチを用いた遅く進化するサンプルを動的に生成し、これらのサンプルのモデルスコアを実際の品質に合わせるように学習します。実験結果は、MoCaが強力な事前学習済みTransformerを改善し、最先端の結果を達成していることを示しています。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/997">BRIO: Bringing Order to Abstractive Summarization, Yixin Liu+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>従来の抽象的要約モデルでは、最尤推定を使用して訓練されていましたが、この方法では複数の候補要約を比較する際に性能が低下する可能性があります。そこで、非確定論的な分布を仮定し、候補要約の品質に応じて確率を割り当てる新しい訓練パラダイムを提案しました。この手法により、CNN/DailyMailとXSumのデータセットで最高の結果を達成しました。さらに、モデルが候補要約の品質とより相関のある確率を推定できることも示されました。</span>
<span class="snippet"><span>Comment</span>ビーム内のトップがROUGEを最大化しているとは限らなかったため、ROUGEが最大となるような要約を選択するようにしたら性能爆上げしましたという研究。実質現在のSoTA ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/80">Sequence-to-Sequence Learning as Beam-Search Optimization, Wiseman+, EMNLP16</a>
<span class="snippet"><span>Comment</span>seq2seqを学習する際には、gold-history（これまで生成した単語がgoldなものと一緒）を使用し、次に続く単語の尤度を最大化するように学習するが、これには、1. Explosure Bias: test時ではtraining時と違いgold historyを使えないし、trai ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><br><span class="issue_date">Issue Date: 2021-06-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/392">beam search解説 _ コード付き</a>
<span class="snippet"><span>Comment</span>ビームサーチについて、コード付きで説明してくれており、大変わかりやすい。heapqを使って実装している。また、ビームサーチをbatchに対して行う方法についても書いてある（ただ、一部に対してしかbatchでの処理は適用できていない）。自分もバッチに対して効率的にビームサーチするにはどのように ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
