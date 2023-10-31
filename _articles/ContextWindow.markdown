---
layout: post
title: ContextWindowに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## ContextWindow
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/801">Extending Context Window of Large Language Models via Positional  Interpolation, Shouyuan Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、Position Interpolation（PI）という手法を提案します。これにより、RoPEベースの事前学習済みLLM（例：LLaMAモデル）のコンテキストウィンドウサイズを最大32768まで拡張することができます。PIを使用することで、長いコンテキストが必要なタスクで強力な性能を示し、元のコンテキストウィンドウ内のタスクに対しても良好な品質を保持します。PIは、注意スコアを壊滅的に高くすることを防ぐために、入力の位置インデックスを線形にダウンスケールして元のコンテキストウィンドウサイズに合わせます。この手法は、既存の最適化とインフラストラクチャを再利用することができます。</span>
<span class="snippet"><span>Comment</span>LLMのContext Windowを最大32kまで拡張する手法を提案。1000 step以内のminimalなfinetuningでモデルの性能を維持しながら実現できる。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Survey.html">#Survey</a><br><span class="issue_date">Issue Date: 2023-07-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/778">Extending Context is Hard…but not Impossible</a>
<span class="snippet"><span>Comment</span>Open source LLMのcontext lengthをどのように大きくするかに関する議論 ...</span>
</div>
