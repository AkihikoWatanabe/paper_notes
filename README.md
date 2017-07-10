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
- [Teaching Machines to Read and Comprehend](notes/teaching_machines_to_read_and_comprehend.md), Hermann+, [NIPS 2015](http://dl.acm.org/citation.cfm?id=2969428)

## Beam-Search
- Sequence-to-Sequence Learning as Beam-Search Optimization, Wiseman+, EMNLP'16.

# Natural Language Generation
## Survey
- Survey of the State of the Art in Natural Language Generation: Core tasks, applications and evaluation, Gatt+, arXiv'17.

## Controllable NLG
- [Controllable Text Generation, Hu+, arXiv'17.](notes/controllable_text_generation.md)

# Machine Learning
## Online Learning
- [Tutorial, in Japanese](http://www.r.dl.itc.u-tokyo.ac.jp/~nakagawa/SML1/online-L1.pdf)

## Structured Learning
- [Online Distributed Passive-Aggressive Algorithm for Structured Learning](notes/online_distributed_passive_aggressive_algorithm_for_structured_learning.md), Zhao+, CCL and NLP-NABD'13
- Scalable Large-Margin Online Learning for Structured Classification, Crammer+, 2005.
- [Structured Learning for Non-Smooth Ranking Losses](notes/structured_learning_for_non_smooth_ranking_losses.md), Chakrabarti+, KDD'08, [paper](http://mllab.csa.iisc.ernet.in/html/pubs/chiru_chakrabarti_KDD_08.pdf)
- [A support vector method for Optimizing Average Precision](notes/a_support_vector_method_for_optimizing_average_precision.md), Yue+, SIGIR'07, [paper](https://www.cs.cornell.edu/people/tj/publications/yue_etal_07a.pdf)
- [tool, SVMmap](http://projects.yisongyue.com/svmmap)

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
## Online Evaluation
- [Tutorial](http://www.yisongyue.com/talks/sigir_tutorial_combined.pptx)
## Learning to Rank
### Survey
- Learning to Rank for Information Retriefval, Liu+, [paper](http://didawiki.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/ir/ir13/1_-_learning_to_rank.pdf)
- [Tutorial](http://mklab.iti.gr/essir2015/wp-content/uploads/2015/03/ESSIR2015_Hofmann.pdf)
- [Tutorial, in Japanese](https://www.slideshare.net/sleepy_yoshi/dsirnlp1)
- [Tutorial, in Japanese](https://www.slideshare.net/tkng/confidence-weighted)

### Point-wise
- PRanking with Ranking, Crammer+, NIPS'01, [paper](https://pdfs.semanticscholar.org/906f/50f545890ca81231be7cec7c59555c679dba.pdf)

### Pair-wise 
- [Large Scale Learning to Rank](notes/large_scale_learning_to_rank.md), Sculley+, NIPS 2009, [paper](https://pdfs.semanticscholar.org/0571/3da3bd396fef9611761fab4d88a21671ca43.pdf)
- Learning to Rank using Gradient Descent (RankNet), Burges+, ICML'2005, [paper](http://icml.cc/2015/wp-content/uploads/2015/06/icml_ranking.pdf)

### List-wise
- Learning to Rank: From Pairwise Approach to Listwise Approach (ListNet), Cao+, ICML'2007, [paper](http://www.machinelearning.org/proceedings/icml2007/papers/139.pdf)
- Listwise Approach to Learning to Rank - Theory and Algorithm (ListMLE), Xia+, ICML'2008, [paper](http://www.machinelearning.org/archive/icml2008/papers/167.pdf)
- A General Approximation Framework for Direct Optimization of Information Retrieval Measures, Qin+, Information Retrieval, 2010, [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-164.pdf)

### Online (or Interactive)
- Fast and Reliable Online Learning to Rank for Information Retrieeval, Katja Hofmann, Doctoral Thesis, 2013. [Thesis](https://khofm.files.wordpress.com/2013/04/thesis-katja-hofmann-online-learning.pdf)
- [Interactively Optimizing Information Retrieval Systems as a Dueling Bandits Problem](notes/interactively_optimizing_information_retrieval_systems_as_a_dueling_baqndits_problem.md), Yue+, ICML'09
- Reusing Historical Interaction Data for Faster Online Learning to Rank for IR, Hofmann+, WSDM'13
- Contextual Dueling Bandits, Dudik+, JMLR'15
- [Tutorial](http://www.anneschuth.nl/wp-content/uploads/2012/08/20140626-textkernel-anneschuth.pdf)
- [Tools: Lerot: Online Learning to rank Framework](http://ilps.science.uva.nl/resources/online-learning-framework/)
- PRanking with Ranking, Crammer+, NIPS'01, [paper](https://pdfs.semanticscholar.org/906f/50f545890ca81231be7cec7c59555c679dba.pdf)
- Fast Learning of Document Ranking Functions with the Committee Perceptrion, Elsas+, WSDM'08. [paper](http://delivery.acm.org/10.1145/1350000/1341542/p55-elsas.pdf?ip=131.112.138.2&id=1341542&acc=ACTIVE%20SERVICE&key=D2341B890AD12BFE%2EE857D5F645C75AE5%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=781623828&CFTOKEN=57476606&__acm__=1499155717_780c7ac7b015e2c7cdefe0c2a5b73c2d)

### Interleaved Method
- How Does Clickthrough Data Reflect Retrieval Quality?, Radlijnski+, CIKM'08

## Relevance Feedback
### Survey
- (Explicit Feedback) A survey on the use of relevance feedback for information access systems., Ruthven+, The Knowledge Engineering Review, 2003.
- (Implicit Feedaback) Evaluating implicit measures to improve web search, Fox+, ACM Transactions aon Imformation Systems, 2005.#
