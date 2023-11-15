---
layout: post
title: Abstractiveに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Abstractive
<div class="visible-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/FactualConsistency.html">#FactualConsistency</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/865">Improving Factuality of Abstractive Summarization without Sacrificing Summary Quality, ACL23</a>
<span class="snippet"><span>Summary</span>事実性を意識した要約の品質向上に関する研究はあるが、品質を犠牲にすることなく事実性を向上させる手法がほとんどない。本研究では「Effective Factual Summarization」という技術を提案し、事実性と類似性の指標の両方で大幅な改善を示すことを示した。トレーニング中に競合を防ぐために2つの指標を組み合わせるランキング戦略を提案し、XSUMのFactCCでは最大6ポイント、CNN/DMでは11ポイントの改善が見られた。また、類似性や要約の抽象性には負の影響を与えない。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/859">Abstractive Summarizers are Excellent Extractive Summarizers, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、抽出型要約と要約型要約の相乗効果を探求し、シーケンス・トゥ・シーケンス・アーキテクチャを使用した3つの新しい推論アルゴリズムを提案しています。これにより、要約型システムが抽出型システムを超えることができることを示しました。また、要約型システムは抽出型のオラクル要約にさらされることなく、両方の要約を単一のモデルで生成できることも示しました。これは、抽出型ラベルの必要性に疑問を投げかけるものであり、ハイブリッドモデルの有望な研究方向を示しています。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Conversation.html">#Conversation</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/836">TACL Abstractive Meeting Summarization: A Survey, TACL23</a>
<span class="snippet"><span>Summary</span>会議の要約化において、深層学習の進歩により抽象的要約が改善された。本論文では、抽象的な会議の要約化の課題と、使用されているデータセット、モデル、評価指標について概説する。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><a class="button" href="articles/pretrained-LM.html">#pretrained-LM</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/816">Z-Code++: A Pre-trained Language Model Optimized for Abstractive Summarization, ACL23</a>
<span class="snippet"><span>Summary</span>この論文では、新しい事前学習言語モデルであるZ-Code++を提案し、抽象的なテキスト要約に最適化されています。Z-Code++は、2つのフェーズの事前学習とディセントラル化アテンション層、およびエンコーダー内のフュージョンを使用しています。このモデルは、低リソースの要約タスクで最先端の性能を発揮し、パラメータ効率的であり、他の競合モデルを大幅に上回ります。</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2022-09-02</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/482">Long Document Summarization with Top-down and Bottom-up Inference, Pang+, Salesforce Research, arXiv22</a>
<span class="snippet"><span>Comment</span>日本語解説: https://zenn.dev/ty_nlp/articles/9f5e5dd3084dbd以下、上記日本語解説記事を読んで理解した内容をまとめます。ありがとうございます。# 概要基本的にTransformerベースのモデル（e.g. BERTSum, BART,>The  ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/135">Get To The Point: Summarization with Pointer-Generator Networks, See+, ACL17</a>
<span class="snippet"><span>Comment</span>解説スライド：https://www.slideshare.net/akihikowatanabe3110/get-to-the-point-summarization-with-pointergenerator-networks/1単語の生成と単語のコピーの両方を行えるハイブリッドなニューラル文書 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/134">A Deep Reinforced Model for Abstractive Summarization, Paulus+（with Socher）, arXiv17</a>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/133">Cutting-off redundant repeating generations for neural abstractive summarization, Suzuki+, EACL17</a>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/136">Incorporating Copying Mechanism in Sequence-to-Sequence Learning, Gu+, ACL16</a>
<span class="snippet"><span>Comment</span>解説スライド：https://www.slideshare.net/akihikowatanabe3110/incorporating-copying-mechanism-in-sequene-to-sequence-learning単語のコピーと生成、両方を行えるネットワークを提案。locati ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/132">Distraction-Based Neural Networks for Modeling Documents, Chen+, IJCAI16</a>
<span class="snippet"><span>Comment</span>Neuralなモデルで「文書」の要約を行う研究。提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。distractionを導入するmotivationは、入力文書中の異なる情報を横断 ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/73">Distraction-Based Neural Networks for Modeling Documents, Chen+, IJCAI16</a>
<span class="snippet"><span>Comment</span>Neuralなモデルで「文書」の要約を行う研究。提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。distractionを導入するmotivationは、入力文書中の異なる情報を横断Dist ...</span>
<a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2017-12-31</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/137">A Neural Attention Model for Sentence Summarization, Rush+, EMNLP15</a>
<span class="snippet"><span>Comment</span>解説スライド：https://www.slideshare.net/akihikowatanabe3110/a-neural-attention-model-for-sentence-summarization-65612331 ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Sentence.html">#Sentence</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/75">LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP15</a>
<span class="snippet"><span>Comment</span>Large Chinese Short Text Summarization (LCSTS) datasetを作成データセットを作成する際は、Weibo上の特定のorganizationの投稿の特徴を利用。Weiboにニュースを投稿する際に、投稿の冒頭にニュースのvery short sCop ...</span>
<a class="button" href="articles/Single.html">#Single</a><a class="button" href="articles/DocumentSummarization.html">#DocumentSummarization</a><a class="button" href="articles/Document.html">#Document</a><a class="button" href="articles/Supervised.html">#Supervised</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Extractive.html">#Extractive</a><br><span class="issue_date">Issue Date: 2018-01-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/143">Learning to Generate Coherent Sumamry with Discriminative Hidden Semi-Markov Model, Nishikawa+, COLING14</a>
<span class="snippet"><span>Comment</span>Hidden-semi-markovモデルを用いた単一文書要約手法を提案。通常のHMMでは一つの隠れ状態に一つのunit（要約の文脈だと文？）が対応するが、hidden-semi-markov(HSMM)モデルでは複数のunitを対応づけることが可能。隠れ状態に対応するunitを文だと考評価に ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
