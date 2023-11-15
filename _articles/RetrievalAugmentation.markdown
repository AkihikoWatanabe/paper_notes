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
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-11-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1116">The Perils & Promises of Fact-checking with Large Language Models, Dorian Quelle+, N_A, arXiv23</a>
<span class="snippet">自律型の事実チェックにおいて、大規模言語モデル（LLMs）を使用することが重要である。LLMsは真実と虚偽を見分ける役割を果たし、その出力を検証する能力がある。本研究では、LLMエージェントを使用して事実チェックを行い、推論を説明し、関連する情報源を引用する能力を評価した。結果は、文脈情報を備えた ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/1f310edd-58f3-4e45-ac40-e75337bff884" alt="image"><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-11-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1118">Retrieval-based LM （RAG System）ざっくり理解する, 2023</a>
<span class="snippet">（以下スクショはスライドより引用）次のスクショはRAGにかかわる周辺技術がよくまとまっていると思う。以下ざっくり私の中の認識として計画    クエリ拡張        クエリの質が悪い場合検索性能が劣化するため、クエリをより適切に検索ができるように修正（昔 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/35f9f589-770c-435b-8d1b-81e615e86597" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1136">ChatGPTに社内文書に基づいた回答を生成させる仕組みを構築しました, 2023</a>
<span class="snippet">低コストで社内文書に対するRAGを実現することに注力している。以下、図はブログから引用。基本的にはバッチジョブで社内文書をベクトル化しS3へ格納。アプリ起動時にS3から最新データを読み込み検索可能にしRAGするという流れ。低コスト化のために、Embedding作成にOpenSourceの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/5f71b0b7-14bb-442d-99c8-09a0b3840210" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1100">LangChainのRAGの改善法, LayerX機械学習勉強会</a>
<span class="snippet">以下リンクからの引用。LangChainから提供されているRetrieverのcontext抽出の性能改善のためのソリューション> Multi representation indexing：検索に適した文書表現（例えば要約）の作成Query transformation：人間の質問を変換して ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1101">Evaluating RAG Pipelines</a>
<span class="snippet">RAG pipeline （retrieval + generation）を評価するライブラリRagasについて紹介されている。評価に活用される指標は下記で、背後にLLMを活用しているため、大半の指標はラベルデータ不要。ただし、context_recallを測定する場合はreference an ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/553e7f91-84cd-4aac-bef3-c84bc279547e" alt="image"><a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1113">幻日さんのUsefulMaterials（RAG等）</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-11-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1125">Boosting RAG: Picking the Best Embedding & Reranker models</a>
<span class="snippet">No description ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
