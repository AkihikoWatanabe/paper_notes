---
layout: post
title: reviewに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## review
<div class="visible-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Explanation.html">#Explanation</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/862">Explainable Recommendation with Personalized Review Retrieval and Aspect Learning, ACL23</a>
<span class="snippet"><span>Summary</span>説明可能な推薦において、テキスト生成の精度向上とユーザーの好みの捉え方の改善を目指し、ERRAモデルを提案。ERRAは追加情報の検索とアスペクト学習を組み合わせることで、より正確で情報量の多い説明を生成することができる。さらに、ユーザーの関心の高いアスペクトを選択することで、関連性の高い詳細なユーザー表現をモデル化し、説明をより説得力のあるものにする。実験結果は、ERRAモデルが最先端のベースラインを上回ることを示している。</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/647">Towards Personalized Review Summarization by Modeling Historical Reviews  from Customer and Product Separately, Xin Cheng+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>レビュー要約は、Eコマースのウェブサイトにおいて製品レビューの主要なアイデアを要約することを目的としたタスクである。本研究では、評価情報を含む2種類の過去のレビューをグラフ推論モジュールと対比損失を用いて別々にモデル化するHHRRSを提案する。レビューの感情分類と要約を共同で行うマルチタスクフレームワークを採用し、4つのベンチマークデータセットでの徹底的な実験により、HHRRSが両方のタスクで優れた性能を発揮することが示された。</span>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/655">Transformer Reasoning Network for Personalized Review Summarization, Xu+, SIGIR21</a>
<span class="snippet"><span>Comment</span>先行研究は、review summarizationにおいて生成されるsummaryは、過去にユーザが作成したsummaryのwriting styleやproductに非常に関係しているのに、これらを活用してこなかったので、活用しました（=personalized）という話っぽい ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/656">A Unified Dual-view Model for Review Summarization and Sentiment  Classification with Inconsistency Loss, Hou Pong Chan+, N_A, arXiv20</a>
<span class="snippet"><span>Summary</span>ユーザーレビューから要約と感情を取得するために、新しいデュアルビューモデルを提案。エンコーダーがレビューの文脈表現を学習し、サマリーデコーダーが要約を生成。ソースビュー感情分類器はレビューの感情ラベルを予測し、サマリービュー感情分類器は要約の感情ラベルを予測。不一致損失を導入して、2つの分類器の不一致を罰することで、デコーダーが一貫した感情傾向を持つ要約を生成し、2つの感情分類器がお互いから学ぶことができるようになる。4つの実世界データセットでの実験結果は、モデルの効果を示している。</span>
<span class="snippet"><span>Comment</span>Review SummarizationとSentiment Classificationをjointで学習した研究。既存研究ではreviewのみからsentimentの情報を獲得する枠組みは存在したが、summaryの情報が活用できていなかった。#653 のratingをsentiment lし ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/658">Neural Review Summarization Leveraging User and Product Information, Liu+, CIKM19</a>
<a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-06</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/652">A Hierarchical End-to-End Model for Jointly Improving Text Summarization  and Sentiment Classification, Shuming Ma+, N_A, arXiv18</a>
<span class="snippet"><span>Summary</span>テキスト要約と感情分類を共同学習するための階層的なエンドツーエンドモデルを提案し、感情分類ラベルをテキスト要約の出力の「要約」として扱う。提案モデルはAmazonオンラインレビューデータセットでの実験で、抽象的な要約と感情分類の両方で強力なベースラインシステムよりも優れた性能を発揮することが示された。</span>
<span class="snippet"><span>Comment</span>review summarizationに初めてamazon online review data #653 使った研究？ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-05-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/663">Empirical analysis of exploiting review helpfulness for extractive summarization of online reviews, Xiong+, COLING14</a>
<span class="snippet"><span>Comment</span>レビューのhelpfulnessを利用したunsupervisedなreview summarization手法を提案。helpfulessによりレビューをフィルタリングするだけでなく、トピックモデルでsentenceをクラスタリングする際にhelpfulnessの情報も活用している模様。最 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/OpinionMining.html">#OpinionMining</a><br><span class="issue_date">Issue Date: 2023-05-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/662">Mining and summarizing customer reviews, Hu+, KDD04</a>
<span class="snippet"><span>Comment</span>レビュー中のユーザが記述したopinion sentenceを同定し、極性がpos/negのどちらかを判定し、pos/negそれぞれの代表的なsentenceを抽出することで要約する手法評価をする際は、Amazon等のレビューを収集し、人間がレビューを読み、どれがopinion senten ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/PersonalizedDocumentSummarization.html">#PersonalizedDocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Personalization.html">#Personalization</a><br><span class="issue_date">Issue Date: 2023-05-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/648">Personalized summarization of customer reviews based on user’s browsing history, Zehra+, International Journal on Computer Science and Information Systems 8.2, 12</a>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
