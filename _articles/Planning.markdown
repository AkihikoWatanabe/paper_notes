---
layout: post
title: Planningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Planning
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-21</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/696">Chain-of-Symbol Prompting Elicits Planning in Large Langauge Models, Hanxu Hu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本論文では、LLMsを使用して複雑な計画タスクを解決するための新しいベンチマークであるNatural Language Planning（NLP）を提案し、CoSという新しい手法を導入して、LLMsがシンボリック表現をより理解しやすくすることを示した。CoSはChatGPTやInstructGPTでの入力トークン数を削減し、Brick Worldで60.8％の精度を達成するなど、性能の向上を実現した。</span>
<span class="snippet"><span>Comment</span>LLMは複雑なプランニングが苦手なことが知られており、複雑な環境を自然言語ではなく、spatialでsymbolicなトークンで表現することで、プランニングの性能が向上したという話 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/50e9d7e2-bd75-4341-b7a0-394dc2eaf915" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/526">LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, Liu+, University of Texas at Austin, arXiv23</a>
<span class="snippet"><span>Comment</span>LLMは長いプランニングをすることが苦手だったが、classicalなplannerは適切なinputの形式に変換されていればすぐに最適なプランを導出できる、が、自然言語は受け付けない、といった互いが互いを補完し合う関係にあるので、両者を組み合わせました、という話。LLMを利用して、plannin ...</span>
</div>
