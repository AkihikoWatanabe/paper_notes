---
layout: post
title: Training-Freeに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Training-Free
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/945">SUPERT: Towards New Frontiers in Unsupervised Evaluation Metrics for Multi-Document Summarization, Gao+, ACL20</a>
<span class="snippet"><span>Summary</span>この研究では、教師なしの複数文書要約評価メトリックスについて調査しています。提案手法SUPERTは、擬似的な参照要約として選択された重要な文を使用し、文脈化埋め込みとソフトトークンアラインメント技術を用いて要約の品質を評価します。SUPERTは従来の教師なし評価メトリックスよりも人間の評価との相関が高く、18〜39％の向上が見られます。また、SUPERTを報酬として使用してニューラルベースの強化学習要約器をガイドすることで、有利なパフォーマンスを実現しています。ソースコードはGitHubで入手可能です。</span>
<span class="snippet"><span>Comment</span>pseudo-reference summaryを作成し、referenceに対してSBERTを適用しsystem-reference間の類似度を測ることで、unsupervisedに複数文書要約を評価する手法。まずTACのデータに対して、既存研究（single document summarips ...</span>
</div>
