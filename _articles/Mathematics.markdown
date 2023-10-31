---
layout: post
title: Mathematicsに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Mathematics
<div class="visible-content">
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/FoundationModel.html">#FoundationModel</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1104">Llemma: An Open Language Model For Mathematics, Zhangir Azerbayev+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、数学のための大規模な言語モデルであるLlemmaを提案します。Llemmaは、Proof-Pile-2と呼ばれるデータセットを用いて事前学習され、MATHベンチマークで他のモデルを上回る性能を示しました。さらに、Llemmaは追加のfine-tuningなしでツールの使用や形式的な定理証明が可能です。アーティファクトも公開されています。</span>
<span class="snippet"><span>Comment</span>CodeLLaMAを200B tokenの数学テキスト（proof-pile-2データ;論文、数学を含むウェブテキスト、数学のコードが含まれるデータ）で継続的に事前学習することでfoundation modelを構築約半分のパラメータ数で数学に関する性能でGoogleのMinervaと同等の性元ツイ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/87f9bbe1-3377-4e80-a7d4-904345ebb7d9" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><a class="button" href="articles/NumericReasoning.html">#NumericReasoning</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1050">MAmmoTH: Building Math Generalist Models through Hybrid Instruction  Tuning, Xiang Yue+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>MAmmoTHは、数学の問題解決に特化した大規模言語モデルであり、厳密にキュレーションされた教育データセットで訓練されています。このモデルは、CoTとPoTのハイブリッドな根拠を提供し、さまざまな数学の分野を包括的にカバーしています。MAmmoTHは、既存のオープンソースモデルを大幅に上回り、特にMATHデータセットで高い精度を示しています。この研究は、多様な問題のカバレッジとハイブリッドな根拠の使用の重要性を強調しています。</span>
<span class="snippet"><span>Comment</span>9つのmath reasoningが必要なデータセットで13-29%のgainでSoTAを達成。260kの根拠情報を含むMath Instructデータでチューニングされたモデル。project page: https://tiger-ai-lab.github.io/MAmmoTH/ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/838">Solving Math Word Problems via Cooperative Reasoning induced Language Models, ACL23</a>
<span class="snippet"><span>Summary</span>大規模な事前学習言語モデル（PLM）を使用して、数学の文章問題（MWPs）を解決するためのCooperative Reasoning（CoRe）アーキテクチャを開発しました。CoReでは、生成器と検証器の二つの推論システムが相互作用し、推論パスを生成し評価を監督します。CoReは、数学的推論データセットで最先端の手法に比べて最大9.6％の改善を達成しました。</span>
</div>
