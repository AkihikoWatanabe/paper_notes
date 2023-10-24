---
layout: post
title: Promptに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## Prompt
<div class="visible-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/532">Enhancing LLM Chain-of-Thought w_ Iterative Bootstrapping, Sun+, Xiamen University （w_ MSRA et al.）, arXiv23</a>
<span class="snippet"># 実験Manual-CoT #551 , Random-CoT #551, Auto-CoT #554 と比較。Iter-CoTが11個のデータセット全てでoutperformした。![image](https://user-images.githubusercontent.com ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/CoT.html">#CoT</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/568">Answering Questions by Meta-Reasoning over Multiple Chains of Thought, Yoran+, Tel Aviv University （w_ Allen Institute for AI）, arXiv23</a>
<span class="snippet">self-consistency #558 のようなvoting basedなアルゴリズムは、複数のCoTのintermediate stepを捨ててしまい、結果だけを採用するが、この研究は複数のCoTの中からquestionに回答するために適切なfactual informationを抽出するMe ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/569">Exploring the Curious Case of Code Prompts, Zhang+, University of Pennsylvania, arXiv23</a>
<span class="snippet">コードベースのモデルをtextでinstruction tuningしている場合でも、効果があるタスクがある。 ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/QuestionAnswering.html">#QuestionAnswering</a><a class="button" href="articles/TheoryOfMind.html">#TheoryOfMind</a><br><span class="issue_date">Issue Date: 2023-04-28</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/581">Boosting Theory-of-Mind Performance in Large Language Models via Prompting, Moghaddam+, Johns Hopkins University, arXiv23</a>
<span class="snippet">LLMはTheory-of-mind reasoningタスクが苦手なことが知られており、特にzero shotでは非常にパフォーマンスが低かった。ToMタスクとは、エージェントの信念、ゴール、メンタルstate、エージェントが何を知っているか等をトラッキングすることが求められるタスクのこと。このよ ...</span>
<a class="button" href="articles/Tutorial.html">#Tutorial</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Article.html">#Article</a><br><span class="issue_date">Issue Date: 2023-05-12</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/678">Prompt Engineering vs. Blind Prompting, 2023</a>
<span class="snippet">experimentalな手法でprompt engineeringする際のoverview ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/795">A Survey of Large Language Models, Wayne Xin Zhao+, N_A, arXiv23</a>
<span class="snippet">言語モデリングの進化により、大規模言語モデル（LLM）が注目されている。LLMは、事前学習、適応調整、利用、容量評価の4つの側面に焦点を当てて研究されており、AIアルゴリズムの開発と使用方法に革新をもたらす可能性がある。本調査では、LLMの最近の進展と将来の方向性についてレビューし、残された課題に ...</span>
<a class="button" href="articles/InformationRetrieval.html">#InformationRetrieval</a><a class="button" href="articles/LearningToRank.html">#LearningToRank</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-07-11</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/799">Large Language Models are Effective Text Rankers with Pairwise Ranking  Prompting, Zhen Qin+, N_A, arXiv23</a>
<span class="snippet">LLMsを使用してドキュメントをランキングする際に、Pairwise Ranking Prompting（PRP）という新しい技術を提案する。PRPは、LLMsへの負荷を軽減し、最先端のランキングパフォーマンスを達成することができる。具体的には、20Bパラメータを持つFlan-UL2モデルに基づく ...</span>
<a class="button" href="articles/NaturalLanguageGeneration.html">#NaturalLanguageGeneration</a><a class="button" href="articles/Controllable.html">#Controllable</a><a class="button" href="articles/NLP.html">#NLP</a><br><span class="issue_date">Issue Date: 2023-07-15</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/837">Tailor: A Soft-Prompt-Based Approach to Attribute-Based Controlled Text Generation, ACL23</a>
<span class="snippet">属性ベースの制御されたテキスト生成（CTG）では、望ましい属性を持つ文を生成することが目指されている。従来の手法では、ファインチューニングや追加の属性分類器を使用していたが、ストレージと推論時間の増加が懸念されていた。そこで、本研究では効率的なパラメータを使用した属性ベースのCTGを提案している。 ...</span>
<a class="button" href="articles/Survey.html">#Survey</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Reasoning.html">#Reasoning</a><br><span class="issue_date">Issue Date: 2023-07-18</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/849">Reasoning with Language Model Prompting: A Survey, ACL23</a>
<span class="snippet">本論文では、推論に関する最新の研究について包括的な調査を行い、初心者を支援するためのリソースを提供します。また、推論能力の要因や将来の研究方向についても議論します。リソースは定期的に更新されています。 ...</span>
<a class="button" href="articles/GraphBased.html">#GraphBased</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1061">Graph Neural Prompting with Large Language Models, Yijun Tian+, N_A, arXiv23</a>
<span class="snippet">本研究では、大規模言語モデル（LLMs）を知識グラフと組み合わせるための新しい手法であるGraph Neural Prompting（GNP）を提案しています。GNPは、標準的なグラフニューラルネットワークエンコーダやクロスモダリティプーリングモジュールなどの要素から構成されており、異なるLLMの ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/434daf26-f82f-43b9-8807-13517975383b" alt="image"><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1065">Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models  through Logic, Xufeng Zhao+, N_A, arXiv23</a>
<span class="snippet">大規模言語モデルの進歩は驚異的だが、多段階の推論には改善の余地がある。大規模言語モデルは知識を持っているが、推論には一貫性がなく、幻覚を示すことがある。そこで、Logical Chain-of-Thought（LogiCoT）というフレームワークを提案し、論理による推論パラダイムの効果を示した。 ...</span>
<a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1066">Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution, Chrisantha Fernando+, N_A, arXiv23</a>
<span class="snippet">本研究では、Promptbreederという自己参照的な自己改善メカニズムを提案し、大規模言語モデル（LLM）の推論能力を向上させるための汎用的なプロンプト戦略を進化させる方法を示しています。Promptbreederは、LLMが自己参照的な方法で進化する変異プロンプトによって制御され、タスクプロ ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/PromptTuning.html">#PromptTuning</a><br><span class="issue_date">Issue Date: 2023-10-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1079">日本語LLMベンチマークと自動プロンプトエンジニアリング</a>
<span class="snippet">面白かった。特に、promptingによってrinnaとcyberのLLMの順位が逆転しているのが興味深かった。GAを使ったプロンプトチューニングは最近論文も出ていたが、日本語LLMで試されているのは面白かった。 ...</span>
<button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
