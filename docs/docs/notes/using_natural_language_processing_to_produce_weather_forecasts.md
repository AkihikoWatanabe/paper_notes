タスク： 天気予報の生成，システム名 FOG (EnglishとFrenchのレポートを作成できる)

手法概要： ルールベースな手法，weather predictinon dataから，天気予報を自動生成．Text Planner がルールに従い各sentenceに入れる情報を抽出すると同時に，sentence orderを決め，abstractiveな中間状態を生成．その後，中間状態からText Realization（grammarやdictionaryを用いる）によって，テキストを生成．
