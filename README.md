# paper_notes
雑すぎる論文メモ

# Deep Learning
## Vision
- Generating Visual Explanations, Hendrickks+, ECCV'16, [link](https://www.semanticscholar.org/paper/Generating-Visual-Explanations-Hendricks-Akata/e32dcf5aa3c28e6fbf4da381e03f1bea73e4f1b0)
### Explicitly using visual words
- What Value Do Explicit High Level Concepts Have in Vision to Language Problems?, Wu+, CVPR'16.
- Image Captioning with Semantic Attention, You+, CVPR'16.

## Machine Translation
- Neural Machine Translation with Source-Side Latent Graph Parsing, Hashimoto+, arXiv'17., [link](https://arxiv.org/abs/1702.02265)

## Representation
### Sentence Level
- A structured self-attentive sentence embedding, Li+ (Bengio group), [arXiv](https://arxiv.org/pdf/1703.03130.pdf)

### Document Level
- [Document Modeling with Gated Recurrent Neural Network for Sentiment Classification](notes/document_modeling_gru.md), Tang+, EMNLP'15.
- [Distraction-Based Neural Networks for Modeling Documents](notes/distraction_based_summ.md), Chen+, IJCAI'16., [paper](https://www.ijcai.org/Proceedings/16/Papers/391.pdf)
- [A hierarchical neural autoencoder for paragraphs and documents](notes/a_hierarchical_neural_autoencoder_for_paragraphs_and_documents.md), Li+, ACL'15.
- LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP'15.
- Larger-context language modelling with recurrent neural networks, Wang+, [arXiv](https://arxiv.org/abs/1511.03729)
- Teaching Machines to Read and Comprehend, Hermann+, [NIPS 2015](http://dl.acm.org/citation.cfm?id=2969428)

## Beam-Search
- Sequence-to-Sequence Learning as Beam-Search Optimization, Wiseman+, EMNLP'16.

# Natural Language Generation
## Survey
- Survey of the State of the Art in Natural Language Generation: Core tasks, applications and evaluation, Gatt+, arXiv'17.

## Controllable NLG
- [Controllable Text Generation, Hu+, arXiv'17.](notes/controllable_text_generation.md)

# Document Summarization
## Survey
- Recent Advances in Document Summarization, Yao+, Knowledge and Information Systems'17, [paper](http://www.icst.pku.edu.cn/lcwm/wanxj/files/summ_survey_draft.pdf)
- A Survey of Text Summarization Techniques, Nenkova+, Springer'12, [book](https://link.springer.com/chapter/10.1007%2F978-1-4614-3223-4_3)
- (A survey on Automatic Text Summarization, Das+, CMUの教材？) 

## Neural Model
- Neural Summarization by Extracting Sentences and Words, Chenc+, ACL'16, [paper](http://www.aclweb.org/anthology/P16-1046).
- [Distraction-Based Neural Networks for Modeling Documents](notes/disraction_based_summ.md), Chen+, IJCAI'16., [paper](https://www.ijcai.org/Proceedings/16/Papers/391.pdf)
- Cutting-off redundant repeating generations for neural abstractive summarization, Suzuki+, EACL'17 [paper](https://www.aclweb.org/anthology/E/E17/E17-2047.pdf)
- A Deep Reinforced Model for Abstractive Summarization, Paulus+(Socherもいる), arXiv'17, [paper](https://arxiv.org/pdf/1705.04304.pdf)

## Supervised
- A Trainable Document Summarizer, Kupiec+, SIGIR'95.
- Text Summarization using a trainable summarizer and latent semantic analysis, Yeh+, Information Processing and Management 2005.
- Document Summarization using Conditional Random Fields, Shen+, IJCAI07.
- (構造学習) 転移学習による抽出型要約の精度向上, 西川+, 情報処理学会研究報告, 2011.
- (構造学習) Learning from Numerous Untailored Summaries, Kikuchi+, PRICAI'16.
- Learning to Generate Coherent Sumamry with Discriminative Hidden Semi-Markov Model, Nishikawa+, COLING'14

# Personalized Document Summarization
- User-model based personalized summarization, Diaz+, Information Processing and Management 2007.

# Recommender Systems
## News Citations
- [News Citation Recommendation with Implicit and Explicit Semantics](notes/news_citation.md), Peng+, ACL'16, [paper](https://www.aclweb.org/anthology/P/P16/P16-1037.pdf)

# IR
## Learning to Rank
### Survey
- Learning to Rank for Information Retriefval, Liu+, [paper](http://didawiki.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/ir/ir13/1_-_learning_to_rank.pdf)
- [Tutorials](http://mklab.iti.gr/essir2015/wp-content/uploads/2015/03/ESSIR2015_Hofmann.pdf)
- [Tutorials, in Japanese](https://www.slideshare.net/sleepy_yoshi/dsirnlp1)
- [Tutorials, in Japanese](https://www.slideshare.net/tkng/confidence-weighted)

### Pair-wise 
- Large Scale Learning to Rank, Sculley+, NIPS 2009, [paper](https://pdfs.semanticscholar.org/0571/3da3bd396fef9611761fab4d88a21671ca43.pdf)
### Online (Dueling Bandits)
- Fast and Reliable Online Learning to Rank for Information Retrieeval, Katja Hofmann, Doctoral Thesis, 2013. [Thesis](https://khofm.files.wordpress.com/2013/04/thesis-katja-hofmann-online-learning.pdf)
- Interactively Optimizing Information Retrieval Systems as a Dueling Bandits Problem, Yue+, ICML'09
- Reusing Historical Interaction Data for Faster Online Learning to Rank for IR, Hofmann+, WSDM'13
- Contextual Dueling Bandits, Dudik+, JMLR'15
- [Tutorials](http://www.anneschuth.nl/wp-content/uploads/2012/08/20140626-textkernel-anneschuth.pdf)
- [Tools: Lerot: Online Learning to rank Framework](http://ilps.science.uva.nl/resources/online-learning-framework/)

### Interleaved Method
- How Does Clickthrough Data Reflect Retrieval Quality?, Radlijnski+, CIKM'08

## Relevance Feedback
### Survey
- (Explicit Feedback) A survey on the use of relevance feedback for information access systems., Ruthven+, The Knowledge Engineering Review, 2003.
- (Implicit Feedaback) Evaluating implicit measures to improve web search, Fox+, ACM Transactions aon Imformation Systems, 2005.
