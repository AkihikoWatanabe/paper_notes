---
layout: post
title: PromptTuningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## PromptTuning
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1066">Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution, Chrisantha Fernando+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、Promptbreederという自己参照的な自己改善メカニズムを提案し、大規模言語モデル（LLM）の推論能力を向上させるための汎用的なプロンプト戦略を進化させる方法を示しています。Promptbreederは、LLMが自己参照的な方法で進化する変異プロンプトによって制御され、タスクプロンプトの集団を変異させて改善します。この手法は、算術や常識的な推論のベンチマークだけでなく、ヘイトスピーチ分類などの難しい問題に対しても優れた性能を発揮します。</span>
<span class="snippet"><span>Comment</span>以下AIDBのツイートの引用>プロンプトを遺伝的アルゴリズムで最適化するプロンプトエンジニアリング自動化手法『Promptbreeder（プロンプトブリーダー）』が発表されました。>CoT（ステップバイステップ）を上回る性能を確認したとのこと。>DeepMindによる研究です。>○ C詳細な解説記事 ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1065">Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models  through Logic, Xufeng Zhao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデルの進歩は驚異的だが、多段階の推論には改善の余地がある。大規模言語モデルは知識を持っているが、推論には一貫性がなく、幻覚を示すことがある。そこで、Logical Chain-of-Thought（LogiCoT）というフレームワークを提案し、論理による推論パラダイムの効果を示した。</span>
<span class="snippet"><span>Comment</span>まーた新しいX of Thoughtが出た。必要そうなら読む。 ...</span>
<a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1061">Graph Neural Prompting with Large Language Models, Yijun Tian+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を知識グラフと組み合わせるための新しい手法であるGraph Neural Prompting（GNP）を提案しています。GNPは、標準的なグラフニューラルネットワークエンコーダやクロスモダリティプーリングモジュールなどの要素から構成されており、異なるLLMのサイズや設定において、常識的な推論タスクやバイオメディカル推論タスクで優れた性能を示すことが実験によって示されました。</span>
<span class="snippet"><span>Comment</span>以下elvis氏のツイートの意訳事前学習されたLLMがKGから有益な知識を学習することを支援する手法を提案。元ツイート: https://arxiv.org/abs/2309.15427しっかり論文を読んでいないが、freezeしたLLMがあった時に、KGから求めたGraph Neural Prom ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/434daf26-f82f-43b9-8807-13517975383b" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/834">Focused Prefix Tuning for Controllable Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、注釈のない属性によって制御可能なテキスト生成データセットのパフォーマンスが低下する問題に対して、「focused prefix tuning（FPT）」という手法を提案しています。FPTは望ましい属性に焦点を当てることで、制御精度とテキストの流暢さを向上させることができます。また、FPTは複数属性制御タスクにおいても、既存のモデルを再トレーニングすることなく新しい属性を制御する柔軟性を持ちながら、制御精度を保つことができます。</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1079">日本語LLMベンチマークと自動プロンプトエンジニアリング</a>
<span class="snippet"><span>Comment</span>面白かった。特に、promptingによってrinnaとcyberのLLMの順位が逆転しているのが興味深かった。GAを使ったプロンプトチューニングは最近論文も出ていたが、日本語LLMで試されているのは面白かった。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2022-08-19</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/473">The Power of Scale for Parameter-Efficient Prompt Tuning, Lester+, Google Research, EMNLP‘21</a>
<span class="snippet"><span>Comment</span>日本語解説: https://qiita.com/kts_plea/items/79ffbef685d362a7b6ceT5のような大規模言語モデルに対してfinetuningをかける際に、大規模言語モデルのパラメータは凍結し、promptをembeddingするパラメータを独立して学習する手法 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
