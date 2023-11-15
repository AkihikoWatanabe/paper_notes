---
layout: post
title: InstructionTuningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## InstructionTuning
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionGeneration.html">#InstructionGeneration</a><br><span class="issue_date">Issue Date: 2023-10-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1092">Auto-Instruct: Automatic Instruction Generation and Ranking for  Black-Box Language Models, Zhihan Zhang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）の性能を向上させるための新しい手法であるAuto-Instructを提案しています。この手法では、LLMsが生成する指示の品質を自動的に向上させるために、多様な候補の指示を生成し、スコアリングモデルでランク付けします。実験結果では、Auto-Instructが人間による指示や既存のLLM生成指示を上回ることが示されています。また、他のLLMsでも顕著な汎化性能を示すことも確認されています。</span>
<span class="snippet"><span>Comment</span>seed instructionとdemonstrationに基づいて、異なるスタイルのinstructionを自動生成し、自動生成したinstructionをとinferenceしたいexampleで条件づけてランキングし、良質なものを選択。選択したinstructionでinferenceを実施 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/3b318cac-516d-4fc8-9097-ad695ab8223b" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/NumericReasoning.html">#NumericReasoning</a><a class="button" href="articles/Mathematics.html">#Mathematics</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1050">MAmmoTH: Building Math Generalist Models through Hybrid Instruction  Tuning, Xiang Yue+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>MAmmoTHは、数学の問題解決に特化した大規模言語モデルであり、厳密にキュレーションされた教育データセットで訓練されています。このモデルは、CoTとPoTのハイブリッドな根拠を提供し、さまざまな数学の分野を包括的にカバーしています。MAmmoTHは、既存のオープンソースモデルを大幅に上回り、特にMATHデータセットで高い精度を示しています。この研究は、多様な問題のカバレッジとハイブリッドな根拠の使用の重要性を強調しています。</span>
<span class="snippet"><span>Comment</span>9つのmath reasoningが必要なデータセットで13-29%のgainでSoTAを達成。260kの根拠情報を含むMath Instructデータでチューニングされたモデル。project page: https://tiger-ai-lab.github.io/MAmmoTH/ ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/877">Instruction-following Evaluation through Verbalizer Manipulation, Shiyang Li+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、指示に従う能力を正確に評価するための新しい評価プロトコル「verbalizer manipulation」を提案しています。このプロトコルでは、モデルに異なる程度で一致する言葉を使用してタスクラベルを表現させ、モデルの事前知識に依存する能力を検証します。さまざまなモデルを9つのデータセットで評価し、異なるverbalizerのパフォーマンスによって指示に従う能力が明確に区別されることを示しました。最も困難なverbalizerに対しても、最も強力なモデルでもランダムな推測よりも優れたパフォーマンスを発揮するのは困難であり、指示に従う能力を向上させるために継続的な進歩が必要であることを強調しています。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/832">Do Models Really Learn to Follow Instructions? An Empirical Study of Instruction Tuning, ACL23</a>
<span class="snippet"><span>Summary</span>最近のinstruction tuning（IT）の研究では、追加のコンテキストを提供してモデルをファインチューニングすることで、ゼロショットの汎化性能を持つ素晴らしいパフォーマンスが実現されている。しかし、IT中にモデルがどのように指示を利用しているかはまだ研究されていない。本研究では、モデルのトレーニングを変更された指示と元の指示との比較によって、モデルがIT中に指示をどのように利用するかを分析する。実験の結果、トレーニングされたモデルは元の指示と同等のパフォーマンスを達成し、ITと同様のパフォーマンスを達成することが示された。この研究は、より信頼性の高いIT手法と評価の緊急性を強調している。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/815">Unnatural Instructions: Tuning Language Models with （Almost） No Human Labor, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、人間の監督を必要としない方法で収集された大規模なデータセット「Unnatural Instructions」を紹介します。このデータセットを使用して、言語モデルのトレーニングを行い、既存のモデルを上回る性能を実現しました。これにより、クラウドソーシングに頼らずにデータセットを拡張し、多様性を持たせることができることが示されました。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/542">Scaling Instruction-Finetuned Language Models, Chung+, Google, arXiv22</a>
<span class="snippet"><span>Comment</span>T5をinstruction tuningしたFlanT5の研究 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-03-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/513">Self-Instruct: Aligning Language Model with Self Generated Instructions, Wang+ （w_ Noah Smith）, Univesity of Washington, arXiv22</a>
<span class="snippet"><span>Comment</span>Alpacaなどでも利用されているself-instruction技術に関する論文# 概要![image](https://user-images.githubusercontent.com/12249301/228716254-5f4d7451-a37a-4354-843d-7e4052ba23 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/548">LaMini-instruction</a>
<span class="snippet"><span>Summary</span>私たちは、大規模言語モデルからの知識を抽出するために、文/オフライン蒸留を行います。具体的には、いくつかの既存のプロンプトリソースに基づいて、合計258万ペアの指示と応答を生成します。詳細は論文を参照してください。</span>
<span class="snippet"><span>Comment</span>既存のInstruction DatasetのInstructionをseedとして、gpt-3.5-turboで新たなInstructionとresponseを生成したデータセット ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/23a85991-6af9-4663-a293-c22a6cdba9f0" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
