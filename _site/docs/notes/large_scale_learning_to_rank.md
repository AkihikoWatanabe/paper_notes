sofia-mlの実装内容について記述されている論文

よくonline学習の文脈で触れられるが、気をつけないと罠にはまる。
というのは、sofia-ml内のMethodsによって、最適化している目的関数が異なるからだ。
実装をみると、全てのmethodsがonlineでできちゃいそうに見える（学習済みのモデルをinputして学習を再開させられるため）が、落とし穴。

まず、SGD SVM, Pegasos SVM,については、最適化している目的関数がbatchになっているため、online learningではない。
passive-aggressive perceptrionは目的関数が個別の事例に対して定式化される(要確認)のでonline learningといえる。
(ROMMAは調べないとわからん)

pairwiseのlearning to rankでは、サンプルのペアを使って学習するので、最悪の場合O(n^2)の計算量がかかってしまってめっちゃ遅いのだが、実は学習データを一部サンプリングして重みを更新するってのをたくさん繰り返すだけで、高速に学習できちゃうという話。

実際、sofia-mlを使って見たら、liblinearのranking SVM実装で40分かかった学習が数秒で終わり、なおかつ精度も良かった。
