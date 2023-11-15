---
layout: post
title: Spoken Language Processingに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Spoken Language Processing
<div class="visible-content">
<a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><a class="button" href="articles/AudioProcessing.html">#AudioProcessing</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/875">Meta-Transformer: A Unified Framework for Multimodal Learning, Yiyuan Zhang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、マルチモーダル学習のためのMeta-Transformerというフレームワークを提案しています。このフレームワークは、異なるモダリティの情報を処理し関連付けるための統一されたネットワークを構築することを目指しています。Meta-Transformerは、対応のないデータを使用して12のモダリティ間で統一された学習を行うことができ、テキスト、画像、ポイントクラウド、音声、ビデオなどの基本的なパーセプションから、X線、赤外線、高分光、IMUなどの実用的なアプリケーション、グラフ、表形式、時系列などのデータマイニングまで、幅広いタスクを処理することができます。Meta-Transformerは、トランスフォーマーを用いた統一されたマルチモーダルインテリジェンスの開発に向けた有望な未来を示しています。</span>
<span class="snippet"><span>Comment</span>12種類のモダリティに対して学習できるTransformerを提案Dataをsequenceにtokenizeし、unifiedにfeatureをencodingし、それぞれのdownstreamタスクで学習 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/8734073a-573e-442e-8b9f-fed559199d56" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/SpokenLanguageGeneration.html">#SpokenLanguageGeneration</a><br><span class="issue_date">Issue Date: 2023-05-04</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/620">Bark</a>
<span class="snippet"><span>Comment</span>テキストプロンプトで音声生成ができるモデル。MIT License ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/527">CLAP</a>
<span class="snippet"><span>Comment</span>テキストとオーディオの大量のペアを事前学習することで、テキストとオーディオ間を同じ空間に写像し、類似度を測れるようにしたモデルたとえばゼロショットでaudio分類ができる![image](https://user-images.githubusercontent.com/12249301/23429 ...</span>
</div>
