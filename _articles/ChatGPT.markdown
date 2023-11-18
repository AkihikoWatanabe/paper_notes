---
layout: post
title: ChatGPTに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## ChatGPT
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/887">How is ChatGPTs behavior changing over time?, Lingjiao Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>GPT-3.5とGPT-4は、大規模言語モデル（LLM）のサービスであり、その性能と振る舞いは時間とともに変動することがわかった。例えば、GPT-4は素数の特定に優れていたが、後のバージョンでは低い正答率となった。また、GPT-3.5はGPT-4よりも優れた性能を示した。さらに、GPT-4とGPT-3.5の両方が時間とともに敏感な質問への回答やコード生成でのミスが増えた。この結果から、LLMの品質を継続的に監視する必要性が示唆される。</span>
<span class="snippet"><span>Comment</span>GPT3.5, GPT4共にfreezeされてないのなら、研究で利用すると結果が再現されないので、研究で使うべきではない。また、知らんうちにいくつかのタスクで勝手に性能低下されたらたまったものではない。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/DataDistillation.html">#DataDistillation</a><br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/700">LIMA: Less Is More for Alignment, Chunting Zhou+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、65BパラメータのLLaMa言語モデルであるLIMAを訓練し、強化学習や人間の好みモデリングなしに、厳選された1,000のプロンプトとレスポンスのみで標準的な教師あり損失で微調整しました。LIMAは、幅広いクエリに対応する驚くべき強力なパフォーマンスを示し、トレーニングデータに現れなかった未知のタスクにも一般化する傾向があります。制御された人間の研究では、LIMAのレスポンスは、GPT-4、Bard、DaVinci003と比較して優れていることが示されました。これらの結果から、大規模言語モデルのほとんどの知識は事前トレーニング中に学習され、高品質の出力を生成するためには限られた指示調整データしか必要ないことが示唆されます。</span>
<span class="snippet"><span>Comment</span>LLaMA65Bをたった1kのdata point（厳選された物）でRLHF無しでfinetuningすると、旅行プランの作成や、歴史改変の推測（？）幅広いタスクで高いパフォーマンスを示し、未知のタスクへの汎化能力も示した。最終的にGPT3,4,BARD,CLAUDEよりも人間が好む回答を返した。L ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/db025381-0bf0-47a3-bd18-5d88bff666df" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/Education.html">#Education</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/617">A Review of ChatGPT Applications in Education, Marketing, Software  Engineering, and Healthcare: Benefits, Drawbacks, and Research Directions, Mohammad Fraiwan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>ChatGPTは、深層学習アルゴリズムを使用して人間らしい応答を生成する人工知能言語モデルである。最新のChatGPTバージョンが導入され、他の言語モデルも登場している。これらのモデルは、教育、ソフトウェアエンジニアリング、医療、マーケティングなどの分野で応用可能性がある。本論文では、これらのモデルの可能な応用、制限、欠点、および研究方向について議論する。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Education.html">#Education</a><a class="button" href="articles/EssayScoring.html">#EssayScoring</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/571">AI, write an essay for me: A large-scale comparison of human-written versus ChatGPT-generated essays, Herbold+, University of Passau, arXiv23</a>
<span class="snippet"><span>Comment</span>ChatGPTは人間が書いたエッセイよりも高品質なエッセイが書けることを示した。また、AIモデルの文体は、人間が書いたエッセイとは異なる言語的特徴を示している。たとえば、談話や認識マーカーが少ないが、名詞化が多く、語彙の多様性が高いという特徴がある、とのこと。![image](https ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Assessment.html">#Assessment</a><a class="button" href="articles/InformationExtraction.html">#InformationExtraction</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/534">Evaluating ChatGPTs Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness, Li+, Peking University, arXiv23</a>
<span class="snippet"><span>Comment</span>情報抽出タスクにおいてChatGPTを評価した研究。スタンダードなIEの設定ではBERTベースのモデルに負けるが、OpenIEの場合は高い性能を示した。また、ChatGPTは予測に対してクオリティが高く信頼に足る説明をしたが、一方で自信過剰な傾向がある。また、ChatGPTの予測はinput teあ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1052">GPT-4V</a>
<span class="snippet"><span>Comment</span>おう…やべえな… ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/3ee7dc96-af6f-47f9-98c0-c6be5d9384f1" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/562">HuggingChat, 2023</a>
<span class="snippet"><span>Comment</span>closedな世界で開発されるOpenAIのChatGPTに対して、Openなものが必要ということで、huggingfaceが出してきた例のアレです ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
