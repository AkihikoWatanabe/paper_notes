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
- Pointing the unknown words, Gulcehre+, ACL'16, [paper](http://www.aclweb.org/anthology/P16-1014)
- [Sequence-to-Dependency Neural Machine Translation](https://www.slideshare.net/mamoruk/acl2017-seq2dep-nmt), Wu+, ACL'17, [paper](http://aclweb.org/anthology/P/P17/P17-1065.pdf)
- [What do Neural Machine Translation Models Learn about Morphology?](http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/06.pdf), Belinkov+, ACL'17, [paper](http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/06.pdf)

## Representation
### General Purpose
- [StarSpace: Embed All The Things!](notes/starspace_embed_all_the_things.md), Wu+, arXiv'17, [arXiv](https://arxiv.org/abs/1709.03856), [project](https://github.com/facebookresearch/Starspace)

### Sentence Level
- A structured self-attentive sentence embedding, Li+ (Bengio group), [arXiv](https://arxiv.org/pdf/1703.03130.pdf)
- [Learning Distributed Representations of Sentences from Unlabelled Data](notes/learning_distributed_representations_of_sentences_from_unlabelled_data.md), Hill+, NAACL'16, [paper](http://www.aclweb.org/anthology/N16-1162)
- [Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](https://www.slideshare.net/naoakiokazaki/supervised-learning-of-universal-sentence-representations-from-natural-language-inference-data), Conneau+, EMNLP'17, [paper](https://www.slideshare.net/naoakiokazaki/supervised-learning-of-universal-sentence-representations-from-natural-language-inference-data)[memo](notes/supervised_learning_of_universal_sentence_representations_from_natural_language_inference_data.md)

### Document Level
- [Document Modeling with Gated Recurrent Neural Network for Sentiment Classification](notes/document_modeling_gru.md), Tang+, EMNLP'15.
- [Distraction-Based Neural Networks for Modeling Documents](notes/distraction_based_summ.md), Chen+, IJCAI'16., [paper](https://www.ijcai.org/Proceedings/16/Papers/391.pdf)
- [A hierarchical neural autoencoder for paragraphs and documents](notes/a_hierarchical_neural_autoencoder_for_paragraphs_and_documents.md), Li+, ACL'15.
- LCSTS: A large scale chinese short text summarizatino dataset, Hu+, EMNLP'15.
- Larger-context language modelling with recurrent neural networks, Wang+, [arXiv](https://arxiv.org/abs/1511.03729)
- [Teaching Machines to Read and Comprehend](notes/teaching_machines_to_read_and_comprehend.md), Hermann+, [NIPS 2015](http://dl.acm.org/citation.cfm?id=2969428)

### Additivity
- [Skip-Gram – Zipf + Uniform = Vector Additivity](http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/09.pdf), Gittens+, ACL'17, [paper](http://aclweb.org/anthology/P/P17/P17-1007.pdf)

## Beam-Search
- Sequence-to-Sequence Learning as Beam-Search Optimization, Wiseman+, EMNLP'16.

## Speed-Up
- [Learning to skim text](http://www.lr.pi.titech.ac.jp/~haseshun/acl2017suzukake/slides/07.pdf), Yu+, ACL'17, [paper](http://aclweb.org/anthology/P/P17/P17-1172.pdf)

# Natural Language Generation (data2text, concept2text)
## Survey
- Survey of the State of the Art in Natural Language Generation: Core tasks, applications and evaluation, Gatt+, arXiv'17.
- An Architecture for Data to Text Systems, Reiter, ENLG'07, [paper](http://delivery.acm.org/10.1145/1620000/1610180/p97-reiter.pdf?ip=125.14.202.208&id=1610180&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=805759951&CFTOKEN=87389191&__acm__=1505308749_f6370e1bae15e555243056b991922cad)
- Content Selection in Data-to-Text Systems: A Survey, arXiv'16, Gkatzia, [arXiv](https://arxiv.org/pdf/1610.08375.pdf)
- [slide](https://www.slideshare.net/akihikowatanabe3110/brief-survey-of-datatotext-systems)

## Neural
- What to talk about and how? Selective Generation using LSTMs with Coarse-to-Fine Alignment, Mei+, NAACL-HLT’16, [paper](http://www.aclweb.org/anthology/N16-1086)

- (concept2text) [Neural Text Generation from Structured Data with Application to the Biography Domain, Lebret+](https://www.slideshare.net/akihikowatanabe3110/neural-text-generation-from-structured-data-with-application-to-the-biography-domain), Lebret+, EMNLP'16, [paper](https://arxiv.org/pdf/1603.07771.pdf)
- [Multi-Task Video Captioning with Video and Entailment Generation](https://www.slideshare.net/HangyoMasatsugu/hangyo-acl-paperreading2017multitask-video-captioning-with-video-and-entailment-generation/1), Pasunuru+, ACL'17, [paper](http://aclweb.org/anthology/P/P17/P17-1117.pdf), [memo](notes/multi_task_video_captioning_with_video_and_entailment_generation.md)

## Controllable NLG
- [Controllable Text Generation, Hu+, arXiv'17.](notes/controllable_text_generation.md)

## Single-framework (jointly solve content-selection and surface realization)
- Learning to sportscast: a test of grounded language acquisition, Chen+, ICML'08, [paper](http://www.cs.utexas.edu/~ml/papers/david-icml-08.pdf)
- Training a multilingual sportscaster: Using perceptual context to learn language, Chen+, Artificial Intelligence Research'10, [paper](https://arxiv.org/pdf/1405.7711.pdf)
- A simple domain-independent probabilistic approach to generation, Angeli+, EMNLP'10, [paper](http://nlp.cs.berkeley.edu/pubs/Angeli-Liang-Klein_2010_Generation_paper.pdf)
- (concept2text) Generative alignment and semantic parsing for learning from ambiguous supervision, Kim+, COLING'10, [paper](https://aclweb.org/anthology/C/C10/C10-2062.pdf)
- (concept2text) Unsupervised concept-to-text generation with hypergraphs, Konstas+, NAACL-HLT'12, [paper](http://delivery.acm.org/10.1145/2390000/2382151/p752-konstas.pdf?ip=125.14.202.208&id=2382151&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=805759951&CFTOKEN=87389191&__acm__=1505310128_57b77b92df6f4df850de87ef9bb705ea)
- (concept2text) A Global Model for Concept-to-Text Generation, Konstas+, Journal of Artificial Intelligence Research, Vol. 48, pp.305--346, 2013, [paper](http://www.jair.org/media/4025/live-4025-7407-jair.pdf)
- (concept2text) Inducing document plans for concept-to-text generation, Konstas+, EMNLP'13, [paper](http://www.aclweb.org/anthology/D13-1157)
- (concept2text, BabyTalk論文) Automatic generation of textual summaries from neonatal intensive care data, Porter+, AIME'07, [paper](http://www.sciencedirect.com/science/article/pii/S0004370208002117)

## Data-Driven Approach
(concept2text) Collective content selection for concept-to-text generation, Barzilay+, HLT/EMNLP'05, [paper](http://delivery.acm.org/10.1145/1230000/1220617/p331-barzilay.pdf?ip=125.14.202.208&id=1220617&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=805759951&CFTOKEN=87389191&__acm__=1505310520_1f2899d03172876aae83af892267bdb0)
(concept2text) Aggregation via set partitioning for natural language generation, Barzilay+,  HLT-NAACL, [paper](http://delivery.acm.org/10.1145/1230000/1220881/p359-barzilay.pdf?ip=125.14.202.208&id=1220881&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=805759951&CFTOKEN=87389191&__acm__=1505310641_68b6ba80706ed3de5815ee81a8b4d791)

## Rule-based
- [Choosing words in computer-generated weather forecasts](notes/choosing_words_in_computer_generated_weather_forecasts.md), Reiter+, Artificial Intelligence'05 [paper](http://www.sciencedirect.com/science/article/pii/S0004370205000998)
- [Using natural language processing to produce weather forecasts](notes/using_natural_language_processing_to_produce_weather_forecasts.md), Goldberg+, IEEE Expert: Intelligent Systems and Their Applications'94, [paper](http://ieeexplore.ieee.org/document/294135/)
- [Design of a knowledge-based report generator](notes/design_of_a_knowledge_based_report_generator.md), Kukich, ACL'83, [paper](http://delivery.acm.org/10.1145/990000/981340/p145-kukich.pdf?ip=125.14.202.208&id=981340&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=805759951&CFTOKEN=87389191&__acm__=1505309566_e38d2569c8ab995fe978080ecc4d7df0)
- Generating approximate geographic descriptions, Turner+, ENLG'10, [paper](http://www.aclweb.org/anthology/W09-0607)
- (concept2text) Coral: Using natural language generation for navigational assistance, Dale+, Australasian computer science conference'03, [paper](https://pdfs.semanticscholar.org/5ca0/2daaa0d676520d8642ad00351121ff1f29c4.pdf)

## others
- Comparing Multi-label Classification with Reinforcement Learning for Summarization of Time-series Data, Gkatzia+, ACL'14, [paper](http://www.aclweb.org/anthology/P14-1116)
- A framework for automatic text generation of trends in physiological time series data, Banaee+, In Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics, 2013, [paper](http://ieeexplore.ieee.org/document/6722414/)
- Automatically generated linguistic summaries of energy consumption data, van der Heide+, In Proceedings of the Ninth International Conference on Intelligent Systems Design and Applications, pages 553-559, 2009, [paper](http://ieeexplore.ieee.org/document/5364975/)
- Verbalizing time-series data: with an example of stock price trends, Kobayashi+, IFSA-EUSFLAT'09, [paper](https://pdfs.semanticscholar.org/c0e2/ab34befbb9b401b6ad1d02c71ab2bd1c4794.pdf?_ga=2.46822437.363135274.1505310881-1340047873.1468486303)
- Deep Match between Geology Reports and Well Logs Using Spatial Information, Tong+, CIKM'16, [paper](http://dl.acm.org/citation.cfm?id=2983352)
- (concept2text) Learning semantic correspondences with less supervision, Liang+, ACL/IJCNLP'09, [paper](https://cs.stanford.edu/~pliang/papers/semantics-acl2009.pdf)
- (concept2text) A generative model for parsing natural language to meaning representations, Lu+, EMNLP'08, [paper](http://www.aclweb.org/anthology/D08-1082)

# Time Series data Processing
- Artificial neural networks in business: Two decades of research, Tkac+, Applied Soft Computing 2016, [paper](http://www.sciencedirect.com/science/article/pii/S1568494615006122)
- [Prediction-based portfolio optimization model using neural networks](notes/prediction_based_portfolio_optimization_model_using_neural_networks.md), Freitas+, Neurocomputing'09, [paper](http://dl.acm.org/citation.cfm?id=1539984)
- [Recurrent neural network and a hybrid model for prediction of stock returns](notes/recurrent_neural_network_and_a_hybrid_model_for_prediction_of_stock_returns.md), Akhter+, Expert Systems with Applications'14, [paper](http://dl.acm.org/citation.cfm?id=2776067)
- Derivative Delay Embedding: Online Modeling of Streaming Time Series, Zhang+, CIKM'16, [paper](https://arxiv.org/pdf/1609.07540.pdf)

# Machine Learning
## Online Learning
- [Tutorial, in Japanese](http://www.r.dl.itc.u-tokyo.ac.jp/~nakagawa/SML1/online-L1.pdf)

## Structured Learning
- [Online Distributed Passive-Aggressive Algorithm for Structured Learning](notes/online_distributed_passive_aggressive_algorithm_for_structured_learning.md), Zhao+, CCL and NLP-NABD'13
- Scalable Large-Margin Online Learning for Structured Classification, Crammer+, 2005.
- [Structured Learning for Non-Smooth Ranking Losses](notes/structured_learning_for_non_smooth_ranking_losses.md), Chakrabarti+, KDD'08, [paper](http://mllab.csa.iisc.ernet.in/html/pubs/chiru_chakrabarti_KDD_08.pdf)
- [A support vector method for Optimizing Average Precision](notes/a_support_vector_method_for_optimizing_average_precision.md), Yue+, SIGIR'07, [paper](https://www.cs.cornell.edu/people/tj/publications/yue_etal_07a.pdf)
- [tool, SVMmap](http://projects.yisongyue.com/svmmap)

## domain adaptation
- [Human Centered NLP with User-Factor Adaptation](notes/human_centered_nlp_with_user_factor_adaptation.md), Lynn+, EMNLP'17, [paper](http://aclweb.org/anthology/D17-1120)

# Document Summarization
## Survey
- Recent Advances in Document Summarization, Yao+, Knowledge and Information Systems'17, [paper](http://www.icst.pku.edu.cn/lcwm/wanxj/files/summ_survey_draft.pdf)
- A Survey of Text Summarization Techniques, Nenkova+, Springer'12, [book](https://link.springer.com/chapter/10.1007%2F978-1-4614-3223-4_3)
- (A survey on Automatic Text Summarization, Das+, CMUの教材？) 

## Neural
- Neural Summarization by Extracting Sentences and Words, Chenc+, ACL'16, [paper](http://www.aclweb.org/anthology/P16-1046).
- [Distraction-Based Neural Networks for Modeling Documents](notes/disraction_based_summ.md), Chen+, IJCAI'16., [paper](https://www.ijcai.org/Proceedings/16/Papers/391.pdf)
- Cutting-off redundant repeating generations for neural abstractive summarization, Suzuki+, EACL'17 [paper](https://www.aclweb.org/anthology/E/E17/E17-2047.pdf)
- A Deep Reinforced Model for Abstractive Summarization, Paulus+(Socherもいる), arXiv'17, [paper](https://arxiv.org/pdf/1705.04304.pdf)
- [Get To The Point: Summarization with Pointer-Generator Networks](https://www.slideshare.net/secret/zIGREgUWCfzLnT), See+, ACL'17, [paper](https://arxiv.org/pdf/1704.04368.pdf)[code](https://github.com/abisee/pointer-generator)
- [Incorporating Copying Mechanism in Sequence-to-Sequence Learning](https://www.slideshare.net/akihikowatanabe3110/incorporating-copying-mechanism-in-sequene-to-sequence-learning), Gu+, ACL'16, [paper](http://www.aclweb.org/anthology/P16-1154)
- [A Neural Attention Model for Sentence Summarization](https://www.slideshare.net/akihikowatanabe3110/a-neural-attention-model-for-sentence-summarization-65612331), Rush+, EMNLP'15, [paper](https://aclweb.org/anthology/D/D15/D15-1044.pdf)

## Supervised
- A Trainable Document Summarizer, Kupiec+, SIGIR'95.
- Text Summarization using a trainable summarizer and latent semantic analysis, Yeh+, Information Processing and Management 2005.
- Document Summarization using Conditional Random Fields, Shen+, IJCAI07.
- (構造学習) 転移学習による抽出型要約の精度向上, 西川+, 情報処理学会研究報告, 2011.
- (構造学習) Learning from Numerous Untailored Summaries, Kikuchi+, PRICAI'16.
- Learning to Generate Coherent Sumamry with Discriminative Hidden Semi-Markov Model, Nishikawa+, COLING'14

## Unsupervised(Graph-based)
- [CTSUM: Extracting More Certain Summaries for News Articles](https://www.slideshare.net/akihikowatanabe3110/ctsum-extracting-more-certain-summaries-for-news-articles), Wan+, SIGIR'14, [paper](http://dl.acm.org/citation.cfm?id=2609559)

## Metrics
- Re-evaluating Automatic Summarization with BLEU and 192 Shades of ROUGE, Graham, EMNLP'15, [paper](http://aclweb.org/anthology/D/D15/D15-1013.pdf)
- Why We Need New Evaluation Metrics for NLG, Novikova+, EMNLP'17, [paper](http://aclweb.org/anthology/D17-1237) 

# Sentence Compression
## Neural
- [Sentence Compression by Deletion with LSTMs](https://www.slideshare.net/akihikowatanabe3110/sentence-compression-by-deletion-with-lstms), Fillipova+, EMNLP'15, [paper](https://static.googleusercontent.com/media/research.google.com/ja//pubs/archive/43852.pdf)

# Personalized Document Summarization
- User-model based personalized summarization, Diaz+, Information Processing and Management 2007.
- [Joint Optimization of User-desired Content in Multi-document Summaries by Learning from User Feedback](notes/joint_optimization_of_user_desired_content_in_multi_document_summaries_by_learning_from_user_feedback.md), P.V.S+, ACL'17. [paper](http://aclweb.org/anthology/P/P17/P17-1124.pdf)
- Extended Recommendation Framework: Generating the Text of a User Review as a Personalized Summary Poussevin+, CBRecsys'15, [paper](http://ceur-ws.org/Vol-1448/paper7.pdf)

# Recommender Systems[tools](./notes/recsys_tools.md)
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
- A General Approximation Framework for Direct Optimization of Information Retrieval Measures (ApproxAP, ApproxNDCG), Qin+, Information Retrieval, 2010, [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-164.pdf)

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

# SentimentAnalysis
- [Tutorial on ENLP2016](https://www.aclweb.org/mirror/emnlp2016/tutorials/zhang-vo-t4.pdf)

# 後で読む
- Multi-View Unsupervised User Feature Embedding for Social Media-based Substance Use Prediction, Ding+, EMNLP'17, [paper](http://aclweb.org/anthology/D/D17/D17-1240.pdf)
- MoodSwipe: A Soft Keyboard that Suggests Messages Based on User-Specified Emotions, Huang+, EMNLP'17, [paper](http://aclweb.org/anthology/D/D17/D17-2013.pdf)
