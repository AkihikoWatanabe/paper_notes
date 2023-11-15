---
layout: post
title: FactualConsistencyに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## FactualConsistency
<div class="visible-content">
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><a class="button" href="articles/NaturalLanguageUnderstanding.html">#NaturalLanguageUnderstanding</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/821">Direct Fact Retrieval from Knowledge Graphs without Entity Linking, ACL23</a>
<span class="snippet">従来の知識取得メカニズムの制限を克服するために、我々はシンプルな知識取得フレームワークであるDiFaRを提案する。このフレームワークは、入力テキストに基づいて直接KGから事実を取得するものであり、言語モデルとリランカーを使用して事実のランクを改善する。DiFaRは複数の事実取得タスクでベースライン ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/841">On Improving Summarization Factual Consistency from Natural Language Feedback, ACL23</a>
<span class="snippet">本研究では、自然言語の情報フィードバックを活用して要約の品質とユーザーの好みを向上させる方法を調査しました。DeFactoという高品質なデータセットを使用して、要約の編集や修正に関する自然言語生成タスクを研究しました。また、微調整された言語モデルを使用して要約の品質を向上させることも示しました。し ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Abstractive.html">#Abstractive</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/865">Improving Factuality of Abstractive Summarization without Sacrificing Summary Quality, ACL23</a>
<span class="snippet">事実性を意識した要約の品質向上に関する研究はあるが、品質を犠牲にすることなく事実性を向上させる手法がほとんどない。本研究では「Effective Factual Summarization」という技術を提案し、事実性と類似性の指標の両方で大幅な改善を示すことを示した。トレーニング中に競合を防ぐため ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/866">WeCheck: Strong Factual Consistency Checker via Weakly Supervised Learning, ACL23</a>
<span class="snippet">現在のテキスト生成モデルは、入力と矛盾するテキストを制御できないという課題があります。この問題を解決するために、私たちはWeCheckという弱教師付きフレームワークを提案します。WeCheckは、弱教師付きラベルを持つ言語モデルから直接訓練された実際の生成サンプルを使用します。さまざまなタスクでの ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/933">ChatGPT as a Factual Inconsistency Evaluator for Text Summarization, Zheheng Luo+, N_A, arXiv23</a>
<span class="snippet">事前学習された言語モデルによるテキスト要約の性能向上が注目されているが、生成された要約が元の文書と矛盾することが問題となっている。この問題を解決するために、効果的な事実性評価メトリクスの開発が進められているが、計算複雑性や不確実性の制約があり、人間の判断との一致に限定されている。最近の研究では、大 ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1077">Survey on Factuality in Large Language Models: Knowledge, Retrieval and  Domain-Specificity, Cunxiang Wang+, N_A, arXiv23</a>
<span class="snippet">この研究では、大規模言語モデル（LLMs）の事実性の問題に取り組んでいます。LLMsの出力の信頼性と正確性は重要であり、事実に矛盾した情報を生成することがあるため、その問題を解決する方法を探求しています。具体的には、LLMsの事実的なエラーの影響や原因を分析し、事実性を評価する手法や改善策を提案し ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4d3ab4df-aaa0-460f-b16a-6114432336cd" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/RetrievalAugmentation.html">#RetrievalAugmentation</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1105">Self-RAG: Learning to Retrieve, Generate, and Critique through  Self-Reflection, Akari Asai+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）は、事実に基づかない回答を生成することがあります。そこで、自己反省的な検索増強生成（Self-RAG）という新しいフレームワークを提案します。このフレームワークは、検索と自己反省を通じてLLMの品質と事実性を向上させます。実験結果は、Self-RAGが最先端のLLMsお ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/282eb6fd-d2bd-4804-a0bc-652158e2f857" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/RetrievalAugmentation.html">#RetrievalAugmentation</a><br><span class="issue_date">Issue Date: 2023-11-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1116">The Perils & Promises of Fact-checking with Large Language Models, Dorian Quelle+, N_A, arXiv23</a>
<span class="snippet">自律型の事実チェックにおいて、大規模言語モデル（LLMs）を使用することが重要である。LLMsは真実と虚偽を見分ける役割を果たし、その出力を検証する能力がある。本研究では、LLMエージェントを使用して事実チェックを行い、推論を説明し、関連する情報源を引用する能力を評価した。結果は、文脈情報を備えた ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/1f310edd-58f3-4e45-ac40-e75337bff884" alt="image"><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/962">TRUE: Re-evaluating Factual Consistency Evaluation, Or Honovich+, N_A, the Second DialDoc Workshop on Document-grounded Dialogue and Conversational Question Answering22</a>
<span class="snippet">事実の整合性メトリックの包括的な調査と評価であるTRUEを紹介。さまざまな最先端のメトリックと11のデータセットを対象に行った結果、大規模なNLIおよび質問生成・回答ベースのアプローチが強力で補完的な結果を達成することがわかった。TRUEをモデルおよびメトリックの開発者の出発点として推奨し、さらな ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/LM-based.html">#LM-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/965">SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization, Laban+, TACL22</a>
<span class="snippet">要約の領域では、入力ドキュメントと要約が整合していることが重要です。以前の研究では、自然言語推論（NLI）モデルを不整合検出に適用するとパフォーマンスが低下することがわかりました。本研究では、NLIを不整合検出に再評価し、過去の研究での入力の粒度の不一致が問題であることを発見しました。新しい手法S ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/LM-based.html">#LM-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/964">Compression, Transduction, and Creation: A Unified Framework for Evaluating Natural Language Generation, Deng+, EMNLP21</a>
<span class="snippet">本研究では、自然言語生成（NLG）タスクの評価において、情報の整合性を重視した統一的な視点を提案する。情報の整合性を評価するための解釈可能な評価指標のファミリーを開発し、ゴールドリファレンスデータを必要とせずに、さまざまなNLGタスクの評価を行うことができることを実験で示した。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><a class="button" href="articles/QA-based.html">#QA-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/966">Q2: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering, Honovich+, EMNLP21</a>
<span class="snippet">本研究では、ニューラルな知識に基づく対話生成モデルの信頼性と適用範囲の制限についての問題を解決するため、自動的な質問生成と質問応答を使用した事実的な整合性の自動評価尺度を提案します。この尺度は、自然言語推論を使用して回答スパンを比較することで、以前のトークンベースのマッチングよりも優れた評価を行い ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/LM-based.html">#LM-based</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/963">Evaluating the Factual Consistency of Abstractive Text Summarization, Kryscinski+, EMNLP20</a>
<span class="snippet">本研究では、要約の事実的な整合性を検証するためのモデルベースのアプローチを提案しています。トレーニングデータはルールベースの変換を用いて生成され、モデルは整合性の予測とスパン抽出のタスクで共同してトレーニングされます。このモデルは、ニューラルモデルによる要約に対して転移学習を行うことで、以前のモデ ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
