分類やランキング、レコメンドなど、様々なタスクで汎用的に使用できるEmbeddingの学習手法を提案。  
  
Embeddingを学習する対象をEntityと呼び、Entityはbag-of-featureで記述される。  
Entityはbag-of-featureで記述できればなんでもよく、  
これによりモデルの汎用性が増し、異なる種類のEntityでも同じ空間上でEmbeddingが学習される。  
  
学習方法は非常にシンプルで、Entity同士のペアをとったときに、relevantなpairであれば類似度が高く、  
irelevantなペアであれば類似度が低くなるようにEmbeddingを学習するだけ。  
たとえば、Entityのペアとして、documentをbag-of-words, bag-of-ngrams, labelをsingle wordで記述しテキスト分類、  
あるいは、user_idとユーザが過去に好んだアイテムをbag-of-wordsで記述しcontent-based recommendationを行うなど、
応用範囲は幅広い。  

5種類のタスクで提案手法を評価し、既存手法と比較して、同等かそれ以上の性能を示すことが示されている。  

手法の汎用性が高く学習も高速なので、色々な場面で役に立ちそう。  
また、異なる種類のEntityであっても同じ空間上でEmbeddingが学習されるので、学習されたEmbeddingの応用先が広く有用。
