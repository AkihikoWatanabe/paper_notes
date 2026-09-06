# paper_notes
![Open issues](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes) ![Stars](https://img.shields.io/github/stars/AkihikoWatanabe/paper_notes) ![visitors](https://visitor-badge.laobi.icu/badge?page_id=akihiko_watanabe.paper_notes) ![License](https://img.shields.io/github/license/AkihikoWatanabe/paper_notes)  
[![AI Research Trends](https://img.shields.io/badge/Wiki-Trends-blue)](https://github.com/AkihikoWatanabe/paper_notes/wiki/X%E4%B8%8A%E3%81%AEAI%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89%EF%BC%88%EF%BC%9F%EF%BC%89%EF%BC%88%E5%80%8B%E4%BA%BA%E3%81%AE%E6%84%9F%E6%83%B3%E3%81%A7%E3%81%99%EF%BC%89)
[![DeepWiki (Devin)](https://img.shields.io/badge/DeepWiki(Devin)-Chat-800080?logo=readme)](https://deepwiki.com/AkihikoWatanabe/paper_notes)
[![CodeWiki (Google)](https://img.shields.io/badge/CodeWiki(Google)-Chat-800080?logo=readme)]([https://deepwiki.com/AkihikoWatanabe/paper_notes](https://codewiki.google/github.com/akihikowatanabe/paper_notes))

[![Initial Impression Notes](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/Initial%20Impression%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Initial%20Impression%20Notes")
[![One-Line Notes](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/One-Line%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22One-Line%20Notes%22)
[![Surface-level Notes](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/Surface-level%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Surface-level%20Notes%22)
[![KeyPoint Notes](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/KeyPoint%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22KeyPoint%20Notes%22)
[![Reading Reflections](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/Reading%20Reflections)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reading%20Reflections%22)
[![In-Depth Notes](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/In-Depth%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22In-Depth%20Notes%22)
[![Reference Collection](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/Reference%20Collection)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reference%20Collection%22)
[![Author Thread-Post](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes/Author%20Thread-Post)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Author%20Thread-Post%22)

[[English](https://github.com/AkihikoWatanabe/paper_notes/blob/master/README.md) | 日本語]

AI関連の論文やブログ・リポジトリ・スライド・SNSポスト等を手動で収集し、Issueで管理しているリポジトリです。  
主にリポジトリの管理人が勉強した内容の備忘録のために、論文のメモを**日本語**で残しています。
GitHub Issuesで管理されるメモはdailyで`agent_docs/`以下にダンプされ、エージェントを通じて対話できます。[対話インタフェース](#対話インタフェース)を参照してください。

## Issueの記載内容

Issueには主に以下の内容がメモされています:
- 🔗 論文/ブログ等のリンク
- 📄 論文のAbstract, メタデータ [^1]
- 🌐 Abstractの日本語訳と日本語要約 [^1]
- 📝 管理人の理解に基づいたメモ
- 🏷️ 管理人の内容理解に基づいた手動でのラベル
- 📚 参考になる外部リンク

論文のメタデータや Abstract は arXiv APIから取得しています。  
また、管理人が日本人であるため、Abstractの日本語訳・日本語での要約をGPTで自動生成しています。

---

## 現在積極的に収集している分野

現在は以下の4つの分野のメモが多めだと思います:

- Natural Language Processing (NLP)
- Computer Vision (CV)
- Speech Processing
- Recommender Systems (RecSys)

---

## 最近関心の強いトピック

最近関心の強いトピックは以下となります（ただし収集していくメモはこれらに限りません）:

- Large Language Models (LLMs) / Vision-Language Models (VLMs) / Diffusion Models
- Proprietary / Open-Weight / Open-Source Models
- Multimodal Models / Unified Multimodal Models (UMMs)
- AI Agents / Context Engineering / Memory / Evaluation Harnesses / Scaffoldings
- (Synthetic) Datasets / Evaluation / Benchmarks
- Pre-training / Mid-training / Post-training / Continual Learning
- Reinforcement Learning
- Test-time Scaling / (Memory-based) Test-time Learning / Test Time Training (TTT)
- Representation Learning / Embeddings
- Self-Improving AI / Recursive Self-Improvement
- Transformer architectures (Attention, Positional Encoding, Residual Streams, etc.)

---

## Issue中のメモとメモの粒度

各Issueには以下が主に含まれています:

- 管理人の理解や解釈 [^2]
- Abstractや関連ポスト、論文を斜め読みした上での第一印象
- 収集元ポストやSNS上の解説ポスト

メモの粒度はその時々の可処分時間や関心によって変わっており、以下のラベルで管理されています（後からラベルを追加したのでまだ全てのメモに付与しきれていません）:

- [![Initial Impression Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Initial%20Impression%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Initial%20Impression%20Notes"): Abstract, 関連ポスト, 論文をななめ読みをした後の第一印象
- [![One-Line Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/One-Line%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22One-Line%20Notes%22): 一言メモ
- [![Surface-level Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Surface-level%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Surface-level%20Notes%22): 論文全体の要約
- [![KeyPoint Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/KeyPoint%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22KeyPoint%20Notes%22): 論文のキーとなるポイントのまとめ
- [![Reading Reflections](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Reading%20Reflections)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reading%20Reflections%22): （読了後、あるいはskim reading後の）感想、意見
- [![In-Depth Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/In-Depth%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22In-Depth%20Notes%22): 論文の詳細と個人的な感想や意見
- [![Reference Collection](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Reference%20Collection)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reference%20Collection%22): SNS上の有識者の解説ポスト等の関連リンク集
- [![Author Thread-Post](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Author%20Thread-Post)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Author%20Thread-Post%22): 論文・ブログ等の著者自身による解説ポスト

---

## Label Taxonomy

ラベルの分類は以下となっており、色分けして管理しています:

- **媒体**: [![Blog](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Blog)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ABlog), [![Video](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Video)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AVideo), [![Slide](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Slide)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ASlide), ...

- **研究分野**: [![NLP](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/NLP)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ANLP), [![ComputerVision](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ComputerVision)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AComputerVision), [![SpeechProcessing](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/SpeechProcessing)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ASpeechProcessing), [![RecommenderSystems](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/RecommenderSystems)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ARecommenderSystems), ...

- **タスク**: [![DocumentSummarization](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/DocumentSummarization)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ADocumentSummarization), [![MachineTranslation](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/MachineTranslation)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AMachineTranslation), [![Evaluation](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Evaluation)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AEvaluation), ...

- **手法**: [![LanguageModel](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/LanguageModel)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ALanguageModel), [![AIAgents](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/AIAgents)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AAIAgents), [``![ReinforcementLearning](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ReinforcementLearning)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AReinforcementLearning), ...

- **細分類**: [![OpenWeight](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/OpenWeight)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AOpenWeight), [![AttentionSinks](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/AttentionSinks)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AAttentionSinks), [![Architecture](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Architecture)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AArchitecture), ...

- **性質・特徴**: [![Controllable](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Controllable)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AControllable), [![EfficiencyImprovement](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/EfficiencyImprovement)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AEfficiencyImprovement), [![LowResource](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/LowResource)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ALowResource), ...

- **会議 / ジャーナル**: [![ACL](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ACL)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AACL), [![CVPR](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/CVPR)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ACVPR), [![TACL](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/TACL)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ATACL), ...


上記ラベルは一例であり、600以上のユニークラベルが存在します。これらのラベルによってIssueをフィルタリングすることができます。

---

## Wiki / {Deep, Code}Wiki

Issueでの管理に加えて、2種類の補足的なコンテンツがあります。

### [Wiki](https://github.com/AkihikoWatanabe/paper_notes/wiki): 個人の観測に基づく研究トレンドに関するノート

個人が観測した範囲に基づくAI関連の研究のトレンドをWikiにメモしています。このメモについては以下の点にご留意ください:

- Wiki中のメモはあくまで個人が観測した範囲内部での主観的な判断や解釈に基づいたものです
- 不正確な点や見落とし、バイアスなどが間違いなく存在します
- 更新は不定期です

---

### 対話インタフェース

本リポジトリをローカルにcloneし、エージェントを用いてIssueに収集された情報に基づいてchatできます。

```bash
git clone https://github.com/AkihikoWatanabe/paper_notes.git
cd paper_notes
```

以下に質問と応答の例を示します（gpt-5.6-luna, reasoning_effort=medium）:

> 過去1年間の事前学習の研究について、時系列に従ってまとめてください。表形式でreferenceも用意してください。

<details>
<summary>回答例（クリックして展開）</summary>

### 時系列まとめ

| 日付 | 研究 | 主な内容・意義 |
|---|---|---|
| 2025-09-17 | [MachineLearningLM](https://arxiv.org/abs/2509.06806) | 継続事前学習により、LLMのmany-shot in-context learning能力を強化。 |
| 2025-09-20 | [Pre-training under infinite compute](https://arxiv.org/abs/2509.14786) | 限られたデータを前提に、正則化・モデル拡大・アンサンブル・蒸留によるデータ効率化を検討。 |
| 2025-09-22 | [Synthetic Bootstrapped Pretraining](https://arxiv.org/abs/2509.15248) | 文書間の関係を学習し、共有概念をもとに新しい訓練文書を合成。 |
| 2025-09-24 | [Reinforcement Learning on Pre-Training Data](https://arxiv.org/abs/2509.19249) | 強化学習によって事前学習データの選択・利用を最適化。 |
| 2025-09-25 | [Thinking Augmented Pre-training](https://arxiv.org/abs/2509.20186) | 思考過程を含むデータを事前学習に導入し、reasoning能力を形成。 |
| 2025-10-01 | [Scaling Law of Mixture-of-Experts](https://arxiv.org/abs/2509.23678) | MoEにおけるモデルサイズ、expert数、計算量、トークン数の関係を分析。 |
| 2025-10-03 | [Demystifying Synthetic Data](https://arxiv.org/abs/2510.01631) | 合成データの量・生成モデル・混合比率が性能に与える影響を系統的に評価。 |
| 2025-10-18 | [Beyond Multi-Token Prediction](https://arxiv.org/abs/2510.14751) | 将来の要約表現を予測する補助目的により、長期的な意味表現を学習。 |
| 2025-11-12 | [Why Less is More](https://arxiv.org/abs/2511.03492) | データ量の増加だけでなく、情報密度の高いデータキュレーションを検討。 |
| 2025-12-04 | [PretrainZero](https://arxiv.org/abs/2512.03442) | 強化学習を用いて、事前学習中に有用なデータを能動的に探索・選択。 |
| 2026-01-30 | [Self-Improving Pretraining](https://arxiv.org/abs/2601.21343) | post-training済みモデルで高品質なデータを生成し、次のモデルを学習する自己改善ループ。 |
| 2026-02-05 | [Noisy Data and LLM Pretraining Loss Divergence](https://arxiv.org/abs/2602.02400) | ノイズの種類・量・モデル規模が事前学習のloss発散に与える影響を分析。 |
| 2026-02-12 | [Data Darwinism](https://arxiv.org/abs/2602.07824) | LLMによる生成的洗練・認知的補完を用いて、高品質な科学データを構築。 |
| 2026-02-12 | [OPUS](https://arxiv.org/abs/2602.05400) | optimizerが生む更新方向を基準に、訓練サンプルの有用性を動的に評価。 |
| 2026-05-13 | [Compute Optimal Tokenization](https://arxiv.org/abs/2605.01188) | tokenizerを事前学習の計算量に対して最適化。 |
| 2026-05-23 | [A Bitter Lesson for Data Filtering](https://arxiv.org/abs/2605.19407) | 大規模モデル・十分な計算量では、強いデータ除外より広いデータ利用が有利になる可能性を検証。 |
| 2026-08-07 | [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/abs/2607.25271) | 計算量最適とデータ量最適のトレードオフを検討。 |
| 2026-08-14 | [Hyperball Optimization](https://arxiv.org/abs/2606.16899) | 勾配更新の幾何構造を利用して、事前学習の安定性・効率を改善。 |

この期間の主な傾向は、次のとおりです。

- データ量の拡大から、データ選択・混合・合成・情報密度の最適化へ移行
- 次トークン予測から、文書間関係・思考過程・将来要約などへ事前学習目的を拡張
- reasoning能力をpost-trainingだけでなく、事前学習段階から形成
- MoE、低精度計算、tokenizer、optimizerを含むスケーリング則の再検討
- モデルによるデータ改善と、そのデータによる次世代モデル学習という共進化

</details>

エージェントは、リポジトリ内の `AGENTS.md` の指示と `agent_docs/` を参照し、Issueや勉強ノートに基づいて回答できます。
`agent_docs/` 以下にはdailyでIssueの内容がxml形式でダンプされています。

従来どおり、以下のDeepWiki/CodeWikiから対話形式で探索することもできます。

### [DeepWiki](https://deepwiki.com/AkihikoWatanabe/paper_notes)/[CodeWiki](https://codewiki.google/github.com/akihikowatanabe/paper_notes)

DeepWiki/CodeWikiを利用することで、Issueで管理されている情報に対話ベースでアクセスできます。
これにより、興味のある情報を対話形式で探索できます。

---

## Updates

**2026.03.07**
- Agenticなユースケースのために、AGENTS.mdとエージェント用のドキュメントをagent_docに追加しました。これにより、AI AgentがHTMLの余分な文字列でcontextを浪費することを防止します。

**2026.01.20**
- README.mdを更新しました。

**2025.10.17**  
- X上で流れてくる論文のストリーミングを眺めていて個人が感じたトレンド（感想）をメモする[Wiki](https://github.com/AkihikoWatanabe/paper_notes/wiki)を作ってみました
- 個人の感想なので誤り等あるかもしれませんがご容赦ください。ゆるりと不定期に更新していきます

**2025.08.05**  
- 本リポジトリの使い方としては、現状本リポジトリの[DeepWiki](https://deepwiki.com/AkihikoWatanabe/paper_notes)を通じて対話形式で何らかの文献や資料、知識を抽出するという方法が一番使いやすいかもしれません

**2025.07.19**  
- ブログのレスポンスタイムが悪化していた問題を改善しました
- ブログの表示コンテンツを変更しました
- （リニューアルはまだです🫠

**2024.12.28**  
- ブログをリニューアルしたいと思い早くもNカ月が過ぎ去りました

**2024.09**
- Issueにメモした内容をブログ形式にしてみました。
- ブログは[こちら](https://akihikowatanabe.github.io/paper_notes/).

**2017.12.28**
- リポジトリを作成し、最初のIssueを作成しました。

---

## Star History
<a href="https://www.star-history.com/?repos=AkihikoWatanabe%2Fpaper_notes&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AkihikoWatanabe/paper_notes&type=date&theme=dark&legend=top-left&sealed_token=wC6UGRkA6T4FCkrJn63IaVH8smYc8Sy2GTNBrpp_sEamF_oFjcJg4uyJkIHTuueUi7-bPlfEN7D54CYMooWYcnSkfwTqv7aq9PgjaChryTReLHiDK0kcW9UuHZ-wsnt3HCXpOIxapU_FjR63bsJPHVo_WzK44mik4lKijQfvnpBCoNhwKeo1rPc9a0kX" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AkihikoWatanabe/paper_notes&type=date&legend=top-left&sealed_token=wC6UGRkA6T4FCkrJn63IaVH8smYc8Sy2GTNBrpp_sEamF_oFjcJg4uyJkIHTuueUi7-bPlfEN7D54CYMooWYcnSkfwTqv7aq9PgjaChryTReLHiDK0kcW9UuHZ-wsnt3HCXpOIxapU_FjR63bsJPHVo_WzK44mik4lKijQfvnpBCoNhwKeo1rPc9a0kX" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AkihikoWatanabe/paper_notes&type=date&legend=top-left&sealed_token=wC6UGRkA6T4FCkrJn63IaVH8smYc8Sy2GTNBrpp_sEamF_oFjcJg4uyJkIHTuueUi7-bPlfEN7D54CYMooWYcnSkfwTqv7aq9PgjaChryTReLHiDK0kcW9UuHZ-wsnt3HCXpOIxapU_FjR63bsJPHVo_WzK44mik4lKijQfvnpBCoNhwKeo1rPc9a0kX" />
 </picture>
</a>

[^1]: メタデータと論文の Abstract は arXiv API の terms of use に記載されている CC0 1.0 License に基づいて利用しています。
[^2]: Issue/Blog中の画像やスクリーンショットは原則Issue中に記載してあるリンク（元論文、元記事、元スライド等）から引用したものです。
