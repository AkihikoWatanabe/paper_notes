---
layout: post
title: Generalに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## General
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1047">RAIN: Your Language Models Can Align Themselves without Finetuning, Yuhui Li+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、追加のデータなしで凍結された大規模言語モデル（LLMs）を整列させる方法を探求しました。自己評価と巻き戻しメカニズムを統合することで、LLMsは自己ブースティングを通じて人間の好みと一致する応答を生成することができることを発見しました。RAINという新しい推論手法を導入し、追加のデータやパラメータの更新を必要とせずにAIの安全性を確保します。実験結果は、RAINの効果を示しており、LLaMA 30Bデータセットでは無害率を向上させ、Vicuna 33Bデータセットでは攻撃成功率を減少させることができました。</span>
<span class="snippet"><span>Comment</span>トークンのsetで構成されるtree上を探索し、出力が無害とself-evaluationされるまで、巻き戻しと前方生成を繰り返し、有害なトークンsetの重みを動的に減らすことでalignmentを実現する。モデルの追加のfinetuning等は不要。self-evaluationでは下記のようなp ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/05bebc0a-325b-423d-ae36-4bc5698063fe" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/RepresentationLearning.html">#RepresentationLearning</a><a class="button" href="articles/EssayScoring.html">#EssayScoring</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/847">Improving Domain Generalization for Prompt-Aware Essay Scoring via Disentangled Representation Learning, ACL23</a>
<span class="snippet"><span>Summary</span>自動エッセイスコアリング（AES）は、エッセイを評価するためのモデルですが、既存のモデルは特定のプロンプトにしか適用できず、新しいプロンプトに対してはうまく汎化できません。この研究では、プロンプトに依存しない特徴とプロンプト固有の特徴を抽出するためのニューラルAESモデルを提案し、表現の汎化を改善するための分離表現学習フレームワークを提案しています。ASAPとTOEFL11のデータセットでの実験結果は、提案手法の有効性を示しています。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/In-Context Learning.html">#In-Context Learning</a><a class="button" href="articles/Composition.html">#Composition</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/814">How Do In-Context Examples Affect Compositional Generalization?, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、組成的な一般化を調査するためのテストスイートであるCoFeを提案し、インコンテキスト学習の組成的な一般化について研究しました。インコンテキストの例の選択が組成的な一般化のパフォーマンスに影響を与えることを発見し、類似性、多様性、複雑さの要素を研究しました。さらに、架空の単語に対する組成的な一般化は一般的な単語に比べて弱いことが観察されました。インコンテキストの例が言語構造をカバーすることが重要であることも示されました。</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/RecommenderSystems.html">#RecommenderSystems</a><a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/Embed.html">#Embed</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><br><span class="issue_date">Issue Date: 2017-12-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/68">StarSpace: Embed All The Things, Wu+, arXiv17</a>
<span class="snippet"><span>Comment</span>分類やランキング、レコメンドなど、様々なタスクで汎用的に使用できるEmbeddingの学習手法を提案。Embeddingを学習する対象をEntityと呼び、Entityはbag-of-featureで記述される。Entityはbag-of-featureで記述できればなんでもよく、こ実際にS ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
