---
layout: post
title: In-ContextLearningに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## In-ContextLearning
<div class="visible-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Alignment.html">#Alignment</a><br><span class="issue_date">Issue Date: 2023-12-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1179">The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context  Learning, Bill Yuchen Lin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>アラインメント調整は、大規模言語モデル（LLMs）のパフォーマンスを向上させるために使用されます。しかし、アラインメント調整の効果は「表面的」である可能性があります。この研究では、基本的なLLMとアラインメント調整されたバージョンのトークン分布のシフトを分析しました。結果は、アラインメント調整が主にスタイルトークンに影響を与えることを示しました。さらに、シンプルでチューニングフリーなアラインメント手法であるURIALを導入し、基本的なLLMのパフォーマンスを向上させることができることを示しました。これらの結果から、アラインメントのより深い分析と理論的な理解が重要であることが示唆されます。</span>
<span class="snippet"><span>Comment</span>モデルの知識はPre-training時に十分獲得されており、モデルのAlignmentをとることで生じるものは表面的な変化のみであるという仮説がある。この仮説に関して分析をし、結果的にスタイリスティックな情報を生成する部分でAlignmentの有無で違いが生じることを明らかにし、そうであればわざわ ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/b8c62b33-dd72-43ea-8953-abb5c04cc504" alt="image"><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/ImageSegmentation.html">#ImageSegmentation</a><a class="button" href="articles/Prompting.html">#Prompting</a><br><span class="issue_date">Issue Date: 2023-11-23</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1160">Visual In-Context Prompting, Feng Li+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、ビジョン領域における汎用的なビジュアルインコンテキストプロンプティングフレームワークを提案します。エンコーダーデコーダーアーキテクチャを使用し、さまざまなプロンプトをサポートするプロンプトエンコーダーを開発しました。さらに、任意の数の参照画像セグメントをコンテキストとして受け取るように拡張しました。実験結果から、提案手法が非凡な参照および一般的なセグメンテーション能力を引き出し、競争力のあるパフォーマンスを示すことがわかりました。</span>
<span class="snippet"><span>Comment</span>Image Segmentationには、ユーザが与えたプロンプトと共通のコンセプトを持つすべてのオブジェクトをセグメンテーションするタスクと、ユーザの入力の特定のオブジェクトのみをセグメンテーションするタスクがある。従来は個別のタスクごとに、特定の入力方法（Visual Prompt, Image ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/f5da3d7b-68aa-4120-a37c-7c42be1704f8" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-10-26</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1090">In-Context Learning Creates Task Vectors, Roee Hendel+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）におけるインコンテキスト学習（ICL）の基本的なメカニズムはまだ十分に理解されていない。本研究では、ICLによって学習される関数が非常に単純な構造を持つことを示し、ICLがトランスフォーマーLLMを使用して単一のタスクベクトルを生成し、それを使用して出力を生成するということを明らかにする。さまざまなモデルとタスクにわたる実験によって、この主張を支持している。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんとツイートの引用>In-Context Learningの文脈中で計算された最後の活性値をθとし、クエリに対する結果を求める際に文脈に注意を当てず、活性値にθをコピーして予測してもICLと近い性能を達成できる。θはタスクを要約したタスクベクトルとみなせLLMは前向き計算でタIC ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Analysis.html">#Analysis</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><br><span class="issue_date">Issue Date: 2023-09-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1029">CausalLM is not optimal for in-context learning, Nan Ding+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>最近の研究では、トランスフォーマーベースのインコンテキスト学習において、プレフィックス言語モデル（prefixLM）が因果言語モデル（causalLM）よりも優れたパフォーマンスを示すことがわかっています。本研究では、理論的なアプローチを用いて、prefixLMとcausalLMの収束挙動を分析しました。その結果、prefixLMは線形回帰の最適解に収束する一方、causalLMの収束ダイナミクスはオンライン勾配降下アルゴリズムに従い、最適であるとは限らないことがわかりました。さらに、合成実験と実際のタスクにおいても、causalLMがprefixLMよりも性能が劣ることが確認されました。</span>
<span class="snippet"><span>Comment</span>以下hillbigさんのツイートの引用> In-Context Learningで文脈中サンプルの学習が仮想的に行われるが、CausalLM（各トークンは自分より前のみ注意対象）はオンライン学習の解に対応するがステップ幅が減衰しないため最適解に収束せず、PrefixLM（文脈中トークンは全て注意対C ...</span>
<a class="button" href="articles/Pretraining.html">#Pretraining</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/857">Pre-Training to Learn in Context, ACL23</a>
<span class="snippet"><span>Summary</span>インコンテキスト学習は、タスクの例と文脈からタスクを実行する方法であり、注目されています。しかし、現在の方法では十分に活用されていないため、私たちはPICLというフレームワークを提案します。これは、一般的なテキストコーパスでモデルを事前学習し、文脈に基づいてタスクを推論して実行する能力を向上させます。私たちは、PICLでトレーニングされたモデルのパフォーマンスを評価し、他のモデルを上回ることを示しました。コードはGitHubで公開されています。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LabelBias.html">#LabelBias</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/833">Mitigating Label Biases for In-context Learning, ACL23</a>
<span class="snippet"><span>Summary</span>インコンテキスト学習（ICL）におけるラベルバイアスの種類を定義し、その影響を軽減するための方法を提案する研究が行われました。特に、ドメインラベルバイアスについて初めて概念化され、その影響を軽減するためのバイアス補正方法が提案されました。この方法により、GPT-JとGPT-3のICLパフォーマンスが大幅に改善されました。さらに、異なるモデルやタスクにも一般化され、ICLにおけるラベルバイアスの問題を解決する手法として有効であることが示されました。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/InductiveBias.html">#InductiveBias</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/830">Measuring Inductive Biases of In-Context Learning with Underspecified Demonstrations, ACL23</a>
<span class="snippet"><span>Summary</span>インコンテキスト学習（ICL）は、大規模言語モデル（LLMs）を新しいタスクに適応させるための重要なパラダイムですが、ICLの一般化の振る舞いはまだ十分に理解されていません。本研究では、ICLの帰納的なバイアスについて調査を行いました。具体的には、不完全なデモンストレーションが与えられた場合、ICLはどのフィーチャーをより頻繁に使用する傾向があるのかを調べました。実験の結果、LLMsが明確なフィーチャーバイアスを示すことがわかりました。また、特定のフィーチャーを好むような帰納的なバイアスを課すためのさまざまな介入の効果も評価しました。全体として、ICLがより頻繁に利用する可能性のあるフィーチャーのタイプと、意図したタスクとより一致した帰納的なバイアスを課す方法について、より広範な情報を提供する結果となりました。</span>
<a class="button" href="articles/Efficiency/SpeedUp.html">#Efficiency/SpeedUp</a><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Zero/Few-shot.html">#Zero/Few-shot</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/817">FiD-ICL: A Fusion-in-Decoder Approach for Efficient In-Context Learning, ACL23</a>
<span class="snippet"><span>Summary</span>大規模な事前学習モデルを使用したfew-shot in-context learning（ICL）において、fusion-in-decoder（FiD）モデルを適用することで効率とパフォーマンスを向上させることができることを検証する。FiD-ICLは他のフュージョン手法と比較して優れたパフォーマンスを示し、推論時間も10倍速くなる。また、FiD-ICLは大規模なメタトレーニングモデルのスケーリングも可能にする。</span>
<a class="button" href="articles/General.html">#General</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Composition.html">#Composition</a><br><span class="issue_date">Issue Date: 2023-07-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/814">How Do In-Context Examples Affect Compositional Generalization?, ACL23</a>
<span class="snippet"><span>Summary</span>本研究では、組成的な一般化を調査するためのテストスイートであるCoFeを提案し、インコンテキスト学習の組成的な一般化について研究しました。インコンテキストの例の選択が組成的な一般化のパフォーマンスに影響を与えることを発見し、類似性、多様性、複雑さの要素を研究しました。さらに、架空の単語に対する組成的な一般化は一般的な単語に比べて弱いことが観察されました。インコンテキストの例が言語構造をカバーすることが重要であることも示されました。</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/793">Lost in the Middle: How Language Models Use Long Contexts, Nelson F. Liu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>最近の言語モデルは、長い文脈を入力として受け取ることができますが、その長い文脈をどれだけうまく利用しているかについてはまだよくわかっていません。この研究では、マルチドキュメントの質問応答とキー・バリューの検索という2つのタスクにおいて、言語モデルのパフォーマンスを分析しました。その結果、関連情報が入力文脈の始まりや終わりにある場合、パフォーマンスが最も高くなることがわかりましたが、長い文脈の中で関連情報にアクセスする必要がある場合、パフォーマンスが著しく低下します。さらに、入力文脈が長くなるにつれて、明示的に長い文脈を扱うモデルでもパフォーマンスが大幅に低下します。この分析は、言語モデルが入力文脈をどのように利用しているかをより良く理解するためのものであり、将来の長い文脈モデルのための新しい評価プロトコルを提供します。</span>
<span class="snippet"><span>Comment</span>元ツイートhttps://twitter.com/drjimfan/status/1678460065811136512?s=46&t=5BO_qSlNBSEGSugyUlP5Hw非常に重要な知見がまとめられている1. モデルはコンテキストのはじめと最後の情報をうまく活用でき、真ん中の情報をうまく活 ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/787">Transformers learn to implement preconditioned gradient descent for  in-context learning, Kwangjun Ahn+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>トランスフォーマーは勾配降下法のアルゴリズムを学習できるかどうかについての研究があります。この研究では、トランスフォーマーが勾配降下法の反復をシミュレートすることができることが示されています。さらに、線形トランスフォーマーについての分析から、訓練目的のグローバル最小値が事前条件付き勾配降下法の単一の反復を実装することが証明されました。また、k個のアテンション層を持つトランスフォーマーについても、特定の臨界点が事前条件付き勾配降下法のk回の反復を実装することが証明されました。これらの結果は、トランスフォーマーを訓練して学習アルゴリズムを実装するための将来の研究を促しています。</span>
<span class="snippet"><span>Comment</span>元ツイートhttps://twitter.com/hillbig/status/1678525778492018688?s=46&t=5BO_qSlNBSEGSugyUlP5Hwつまり、事前学習の段階でIn context learningが可能なように学習がなされているということなのか。それはどの ...</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-05-20</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/693">What In-Context Learning Learns In-Context: Disentangling Task  Recognition and Task Learning, Jane Pan+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）がどのようにコンテキスト学習（ICL）を利用してタスクを解決するかを調査しました。タスク認識（TR）とタスク学習（TL）の役割を分離するための実験を行い、LLMsがデモンストレーションを通じて暗黙的に学習を行う可能性があることを示しました。また、モデルがスケールするにつれてTLのパフォーマンスが改善されることも明らかになりました。これらの結果は、ICLの背後にある2つの異なる力を明らかにし、将来のICL研究でそれらを区別することを提唱しています。</span>
<span class="snippet"><span>Comment</span>LLMがIn context Learningで新しい何かを学習しているのかを調査TaskRecognition（TR）はGround Truth無しでデモンストレーションのみで実施TaskLearning（TL）は訓練データになかったテキストとラベルのマッピングを捉える必要があるタスク。TR ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/729cc613-7487-47be-9225-e02921091969" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
