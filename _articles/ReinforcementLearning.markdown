---
layout: post
title: ReinforcementLearningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## ReinforcementLearning
<div class="visible-content">
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-08-08</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/919">Open Problems and Fundamental Limitations of Reinforcement Learning from  Human Feedback, Stephen Casper+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>人間のフィードバックからの強化学習（RLHF）は、AIシステムを人間の目標に合わせてトレーニングするための技術であり、最先端の大規模言語モデル（LLMs）を微調整するために使用されている。しかし、RLHFの欠点を体系化するための公開された研究は少ない。本論文では、RLHFのオープンな問題と制約を調査し、実践における理解、改善、補完技術を概説し、RLHFシステムの社会的な監視を向上させるための監査と開示の基準を提案する。この研究は、RLHFの制約を強調し、安全なAIシステムの開発に多面的なアプローチの重要性を強調している。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/RLHF.html">#RLHF</a><a class="button" href="articles/PPO.html">#PPO</a><br><span class="issue_date">Issue Date: 2023-07-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/807">Secrets of RLHF in Large Language Models Part I: PPO, Rui Zheng+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）を使用した人間中心のアシスタントの開発には、報酬設計やトレーニングの課題などの障壁があります。この研究では、強化学習（RLHF）のフレームワークを解析し、PPOアルゴリズムの内部動作を再評価し、ポリシーモデルのトレーニングの安定性を改善するための高度なバージョンを提案します。さらに、SFTモデルとChatGPTと比較してRLHFの能力を分析し、オープンソースの実装を公開することを目指しています。</span>
<span class="snippet"><span>Comment</span>RLHFとPPOをの内部構造を調査したレポート。RLHFに興味がある場合は読むべし。github: https://github.com/OpenLMLab/MOSS-RLHF ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Finetuning.html">#Finetuning</a><br><span class="issue_date">Issue Date: 2023-03-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/512">Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、言語エージェントを強化するための新しいフレームワークであるReflexionを提案しています。Reflexionエージェントは、言語的フィードバックを通じて自己反省し、より良い意思決定を促すために反省的なテキストを保持します。Reflexionはさまざまなタスクでベースラインエージェントに比べて大幅な改善を実現し、従来の最先端のGPT-4を上回る精度を達成しました。さらに、異なるフィードバック信号や統合方法、エージェントタイプの研究を行い、パフォーマンスへの影響についての洞察を提供しています。</span>
<span class="snippet"><span>Comment</span>なぜ回答を間違えたのか自己反省させることでパフォーマンスを向上させる研究 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Library.html">#Library</a><br><span class="issue_date">Issue Date: 2023-07-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/894">trl_trlx</a>
<span class="snippet"><span>Comment</span>TRL 強化学習によるLLMの学習のためのライブラリhttps://note.com/npaka/n/nbb974324d6e1trlを使って日本語LLMをSFTからRLHFまで一通り学習させてみるhttps://www.ai-shift.co.jp/techblog/3583 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
