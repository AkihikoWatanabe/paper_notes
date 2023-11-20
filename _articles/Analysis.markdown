---
layout: post
title: Analysisに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Analysis
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1120">Do LLMs exhibit human-like response biases? A case study in survey  design, Lindia Tjuatja+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLMsを使用して人間の代理としてタスクを実行する際に、LLMsが人間の応答バイアスをどの程度反映するかを調査する必要がある。この研究では、調査設計を使用して人間の応答バイアスを評価するデータセットとフレームワークを設計し、9つのモデルを評価した結果、一般的なLLMsが人間のような振る舞いを反映することに失敗していることが示された。これらの結果は、LLMsを人間の代わりに使用する際の潜在的な落とし穴を強調し、モデルの振る舞いの細かい特性の重要性を強調している。</span>
<span class="snippet"><span>Comment</span>LLMはPromptにsensitiveだが、人間も質問の仕方によって応答が変わるから、sensitiveなのは一緒では？ということを調査した研究。Neubigさんのツイートだと、instruction tuningやRLHFをしていないBase LLMの方が、より人間と類似した回答をするのだそう。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/de129e78-5d52-41e3-a3bb-9aec20cf2b05" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><br><span class="issue_date">Issue Date: 2023-11-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1117">Pretraining Data Mixtures Enable Narrow Model Selection Capabilities in  Transformer Models, Steve Yadlowsky+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、トランスフォーマーモデルの文脈学習（ICL）能力を調査しました。トランスフォーマーモデルは、事前学習データの範囲内で異なるタスクを特定し、学習する能力を持っています。しかし、事前学習データの範囲外のタスクや関数に対しては一般化が劣化することが示されました。また、高容量のシーケンスモデルのICL能力は、事前学習データの範囲に密接に関連していることが強調されました。</span>
<span class="snippet"><span>Comment</span>Transformerがpre-training時に利用された学習データ以外の分布に対しては汎化性能が落ちることを示したらしい。もしこれが正しいとすると、結局真に新しい分布というか関数というかタスクというか、をTransformerが創出する可能性は低いと言えるかもしれない。が、新しいものって大体は ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/In-ContextLearning.html">#In-ContextLearning</a><br><span class="issue_date">Issue Date: 2023-09-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1029">CausalLM is not optimal for in-context learning, Nan Ding+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>最近の研究では、トランスフォーマーベースのインコンテキスト学習において、プレフィックス言語モデル（prefixLM）が因果言語モデル（causalLM）よりも優れたパフォーマンスを示すことがわかっています。本研究では、理論的なアプローチを用いて、prefixLMとcausalLMの収束挙動を分析しました。その結果、prefixLMは線形回帰の最適解に収束する一方、causalLMの収束ダイナミクスはオンライン勾配降下アルゴリズムに従い、最適であるとは限らないことがわかりました。さらに、合成実験と実際のタスクにおいても、causalLMがprefixLMよりも性能が劣ることが確認されました。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> In-Context Learningで文脈中サンプルの学習が仮想的に行われるが、CausalLM（各トークンは自分より前のみ注意対象）はオンライン学習の解に対応するがステップ幅が減衰しないため最適解に収束せず、PrefixLM（文脈中トークンは全て注意対C ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/832">Do Models Really Learn to Follow Instructions? An Empirical Study of Instruction Tuning, ACL23</a>
<span class="snippet"><span>Summary</span>最近のinstruction tuning（IT）の研究では、追加のコンテキストを提供してモデルをファインチューニングすることで、ゼロショットの汎化性能を持つ素晴らしいパフォーマンスが実現されている。しかし、IT中にモデルがどのように指示を利用しているかはまだ研究されていない。本研究では、モデルのトレーニングを変更された指示と元の指示との比較によって、モデルがIT中に指示をどのように利用するかを分析する。実験の結果、トレーニングされたモデルは元の指示と同等のパフォーマンスを達成し、ITと同様のパフォーマンスを達成することが示された。この研究は、より信頼性の高いIT手法と評価の緊急性を強調している。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/695">Evidence of Meaning in Language Models Trained on Programs, Charles Jin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、プログラムのコーパスを用いて言語モデルが意味を学習できることを示し、プログラム合成が言語モデルの意味の存在を特徴づけるための中間テストベッドとして適していることを述べている。Transformerモデルを用いた実験により、言語の意味を学習するための帰納バイアスを提供しないにもかかわらず、線形プローブがモデルの状態から現在および将来のプログラム状態の抽象化を抽出できることがわかった。さらに、プローブの精度と、モデルが仕様を実装するプログラムを生成する能力との間には、強い統計的有意な相関があることが示された。本研究は、言語モデルの訓練に新しい技術を提案するものではなく、(形式的な)意味の習得と表現に関する実験的なフレームワークを開発し、洞察を提供するものである。</span>
<span class="snippet"><span>Comment</span>下記岡野原さんのツイートより引用。いつもありがとうございます。>言語モデル（LM）が意味を理解しているのかを調べるため、プログラムに対するLMを構築し、LMの内部状態からプログラムの意味を推定する実験をした結果、単語予測精度と意味推定精度の改善ペースがほぼ一致し、またLMが将来に何を生成するかを ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9db7d5b5-0380-41ab-8570-a0ae873db9ef" alt="image"><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Word.html">#Word</a><br><span class="issue_date">Issue Date: 2017-12-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/79">Skip-Gram – Zipf + Uniform = Vector Additivity, Gittens+, ACL17</a>
<span class="snippet"><span>Comment</span>解説スライド：http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/09.pdfEmbeddingの加法構成性（e.g. man+royal=king）を理論的に理由づけ（解説スライドより） ...</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/6">Aspect-Based Personalized Text Summarization, Berkovsky+（Tim先生のグループ）, AH2008, 31</a>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/34401031-b72623e0-ebda-11e7-9da2-6ce16b630f47.png)Aspect-basedなPDSに関して調査した研究。たとえば、Wi ...</span>
<a class="button" href="articles/Comments.html">#Comments</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/230">Leave a Reply: An Analysis of Weblog Comments, Mishne+, WWW06</a>
<span class="snippet"><span>Comment</span>従来のWeblog研究では、コメントの情報が無視されていたが、コメントも重要な情報を含んでいると考えられる。この研究では、以下のことが言及されている。* （収集したデータの）ブログにコメントが付与されている割合やコメントの長さ、ポストに対するコメントの平均などの統計量* ブログ検索に相当流し ...</span>
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Others.html">#Others</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/183">Usage patterns of collaborative tagging systems, Golder+, Journal of Information Science06</a>
<span class="snippet"><span>Comment</span>Social Tagging Systemの仕組みや使われ方について言及する際にreferすると良いかも。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1108">大規模言語モデルにおいて､「知識は全結合層に蓄積される」という仮説についての文献調査</a>
<span class="snippet"><span>Comment</span>タイトルの通り、知識がFFNに蓄積されていると主張しているらしい原論文を読み解いている。まとめを引用すると> 「知識は全結合層に蓄積される」という表現は､ややラジカルで､少なくともこの論文では「全結合層は知識獲得において重要」という程度の､もう少しマイルドな主張をしているように見受けられまし ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
