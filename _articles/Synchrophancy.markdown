---
layout: post
title: Synchrophancyに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Synchrophancy
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-09-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1038">Simple synthetic data reduces sycophancy in large language models, Jerry Wei+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、機械学習モデルのおべっか行動を減らすための方法を提案しています。まず、言語モデルにおけるおべっか行動の普及度を調査し、その行動を減らすための合成データ介入を提案しています。具体的には、ユーザーの意見に対してモデルが頑健であることを促す合成データを使用し、モデルのファインチューニングを行います。これにより、おべっか行動を大幅に減らすことができます。提案手法の詳細は、https://github.com/google/sycophancy-intervention で確認できます。</span>
<span class="snippet"><span>Comment</span>LLMはユーザの好む回答をするように事前学習されるため、prompt中にユーザの意見が含まれていると、ユーザの意見に引っ張られ仮に不正解でもユーザの好む回答をしてしまう問題があることを示した。また、その対策として人工的にユーザの意見と、claimを独立させるように学習するためのデータセットを生成しF ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/43c03357-5c5c-4ceb-a089-0ad0a35eea1d" alt="image"></div>
