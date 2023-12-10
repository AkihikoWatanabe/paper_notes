Frustratingly easy domain adaptationをPersonalization用に拡張している。  
Frustratingly easy domain adaptationでは、domain adaptationを行うときに、discreteなクラスに分けてfeature vectorを作る（age>28など）が、Personalizationを行う際は、このようなdiscreteな表現よりも、continousな表現の方が表現力が高いので良い（feature vectorとそのままのageを使いベクトルをcompositionするなど）。  
psychologyの分野だと、人間のfactorをdiscreteに表現して、ある人物を表現することはnoisyだと知られているので、continuousなユーザfactorを使って、domain adaptationしましたという話。

やってることは単純で、feature vectorを作る際に、各クラスごとにfeature vectorをコピーして、feature augmentationするのではなく、continuousなuser factorとの積をとった値でfeature augmentationするというだけ。  
これをするだけで、Sentiment analysis, sarcasm detection, PP-attachmentなどのタスクにおいて、F1スコアで1〜3ポイント程度のgainを得ている。特に、sarcasm detectionではgainが顕著。  
pos tagging, stance detection(against, neutral, forなどの同定)では効果がなく、stance detectionではそもそもdiscrete adaptationの方が良い結果。

正直、もっと色々やり方はある気がするし、user embeddingを作り際などは5次元程度でしか作ってないので、これでいいのかなぁという気はする・・・。  
user factorの次元数増やすと、その分feature vectorのサイズも大きくなるから、あまり次元数を増やしたりもできないのかもしれない。
