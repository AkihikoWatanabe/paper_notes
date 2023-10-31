---
layout: post
title: PersonalizedHeadlineGenerationに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## PersonalizedHeadlineGeneration
<div class="visible-content">
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-07-22</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/893">Generating User-Engaging News Headlines, ACL23</a>
<span class="snippet"><span>Summary</span>ニュース記事の見出しを個別化するために、ユーザープロファイリングを組み込んだ新しいフレームワークを提案。ユーザーの閲覧履歴に基づいて個別のシグネチャフレーズを割り当て、それを使用して見出しを個別化する。幅広い評価により、提案したフレームワークが多様な読者のニーズに応える個別の見出しを生成する効果を示した。</span>
<span class="snippet"><span>Comment</span># モチベーション推薦システムのヘッドラインは未だに全員に同じものが表示されており、ユーザが自身の興味とのつながりを正しく判定できるとは限らず、推薦システムの有用性を妨げるので、ユーザごとに異なるヘッドラインを生成する手法を提案した。ただし、クリックベイトは避けるようなヘッドラインを生成しなけれ# ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/847933e1-deb2-4379-addb-6cdd65e29ee8" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-08-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/929">Personalized News Headline Generation System with Fine-grained User Modeling, Yao, MSN22</a>
<span class="snippet"><span>Summary</span>ユーザーの興味に基づいてパーソナライズされたニュースの見出しを生成するために、文レベルの情報を考慮したユーザーモデルを提案する。アテンション層を使用して文とニュースの関連性を計算し、ニュースの内容に基づいて見出しを生成する。実験結果は、提案モデルがベースラインモデルよりも優れたパフォーマンスを示していることを示している。将来の方向性として、情報のレベルと内容を横断する相互作用についても議論されている。</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-08-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/928">Personalized Headline Generation with Enhanced User Interest Perception, Zhang+, ICANN22</a>
<span class="snippet"><span>Summary</span>ユーザーのニュース閲覧履歴をモデル化し、個別化されたニュース見出しを生成するための新しいフレームワークを提案する。提案手法は、ユーザーの興味を強調するために候補テキストに関連する情報を活用し、ニュースのエンティティワードを使用して興味表現を改善する。幅広い実験により、提案手法が見出し生成タスクで優れたパフォーマンスを示すことが示されている。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/PersonalizedGeneration.html">#PersonalizedGeneration</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-05-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/706">PENS: A Dataset and Generic Framework for Personalized News Headline Generation, ACL21</a>
<span class="snippet"><span>Summary</span>この論文では、ユーザーの興味とニュース本文に基づいて、ユーザー固有のタイトルを生成するパーソナライズされたニュース見出し生成の問題を解決するためのフレームワークを提案します。また、この問題のための大規模なデータセットであるPENSを公開し、ベンチマークスコアを示します。データセットはhttps://msnews.github.io/pens.htmlで入手可能です。</span>
<span class="snippet"><span>Comment</span># 概要ニュース記事に対するPersonalizedなHeadlineの正解データを生成。103名のvolunteerの最低でも50件のクリックログと、200件に対する正解タイトルを生成した。正解タイトルを生成する際は、各ドキュメントごとに4名異なるユーザが正解タイトルを生成するようにした。これ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/cd4fa969-03c0-4539-bcec-25ba3204ffc9" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
