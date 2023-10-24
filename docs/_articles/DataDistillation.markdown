---
layout: post
title: DataDistillationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## DataDistillation
<div class="visible-content">
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/698">DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining, Sang Michael Xie+, N_A, arXiv23</a>
<span class="snippet">本論文では、言語モデルの性能に影響を与える事前学習データのドメインの混合比について、DoReMiという手法を提案する。DoReMiは、小さなプロキシモデルを使用してドメインの重みを生成し、再サンプリングして大きなモデルをトレーニングすることで、効率的にドメインの重みを見つけることができる。実験では ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2c0b125a-5ecc-4ee3-8c3b-022c03606c60" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><a class="button" href="articles/ChatGPT.html">#ChatGPT</a><br><span class="issue_date">Issue Date: 2023-05-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/700">LIMA: Less Is More for Alignment, Chunting Zhou+, N_A, arXiv23</a>
<span class="snippet">本研究では、65BパラメータのLLaMa言語モデルであるLIMAを訓練し、強化学習や人間の好みモデリングなしに、厳選された1,000のプロンプトとレスポンスのみで標準的な教師あり損失で微調整しました。LIMAは、幅広いクエリに対応する驚くべき強力なパフォーマンスを示し、トレーニングデータに現れなか ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/db025381-0bf0-47a3-bd18-5d88bff666df" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero_Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/Attention.html">#Attention</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/827">Dataset Distillation with Attention Labels for Fine-tuning BERT, ACL23</a>
<span class="snippet">本研究では、データセットの蒸留を使用して、元のデータセットのパフォーマンスを保持しながら、ニューラルネットワークを迅速にトレーニングするための小さなデータセットを作成する方法に焦点を当てています。具体的には、事前学習済みのトランスフォーマーを微調整するための自然言語処理タスクの蒸留されたfew-s ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><br><span class="issue_date">Issue Date: 2023-04-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/548">LaMini-instruction</a>
<span class="snippet">私たちは、大規模言語モデルからの知識を抽出するために、文/オフライン蒸留を行います。具体的には、いくつかの既存のプロンプトリソースに基づいて、合計258万ペアの指示と応答を生成します。詳細は論文を参照してください。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/23a85991-6af9-4663-a293-c22a6cdba9f0" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
