Neuralなモデルで「文書」の要約を行う研究。

提案手法では、attention-basedなsequence-to-sequenceモデルにdistractionと呼ばれる機構を導入することを提案。

distractionを導入するmotivationは、入力文書中の異なる情報を横断的に参照（一度着目した情報には今後あまり着目しないようなバイアスをかける）したうえで、要約を生成しようというもの。
これにより、生成される要約の冗長性を排除するのが狙い。

以下の3つのアプローチを用いて、distractionを実現

1. [Distraction over input content vectors]
　tステップ目において、decoderのinputとして用いるcontext vectorを
計算する際に、通常の計算に加えて、t-1ステップ目までに使用した
context vectorの情報を活用することで、これまでdecoderのinputとして
利用された情報をあまり重視視しないように、context vectorを生成する。

2. [Distraction over attention weight vectors]
　attentionの重みを計算する際に、過去に高いattentionの重みがついた
encoderのhidden stateについては、あまり重要視しないように
attentionの重みを計算。1と同様に、t-1ステップ目までのattention weightの
historyを保持しておき活用する。

3. [Distration in decoding]
　decodingステップでbeam-searchを行う際のスコア計算に、distraction scoreを導入。distraction
scoreはtステップ目までに用いられたcontext vector、attention
weight、decoderのstateから計算され、これまでと同じような情報に基づいて
単語が生成された場合は、スコアが低くなるようになっている。

CNN、およびLCSTS data (大規模な中国語のheadline generationデータ)で評価した結果、上記3つのdistraction機構を導入した場合に、最も高いROUGEスコアを獲得

特に、原文書が長い場合に、短い場合と比較して、distraction機構を導入すると、
ROUGEスコアの改善幅が大きくなったことが示されている
