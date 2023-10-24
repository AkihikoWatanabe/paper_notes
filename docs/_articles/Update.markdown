---
layout: post
title: Updateに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Update
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/ILP.html">#ILP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/31">Improving Update Summarization via Supervised ILP and Sentence Reranking, Li et al. NAACL’15</a>
<span class="snippet">・update summarizationをILPで定式化．基本的なMDSのILPのterm weightingにsalienceの要素に加えてnoveltyの要素を加える．term weightingにはbigramを用いる．bigram使うとよくなることがupdate summarization ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/35">Update Summarization using Semi-Supervised Learning Based on Hellinger Distance, Wang et al., CIKM’15</a>
<span class="snippet">うーん・・・ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/36">Incremental Update Summarization: Adaptive Sentence Selection based on Prevalence and Novelty, McCreadie et al., CIKM’14</a>
<span class="snippet">・timelyなeventに対してupdate summarizationを適用する場合を考える．たとえば6日間続いたeventがあったときにその情報をユーザが追う為に何度もupdate summarizationシステムを用いる状況を考える．6日間のうち新しい情報が何も出てこない期間はirrele ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/30">Update Summarization Based on Co-Ranking with Constraints, Wiaojun Wan, COLING’12</a>
<span class="snippet">・PageRankの枠組みを拡張してold datasetとnew dataset内のsentenceをco-ranking・co-rankingするときは，update scoreとconsistency scoreというものを求め相互作用させる．・update scoreが高いsente ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/38">DualSum: a Topic-Model based approach for update summarization, Delort et al., EACL’12</a>
<span class="snippet">・大半のupdate summarizationの手法はdocument set Aがgivenのとき，document set Bのupdate summarizationをつくる際には，redundancy removalの問題として扱っている．・この手法は，1つのsentenceの中にre ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/37">Document Update Summarization Using Incremental Hierarchical Clustering, Wang et al.,　CIKM’10</a>
<span class="snippet">・既存のMDSではdocumentをbatch処理するのが前提．typicalなクラスタリングベースの手法やグラフベースの手法はsentence-graphを構築して要約を行う．しかし，情報がsequentialに届き，realtimeで要約を行いたいときにこのような手法を使うと，毎回すでに処理した ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/32">A Scalable MMR Approach to Sentence Scoring for Multi-Document Update Summarization, Boudin et al., COLING’08</a>
<span class="snippet">・MMR #243 をupdate summarization用に拡張．History（ユーザが過去に読んだsentence）の数が多ければ多いほどnon-redundantな要約を出す （Queryに対するRelevanceよりもnon-redundantを重視する）・Historyの大きさに ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/33">The LIA Update Summarization Systems at TAC-2008, Boudin et al. TAC’08</a>
<span class="snippet">・Scalable MMR #32 とVariable length intersection gap n-term modelを組み合わせる．・Variable length intersection gap n-term modelは，あるトピックのterm sequenceは他の異なる語と ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/39">Update Summary Update, Copeck et al., TAC’08</a>
<span class="snippet">被引用数は少ないが、良い論文からreferされているイメージ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/34">TimedTextRank: Adding the Temporal Dimension to Multi-Document Summarization, Xiaojun Wan, SIGIR’07</a>
<span class="snippet">・evolving topicsを要約するときは，基本的に新しい情報が重要だが，TextRankはそれが考慮できないので拡張したという話．・dynamic document setのnew informationをより重視するTimedTextRankを提案・TextRankのvoteの部分 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/40">DUC 2007, Update Summarization Dataset</a>
<span class="snippet">No description ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
