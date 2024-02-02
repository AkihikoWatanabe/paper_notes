---
layout: post
title: LLM-as-a-Judgeに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## LLM-as-a-Judge
<div class="visible-content">
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2024-01-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1220">Large Language Models Are State-of-the-Art Evaluators of Translation Quality, EAMT23</a>
<span class="snippet"><span>Summary</span>GEMBAは、参照翻訳の有無に関係なく使用できるGPTベースの翻訳品質評価メトリックです。このメトリックは、ゼロショットのプロンプティングを使用し、4つのプロンプトバリアントを比較します。私たちの手法は、GPT 3.5以上のモデルでのみ機能し、最先端の精度を達成します。特に、英語からドイツ語、英語からロシア語、中国語から英語の3つの言語ペアで有効です。この研究では、コード、プロンプトテンプレート、およびスコアリング結果を公開し、外部の検証と再現性を可能にします。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/935">GPTScore: Evaluate as You Desire, Jinlan Fu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、生成型AIの評価における課題を解決するために、GPTScoreという評価フレームワークを提案しています。GPTScoreは、生成されたテキストを評価するために、生成型事前学習モデルの新たな能力を活用しています。19の事前学習モデルを探索し、4つのテキスト生成タスクと22の評価項目に対して実験を行いました。結果は、GPTScoreが自然言語の指示だけでテキストの評価を効果的に実現できることを示しています。この評価フレームワークは、注釈付きサンプルの必要性をなくし、カスタマイズされた多面的な評価を実現することができます。</span>
<span class="snippet"><span>Comment</span>BERTScoreと同様、評価したいテキストの対数尤度で評価しているBERTScoreよりも相関が高く、instructionによって性能が向上することが示されている ...</span>
</div>
