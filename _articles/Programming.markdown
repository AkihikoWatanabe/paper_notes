---
layout: post
title: Programmingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Programming
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/868">Socratic Questioning of Novice Debuggers: A Benchmark Dataset and Preliminary Evaluations, ACL-BEA23</a>
<span class="snippet"><span>Summary</span>本研究では、初心者プログラマがバグのある計算問題を解決する際に、ソクラテス的な対話を行うデータセットを紹介し、GPTベースの言語モデルのデバッグ能力を評価しました。GPT-4はGPT-3.5よりも優れたパフォーマンスを示しましたが、まだ人間の専門家には及ばず、さらなる研究が必要です。</span>
<a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/686">Evidence of Meaning in Language Models Trained on Programs, Charles Jin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、プログラムのコーパスを用いて言語モデルが意味を学習できることを示し、プログラム合成が言語モデルの意味の存在を特徴づけるための中間テストベッドとして適していることを述べている。Transformerモデルを用いた実験により、言語の意味を学習するための帰納バイアスを提供しないにもかかわらず、線形プローブがモデルの状態から現在および将来のプログラム状態の抽象化を抽出できることがわかった。また、正しいプログラムを生成することを学習し、平均的に訓練セットよりも短いプログラムを生成することも示した。本論文は、言語モデルの訓練に新しい技術を提案するものではなく、(形式的な)意味の習得と表現に関する実験的なフレームワークを開発し、洞察を提供する。</span>
<span class="snippet"><span>Comment</span>プログラムのコーパスでLLMをNext Token Predictionで訓練し厳密に正解とsemanticsを定義した上で、訓練データと異なるsemanticsの異なるプログラムを生成できることを示した。LLMが意味を理解していることを暗示している ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fa4d2c68-bdbe-40ae-990d-10814ac8a204" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/661">StarCoderBase_StarCoder, 2023</a>
<span class="snippet"><span>Comment</span>・15.5Bパラメータ・80種類以上のプログラミング言語で訓練・Multi Query Attentionを利用・context window size 8192・Fill in the middle objectiveを利用Instruction tuningがされておらず、prefipaper: ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/GenerativeAI.html">#GenerativeAI</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-01-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/506">CodeGPT: The VSCode Extension with ChatGPT-Like Functionalities</a>
<span class="snippet"><span>Comment</span>VSCodeの拡張で、//から始まるPromptをエディタ上で記載することで対応するコードをGPT3が生成してくれる模様。便利そう ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
