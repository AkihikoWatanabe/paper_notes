---
layout: post
title: Promptに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Prompt
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/AutomaticPromptEngineering.html">#AutomaticPromptEngineering</a><br><span class="issue_date">Issue Date: 2023-11-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1128">Prompt Engineering a Prompt Engineer, Qinyuan Ye+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>プロンプトエンジニアリングは、LLMsのパフォーマンスを最適化するための重要なタスクであり、本研究ではメタプロンプトを構築して自動的なプロンプトエンジニアリングを行います。改善されたパフォーマンスにつながる推論テンプレートやコンテキストの明示などの要素を導入し、一般的な最適化概念をメタプロンプトに組み込みます。提案手法であるPE2は、さまざまなデータセットやタスクで強力なパフォーマンスを発揮し、以前の自動プロンプトエンジニアリング手法を上回ります。さらに、PE2は意味のあるプロンプト編集を行い、カウンターファクトの推論能力を示します。</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><br><span class="issue_date">Issue Date: 2023-10-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1110">Re-Reading Improves Reasoning in Language Models, Xiaohan Xu+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）において、推論は重要で困難な問題です。従来のアプローチでは、プロンプティング戦略を開発することに焦点が当てられてきましたが、双方向の相互作用や質問の重要性には注意が払われていませんでした。この問題に対処するため、質問の再読という新しいプロンプティング戦略を提案します。再読は、質問情報を再訪することで、LLMsの推論能力を向上させることができます。実験結果は、この手法の効果と汎用性を示しており、LLMsの領域でのその有用性を強調しています。</span>
<span class="snippet"><span>Comment</span>問題文を2,3回promptで繰り返すだけで、数学のベンチマークとCommonsenseのベンチマークの性能が向上したという非常に簡単なPrompting。self-consistencyなどの他のPromptingとの併用も可能。なぜ性能が向上するかというと、1. LLMはAuporegresこの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/e575e0aa-b76c-444e-b9b0-e984d6fc73cf" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1078">Meta-CoT: Generalizable Chain-of-Thought Prompting in Mixed-task  Scenarios with Large Language Models, Anni Zou+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を使用して、推論のためのチェーン・オブ・ソート（CoT）プロンプトを生成する方法を提案しています。従来のCoTの方法では、一般的なプロンプトや手作業デモンストレーションに依存していましたが、本研究では入力質問のタイプに基づいて自動的にプロンプトを生成するMeta-CoTを提案しています。Meta-CoTは、10のベンチマーク推論タスクで優れたパフォーマンスを示し、SVAMPでは最先端の結果を達成しました。また、分布外データセットでも安定性と汎用性が確認されました。</span>
<span class="snippet"><span>Comment</span>色々出てきたがなんかもう色々組み合わせれば最強なんじゃね?って気がしてきた。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/bb51c119-c1bc-4033-a7d4-f403d3c82d30" alt="image"></div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-10-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1076">Take a Step Back: Evoking Reasoning via Abstraction in Large Language  Models, Huaixiu Steven Zheng+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>Step-Back Promptingは、大規模言語モデル（LLMs）を使用して推論の手順をガイドするシンプルなプロンプティング技術です。この技術により、LLMsは具体的な詳細から高レベルの概念や基本原則を抽象化し、正しい推論経路をたどる能力を向上させることができます。実験により、Step-Back PromptingはSTEM、Knowledge QA、Multi-Hop Reasoningなどのタスクにおいて大幅な性能向上が観察されました。具体的には、MMLU Physics and Chemistryで7%、11%、TimeQAで27%、MuSiQueで7%の性能向上が確認されました。</span>
<span class="snippet"><span>Comment</span>以下AIDBのツイートの引用> LLMに聞きたいことの一歩後ろから質問をはじめる『ステップバック・プロンプティング』が、様々なベンチマークでCoTやTake a Deep Breatheを凌駕する性能を発揮すると報告がありました。>極めてシンプルで具体的な新テクニックです。>DeepMiまた新しいの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/aac94123-7c39-4938-889f-feb5cff9317c" alt="image"><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1066">Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution, Chrisantha Fernando+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、Promptbreederという自己参照的な自己改善メカニズムを提案し、大規模言語モデル（LLM）の推論能力を向上させるための汎用的なプロンプト戦略を進化させる方法を示しています。Promptbreederは、LLMが自己参照的な方法で進化する変異プロンプトによって制御され、タスクプロンプトの集団を変異させて改善します。この手法は、算術や常識的な推論のベンチマークだけでなく、ヘイトスピーチ分類などの難しい問題に対しても優れた性能を発揮します。</span>
<span class="snippet"><span>Comment</span>以下AIDBのツイートの引用>プロンプトを遺伝的アルゴリズムで最適化するプロンプトエンジニアリング自動化手法『Promptbreeder（プロンプトブリーダー）』が発表されました。>CoT（ステップバイステップ）を上回る性能を確認したとのこと。>DeepMindによる研究です。>○ C詳細な解説記事 ...</span>
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1065">Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models  through Logic, Xufeng Zhao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>大規模言語モデルの進歩は驚異的だが、多段階の推論には改善の余地がある。大規模言語モデルは知識を持っているが、推論には一貫性がなく、幻覚を示すことがある。そこで、Logical Chain-of-Thought（LogiCoT）というフレームワークを提案し、論理による推論パラダイムの効果を示した。</span>
<span class="snippet"><span>Comment</span>まーた新しいX of Thoughtが出た。必要そうなら読む。 ...</span>
<a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1061">Graph Neural Prompting with Large Language Models, Yijun Tian+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、大規模言語モデル（LLMs）を知識グラフと組み合わせるための新しい手法であるGraph Neural Prompting（GNP）を提案しています。GNPは、標準的なグラフニューラルネットワークエンコーダやクロスモダリティプーリングモジュールなどの要素から構成されており、異なるLLMのサイズや設定において、常識的な推論タスクやバイオメディカル推論タスクで優れた性能を示すことが実験によって示されました。</span>
<span class="snippet"><span>Comment</span>以下elvis氏のツイートの意訳事前学習されたLLMがKGから有益な知識を学習することを支援する手法を提案。元ツイート: https://arxiv.org/abs/2309.15427しっかり論文を読んでいないが、freezeしたLLMがあった時に、KGから求めたGraph Neural Prom ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/434daf26-f82f-43b9-8807-13517975383b" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-09-30</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1044">Chain-of-Verification Reduces Hallucination in Large Language Models, Shehzaad Dhuliawala+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>私たちは、言語モデルが根拠のない情報を生成する問題に取り組んでいます。Chain-of-Verification（CoVe）メソッドを開発し、モデルが回答を作成し、検証し、最終的な回答を生成するプロセスを経ることで、幻想を減少させることができることを実験で示しました。</span>
<span class="snippet"><span>Comment</span># 概要ユーザの質問から、Verificationのための質問をplanningし、質問に対して独立に回答を得たうえでオリジナルの質問に対するaggreementを確認し、最終的に生成を実施するPrompting手法# 評価## datasetWikidata ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/18763903-2d70-4180-9384-2da55bedad2e" alt="image"><a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Reasoning.html">#Reasoning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/849">Reasoning with Language Model Prompting: A Survey, ACL23</a>
<span class="snippet"><span>Summary</span>本論文では、推論に関する最新の研究について包括的な調査を行い、初心者を支援するためのリソースを提供します。また、推論能力の要因や将来の研究方向についても議論します。リソースは定期的に更新されています。</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/837">Tailor: A Soft-Prompt-Based Approach to Attribute-Based Controlled Text Generation, ACL23</a>
<span class="snippet"><span>Summary</span>属性ベースの制御されたテキスト生成（CTG）では、望ましい属性を持つ文を生成することが目指されている。従来の手法では、ファインチューニングや追加の属性分類器を使用していたが、ストレージと推論時間の増加が懸念されていた。そこで、本研究では効率的なパラメータを使用した属性ベースのCTGを提案している。具体的には、各属性を事前学習された連続ベクトルとして表現し、固定された事前学習言語モデルをガイドして属性を満たす文を生成する。さらに、2つの解決策を提供して、組み合わせを強化している。実験の結果、追加のトレーニングパラメータのみで効果的な改善が実現できることが示された。</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/799">Large Language Models are Effective Text Rankers with Pairwise Ranking  Prompting, Zhen Qin+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>LLMsを使用してドキュメントをランキングする際に、Pairwise Ranking Prompting（PRP）という新しい技術を提案する。PRPは、LLMsへの負荷を軽減し、最先端のランキングパフォーマンスを達成することができる。具体的には、20Bパラメータを持つFlan-UL2モデルに基づくPRPは、商用のGPT-4に基づく従来の手法を上回る結果を示した。さらに、PRPのバリアントを提案し、効率を改善することができることを示した。PRPは生成とスコアリングのLLM APIの両方をサポートし、入力の順序に対して無感度であることも示された。</span>
<span class="snippet"><span>Comment</span>open source LLMをスタンダードなベンチマークでSoTAを達成できるようなprompting技術を提案 ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/795">A Survey of Large Language Models, Wayne Xin Zhao+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>言語モデリングの進化により、大規模言語モデル（LLM）が注目されている。LLMは、事前学習、適応調整、利用、容量評価の4つの側面に焦点を当てて研究されており、AIアルゴリズムの開発と使用方法に革新をもたらす可能性がある。本調査では、LLMの最近の進展と将来の方向性についてレビューし、残された課題についても議論する。</span>
<span class="snippet"><span>Comment</span>現状で最も詳細なLLMのサーベイ600個のリファレンス、LLMのコレクション、promptingのtips、githubリポジトリなどがまとめられている ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/TheoryOfMind.html">#TheoryOfMind</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/581">Boosting Theory-of-Mind Performance in Large Language Models via Prompting, Moghaddam+, Johns Hopkins University, arXiv23</a>
<span class="snippet"><span>Comment</span>LLMはTheory-of-mind reasoningタスクが苦手なことが知られており、特にzero shotでは非常にパフォーマンスが低かった。ToMタスクとは、エージェントの信念、ゴール、メンタルstate、エージェントが何を知っているか等をトラッキングすることが求められるタスクのこと。このよ ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/569">Exploring the Curious Case of Code Prompts, Zhang+, University of Pennsylvania, arXiv23</a>
<span class="snippet"><span>Comment</span>コードベースのLLMに対して、reasoningタスクを解かせる際には、promptもコードにすると10パーセント程度性能上がる場合があるよ、という研究。![image](https://user-images.githubusercontent.com/12249301/235037840-1fた ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/568">Answering Questions by Meta-Reasoning over Multiple Chains of Thought, Yoran+, Tel Aviv University （w_ Allen Institute for AI）, arXiv23</a>
<span class="snippet"><span>Comment</span>self-consistency #558 のようなvoting basedなアルゴリズムは、複数のCoTのintermediate stepを捨ててしまい、結果だけを採用するが、この研究は複数のCoTの中からquestionに回答するために適切なfactual informationを抽出するMe ...</span>
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/532">Enhancing LLM Chain-of-Thought w_ Iterative Bootstrapping, Sun+, Xiamen University （w_ MSRA et al.）, arXiv23</a>
<span class="snippet"><span>Comment</span>Zero shot CoTからスタートし、正しく問題に回答できるようにreasoningを改善するようにpromptをreviseし続けるループを回す。最終的にループした結果を要約し、それらをプールする。テストセットに対しては、プールの中からNshotをサンプルしinferenceを行う。![imで ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-10-29</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1103">LLMのプロンプト技術まとめ</a>
<span class="snippet"><span>Comment</span>ざっと見たが現時点で主要なものはほぼ含まれているのでは、という印象実際のプロンプト例が載っているので、理解しやすいかもしれない。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1079">日本語LLMベンチマークと自動プロンプトエンジニアリング</a>
<span class="snippet"><span>Comment</span>面白かった。特に、promptingによってrinnaとcyberのLLMの順位が逆転しているのが興味深かった。GAを使ったプロンプトチューニングは最近論文も出ていたが、日本語LLMで試されているのは面白かった。 ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/678">Prompt Engineering vs. Blind Prompting, 2023</a>
<span class="snippet"><span>Comment</span>experimentalな手法でprompt engineeringする際のoverview ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
