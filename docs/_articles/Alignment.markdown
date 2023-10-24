---
layout: post
title: Alignmentに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Alignment
<div class="visible-content">
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/918">Aligning Large Language Models with Human: A Survey, Yufei Wang+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデル（LLMs）は、自然言語処理のタスクにおいて重要な役割を果たしていますが、その性能には制約があります。この調査では、LLMsの性能を向上させるためのアラインメント技術について包括的な概要を提供します。具体的には、データ収集方法、トレーニング手法、モデル評価方法について説明します。さ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/6c5288c8-7f5b-4526-ba6f-25c2b9b3fc55" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1063">Large Language Model Alignment: A Survey, Tianhao Shen+, N_A, arXiv23</a>
<span class="snippet">近年、大規模言語モデル（LLMs）の進歩が注目されていますが、その潜在能力と同時に懸念もあります。本研究では、LLMsのアライメントに関する既存の研究と新たな提案を包括的に探求し、モデルの解釈可能性や敵対的攻撃への脆弱性などの問題も議論します。さらに、LLMsのアライメントを評価するためのベンチマ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/09c10110-798f-4493-b431-41c2f2b017c1" alt="image"><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/237">The Mathematics of Statistical Machine Translation: Parameter Estimation, Brown+, CL13</a>
<span class="snippet">IBMモデル論文。 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/233">A Phrase-Based HMM Approach to Document_Abstract Alignment, Daume+, EMNLP04</a>
<span class="snippet">AbstractsとSource TextのAlignmentをとるために、Phrase-Based HMMを提案。Ziff-Davis Corpusのテキストに対して、2人のannotatorによってgold standardを作成。評価においてMTにおけるIBM Model4やHMM b ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/Tools.html">#Tools</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/239">A systematic comparison of various statistical alignment models, Och+, CL03, Giza++</a>
<span class="snippet">評価の際は、Sure, Possibleの二種類のラベルによる単語アライメントのground-truth作成も行っている ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/219">The automatic construction of large-scale corpora for summarization research. Daniel Marcu. SIGIR’99</a>
<span class="snippet"><Abstract, Text>のタプルが与えられた時に、<Abstract, Extract, Text>のタプルを自動的に生成。ExtractはAbstractと対応するText中の重要部（節やsentence）。<Abstract, Extract, Text>に含まれるExtract ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/220">The Decomposition of Human-Written Summary Sentences. Hongyan Jing et al. SIGIR’99.</a>
<span class="snippet">参照要約 原文書対が与えられた時に、参照要約中の単語と原文書中の単語のアライメントをとるHMMベースな手法を提案。![image](https://user-images.githubusercontent.com/12249301/34812500-2d1d7d32-f6e9-11e7 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/232">Generating Extraction-Based Summaries from Hand-Written Summaries by Aligning Text Spans, Banko+, PACLING99</a>
<span class="snippet">文を単位とし、文を文中の単語の出現頻度ベクトルで表し、ベクトル間の距離で文間の類似度を計ることで自由作成要約中の文と現文中の文をもっとも類似度が大きくなるように対応づける。（奥村先生のSurveyより：https://www.jstage.jst.go.jp/article/jnlp1994/9 ...</span>
<a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/238"> HMM-based word alignment in statistical translation, Vogel+, COLING96</a>
<span class="snippet">No description ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2018-01-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/236">ALAGIN 機械翻訳セミナー 単語アライメント, Graham Neubig</a>
<span class="snippet">Neubigさんによる単語アライメントチュートリアル ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
