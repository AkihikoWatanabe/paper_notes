複数文を生成(今回はautoencoder)するために、standardなseq2seq LSTM modelを、拡張したという話。

要は、paragraph/documentのrepresentationが欲しいのだが、アイデアとしては、word-levelの情報を扱うLSTM layerとsentenc-levelの情報を扱うLSTM layerを用意し、それらのcompositionによって、paragraph/documentを表現しましたという話。

sentence-levelのattentionを入れたらよくなっている。

trip advisorのreviewとwikipediaのparagraphを使ってtrainingして、どれだけ文書を再構築できるか実験。
MetricはROUGE, BLEUおよびcoherence(sentence order代替)を測るために、各sentence間のgapがinputとoutputでどれだけ一致しているかで評価。

hierarchical lstm with attention > hierarchical lstm > standard lstm の順番で高性能。
