---
layout: post
title: InstructionGenerationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## InstructionGeneration
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-10-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1092">Auto-Instruct: Automatic Instruction Generation and Ranking for  Black-Box Language Models, Zhihan Zhang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）の性能を向上させるための新しい手法であるAuto-Instructを提案しています。この手法では、LLMsが生成する指示の品質を自動的に向上させるために、多様な候補の指示を生成し、スコアリングモデルでランク付けします。実験結果では、Auto-Instructが人間による指示や既存のLLM生成指示を上回ることが示されています。また、他のLLMsでも顕著な汎化性能を示すことも確認されています。</span>
<span class="snippet"><span>Comment</span>seed instructionとdemonstrationに基づいて、異なるスタイルのinstructionを自動生成し、自動生成したinstructionをとinferenceしたいexampleで条件づけてランキングし、良質なものを選択。選択したinstructionでinferenceを実施 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/3b318cac-516d-4fc8-9097-ad695ab8223b" alt="image"></div>
