---
layout: post
title: In-Context Learningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## In-Context Learning
<div class="visible-content">
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/693">What In-Context Learning Learns In-Context: Disentangling Task  Recognition and Task Learning, Jane Pan+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）がどのようにコンテキスト学習（ICL）を利用してタスクを解決するかを調査しました。タスク認識（TR）とタスク学習（TL）の役割を分離するための実験を行い、LLMsがデモンストレーションを通じて暗黙的に学習を行う可能性があることを示しました。また、モデルがスケ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/729cc613-7487-47be-9225-e02921091969" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/787">Transformers learn to implement preconditioned gradient descent for  in-context learning, Kwangjun Ahn+, N_A, arXiv23</a>
<span class="snippet">トランスフォーマーは勾配降下法のアルゴリズムを学習できるかどうかについての研究があります。この研究では、トランスフォーマーが勾配降下法の反復をシミュレートすることができることが示されています。さらに、線形トランスフォーマーについての分析から、訓練目的のグローバル最小値が事前条件付き勾配降下法の単一 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/793">Lost in the Middle: How Language Models Use Long Contexts, Nelson F. Liu+, N_A, arXiv23</a>
<span class="snippet">最近の言語モデルは、長い文脈を入力として受け取ることができますが、その長い文脈をどれだけうまく利用しているかについてはまだよくわかっていません。この研究では、マルチドキュメントの質問応答とキー・バリューの検索という2つのタスクにおいて、言語モデルのパフォーマンスを分析しました。その結果、関連情報が ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/General.html">#General</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Composition.html">#Composition</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/814">How Do In-Context Examples Affect Compositional Generalization?, ACL23</a>
<span class="snippet">本研究では、組成的な一般化を調査するためのテストスイートであるCoFeを提案し、インコンテキスト学習の組成的な一般化について研究しました。インコンテキストの例の選択が組成的な一般化のパフォーマンスに影響を与えることを発見し、類似性、多様性、複雑さの要素を研究しました。さらに、架空の単語に対する組成 ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/817">FiD-ICL: A Fusion-in-Decoder Approach for Efficient In-Context Learning, ACL23</a>
<span class="snippet">大規模な事前学習モデルを使用したfew-shot in-context learning（ICL）において、fusion-in-decoder（FiD）モデルを適用することで効率とパフォーマンスを向上させることができることを検証する。FiD-ICLは他のフュージョン手法と比較して優れたパフォーマン ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/InductiveBias.html">#InductiveBias</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/830">Measuring Inductive Biases of In-Context Learning with Underspecified Demonstrations, ACL23</a>
<span class="snippet">インコンテキスト学習（ICL）は、大規模言語モデル（LLMs）を新しいタスクに適応させるための重要なパラダイムですが、ICLの一般化の振る舞いはまだ十分に理解されていません。本研究では、ICLの帰納的なバイアスについて調査を行いました。具体的には、不完全なデモンストレーションが与えられた場合、IC ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LabelBias.html">#LabelBias</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/833">Mitigating Label Biases for In-context Learning, ACL23</a>
<span class="snippet">インコンテキスト学習（ICL）におけるラベルバイアスの種類を定義し、その影響を軽減するための方法を提案する研究が行われました。特に、ドメインラベルバイアスについて初めて概念化され、その影響を軽減するためのバイアス補正方法が提案されました。この方法により、GPT-JとGPT-3のICLパフォーマンス ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/857">Pre-Training to Learn in Context, ACL23</a>
<span class="snippet">インコンテキスト学習は、タスクの例と文脈からタスクを実行する方法であり、注目されています。しかし、現在の方法では十分に活用されていないため、私たちはPICLというフレームワークを提案します。これは、一般的なテキストコーパスでモデルを事前学習し、文脈に基づいてタスクを推論して実行する能力を向上させま ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
