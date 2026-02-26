# paper_notes
![Open issues](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes) ![Stars](https://img.shields.io/github/stars/AkihikoWatanabe/paper_notes) ![License](https://img.shields.io/github/license/AkihikoWatanabe/paper_notes)

[[English](https://github.com/AkihikoWatanabe/paper_notes/blob/master/README.md) | 日本語]

AI関連の論文やブログ・リポジトリ・スライド・SNSポスト等を手動で収集し、Issueで管理しているリポジトリです。  
主にリポジトリの管理人が勉強した内容の備忘録のために、論文のメモを**日本語**で残しています。

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
- Self-Improving AI
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
- [![In-Depth Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/In-Depth%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22In-Depth%20Notes%22): 論文の詳細と個人的な感想や意見
- [![Reference Collection](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Reference%20Collection)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reference%20Collection%22): SNS上の有識者の解説ポスト等の関連リンク集

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

## Wiki / DeepWiki

Issueでの管理に加えて、2種類の補足的なコンテンツがあります。

### [Wiki](https://github.com/AkihikoWatanabe/paper_notes/wiki): 個人の観測に基づく研究トレンドに関するノート

個人が観測した範囲に基づくAI関連の研究のトレンドをWikiにメモしています。このメモについては以下の点にご留意ください:

- Wiki中のメモはあくまで個人が観測した範囲内部での主観的な判断や解釈に基づいたものです
- 不正確な点や見落とし、バイアスなどが間違いなく存在します
- 更新は不定期です

---

### [DeepWiki](https://deepwiki.com/AkihikoWatanabe/paper_notes): 対話インタフェース

DeepWikiを利用することで、Issueで管理されている情報に対話ベースでアクセス可能です。
これにより、対話ベースで興味のある情報を探索できます。

---

## Updates

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
[![Star History Chart](https://api.star-history.com/svg?repos=AkihikoWatanabe/paper_notes&type=Date)](https://star-history.com/#AkihikoWatanabe/paper_notes&Date)

[^1]: メタデータと論文の Abstract は arXiv API の terms of use に記載されている CC0 1.0 License に基づいて利用しています。
[^2]: Issue/Blog中の画像やスクリーンショットは原則Issue中に記載してあるリンク（元論文、元記事、元スライド等）から引用したものです。
