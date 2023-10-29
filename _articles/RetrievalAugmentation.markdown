---
layout: post
title: RetrievalAugmentationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## RetrievalAugmentation
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1070">Retrieval meets Long Context Large Language Models, Peng Xu+, N_A, arXiv23</a>
<span class="snippet">最先端の事前学習済みLLMsを使用して、リトリーバル拡張と長いコンテキストウィンドウの組み合わせについて研究しました。結果として、リトリーバル拡張LLMsは、ファインチューニングLLMsと比較しても高いパフォーマンスを示し、計算量も少ないことがわかりました。さらに、リトリーバルはLLMsのパフォー ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1074">RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective  Augmentation, Fangyuan Xu+, N_A, arXiv23</a>
<span class="snippet">ドキュメントの要約を生成することで、言語モデルの性能を向上させる手法を提案する。抽出型の圧縮器と抽象型の圧縮器を使用し、LMsの入力に要約を追加して訓練する。実験結果では、圧縮率が6％まで達成され、市販の要約モデルを上回る性能を示した。また、訓練された圧縮器は他のLMsにも転移可能であることが示さ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2756ba98-d228-45e6-972d-ef239d4b990e" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1105">Self-RAG: Learning to Retrieve, Generate, and Critique through  Self-Reflection, Akari Asai+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）は、事実に基づかない回答を生成することがあります。そこで、自己反省的な検索増強生成（Self-RAG）という新しいフレームワークを提案します。このフレームワークは、検索と自己反省を通じてLLMの品質と事実性を向上させます。実験結果は、Self-RAGが最先端のLLMsお ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/282eb6fd-d2bd-4804-a0bc-652158e2f857" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1100">LangChainのRAGの改善法, LayerX機械学習勉強会</a>
<span class="snippet">以下リンクからの引用。LangChainから提供されているRetrieverのcontext抽出の性能改善のためのソリューション> Multi representation indexing：検索に適した文書表現（例えば要約）の作成Query transformation：人間の質問を変換して ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1101">Evaluating RAG Pipelines</a>
<span class="snippet">RAG pipeline （retrieval + generation）を評価するライブラリRagasについて紹介されている。評価に活用される指標は下記で、背後にLLMを活用しているため、大半の指標はラベルデータ不要。ただし、context_recallを測定する場合はreference an ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/553e7f91-84cd-4aac-bef3-c84bc279547e" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
