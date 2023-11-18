---
layout: post
title: QA-basedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## QA-based
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/974">QuestEval: Summarization Asks for Fact-based Evaluation, Thomas Scialom+, N_A, EMNLP21</a>
<span class="snippet"><span>Summary</span>要約の評価は未解決の課題であり、既存の評価指標は限定的であり、人間の判断との相関が低い。そこで、本研究では質問応答モデルを利用した評価指標QuestEvalを提案する。QuestEvalは正解の参照を必要とせず、一貫性、結束性、流暢さ、関連性の4つの評価次元において人間の判断との相関を大幅に改善することが実験により示された。</span>
<span class="snippet"><span>Comment</span>QuestEval# 概要#984 によって提案されてきたメトリックがROUGEに勝てていないことについて言及し、より良い指標を提案。precision / recall-based な QA metricsを利用してよりロバスト生成されるqueryのsaliencyを学習する手法を提案するこ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/3c1092a6-5a6e-494b-8ec1-a30fdc8ad96c" alt="image"><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DialogueGeneration.html">#DialogueGeneration</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/966">Q2: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering, Honovich+, EMNLP21</a>
<span class="snippet"><span>Summary</span>本研究では、ニューラルな知識に基づく対話生成モデルの信頼性と適用範囲の制限についての問題を解決するため、自動的な質問生成と質問応答を使用した事実的な整合性の自動評価尺度を提案します。この尺度は、自然言語推論を使用して回答スパンを比較することで、以前のトークンベースのマッチングよりも優れた評価を行います。また、新しいデータセットを作成し、事実的な整合性の手動アノテーションを行い、他の尺度とのメタ評価を行いました。結果として、提案手法が人間の判断と高い相関を示しました。</span>
<span class="snippet"><span>Comment</span>（knowledge-grounded; 知識に基づいた）対話に対するFactual ConsistencyをReference-freeで評価できるQGQA手法。機械翻訳やAbstractive Summarizationの分野で研究が進んできたが、対話では対話履歴、個人の意見、ユーザに対 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/979808f2-d31a-49b0-bd25-aba1f1a81d4a" alt="image"><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/961">QACE: Asking Questions to Evaluate an Image Caption, Lee+, EMNLP21</a>
<span class="snippet"><span>Summary</span>本研究では、画像キャプションの評価において、Question Generation（QG）とQuestion Answering（QA）システムに基づいた質問応答メトリックであるQACEを提案する。QACEは評価対象のキャプションに対して質問を生成し、その内容を参照キャプションまたはソース画像に対して質問することで確認する。QACE_Refというメトリックを開発し、最先端のメトリックと競合する結果を報告する。さらに、参照ではなく画像自体に直接質問をするQACE_Imgを提案する。QACE_ImgにはVisual-QAシステムが必要であり、Visual-T5という抽象的なVQAシステムを提案する。QACE_Imgはマルチモーダルで参照を必要とせず、説明可能なメトリックである。実験の結果、QACE_Imgは他の参照を必要としないメトリックと比較して有利な結果を示した。</span>
<span class="snippet"><span>Comment</span>Image Captioningを評価するためのQGQAを提案している。candidateから生成した質問を元画像, およびReferenceを用いて回答させ、candidateに基づいた回答と回答の結果を比較することで評価を実施する。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/552b3bfd-48a6-4915-af96-e8ae91e760dc" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1007">Asking and Answering Questions to Evaluate the Factual Consistency of Summaries, Wang, ACL20</a>
<span class="snippet"><span>Summary</span>要約の事実の不整合を特定するための自動評価プロトコルであるQAGSを提案する。QAGSは、要約とソースについて質問をし、整合性がある回答を得ることで要約の事実的整合性を評価する。QAGSは他の自動評価指標と比較して高い相関を持ち、自然な解釈可能性を提供する。QAGSは有望なツールであり、https://github.com/W4ngatang/qagsで利用可能。</span>
<span class="snippet"><span>Comment</span>QAGS生成された要約からQuestionを生成する手法。precision-oriented ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/991">FEQA: A Question Answering Evaluation Framework for Faithfulness Assessment in Abstractive Summarization, Durmus+, ACL20</a>
<span class="snippet"><span>Summary</span>ニューラル抽象的要約モデルの信頼性を評価するために、人間の注釈を収集し、信頼性の自動評価指標であるFEQAを提案した。FEQAは質問応答を利用して要約の信頼性を評価し、特に抽象的な要約において人間の評価と高い相関を示した。</span>
<span class="snippet"><span>Comment</span>FEQA生成された要約からQuestionを生成する手法。precision-oriented ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/995">Question answering as an automatic evaluation metric for news article summarization, Eyal+, NAACL19</a>
<span class="snippet"><span>Summary</span>最近の自動要約の研究では、ROUGEスコアの最大化に焦点を当てているが、本研究では代替的な評価指標であるAPESを提案する。APESは、要約が一連の手動作成質問に答える能力を定量化する。APESを最大化するエンドツーエンドのニューラル抽象モデルを提案し、ROUGEスコアを向上させる。</span>
<span class="snippet"><span>Comment</span>APES ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/943">Answers Unite Unsupervised Metrics for Reinforced Summarization Models, Scialom+, EMNLP-IJCNLP19</a>
<span class="snippet"><span>Summary</span>最近、再強化学習（RL）を使用した抽象的要約手法が提案されており、従来の尤度最大化を克服するために使用されています。この手法は、複雑で微分不可能なメトリクスを考慮することで、生成された要約の品質と関連性を総合的に評価することができます。ROUGEという従来の要約メトリクスにはいくつかの問題があり、代替的な評価尺度を探求する必要があります。報告された人間評価の分析によると、質問応答に基づく提案されたメトリクスはROUGEよりも有利であり、参照要約を必要としないという特徴も持っています。これらのメトリクスを使用してRLベースのモデルをトレーニングすることは、現在の手法に比べて改善をもたらします。</span>
<span class="snippet"><span>Comment</span>SummaQA ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/994">A Semantic QA-Based Approach for Text Summarization Evaluation, Ping Chen+, N_A, AAAI18</a>
<span class="snippet"><span>Summary</span>自然言語処理システムの評価における問題の一つは、2つのテキストパッセージの内容の違いを特定することです。本研究では、1つのテキストパッセージを小さな知識ベースとして扱い、多数の質問を投げかけて内容を比較する方法を提案します。実験結果は有望であり、2007年のDUC要約コーパスを使用して行われました。</span>
<span class="snippet"><span>Comment</span>QGQAを提案した研究 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1006">Discourse constraints for document compression, Clarke+ （w_ Lapata）, Computational Linguistics10</a>
<span class="snippet"><span>Comment</span>QAベースドなアプローチを人手評価に導入した初めての研究 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
