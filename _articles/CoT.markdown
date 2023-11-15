---
layout: post
title: CoTに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## CoT
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/532">Enhancing LLM Chain-of-Thought w_ Iterative Bootstrapping, Sun+, Xiamen University （w_ MSRA et al.）, arXiv23</a>
<span class="snippet">Zero shot CoTからスタートし、正しく問題に回答できるようにreasoningを改善するようにpromptをreviseし続けるループを回す。最終的にループした結果を要約し、それらをプールする。テストセットに対しては、プールの中からNshotをサンプルしinferenceを行う。![im ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/554">Active prompting with chain-of-thought for large language models, Diao+, The Hong Kong University of Science and Technology, arXiv23</a>
<span class="snippet">Auto-CoTを提案している論文 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/555">Automatic prompt augmentation and selection with chain-of-thought from labeled data, Shum+, The Hong Kong University of Science and Technology, arXiv23</a>
<span class="snippet">LLMによるreasoning chainが人間が作成したものよりも優れていることを示しているとのこと #532 より ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/558">Self-consistency improves chain of thought reasoning in language models, Wang+, Google Research, ICLR23</a>
<span class="snippet">self-consistencyと呼ばれる新たなCoTのデコーディング手法を提案。これは、難しいreasoningが必要なタスクでは、複数のreasoningのパスが存在するというintuitionに基づいている。self-consistencyではまず、普通にCoTを行う。そしてgre ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/568">Answering Questions by Meta-Reasoning over Multiple Chains of Thought, Yoran+, Tel Aviv University （w_ Allen Institute for AI）, arXiv23</a>
<span class="snippet">self-consistency #558 のようなvoting basedなアルゴリズムは、複数のCoTのintermediate stepを捨ててしまい、結果だけを採用するが、この研究は複数のCoTの中からquestionに回答するために適切なfactual informationを抽出するMe ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/754">OlaGPT: Empowering LLMs With Human-like Problem-Solving Abilities, Yuanzhen Xie+, N_A, arXiv23</a>
<span class="snippet">本論文では、人間の認知フレームワークを模倣することで、複雑な推論問題を解決するための新しい知的フレームワークであるOlaGPTを提案しています。OlaGPTは、注意、記憶、推論、学習などの異なる認知モジュールを含み、以前の誤りや専門家の意見を動的に参照する学習ユニットを提供しています。また、Cha ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/NumericReasoning.html">#NumericReasoning</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/797">Teaching Arithmetic to Small Transformers, Nayoung Lee+, N_A, arXiv23</a>
<span class="snippet">本研究では、GPT-4のような大規模言語モデルが、教師なしのトークン予測目的に明示的にエンコードされていないにもかかわらず、算術演算や基本的な関数を効率的に学習できることを示しています。訓練データのフォーマットの変更やchain-of-thoughtスタイルのデータの使用により、精度や収束速度が改 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/42e60fc0-d04b-4338-922c-5a46b69890b9" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Distillation.html">#Distillation</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/829">SCOTT: Self-Consistent Chain-of-Thought Distillation, ACL23</a>
<span class="snippet">本研究では、大規模な言語モデル（LM）から小さなCoTモデルを学習するための知識蒸留手法であるSCOTTを提案しています。SCOTTは、教師モデルからゴールドアンサーをサポートする根拠を引き出し、より信憑性のあるトークンを生成するように学習を促します。さらに、学生モデルはカウンターファクトリーニン ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Distillation.html">#Distillation</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/867">Teaching Small Language Models to Reason, ACL23</a>
<span class="snippet">本研究では、大規模な言語モデルの推論能力を小さなモデルに転送するための知識蒸留を探求しました。具体的には、大きな教師モデルによって生成された出力を用いて学生モデルを微調整し、算術、常識、象徴的な推論のタスクでのパフォーマンスを向上させることを示しました。例えば、T5 XXLの正解率は、PaLM 5 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Faithfulness.html">#Faithfulness</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/896">Measuring Faithfulness in Chain-of-Thought Reasoning, Anthropic, 2023</a>
<span class="snippet">大規模言語モデル（LLMs）は、Chain-of-Thought（CoT）推論を生成することで質問に答える性能を向上させるが、その推論が実際の推論を忠実に表しているかは不明である。本研究では、CoT推論の忠実さを調査し、CoTに介入することでモデルの予測がどのように変化するかを調べる。結果は、モデ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1044">Chain-of-Verification Reduces Hallucination in Large Language Models, Shehzaad Dhuliawala+, N_A, arXiv23</a>
<span class="snippet">私たちは、言語モデルが根拠のない情報を生成する問題に取り組んでいます。Chain-of-Verification（CoVe）メソッドを開発し、モデルが回答を作成し、検証し、最終的な回答を生成するプロセスを経ることで、幻想を減少させることができることを実験で示しました。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/18763903-2d70-4180-9384-2da55bedad2e" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1056">Large Language Models as Analogical Reasoners, Michihiro Yasunaga+, N_A, arXiv23</a>
<span class="snippet">本研究では、言語モデルの推論プロセスを自動的にガイドするための新しいプロンプティング手法であるアナロジカルプロンプティングを提案しています。この手法は、関連する過去の経験を引用して新しい問題に取り組む認知プロセスに倣い、問題を解決する前に文脈内で関連する例示や知識を自己生成させるように言語モデルに ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/8aae5d9d-d8d8-4c86-b55f-0fcde5d5381c" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1076">Take a Step Back: Evoking Reasoning via Abstraction in Large Language  Models, Huaixiu Steven Zheng+, N_A, arXiv23</a>
<span class="snippet">Step-Back Promptingは、大規模言語モデル（LLMs）を使用して推論の手順をガイドするシンプルなプロンプティング技術です。この技術により、LLMsは具体的な詳細から高レベルの概念や基本原則を抽象化し、正しい推論経路をたどる能力を向上させることができます。実験により、Step-Bac ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/aac94123-7c39-4938-889f-feb5cff9317c" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1078">Meta-CoT: Generalizable Chain-of-Thought Prompting in Mixed-task  Scenarios with Large Language Models, Anni Zou+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を使用して、推論のためのチェーン・オブ・ソート（CoT）プロンプトを生成する方法を提案しています。従来のCoTの方法では、一般的なプロンプトや手作業デモンストレーションに依存していましたが、本研究では入力質問のタイプに基づいて自動的にプロンプトを生成するMe ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/bb51c119-c1bc-4033-a7d4-f403d3c82d30" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-24</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1085">Eliminating Reasoning via Inferring with Planning: A New Framework to  Guide LLMs Non-linear Thinking, Yongqi Tong+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）に非線形の思考を促すために、新しいプロンプティング方法であるInferential Exclusion Prompting（IEP）を提案する。IEPは、計画を立てて可能な解を推論し、逆推論を行うことで広い視点を得ることができる。IEPは他の手法と比較して複 ...</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1135">Fast Chain-of-Thought: A Glance of Future from Parallel Decoding Leads  to Answers Faster, Hongxuan Zhang+, N_A, arXiv23</a>
<span class="snippet">この研究では、FastCoTというフレームワークを提案します。FastCoTは、LLMを使用して並列デコーディングと自己回帰デコーディングを同時に行い、計算リソースを最大限に活用します。また、FastCoTは推論時間を約20%節約し、性能の低下がほとんどないことを実験で示しました。さらに、異なるサ ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/551">Chain of thought prompting elicits reasoning in large language models, Wei+, Google Research, arXiv22</a>
<span class="snippet">Chain-of-Thoughtを提案した論文。CoTをする上でパラメータ数が100B未満のモデルではあまり効果が発揮されないということは念頭に置いた方が良さそう。![image](https://user-images.githubusercontent.com/12249301/234739 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/553">Large Language Models are Zero-Shot Reasoners, Kojima+, University of Tokyo, NeurIPS22</a>
<span class="snippet">Zero-Shot CoT (Let's think step-by-step.)論文 ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/556">Automatic Chain of Thought Prompting in Large Language Models, Zhang+, Shanghai Jiao Tong University, arXiv22</a>
<span class="snippet">LLMによるreasoning chainが人間が作成したものよりも優れていることを示しているとのこと #532 より ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
