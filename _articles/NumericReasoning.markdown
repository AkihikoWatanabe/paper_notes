---
layout: post
title: NumericReasoningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## NumericReasoning
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Dataset.html">#Dataset</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/InstructionTuning.html">#InstructionTuning</a><a class="button" href="articles/Mathematics.html">#Mathematics</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1050">MAmmoTH: Building Math Generalist Models through Hybrid Instruction  Tuning, Xiang Yue+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>MAmmoTHは、数学の問題解決に特化した大規模言語モデルであり、厳密にキュレーションされた教育データセットで訓練されています。このモデルは、CoTとPoTのハイブリッドな根拠を提供し、さまざまな数学の分野を包括的にカバーしています。MAmmoTHは、既存のオープンソースモデルを大幅に上回り、特にMATHデータセットで高い精度を示しています。この研究は、多様な問題のカバレッジとハイブリッドな根拠の使用の重要性を強調しています。</span>
<span class="snippet"><span>Comment</span>9つのmath reasoningが必要なデータセットで13-29%のgainでSoTAを達成。260kの根拠情報を含むMath Instructデータでチューニングされたモデル。project page: https://tiger-ai-lab.github.io/MAmmoTH/ ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/851">A Survey of Deep Learning for Mathematical Reasoning, ACL23</a>
<span class="snippet"><span>Summary</span>数学的な推論とディープラーニングの関係についての調査論文をレビューし、数学的な推論におけるディープラーニングの進歩と将来の研究方向について議論しています。数学的な推論は機械学習と自然言語処理の分野で重要であり、ディープラーニングモデルのテストベッドとして機能しています。また、大規模なニューラル言語モデルの進歩により、数学的な推論に対するディープラーニングの利用が可能になりました。既存のベンチマークと方法を評価し、将来の研究方向についても議論しています。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/797">Teaching Arithmetic to Small Transformers, Nayoung Lee+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、GPT-4のような大規模言語モデルが、教師なしのトークン予測目的に明示的にエンコードされていないにもかかわらず、算術演算や基本的な関数を効率的に学習できることを示しています。訓練データのフォーマットの変更やchain-of-thoughtスタイルのデータの使用により、精度や収束速度が改善されます。また、訓練中の算術とテキストデータの相互作用やモデルのスケールの影響も研究されています。この研究は、高品質な指導的なデータが算術能力の引き出しにおいて重要であることを強調しています。</span>
<span class="snippet"><span>Comment</span>小規模なtransformerに算術演算を学習させ、どのような学習データが効果的か調査。CoTスタイルの詳細なスクラッチパッドを学習データにすることで、plainなもの等と比較して、予測性能や収束速度などが劇的に改善した結局next token predictionで学習させているみたいだけど、本当 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/42e60fc0-d04b-4338-922c-5a46b69890b9" alt="image"></div>
