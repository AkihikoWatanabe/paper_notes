---
layout: post
title: Controllableに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Controllable
<div class="visible-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/860">An Invariant Learning Characterization of Controlled Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>制御された生成では、予測器の訓練に使用される分布と異なるテキストの分布がある場合、パフォーマンスが低下することが示されている。この問題に対処するために、不変性を持つ予測器が効果的であるという考え方が提案されている。さらに、この特性を活かすための自然な解決策とヒューリスティックも提案されている。実験結果は、制御された生成における分布シフトの課題と不変性手法の潜在能力を示している。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Argument.html">#Argument</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/855">ArgU: A Controllable Factual Argument Generator, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、高品質な論証を自動生成するために、制御コードを使用したニューラル論証生成器ArgUを提案します。また、論証スキームを特定するための大規模なデータセットを作成し、注釈付けとデータセット作成のフレームワークについて詳細に説明します。さらに、論証テンプレートを生成する推論戦略を試行し、多様な論証を自動的に生成することが可能であることを示します。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/846">Controllable Text Generation via Probability Density Estimation in the Latent Space, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、潜在空間での確率密度推定を用いた新しい制御フレームワークを提案しています。この手法は、可逆変換関数を使用して潜在空間の複雑な分布を単純なガウス分布にマッピングし、洗練された柔軟な制御を行うことができます。実験結果では、提案手法が属性の関連性とテキストの品質において強力なベースラインを上回り、新たなSOTAを達成していることが示されています。さらなる分析により、制御戦略の柔軟性が示されています。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/841">On Improving Summarization Factual Consistency from Natural Language Feedback, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、自然言語の情報フィードバックを活用して要約の品質とユーザーの好みを向上させる方法を調査しました。DeFactoという高品質なデータセットを使用して、要約の編集や修正に関する自然言語生成タスクを研究しました。また、微調整された言語モデルを使用して要約の品質を向上させることも示しました。しかし、大規模な言語モデルは制御可能なテキスト生成には向いていないことがわかりました。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompting.html">#Prompting</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/837">Tailor: A Soft-Prompt-Based Approach to Attribute-Based Controlled Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>属性ベースの制御されたテキスト生成（CTG）では、望ましい属性を持つ文を生成することが目指されている。従来の手法では、ファインチューニングや追加の属性分類器を使用していたが、ストレージと推論時間の増加が懸念されていた。そこで、本研究では効率的なパラメータを使用した属性ベースのCTGを提案している。具体的には、各属性を事前学習された連続ベクトルとして表現し、固定された事前学習言語モデルをガイドして属性を満たす文を生成する。さらに、2つの解決策を提供して、組み合わせを強化している。実験の結果、追加のトレーニングパラメータのみで効果的な改善が実現できることが示された。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Adapter/LoRA.html">#Adapter/LoRA</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/834">Focused Prefix Tuning for Controllable Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、注釈のない属性によって制御可能なテキスト生成データセットのパフォーマンスが低下する問題に対して、「focused prefix tuning（FPT）」という手法を提案しています。FPTは望ましい属性に焦点を当てることで、制御精度とテキストの流暢さを向上させることができます。また、FPTは複数属性制御タスクにおいても、既存のモデルを再トレーニングすることなく新しい属性を制御する柔軟性を持ちながら、制御精度を保つことができます。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/813">Explicit Syntactic Guidance for Neural Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>既存のテキスト生成モデルには制約があり、シーケンス・トゥ・シーケンスのパラダイムに従っている。私たちは、構文にガイドされた生成スキーマを提案し、構文解析木に従ってシーケンスを生成する。提案手法は、パラフレーズ生成と機械翻訳の実験でベースラインを上回り、解釈可能性、制御可能性、多様性の観点でも効果的であることを示している。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-04-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/594">Controlled Text Generation with Natural Language Instructions, Wangchunshu Zhou+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、自然言語の説明と制約のデモンストレーションに基づいて、異なる制約を組み込むことができる制御されたテキスト生成フレームワークであるInstructCTGを提案しています。制約を自然言語の指示に言い換えて、弱く監督されたトレーニングデータを形成し、事前にトレーニングされた言語モデルを微調整して、さまざまなタイプの制約を組み込むことができます。InstructCTGは、異なる制約タイプに対してより柔軟であり、生成品質と速度にはほとんど影響を与えず、再トレーニングなしに新しい制約に適応することができます。</span>
<span class="snippet"><span>Comment</span>![image](https://user-images.githubusercontent.com/12249301/235351783-1435816a-b51a-4379-b4b5-cf3097b70de5.png) ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/573">Tractable Control for Autoregressive Language Generation, Zhang+, UCLA, arXiv23</a>
<span class="snippet"><span>Comment</span>自然言語生成モデルで、何らかのシンプルなconstiaint αの元p(xi|xi-1,α)を生成しようとしても計算ができない。このため、言語モデルをfinetuningするか、promptで制御するか、などがおこなわれる。しかしこの方法は近似的な解法であり、αがたとえシンプルであっても（何らかの語 ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/861">An Extensible Plug-and-Play Method for Multi-Aspect Controllable Text  Generation, Xuancheng Huang+, N_A, arXiv22</a>
<span class="snippet"><span>Summary</span>本研究では、テキスト生成において複数の側面を制御する方法について研究しました。従来の方法では、プレフィックスの相互干渉により制約が低下し、未知の側面の組み合わせを制御することが制限されていました。そこで、トレーニング可能なゲートを使用してプレフィックスの介入を正規化し、相互干渉の増加を抑制する方法を提案しました。この方法により、トレーニング時に未知の制約を低コストで拡張することができます。さらに、カテゴリカルな制約と自由形式の制約の両方を処理する統一された方法も提案しました。実験により、提案手法が制約の正確さ、テキストの品質、拡張性においてベースラインよりも優れていることが示されました。</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/DataToText.html">#DataToText</a><a class="button" href="articles/ConceptToText.html">#ConceptToText</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/91">Toward Controlled Generation of Text, Hu+, ICML17</a>
<span class="snippet"><span>Comment</span>Text Generationを行う際は、現在は基本的に学習された言語モデルの尤度に従ってテキストを生成するのみで、outputされるテキストをcontrolすることができないので、できるようにしましたという論文。 VAEによるテキスト生成にGANを組み合わせたようなモデル。 decodingする元 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
