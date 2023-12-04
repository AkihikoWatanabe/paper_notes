Graph Convolutional Network (GCN)を使って、MDSやりましたという話。
既存のニューラルなMDSモデル [Cao et al., 2015, 2017] では、sentence間のrelationが考慮できていなかったが、GCN使って考慮した。
また、MDSの学習データはニューラルなモデルを学習するには小さすぎるが（abstractiveにするのは厳しいという話だと思われる？）、sentenceのsalienceを求める問題に帰着させることで、これを克服。

GCNで用いるAdjacent Matrixとして3種類の方法(cosine similarity, G-Flow, PDG)を試し、議論をしている。PDGが提案手法だが、G-Flowによる重みをPersonalization Features（position, leadか否か等のベーシックな素性）から求まるweightで、よりsentenceのsalienceを求める際にリッチな情報を扱えるように補正している。PDGを用いた場合が（ROUGE的な観点で）最も性能がよかった。

モデルの処理の流れとしては、Document Cluster中の各sentenceのhidden stateをGRUベースなRNNでエンコードし、それをGCNのノードの初期値として利用する。GCNでL回のpropagation後（実験では3回）に得られたノードのhidden stateを、salienceスコア計算に用いるsentence embedding、およびcluster embeddingの生成に用いる。
cluster embeddingは、document clusterをglobalな視点から見て、salienceスコアに反映させるために用いられる。
最終的にこれら2つの情報をlinearなlayerにかけてsoftmaxかけて正規化して、salienceスコアとする。

要約を生成する際はgreedyな方法を用いており、salienceスコアの高いsentenceから要約長に達するまで選択していく。このとき、冗長性を排除するため、candidateとなるsentenceと生成中の要約とのcosine similarityが0.5を超えるものは選択しないといった、よくある操作を行なっている。

DUC01, 02のデータをtraining data, DUC03 をvalidation data, DUC04をtest dataとし、ROUGE1,2で評価。
評価の結果、CLASSY04(DUC04のbest system)やLexRank等のよく使われるベースラインをoutperform。
ただ、regression basedなRegSumにはスコアで勝てないという結果に。
RegSumはwordレベルでsalienceスコアをregressionする手法で、リッチな情報を結構使っているので、これらを提案手法に組み合わせるのは有望な方向性だと議論している。

[Cao+, 2015] Ranking with recursive neural networks and its application to multi-document summarization, Cao+, AAAI'15
[Cao+, 2017] Improving multi-document summarization via text classification, Cao+, AAAI'17

[所感]
・ニューラルなモデルは表現力は高そうだけど、学習データがDUC01と02だけだと、データが足りなくて持ち前の表現力が活かせていないのではないかという気がする。
・冗長性の排除をアドホックにやっているので、モデルにうまく組み込めないかなという印象（distraction機構とか使えばいいのかもしれん）
・ROUGEでしか評価してないけど、実際のoutputはどんな感じなのかちょっと見てみたい。（ハイレベルなシステムだとROUGEスコア上がっても人手評価との相関がないっていう研究成果もあるし。）
・GCN、あまり知らなかったかけど数式追ったらなんとなく分かったと思われる。（元論文読めという話だが）
