---
layout: post
title: FoundationModelに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## FoundationModel
<div class="visible-content">
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Mathematics.html">#Mathematics</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1104">Llemma: An Open Language Model For Mathematics, Zhangir Azerbayev+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、数学のための大規模な言語モデルであるLlemmaを提案します。Llemmaは、Proof-Pile-2と呼ばれるデータセットを用いて事前学習され、MATHベンチマークで他のモデルを上回る性能を示しました。さらに、Llemmaは追加のfine-tuningなしでツールの使用や形式的な定理証明が可能です。アーティファクトも公開されています。</span>
<span class="snippet"><span>Comment</span>CodeLLaMAを200B tokenの数学テキスト（proof-pile-2データ;論文、数学を含むウェブテキスト、数学のコードが含まれるデータ）で継続的に事前学習することでfoundation modelを構築約半分のパラメータ数で数学に関する性能でGoogleのMinervaと同等の性元ツイ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/87f9bbe1-3377-4e80-a7d4-904345ebb7d9" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/914">Foundational Models Defining a New Era in Vision: A Survey and Outlook, Muhammad Awais+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、視覚システムの基礎モデルについて包括的なレビューを提供します。これには、異なるモダリティを組み合わせるためのアーキテクチャ設計やトレーニング目標、トレーニングデータセットなどが含まれます。また、基礎モデルの評価や課題、最近の発展についても議論します。詳細なリストは、\url{https://github.com/awaisrauf/Awesome-CV-Foundational-Models}で入手できます。</span>
<span class="snippet"><span>Comment</span>CVにおけるfoundation modelのsurvey。残されたチャレンジと研究の方向性が議論されている ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/888">Llama 2: Open Foundation and Fine-Tuned Chat Models, Hugo Touvron+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>この研究では、大規模な言語モデルであるLlama 2を開発し、微調整しています。Llama 2-Chatは対話に特化しており、オープンソースのチャットモデルを上回る性能を示しています。安全性の改善にも取り組んでおり、責任ある開発に貢献することを目指しています。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイート引用> Llama2は学習データを2Tトークンに増やしコンテキスト長を4KにしGQAを採用。報告書では有用性と安全性の向上に向けたSFTとRLHFの詳細が充実している。SFTは量より質が大事。2万程度作るとSFT向けアノテーションデータは生成と人手が区別できないレ ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Navigation.html">#Navigation</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/802">ViNT: A Foundation Model for Visual Navigation, Dhruv Shah+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、汎用事前学習モデルであるVisual Navigation Transformer（ViNT）を提案し、ビジョンベースのロボットナビゲーションに成功をもたらします。ViNTは、大規模なナビゲーションデータセットで訓練され、柔軟なTransformerベースのアーキテクチャを使用してさまざまなナビゲーションタスクに適応します。ViNTは、拡散ベースのサブゴール提案と組み合わせることで、新しい環境を探索し、キロメートルスケールのナビゲーション問題を解決することができます。また、ViNTはプロンプトチューニングに触発された技術を使用して、新しいタスク仕様に適応することができます。ViNTはモバイルロボティクスのための効果的な基礎モデルとして確立されています。詳細はプロジェクトページを参照してください。</span>
<span class="snippet"><span>Comment</span>事前学習済みモデルを視覚ベースのロボットナビゲーションに活用するFoundation Model。FlexibleなTransformerベースのアーキテクチャに基づいて構築されており、さまざまなナビゲーションタスクに取り組むことが可能 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fcb59d61-9a89-4ac8-989c-ffb125e90cbd" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1111">tsuzumi, NTT’23</a>
<span class="snippet"><span>Comment</span>NTT製のLLM。パラメータ数は7Bと軽量だが高性能。MTBenchのようなGPT4に勝敗を判定させるベンチマークで、地理、歴史、政治、社会に関する質問応答タスク（図6）でgpt3.5turboと同等、国産LLMの中でトップの性能。GPT3.5turboには、コーディングや数学などの能力では劣るとt ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/d064e0dc-b598-4853-9466-f56f39986acc" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/897">Introducing CM3leon, a more efficient, state-of-the-art generative model for text and images, 2023</a>
<span class="snippet"><span>Summary</span>最近の自然言語処理の進歩により、生成型AIモデルへの関心と研究が加速しています。CM3leonは、テキストから画像への生成と画像からテキストへの生成を行う単一の基礎モデルです。</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/InductiveBias.html">#InductiveBias</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/809">Objaverse-XL: A Universe of 10M+ 3D Objects</a>
<span class="snippet"><span>Comment</span>10Mを超える3D objectのデータセットを公開し、3D Modelの基盤モデルとしてZero123-XLを訓練。元ツイートのGifがわかりやすい。https://twitter.com/mattdeitke/status/1678855859089326080?s=46&t=8VBxVyn ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-06-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/771">LM Flow</a>
<span class="snippet"><span>Comment</span>一般的なFoundation Modelのファインチューニングと推論を簡素化する拡張可能なツールキット。継続的なpretragning, instruction tuning, parameter efficientなファインチューニング,alignment tuning,大規模モデルの推論などさま ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Repository.html">#Repository</a><br><span class="issue_date">Issue Date: 2023-05-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/665">OpenSource PaLM, 2023</a>
<span class="snippet"><span>Comment</span>150m,410m,1bのモデルがある。Googleの540bには遠く及ばないし、emergent abilityも期待できないパラメータ数だが、どの程度の性能なのだろうか。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Programming.html">#Programming</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/661">StarCoderBase_StarCoder, 2023</a>
<span class="snippet"><span>Comment</span>・15.5Bパラメータ・80種類以上のプログラミング言語で訓練・Multi Query Attentionを利用・context window size 8192・Fill in the middle objectiveを利用Instruction tuningがされておらず、prefipaper: ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
