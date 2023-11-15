---
layout: post
title: DataDistillationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## DataDistillation
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero_Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/827">Dataset Distillation with Attention Labels for Fine-tuning BERT, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、データセットの蒸留を使用して、元のデータセットのパフォーマンスを保持しながら、ニューラルネットワークを迅速にトレーニングするための小さなデータセットを作成する方法に焦点を当てています。具体的には、事前学習済みのトランスフォーマーを微調整するための自然言語処理タスクの蒸留されたfew-shotデータセットの構築を提案しています。実験結果では、注意ラベルを使用してfew-shotデータセットを作成し、BERTの微調整において印象的なパフォーマンスを実現できることを示しました。例えば、ニュース分類タスクでは、わずか1つのサンプルとわずか1つの勾配ステップのみで、元のデータセットの98.5％のパフォーマンスを達成しました。</span>
<span class="snippet"><span>Comment</span>Datadistillationしたら、データセットのうち1サンプルのみで、元のデータセットの98.5%の性能を発揮できたという驚異的な研究（まえかわ君） ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/ChatGPT.html">#ChatGPT</a><br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/700">LIMA: Less Is More for Alignment, Chunting Zhou+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、65BパラメータのLLaMa言語モデルであるLIMAを訓練し、強化学習や人間の好みモデリングなしに、厳選された1,000のプロンプトとレスポンスのみで標準的な教師あり損失で微調整しました。LIMAは、幅広いクエリに対応する驚くべき強力なパフォーマンスを示し、トレーニングデータに現れなかった未知のタスクにも一般化する傾向があります。制御された人間の研究では、LIMAのレスポンスは、GPT-4、Bard、DaVinci003と比較して優れていることが示されました。これらの結果から、大規模言語モデルのほとんどの知識は事前トレーニング中に学習され、高品質の出力を生成するためには限られた指示調整データしか必要ないことが示唆されます。</span>
<span class="snippet"><span>Comment</span>LLaMA65Bをたった1kのdata point（厳選された物）でRLHF無しでfinetuningすると、旅行プランの作成や、歴史改変の推測（？）幅広いタスクで高いパフォーマンスを示し、未知のタスクへの汎化能力も示した。最終的にGPT3,4,BARD,CLAUDEよりも人間が好む回答を返した。L ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/db025381-0bf0-47a3-bd18-5d88bff666df" alt="image"><a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/698">DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining, Sang Michael Xie+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、言語モデルの性能に影響を与える事前学習データのドメインの混合比について、DoReMiという手法を提案する。DoReMiは、小さなプロキシモデルを使用してドメインの重みを生成し、再サンプリングして大きなモデルをトレーニングすることで、効率的にドメインの重みを見つけることができる。実験では、DoReMiはThe PileやGLaMデータセットで高い精度を発揮し、few-shot下流精度を6.5％改善することができる。</span>
<span class="snippet"><span>Comment</span>事前学習する際の各ドメインのデータをどのような比率でmixtureするかの話。各ドメインごとに小さなproxy modelを訓練し、downstream taskの知識無しでドメインごとの重みを生成。データセットを生成されたドメインごとの重みに従いリサンプリングすることで、（1/30のプロキシモデル ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2c0b125a-5ecc-4ee3-8c3b-022c03606c60" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/548">LaMini-instruction</a>
<span class="snippet"><span>Summary</span>私たちは、大規模言語モデルからの知識を抽出するために、文/オフライン蒸留を行います。具体的には、いくつかの既存のプロンプトリソースに基づいて、合計258万ペアの指示と応答を生成します。詳細は論文を参照してください。</span>
<span class="snippet"><span>Comment</span>既存のInstruction DatasetのInstructionをseedとして、gpt-3.5-turboで新たなInstructionとresponseを生成したデータセット ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/23a85991-6af9-4663-a293-c22a6cdba9f0" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
