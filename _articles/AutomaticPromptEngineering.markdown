---
layout: post
title: AutomaticPromptEngineeringに関する論文・技術記事メモの一覧
author: AkihikoWATANABE
---
## AutomaticPromptEngineering
<div class="visible-content">
<a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><a class="button" href="articles/Prompting.html">#Prompting</a><br><span class="issue_date">Issue Date: 2023-11-13</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1128">Prompt Engineering a Prompt Engineer, Qinyuan Ye+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>プロンプトエンジニアリングは、LLMsのパフォーマンスを最適化するための重要なタスクであり、本研究ではメタプロンプトを構築して自動的なプロンプトエンジニアリングを行います。改善されたパフォーマンスにつながる推論テンプレートやコンテキストの明示などの要素を導入し、一般的な最適化概念をメタプロンプトに組み込みます。提案手法であるPE2は、さまざまなデータセットやタスクで強力なパフォーマンスを発揮し、以前の自動プロンプトエンジニアリング手法を上回ります。さらに、PE2は意味のあるプロンプト編集を行い、カウンターファクトの推論能力を示します。</span>
<a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-09</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1037">Large Language Models as Optimizers, Chengrun Yang+, N_A, arXiv23</a>
<span class="snippet"><span>Summary</span>本研究では、最適化タスクを自然言語で記述し、大規模言語モデル（LLMs）を使用して最適化を行う手法「Optimization by PROmpting（OPRO）」を提案しています。この手法では、LLMが以前の解とその値を含むプロンプトから新しい解を生成し、評価して次の最適化ステップのためのプロンプトに追加します。実験結果では、OPROによって最適化された最良のプロンプトが、人間が設計したプロンプトよりも優れていることが示されました。</span>
<span class="snippet"><span>Comment</span>`Take a deep breath and work on this problem step-by-step. `論文# 概要LLMを利用して最適化問題を解くためのフレームワークを提案したという話。論文中では、linear regressionや巡回セールスマン問題に適用している。 ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/2a469085-8a14-4eac-85ee-3918fe1becd5" alt="image"><a class="button" href="articles/MachineLearning.html">#MachineLearning</a><a class="button" href="articles/Pocket.html">#Pocket</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/LanguageModel.html">#LanguageModel</a><br><span class="issue_date">Issue Date: 2023-09-05</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1034">Large Language Models Are Human-Level Prompt Engineers, Yongchao Zhou+, ICLR23</a>
<span class="snippet"><span>Summary</span>大規模言語モデル（LLMs）は、自然言語の指示に基づいて一般的な用途のコンピュータとして優れた能力を持っています。しかし、モデルのパフォーマンスは、使用されるプロンプトの品質に大きく依存します。この研究では、自動プロンプトエンジニア（APE）を提案し、LLMによって生成された指示候補のプールから最適な指示を選択するために最適化します。実験結果は、APEが従来のLLMベースラインを上回り、19/24のタスクで人間の生成した指示と同等または優れたパフォーマンスを示しています。APEエンジニアリングされたプロンプトは、モデルの性能を向上させるだけでなく、フューショット学習のパフォーマンスも向上させることができます。詳細は、https://sites.google.com/view/automatic-prompt-engineerをご覧ください。</span>
<span class="snippet"><span>Comment</span>プロジェクトサイト: https://sites.google.com/view/automatic-prompt-engineer ...</span>
</div>
<button onclick="showMore(0)">more</button>

<div class="hidden-content">
<a class="button" href="articles/Neural.html">#Neural</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/CoT.html">#CoT</a><a class="button" href="articles/Prompting.html">#Prompting</a><br><span class="issue_date">Issue Date: 2023-04-25</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/532">Enhancing LLM Chain-of-Thought w_ Iterative Bootstrapping, Sun+, Xiamen University （w_ MSRA et al.）, arXiv23</a>
<span class="snippet"><span>Comment</span>Zero shot CoTからスタートし、正しく問題に回答できるようにreasoningを改善するようにpromptをreviseし続けるループを回す。最終的にループした結果を要約し、それらをプールする。テストセットに対しては、プールの中からNshotをサンプルしinferenceを行う。![imで ...</span>
<a class="button" href="articles/Article.html">#Article</a><a class="button" href="articles/ComputerVision.html">#ComputerVision</a><a class="button" href="articles/NLP.html">#NLP</a><a class="button" href="articles/Prompting.html">#Prompting</a><a class="button" href="articles/MulltiModal.html">#MulltiModal</a><br><span class="issue_date">Issue Date: 2023-12-01</span>
<a href="https://github.com/AkihikoWatanabe/paper_notes/issues/1171">multimodal-maestro</a>
<span class="snippet"><span>Comment</span>Large Multimodal Model (LMM)において、雑なpromptを与えるても自動的に良い感じoutputを生成してくれるっぽい？以下の例はリポジトリからの引用であるが、この例では、"Find dog." という雑なpromptから、画像中央に位置する犬に[9]というラベルを ...</span>
<img src="https://github.com/AkihikoWatanabe/paper_notes/assets/12249301/5220e62f-93f1-4eb9-b365-a9caaf933778" alt="image"><button onclick="hideContent(0)" style="display: none;">hide</button>
</div>
