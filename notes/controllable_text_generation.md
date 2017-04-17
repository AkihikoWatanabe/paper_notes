Text Generationを行う際は、現在は基本的に学習された言語モデルの尤度に従ってテキストを生成するのみで、outputされるテキストをcontrolすることができないので、できるようにしましたという論文。
VAEによるテキスト生成にGANを組み合わせたようなモデル。
decodingする元となるfeatureのある次元が、たとえばpolarityなどに対応しており、その次元の数値をいじるだけで生成されるテキストをcontrolできる。
後で詳しく読む。

（追記）

テキストを生成する際に、生成されるテキストをコントロールするための研究。
テキストを生成する際には、基本的にはVariational Auto Encoder(VAE)を用いる。

VAEは、入力をエンコードするEncoderと、エンコードされた潜在変数zからテキストを生成するGeneratorの2つの機構によって構成されている。

この研究では、生成されるテキストをコントロールするために、VAEの潜在変数zに、生成するテキストのattributeを表す変数cを新たに導入。

たとえば、一例として、変数cをsentimentに対応させた場合、変数cの値を変更すると、生成されるテキストのsentimentが変化するような生成が実現可能。

次に、このような生成を実現できるようなパラメータを学習したいが、学習を行う際のポイントは、以下の二つ。

1. cで指定されたattributeが反映されたテキストを生成するように学習

2. 潜在変数zとattributeに関する変数cの独立性を保つように学習
（cには制御したいattributeに関する情報のみが格納され、その他の情報は潜在変数zに格納されるように学習する)

1を実現するために、新たにdiscriminatorと呼ばれる識別器を用意し、VAEが生成したテキストのattributeをdiscriminatorで分類し、その結果をVAEのGeneratorにフィードバックすることで、attributeが反映されたテキストを生成できるようにパラメータの学習を行う。
（これにはラベル付きデータが必要ですが、少量でも学習できることに加えて、sentence levelのデータだけではなくword levelのデータでも学習できる。）

また、2を実現するために、VAEが生成したテキストから、生成する元となった潜在変数zが再現できるようにEncoderのパラメータを学習。

実験では、sentimentとtenseをコントロールする実験が行われており、attributeを表す変数cを変更することで、以下のようなテキストが生成されており興味深い。

[sentimentを制御した例]
- this movie was awful and boring. (negative)
- this movie was funny and touching. (positive)

[tenseを制御した例]
- this was one of the outstanding thrillers of the last decade
- this is one of the outstanding thrillers of the all time
- this will be one of the great thrillers of the all time
