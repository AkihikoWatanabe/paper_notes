---
layout: post
title: LongSequenceに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## LongSequence
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1060">Effective Long-Context Scaling of Foundation Models, Wenhan Xiong+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、長いコンテキストをサポートする一連のLLMsを提案します。これらのモデルは、長いテキストを含むデータセットでトレーニングされ、言語モデリングや他のタスクで評価されます。提案手法は、通常のタスクと長いコンテキストのタスクの両方で改善をもたらします。また、70Bバリアントはgpt-3.5-turbo-16kを上回るパフォーマンスを実現します。さらに、私たちはLlamaの位置エンコーディングや事前学習プロセスの設計選択の影響についても分析しました。結果から、長いコンテキストの継続的な事前学習が効果的であることが示されました。</span>
<span class="snippet"><span>Comment</span>以下elvis氏のツイートの意訳Metaが32kのcontext windowをサポートする70BのLLaMa2のvariant提案し、gpt-3.5-turboをlong contextが必要なタスクでoutperform。short contextのLLaMa2を継続的に訓練して実現。これ位置エ ...</span>
<a class="button" href="articles/Efficiency_SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1045">LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models, Yukang Chen+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、計算コストを制限しながら大規模言語モデル（LLMs）のコンテキストサイズを拡張する効率的なファインチューニング手法であるLongLoRAを提案します。従来の方法では、LLMsの長いコンテキストサイズでのトレーニングには高い計算コストとGPUリソースが必要でしたが、提案手法ではコンテキスト拡張を高速化し、非自明な計算コストの削減を実現します。また、パラメータ効率的なファインチューニング手法も再評価し、LongLoRAはさまざまなタスクで強力な実験結果を示しています。さらに、教師ありファインチューニングのためのデータセットであるLongQAも収集されました。</span>
<span class="snippet"><span>Comment</span># 概要context長が大きい場合でも効率的にLoRAする手法。通常のLoRAではcontext lengthが大きくなるにつれてperplexityが大きくなってしまう。一方、通常のFinetuningではperplexityは高い性能を維持するが、計算コストとVRAMの消費量が膨大になって ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/fc3d17c7-b1ac-4741-9895-bce70cf0b356" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/PositionalEncoding.html">#PositionalEncoding</a><br><span class="issue_date">Issue Date: 2023-07-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/820">Randomized Positional Encodings Boost Length Generalization of Transformers, ACL23</a>
<span class="snippet"><span>Summary</span>トランスフォーマーは、固定長のタスクにおいては優れた汎化能力を持つが、任意の長さのシーケンスには対応できない。この問題を解決するために、新しい位置エンコーディング手法を提案する。ランダム化された位置エンコーディングスキームを使用し、長いシーケンスの位置をシミュレートし、順序付けられたサブセットをランダムに選択する。大規模な実証評価により、この手法がトランスフォーマーの汎化能力を向上させ、テストの正確性を平均して12.0％向上させることが示された。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-07-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/777">How Long Can Open-Source LLMs Truly Promise on Context Length?, 2023</a>
<span class="snippet"><span>Comment</span>LLMのcontext長を伸ばす際の方法と得られた知見がまとめられている ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-27</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/560">Unleashing Infinite-Length Input Capacity for Large-scale Language Models with Self-Controlled Memory System, 2023</a>
<span class="snippet"><span>Comment</span>> Our findings indicate that our system outperforms ChatGPT in handling ultra-long inputs or conversations.と書いてあるが、定量評価の結果が全く書いていない模様。全くもって信用できない。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
