---
layout: post
title: QuestionAnsweringに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## QuestionAnswering
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-10-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1110">Re-Reading Improves Reasoning in Language Models, Xiaohan Xu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）において、推論は重要で困難な問題です。従来のアプローチでは、プロンプティング戦略を開発することに焦点が当てられてきましたが、双方向の相互作用や質問の重要性には注意が払われていませんでした。この問題に対処するため、質問の再読という新しいプロンプティング戦略を提案します。再読は、質問情報を再訪することで、LLMsの推論能力を向上させることができます。実験結果は、この手法の効果と汎用性を示しており、LLMsの領域でのその有用性を強調しています。</span>
<span class="snippet"><span>Comment</span>問題文を2,3回promptで繰り返すだけで、数学のベンチマークとCommonsenseのベンチマークの性能が向上したという非常に簡単なPrompting。self-consistencyなどの他のPromptingとの併用も可能。なぜ性能が向上するかというと、1. LLMはAuporegresこの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e575e0aa-b76c-444e-b9b0-e984d6fc73cf" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1068">Improved Baselines with Visual Instruction Tuning, Haotian Liu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLaVAは、ビジョンと言語のクロスモーダルコネクタであり、データ効率が高く強力な性能を持つことが示されています。CLIP-ViT-L-336pxを使用し、学術タスク指向のVQAデータを追加することで、11のベンチマークで最先端のベースラインを確立しました。13Bのチェックポイントはわずか120万の公開データを使用し、1日で完全なトレーニングを終えます。コードとモデルは公開されます。</span>
<span class="snippet"><span>Comment</span>画像分析が可能なオープンソースLLMとのこと。以下AIDBのツイートの引用>画像分析機能を持つオープンソースLLM『LLaVA-1.5』が登場しました。GPT-4に匹敵する能力を持つとのことです。>デモが公開されており、手持ちの画像を分析させることも可能です。>ウィスコンシン大学とM# Overvi ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/8d0382b0-8c2b-438d-8de8-ee451f5e2649" alt="image"><a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/LongSequence.html">#LongSequence</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1045">LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models, Yukang Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、計算コストを制限しながら大規模言語モデル（LLMs）のコンテキストサイズを拡張する効率的なファインチューニング手法であるLongLoRAを提案します。従来の方法では、LLMsの長いコンテキストサイズでのトレーニングには高い計算コストとGPUリソースが必要でしたが、提案手法ではコンテキスト拡張を高速化し、非自明な計算コストの削減を実現します。また、パラメータ効率的なファインチューニング手法も再評価し、LongLoRAはさまざまなタスクで強力な実験結果を示しています。さらに、教師ありファインチューニングのためのデータセットであるLongQAも収集されました。</span>
<span class="snippet"><span>Comment</span># 概要context長が大きい場合でも効率的にLoRAする手法。通常のLoRAではcontext lengthが大きくなるにつれてperplexityが大きくなってしまう。一方、通常のFinetuningではperplexityは高い性能を維持するが、計算コストとVRAMの消費量が膨大になって ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fc3d17c7-b1ac-4741-9895-bce70cf0b356" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1044">Chain-of-Verification Reduces Hallucination in Large Language Models, Shehzaad Dhuliawala+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、言語モデルが根拠のない情報を生成する問題に取り組んでいます。Chain-of-Verification（CoVe）メソッドを開発し、モデルが回答を作成し、検証し、最終的な回答を生成するプロセスを経ることで、幻想を減少させることができることを実験で示しました。</span>
<span class="snippet"><span>Comment</span># 概要ユーザの質問から、Verificationのための質問をplanningし、質問に対して独立に回答を得たうえでオリジナルの質問に対するaggreementを確認し、最終的に生成を実施するPrompting手法# 評価## datasetWikidata ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/18763903-2d70-4180-9384-2da55bedad2e" alt="image"><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/890">RQUGE: Reference-Free Metric for Evaluating Question Generation by Answering the Question, ACL23</a>
<span class="snippet"><span>Summary</span>既存の質問評価メトリックにはいくつかの欠点がありますが、本研究では新しいメトリックRQUGEを提案します。RQUGEは文脈に基づいて候補質問の回答可能性を考慮し、参照質問に依存せずに人間の判断と高い相関を持つことが示されています。さらに、RQUGEは敵対的な破壊に対しても堅牢であり、質問生成モデルのファインチューニングにも有効です。これにより、QAモデルのドメイン外データセットでのパフォーマンスが向上します。</span>
<span class="snippet"><span>Comment</span># 概要質問自動生成の性能指標（e.g. ROUGE, BERTScore）は、表層の一致、あるいは意味が一致した場合にハイスコアを与えるが、以下の欠点がある人手で作成された大量のreference questionが必要表層あるいは意味的に近くないが正しいquestionに対し ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/61c3d939-a678-4c63-9572-f3cf28b3aa20" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/KnowledgeGraph.html">#KnowledgeGraph</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/819">Do I have the Knowledge to Answer? Investigating Answerability of Knowledge Base Questions, ACL23</a>
<span class="snippet"><span>Summary</span>ナレッジベース上の自然言語質問には回答不可能なものが多くありますが、これについての研究はまだ不十分です。そこで、回答不可能な質問を含む新しいベンチマークデータセットを作成しました。最新のKBQAモデルを評価した結果、回答不可能な質問に対して性能が低下することがわかりました。さらに、これらのモデルは誤った理由で回答不可能性を検出し、特定の形式の回答不可能性を扱うことが困難であることもわかりました。このため、回答不可能性に対する堅牢なKBQAシステムの研究が必要です。</span>
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/800">SPAE: Semantic Pyramid AutoEncoder for Multimodal Generation with Frozen  LLMs, Lijun Yu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>この研究では、Semantic Pyramid AutoEncoder（SPAE）を使用して、凍結されたLLMsが非言語的なモダリティを含むタスクを実行できるようにします。SPAEは、LLMの語彙から抽出されたトークンと生のピクセルデータの変換を行います。生成されたトークンは、視覚再構成に必要な意味と詳細を捉え、LLMが理解できる言語に変換します。実験結果では、我々のアプローチが画像理解と生成のタスクにおいて最先端のパフォーマンスを25％以上上回ることを示しています。</span>
<span class="snippet"><span>Comment</span>画像をLLMのtokenスペースにマッピングすることで、LLMがパラメータの更新なしにvisual taskを解くことを可能にした。in context learningによって、様々なvisuataskを解くことができる。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/1e0f962f-e661-44e6-bc59-73d9ae87d6dd" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-06-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/775">Towards Language Models That Can See: Computer Vision Through the LENS  of Natural Language, William Berrios+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、LENSというモジュラーなアプローチを提案しています。このアプローチでは、大規模言語モデル（LLMs）を使用してコンピュータビジョンの問題に取り組みます。LENSは、独立したビジョンモジュールの出力に対して言語モデルを使用して推論を行います。私たちは、ゼロショットおよびフューショットのオブジェクト認識などのコンピュータビジョンの設定でLENSを評価しました。LENSは市販のLLMに適用でき、非常に競争力のあるパフォーマンスを発揮します。コードはオープンソースで提供されています。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートより引用> LENSは様々な画像認識や画像タスクを、画像からそれを説明するプロンプト（タグ、属性、状況説明文）と、テキスト上でのLLMの質問応答に分解し、それぞれ事前学習済みのモデルを使って実現する。マルチモーダル学習データを最小限にできる（書き起こしさえできればよ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e96f9a8a-6ce2-4985-8b0a-8daf4a6e477c" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-06-16</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/732">AVIS: Autonomous Visual Information Seeking with Large Language Models, Ziniu Hu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、自律的な情報収集ビジュアル質問応答フレームワークであるAVISを提案する。AVISは、大規模言語モデル（LLM）を活用して外部ツールの利用戦略を動的に決定し、質問に対する回答に必要な不可欠な知識を獲得する。ユーザースタディを実施して収集したデータを用いて、プランナーや推論エンジンを改善し、知識集約型ビジュアル質問応答ベンチマークで最先端の結果を達成することを示している。</span>
<span class="snippet"><span>Comment</span> ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/9df9b0ce-1f95-4e48-a4c9-b4c6b87d0ac6" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompt.html">#Prompt</a><a class="button" href="articles/TheoryOfMind.html">#TheoryOfMind</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/581">Boosting Theory-of-Mind Performance in Large Language Models via Prompting, Moghaddam+, Johns Hopkins University, arXiv23</a>
<span class="snippet"><span>Comment</span>LLMはTheory-of-mind reasoningタスクが苦手なことが知られており、特にzero shotでは非常にパフォーマンスが低かった。ToMタスクとは、エージェントの信念、ゴール、メンタルstate、エージェントが何を知っているか等をトラッキングすることが求められるタスクのこと。このよ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/TabularData.html">#TabularData</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/580">Large Language Models are Versatile Decomposers: Decompose Evidence and Questions for Table-based Reasoning, Ye+, University of Science and Technology of China, SIGIR23</a>
<span class="snippet"><span>Comment</span>テーブルとquestionが与えられた時に、questionをsub-questionとsmall tableにLLMでin-context learningすることで分割。subquestionの解を得るためのsqlを作成しスポットを埋め、hallucinationを防ぐ。最終的にLLM Reas ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/DialogueGeneration.html">#DialogueGeneration</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/575">q2d: Turning Questions into Dialogs to Teach Models How to Search, Bitton+, The Hebrew University of Jerusalem （w_ Google Research）, arXiv23</a>
<span class="snippet"><span>Comment</span>LLMにquestionを与え、questionを解決するためのinformation seekingの対話ログを生成させる。このデータを用いて、dialogueからquestionを生成するモデルを訓練し、検索APIなどに渡せるようにした研究。全く対話のログがないドメインのデータに対しても、人間と ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><a class="button" href="articles/Prompt.html">#Prompt</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/568">Answering Questions by Meta-Reasoning over Multiple Chains of Thought, Yoran+, Tel Aviv University （w_ Allen Institute for AI）, arXiv23</a>
<span class="snippet"><span>Comment</span>self-consistency #558 のようなvoting basedなアルゴリズムは、複数のCoTのintermediate stepを捨ててしまい、結果だけを採用するが、この研究は複数のCoTの中からquestionに回答するために適切なfactual informationを抽出するMe ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><br><span class="issue_date">Issue Date: 2022-02-07</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/436">JaQuAD: Japanese Question Answering Dataset for Machine Reading Comprehension, arXiv22</a>
<span class="snippet"><span>Comment</span>SQuAD likeな日本語のQAデータセットhttps://github.com/SkelterLabsInc/JaQuAD ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-06-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/275">Learning to Paraphrase for Question Answering, Dong+, EMNLP17</a>
<span class="snippet"><span>Comment</span>question-answeringタスクにおいて、paraphrasingを活用して精度向上させる研究似たような意味の質問が、異なる表現で出現することがあるので、questionの様々なparaphrasingを用意して活用したいという気持ち。たとえば、Is the camQAはデータセ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/77">Teaching Machines to Read and Comprehend, Hermann+, NIPS 2015</a>
<span class="snippet"><span>Comment</span>だいぶ前に読んだので割とうろおぼえ。CNN/DailyMailデータセットの作成を行なった論文（最近Neuralな文”書”要約の学習でよく使われるやつ）。CNN/DailyMailにはニュース記事に対して、人手で作成した要約が付与されており、要約中のEntityを穴埋めにするなどして、 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
