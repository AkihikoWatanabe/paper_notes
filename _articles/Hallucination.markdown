---
layout: post
title: Hallucinationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Hallucination
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/690">TrueTeacher: Learning Factual Consistency Evaluation with Large Language  Models, Zorik Gekhman+, N_A, arXiv23</a>
<span class="snippet">自然言語推論（NLI）モデルを使用した事実の一貫性評価には限界があり、大規模言語モデル（LLMs）は計算コストが高いため実用的ではない。そこで、TrueTeacherというLLMを使用して多様なモデル生成要約を注釈付けすることによって合成データを生成する方法を提案し、既存の合成データ生成方法と比較 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4fb420c8-6a80-4737-bc08-8e59b0ed89d6" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/764">How Language Model Hallucinations Can Snowball, Muru Zhang+, N_A, arXiv23</a>
<span class="snippet">言語モデルを使用する際のリスクとして、幻覚があることが指摘されている。この幻覚は、LMの知識不足によるものだけでなく、以前に生成された幻覚を正当化するために、LMが誤った主張を出力することもあるという仮説が立てられている。ChatGPTとGPT-4は、誤った回答を示し、幻覚のスノーボール効果により ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/6a9e29b7-953f-4e72-bfdd-85daab9317d6" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1048">A Survey of Hallucination in Large Foundation Models, Vipula Rawte+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模ファウンデーションモデル（LFMs）におけるホールシネーションの問題に焦点を当て、その現象を分類し、評価基準を確立するとともに、既存の戦略を検討し、今後の研究の方向性についても議論しています。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/ec507609-5b6d-42ed-92db-296856f93200" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><a class="button" href="articles/GenerativeAI.html">#GenerativeAI</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1115">生成AIが抱えるリスクと対策, LYCorp‘23</a>
<span class="snippet">この資料をスタートにReferしている論文などを勉強すると、GenerativeAIのリスク周りに詳しくなれそう。この辺は疎いので勉強になる。しかし、LLMのAlignmentが不十分だったり、Hallucinationを100%防ぐことは原理的に不可能だと思われるので、この辺とどう付き合っていく ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1123">A Survey on Hallucination in Large Language Models: Principles,  Taxonomy, Challenges, and Open Questions, Lei Huang+, N_A, arXiv23</a>
<span class="snippet">LLMsの出現はNLPにおける重要な進歩をもたらしているが、幻覚を生じることがあり、その信頼性に懸念がある。本調査では、LLMの幻覚に関する最近の進展について包括的に概説し、幻覚の要因や検出手法、軽減アプローチについて紹介する。また、現在の制約や将来の研究方向についても分析する。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/32d8d809-e197-4289-8000-12fee76a69cf" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-11-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1130">Hallucination Leaderboard, 2023</a>
<span class="snippet">1000個の短いドキュメントに対して、事実情報のみを用いて要約を生成させ、要約結果と原文書のFactual consistencyを別に訓練したモデルで測定して評価してリーダーボードを作成している。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/993">Reducing Quantity Hallucinations in Abstractive Summarization, Zheng Zhao+, N_A, EMNLP20</a>
<span class="snippet">Hermanシステムは、抽象的な要約において幻覚を回避するために、数量エンティティを認識し、元のテキストでサポートされている数量用語を持つ要約を上位にランク付けするアプローチを提案しています。実験結果は、このアプローチが高い適合率と再現率を持ち、F$_1$スコアが向上することを示しています。また、 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ImageCaptioning.html">#ImageCaptioning</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/992">Object hallucination in image captioning, Rohbach+, EMNLP18</a>
<span class="snippet">現代の画像キャプションモデルは、オブジェクトの幻覚を生じる傾向がある。本研究では、新しい画像関連性の評価指標を提案し、モデルのアーキテクチャや学習目標が幻覚にどのように寄与するかを評価する。さらに、言語の先入観によるエラーが幻覚を引き起こすことも示された。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
