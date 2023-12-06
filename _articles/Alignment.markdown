---
layout: post
title: Alignmentに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Alignment
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/In-ContextLearning.html">#In-ContextLearning</a><br><span class="issue_date">Issue Date: 2023-12-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1179">The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context  Learning, Bill Yuchen Lin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>アラインメント調整は、大規模言語モデル（LLMs）のパフォーマンスを向上させるために使用されます。しかし、アラインメント調整の効果は「表面的」である可能性があります。この研究では、基本的なLLMとアラインメント調整されたバージョンのトークン分布のシフトを分析しました。結果は、アラインメント調整が主にスタイルトークンに影響を与えることを示しました。さらに、シンプルでチューニングフリーなアラインメント手法であるURIALを導入し、基本的なLLMのパフォーマンスを向上させることができることを示しました。これらの結果から、アラインメントのより深い分析と理論的な理解が重要であることが示唆されます。</span>
<span class="snippet"><span>Comment</span>モデルの知識はPre-training時に十分獲得されており、モデルのAlignmentをとることで生じるものは表面的な変化のみであるという仮説がある。この仮説に関して分析をし、結果的にスタイリスティックな情報を生成する部分でAlignmentの有無で違いが生じることを明らかにし、そうであればわざわ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b8c62b33-dd72-43ea-8953-abb5c04cc504" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-11-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1153">Unbalanced Optimal Transport for Unbalanced Word Alignment, Yuki Arase+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>単一言語の単語アライメントにおいて、null alignmentという現象は重要であり、不均衡な単語アライメントを実現するために最適輸送（OT）のファミリーが有効であることを示している。教師あり・教師なしの設定での包括的な実験により、OTベースのアライメント手法が最新の手法と競争力があることが示されている。</span>
<span class="snippet"><span>Comment</span>最適輸送で爆速でモノリンガルの単語アライメントがとれるらしい実装:https://github.com/yukiar/OTAlign単語のアライメント先がない（null alignment）、one-to-oneの関係ではなく、one-to-many, many-to-manyのアライメントが必要な ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/5e677be2-1001-4454-bc1e-fe3b32888a32" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Conversation.html">#Conversation</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1069">RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities  of Large Language Models, Zekun Moore Wang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を使用して役割演技の能力を向上させるためのフレームワークであるRoleLLMを提案しています。RoleLLMは、役割プロファイルの構築、コンテキストベースの指示生成、役割プロンプトによる話し方の模倣、オープンソースモデルの微調整と役割のカスタマイズの4つのステージで構成されています。さらに、RoleBenchと呼ばれる役割演技のためのベンチマークデータセットを作成し、RoleLLaMAとRoleGLMというモデルを開発しました。これにより、役割演技の能力が大幅に向上し、GPT-4と同等の結果を達成しました。</span>
<span class="snippet"><span>Comment</span># Overview# RoleBench ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/4a4f8ad3-17d1-4a85-b553-6452371e2ccf" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1063">Large Language Model Alignment: A Survey, Tianhao Shen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>近年、大規模言語モデル（LLMs）の進歩が注目されていますが、その潜在能力と同時に懸念もあります。本研究では、LLMsのアライメントに関する既存の研究と新たな提案を包括的に探求し、モデルの解釈可能性や敵対的攻撃への脆弱性などの問題も議論します。さらに、LLMsのアライメントを評価するためのベンチマークと評価手法を提案し、将来の研究の方向性を考察します。この調査は、研究者とAIアライメント研究コミュニティとの連携を促進することを目指しています。</span>
<span class="snippet"><span>Comment</span>LLMのalignmentに関するサーベイ。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/09c10110-798f-4493-b431-41c2f2b017c1" alt="image"><a class="button" href="articles/General.html">#General</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1047">RAIN: Your Language Models Can Align Themselves without Finetuning, Yuhui Li+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、追加のデータなしで凍結された大規模言語モデル（LLMs）を整列させる方法を探求しました。自己評価と巻き戻しメカニズムを統合することで、LLMsは自己ブースティングを通じて人間の好みと一致する応答を生成することができることを発見しました。RAINという新しい推論手法を導入し、追加のデータやパラメータの更新を必要とせずにAIの安全性を確保します。実験結果は、RAINの効果を示しており、LLaMA 30Bデータセットでは無害率を向上させ、Vicuna 33Bデータセットでは攻撃成功率を減少させることができました。</span>
<span class="snippet"><span>Comment</span>トークンのsetで構成されるtree上を探索し、出力が無害とself-evaluationされるまで、巻き戻しと前方生成を繰り返し、有害なトークンsetの重みを動的に減らすことでalignmentを実現する。モデルの追加のfinetuning等は不要。self-evaluationでは下記のようなp ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/05bebc0a-325b-423d-ae36-4bc5698063fe" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/Synchrophancy.html">#Synchrophancy</a><br><span class="issue_date">Issue Date: 2023-09-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1038">Simple synthetic data reduces sycophancy in large language models, Jerry Wei+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、機械学習モデルのおべっか行動を減らすための方法を提案しています。まず、言語モデルにおけるおべっか行動の普及度を調査し、その行動を減らすための合成データ介入を提案しています。具体的には、ユーザーの意見に対してモデルが頑健であることを促す合成データを使用し、モデルのファインチューニングを行います。これにより、おべっか行動を大幅に減らすことができます。提案手法の詳細は、https://github.com/google/sycophancy-intervention で確認できます。</span>
<span class="snippet"><span>Comment</span>LLMはユーザの好む回答をするように事前学習されるため、prompt中にユーザの意見が含まれていると、ユーザの意見に引っ張られ仮に不正解でもユーザの好む回答をしてしまう問題があることを示した。また、その対策として人工的にユーザの意見と、claimを独立させるように学習するためのデータセットを生成しF ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/43c03357-5c5c-4ceb-a089-0ad0a35eea1d" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/918">Aligning Large Language Models with Human: A Survey, Yufei Wang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）は、自然言語処理のタスクにおいて重要な役割を果たしていますが、その性能には制約があります。この調査では、LLMsの性能を向上させるためのアラインメント技術について包括的な概要を提供します。具体的には、データ収集方法、トレーニング手法、モデル評価方法について説明します。さらに、将来の研究の方向性についてもまとめられています。この調査は、LLMsの性能向上に関心のある人々にとって貴重な情報源となるでしょう。</span>
<span class="snippet"><span>Comment</span>LLMのAlignment手法に関するSurvey ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/6c5288c8-7f5b-4526-ba6f-25c2b9b3fc55" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/ChatGPT.html">#ChatGPT</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/700">LIMA: Less Is More for Alignment, Chunting Zhou+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、65BパラメータのLLaMa言語モデルであるLIMAを訓練し、強化学習や人間の好みモデリングなしに、厳選された1,000のプロンプトとレスポンスのみで標準的な教師あり損失で微調整しました。LIMAは、幅広いクエリに対応する驚くべき強力なパフォーマンスを示し、トレーニングデータに現れなかった未知のタスクにも一般化する傾向があります。制御された人間の研究では、LIMAのレスポンスは、GPT-4、Bard、DaVinci003と比較して優れていることが示されました。これらの結果から、大規模言語モデルのほとんどの知識は事前トレーニング中に学習され、高品質の出力を生成するためには限られた指示調整データしか必要ないことが示唆されます。</span>
<span class="snippet"><span>Comment</span>LLaMA65Bをたった1kのdata point（厳選された物）でRLHF無しでfinetuningすると、旅行プランの作成や、歴史改変の推測（？）幅広いタスクで高いパフォーマンスを示し、未知のタスクへの汎化能力も示した。最終的にGPT3,4,BARD,CLAUDEよりも人間が好む回答を返した。L ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/db025381-0bf0-47a3-bd18-5d88bff666df" alt="image"><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/237">The Mathematics of Statistical Machine Translation: Parameter Estimation, Brown+, CL13</a>
<span class="snippet"><span>Comment</span>IBMモデル論文。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/233">A Phrase-Based HMM Approach to Document_Abstract Alignment, Daume+, EMNLP04</a>
<span class="snippet"><span>Comment</span>AbstractsとSource TextのAlignmentをとるために、Phrase-Based HMMを提案。Ziff-Davis Corpusのテキストに対して、2人のannotatorによってgold standardを作成。評価においてMTにおけるIBM Model4やHMM b ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/239">A systematic comparison of various statistical alignment models, Och+, CL03, Giza++</a>
<span class="snippet"><span>Comment</span>標準的に利用される単語アライメントツール評価の際は、Sure, Possibleの二種類のラベルによる単語アライメントのground-truth作成も行っている ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/232">Generating Extraction-Based Summaries from Hand-Written Summaries by Aligning Text Spans, Banko+, PACLING99</a>
<span class="snippet"><span>Comment</span>文を単位とし、文を文中の単語の出現頻度ベクトルで表し、ベクトル間の距離で文間の類似度を計ることで自由作成要約中の文と現文中の文をもっとも類似度が大きくなるように対応づける。（奥村先生のSurveyより：https://www.jstage.jst.go.jp/article/jnlp1994/9 ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/238"> HMM-based word alignment in statistical translation, Vogel+, COLING96</a>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/GenerativeAI.html">#GenerativeAI</a><a class="button" href="articles/Hallucination.html">#Hallucination</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-03</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1115">生成AIが抱えるリスクと対策, LYCorp‘23</a>
<span class="snippet"><span>Comment</span>この資料をスタートにReferしている論文などを勉強すると、GenerativeAIのリスク周りに詳しくなれそう。この辺は疎いので勉強になる。しかし、LLMのAlignmentが不十分だったり、Hallucinationを100%防ぐことは原理的に不可能だと思われるので、この辺とどう付き合っていく ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/236">ALAGIN 機械翻訳セミナー 単語アライメント, Graham Neubig</a>
<span class="snippet"><span>Comment</span>Neubigさんによる単語アライメントチュートリアル ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/220">The Decomposition of Human-Written Summary Sentences. Hongyan Jing et al. SIGIR’99.</a>
<span class="snippet"><span>Comment</span>参照要約 原文書対が与えられた時に、参照要約中の単語と原文書中の単語のアライメントをとるHMMベースな手法を提案。![image](https://user-images.githubusercontent.com/12249301/34812500-2d1d7d32-f6e9-11e7 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/219">The automatic construction of large-scale corpora for summarization research. Daniel Marcu. SIGIR’99</a>
<span class="snippet"><span>Comment</span><Abstract, Text>のタプルが与えられた時に、<Abstract, Extract, Text>のタプルを自動的に生成。ExtractはAbstractと対応するText中の重要部（節やsentence）。<Abstract, Extract, Text>に含まれるExtract ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
