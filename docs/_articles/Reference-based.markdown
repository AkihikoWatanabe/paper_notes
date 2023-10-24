---
layout: post
title: Reference-basedに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Reference-based
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/972">WIDAR -- Weighted Input Document Augmented ROUGE, Raghav Jain+, N_A, ECIR22</a>
<span class="snippet">自動テキスト要約の評価において、ROUGEメトリックには制約があり、参照要約の利用可能性に依存している。そこで、本研究ではWIDARメトリックを提案し、参照要約だけでなく入力ドキュメントも使用して要約の品質を評価する。WIDARメトリックは一貫性、整合性、流暢さ、関連性の向上をROUGEと比較して ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/973">InfoLM: A New Metric to Evaluate Summarization & Data2Text Generation, Pierre Colombo+, N_A, AAAI22</a>
<span class="snippet">自然言語生成システムの品質評価は高価であり、人間の注釈に頼ることが一般的です。しかし、自動評価指標を使用することもあります。本研究では、マスクされた言語モデルを使用した評価指標であるInfoLMを紹介します。この指標は同義語を処理することができ、要約やデータ生成の設定で有意な改善を示しました。 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/Reference-free.html">#Reference-free</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/983">FFCI: A Framework for Interpretable Automatic Evaluation of  Summarization, Fajri Koto+, N_A, JAIR22</a>
<span class="snippet">本論文では、FFCIという細かい要約評価のためのフレームワークを提案しました。このフレームワークは、信頼性、焦点、カバレッジ、および文間の連続性の4つの要素から構成されています。新しいデータセットを構築し、評価メトリックとモデルベースの評価方法をクロス比較することで、FFCIの4つの次元を評価する ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/987">SMART: Sentences as Basic Units for Text Evaluation, Reinald Kim Amplayo+, N_A, arXiv22</a>
<span class="snippet">本研究では、テキスト生成の評価指標の制限を緩和するために、新しい指標であるSMARTを提案する。SMARTは文を基本的なマッチング単位とし、文のマッチング関数を使用して候補文と参照文を評価する。また、ソースドキュメントの文とも比較し、評価を可能にする。実験結果は、SMARTが他の指標を上回ることを ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/953">Towards Question-Answering as an Automatic Metric for Evaluating the Content Quality of a Summary, Deutsch+, TACL21</a>
<span class="snippet">要約の品質を評価するための新しい指標であるQAEvalを提案する。QAEvalは質問応答（QA）を使用して要約と参照の情報の重複を測定するため、従来のテキストの重複に基づく指標とは異なる。実験結果から、QAEvalは現在の最先端の指標よりも優れたパフォーマンスを示し、他の評価とも競争力があることが ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-05-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/668">BERTScore: Evaluating Text Generation with BERT, Tianyi Zhang+, N_A, ICLR20</a>
<span class="snippet">BERTScoreは、文脈埋め込みを使用してトークンの類似度を計算するテキスト生成の自動評価メトリックであり、363の機械翻訳および画像キャプションシステムの出力を使用して評価されました。BERTScoreは、既存のメトリックよりも人間の判断との相関が高く、より強力なモデル選択性能を提供し、敵対的 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/a620d564-72e3-4078-97e2-1ff62b333324" alt="image"><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/TrainedMetrics.html">#TrainedMetrics</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/944">BLEURT: Learning Robust Metrics for Text Generation, Sellam+, ACL20</a>
<span class="snippet">BLEURTは、BERTをベースとした学習済みの評価指標であり、人間の判断と高い相関を持つことが特徴です。BLEURTは、数千のトレーニング例を使用してバイアスのある評価をモデル化し、数百万の合成例を使用してモデルの汎化を支援します。BLEURTは、WMT Metrics共有タスクとWebNLGデ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/982">HOLMS: Alternative Summary Evaluation with Large Language Models, Mrabet+, COLING20</a>
<span class="snippet">要約手法の評価尺度として、ROUGEとBLEUが一般的に使用されているが、これらは語彙的な性質を持ち、ニューラルネットワークのトレーニングには限定的な可能性がある。本研究では、大規模なコーパスで事前学習された言語モデルと語彙的類似度尺度を組み合わせた新しい評価尺度であるHOLMSを提案する。実験に ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/946">MoverScore: Text Generation Evaluating with Contextualized Embeddings and Earth Mover Distance, Zhao+, EMNLP-IJCNLP19</a>
<span class="snippet">本研究では、テキスト生成システムの評価尺度について調査し、システムの出力と参照テキストの意味に基づいて比較する尺度を提案します。この尺度は、要約、機械翻訳、画像キャプション、データからテキストへの生成などのタスクで有効であり、文脈化表現と距離尺度を組み合わせたものが最も優れています。また、提案した ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/ImageCaptioning.html">#ImageCaptioning</a><br><span class="issue_date">Issue Date: 2023-05-10</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/670">CIDEr: Consensus-based Image Description Evaluation, Ramakrishna Vedantam+, N_A, CVPR15</a>
<span class="snippet">画像を文章で自動的に説明することは、長年の課題である。本研究では、人間の合意を利用した画像説明の評価のための新しいパラダイムを提案し、新しい自動評価指標と2つの新しいデータセットを含む。提案手法は、人間の判断をより正確に捉えることができ、5つの最先端の画像説明手法を評価し、将来の比較のためのベンチ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/978"> From word embeddings to document distances, Kusner+, PMLR15</a>
<span class="snippet">私たちは、新しい距離関数であるWord Mover's Distance（WMD）を提案しました。WMDは、テキストドキュメント間の非類似性を測定するために使用されます。私たちの研究では、単語埋め込みの最新の結果に基づいてWMDを開発しました。WMDは、単語が別のドキュメントの単語に到達するために ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/MachineTranslation.html">#MachineTranslation</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/985">chrF: character n-gram F-score for automatic MT evaluation, Mono Popovic, WMT15</a>
<span class="snippet">私たちは、機械翻訳の評価に文字n-gram Fスコアを使用することを提案します。私たちは、このメトリックがシステムレベルとセグメントレベルで人間のランキングと相関しており、特にセグメントレベルでの相関が非常に高いことを報告しました。この提案は非常に有望であり、WMT14の共有評価タスクでも最高のメ ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><a class="button" href="articles/TrainedMetrics.html">#TrainedMetrics</a><br><span class="issue_date">Issue Date: 2023-08-14</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/988">Supervised automatic evaluation for summarization with voted regression model, Hirao+, Information and Processing & Management07</a>
<span class="snippet">要約システムの評価には高品質な人間の評価が必要だが、コストが高いため自動評価方法が必要。提案手法は投票回帰モデル（VRM）を使用し、従来の自動評価方法と比較してエラー削減を達成。さらに、最も高い相関係数を得た。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Metrics.html">#Metrics</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Evaluation.html">#Evaluation</a><br><span class="issue_date">Issue Date: 2023-08-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/947">Learning to Score System Summaries for Better Content Selection Evaluation, Peyard+, Prof. of the Workshop on New Frontiers in Summarization</a>
<span class="snippet">本研究では、古典的な要約データセットを使用して、人間の判断に基づいた自動スコアリングメトリックの学習を提案します。既存のメトリックを組み込み、人間の判断と高い相関を持つ組み合わせを学習します。新しいメトリックの信頼性は手動評価によってテストされます。学習済みのメトリックはオープンソースのツールとし ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
