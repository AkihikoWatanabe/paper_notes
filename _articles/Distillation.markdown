---
layout: post
title: Distillationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Distillation
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/867">Teaching Small Language Models to Reason, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模な言語モデルの推論能力を小さなモデルに転送するための知識蒸留を探求しました。具体的には、大きな教師モデルによって生成された出力を用いて学生モデルを微調整し、算術、常識、象徴的な推論のタスクでのパフォーマンスを向上させることを示しました。例えば、T5 XXLの正解率は、PaLM 540BとGPT-3 175Bで生成された出力を微調整することで、それぞれ8.11％から21.99％および18.42％に向上しました。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/829">SCOTT: Self-Consistent Chain-of-Thought Distillation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模な言語モデル（LM）から小さなCoTモデルを学習するための知識蒸留手法であるSCOTTを提案しています。SCOTTは、教師モデルからゴールドアンサーをサポートする根拠を引き出し、より信憑性のあるトークンを生成するように学習を促します。さらに、学生モデルはカウンターファクトリーニングの目的で教師が生成した根拠を使用して学習されます。実験結果は、提案手法がベースラインよりも忠実なモデルを導くことを示しています。また、根拠を尊重することで意思決定を改善することも可能です。</span>
<span class="snippet"><span>Comment</span>CoTのパフォーマンス向上がパラメータ数が大きいモデルでないと発揮せれないことは元論文 #551 で考察されており、それをより小さいモデルに蒸留し発揮できるようにする、おもしろい ...</span>
</div>
