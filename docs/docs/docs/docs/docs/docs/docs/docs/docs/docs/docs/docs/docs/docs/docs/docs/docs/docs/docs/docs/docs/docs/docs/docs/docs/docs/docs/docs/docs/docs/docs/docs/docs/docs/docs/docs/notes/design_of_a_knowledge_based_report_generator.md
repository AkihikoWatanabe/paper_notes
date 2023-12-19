タスク： numerical stock market dataからstock market reportsを生成，我々と同様なタスク．システム名: ANA

手法概要： ルールベースな手法，1) fact-generator, 2) message generator, 3) discourse organizer, 4) text generatorの4コンポーネントから成る． 2), 3), 4)はそれぞれ120, 16, 109個のルールがある4)ではphrasal dictionaryも使う． 1)では，入力されたpriceデータから，closing averageを求めるなどの数値的な演算などを行う. 2)では，1)で計算された情報に基づいて，メッセージの生成を行う(e.g. market was mixed). 3)では，メッセージのparagraph化，orderの決定，priorityの設定などを行う． 4)では，辞書からフレーズを選択したり，適切なsyntactic formを決定するなどしてテキストを生成．
