---
layout: post
title: DataGenerationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## DataGeneration
<div class="visible-content">
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-10-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1099">Zephyr: Direct Distillation of LM Alignment, Lewis Tunstall+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、小さな言語モデルを作成するために、教師モデルからの優先データを使用する手法を提案しています。この手法により、自然なプロンプトに対するモデルの応答が改善されます。提案手法を用いて学習されたZephyr-7Bモデルは、チャットベンチマークで最先端の性能を発揮し、人間の注釈を必要としません。詳細はGitHubで利用可能です。</span>
<span class="snippet"><span>Comment</span>7BパラメータでLlaMa70Bと同等の性能を達成したZephyrの論文。dSFT:既存データからpromptをサンプリングし、user,assistantのmulti turnの対話をLLMでシミュレーションしてデータ生成しSFTAIF:既存データからpromstをサンプリングし ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/1348b3c1-f70a-49b6-97c9-4a27bf7805fa" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Transformer.html">#Transformer</a><a class="button" href="articles/DataAugmentation.html">#DataAugmentation</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-08-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1024">Prompt2Model: Generating Deployable Models from Natural Language  Instructions, Vijay Viswanathan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を使用して、プロンプトを自然言語でタスクを説明し、特定のモデルを訓練する手法であるPrompt2Modelを提案しています。Prompt2Modelは、既存のデータセットと事前学習済みモデルの検索、LLMsを使用したデータセットの生成、および教師あり微調整のプロセスを通じて行われます。実験結果では、Prompt2Modelが強力なLLMを上回る性能を示し、モデルの信頼性の評価も可能であることが示されています。Prompt2Modelはオープンソースで利用可能です。</span>
<span class="snippet"><span>Comment</span>以下AIDBの引用>プロンプトだけで自然言語処理モデルを作成するフレームワーク「Prompt2Model」が登場しました。カーネギーメロン大などの研究グループによる発表です。>○ Vijay Viswanathan et al. Prompt2Model: Generating DeploDatas ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/533">WizardLM: Empowering Large Language Models to Follow Complex Instructions, Xu+, Microsoft_Peking University, arXiv23</a>
<span class="snippet"><span>Comment</span>instruction trainingは大きな成功を収めているが、人間がそれらのデータを作成するのはコストがかかる。また、そもそも複雑なinstructionを人間が作成するのは苦労する。そこで、LLMに自動的に作成させる手法を提案している（これはself instructと一緒）。データを生成す ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/517">ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks, Gilardi+, University of Zurich, arXiv23</a>
<span class="snippet"><span>Comment</span># 概要2300件程度のツイートを分類するタスクにおいて、訓練した学部生によるアノテーションを正解とし、クラウドワーカーとChatGPTでのzero-shotでの予測の性能を比較した。分類タスクは、比較的難易度の高い分類問題であり、クラウドワーカーでも正解率は難しいタスクでは15~25%程度であ# ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
