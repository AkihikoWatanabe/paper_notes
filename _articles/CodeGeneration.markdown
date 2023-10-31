---
layout: post
title: CodeGenerationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## CodeGeneration
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/692">CodeT5+: Open Code Large Language Models for Code Understanding and  Generation, Yue Wang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、コードのためのエンコーダーデコーダーLLMsのファミリーである「CodeT5+」を提案し、様々なダウンストリームコードタスクに柔軟に適合することができるようにしました。また、事前学習オブジェクティブの混合を提案することで、事前学習とファインチューニングの不一致を緩和し、スパンデノイジング、コントラスティブラーニング、テキストコードマッチング、因果LM事前学習タスクを含めました。CodeT5+は、異なる設定で20以上のコード関連ベンチマークで徹底的に評価され、最先端のモデルパフォーマンスを観察しました。特に、instruction-tuned CodeT5+ 16Bは、他のオープンなコードLLMsに対して、HumanEvalコード生成タスクで新しい最先端の結果を達成しました。</span>
<span class="snippet"><span>Comment</span>様々なコードの理解と生成タスクをサポート異なる訓練手法によって計算効率改善20種類のコードベンチマークで、様々な設定「ゼロショット、finetuning, instruction tuning等）を実施した結果、コード補完、math programming, text to code retri ...</span>
</div>
