# paper_notes

![Open issues](https://img.shields.io/github/issues/AkihikoWatanabe/paper_notes) ![Stars](https://img.shields.io/github/stars/AkihikoWatanabe/paper_notes) ![License](https://img.shields.io/github/license/AkihikoWatanabe/paper_notes)

This repository is a manually curated collection of **AI-related papers and related resources**, such as blog posts, repositories, slides, and SNS posts.  
All items are managed as **GitHub Issues**.

The primary purpose of this repository is to serve as a **personal study log and memory aid** for the maintainer.  
Since the maintainer is Japanese, **paper notes are written in Japanese**, reflecting the maintainer’s own understanding and learning process.

---

## Paper Metadata and Notes

For paper-related Issues, metadata and abstracts are automatically retrieved via the **arXiv API**[^1] and included in the Issue description.

Since the maintainer is Japanese:

- Japanese translations of abstracts  
- Japanese summaries of papers  

are **automatically generated using GPT**, and  **labels are manually assigned** based on the maintainer’s own interpretation and understanding of the content.

---

## Actively Collected Research Areas

The repository currently focuses on the following four areas:

- Natural Language Processing (NLP)
- Computer Vision (CV)
- Speech Processing
- Recommender Systems (RecSys)

---

## Topics of Recent Interest

Recent areas of focus include (but are not limited to):

- Large Language Models (LLMs) / Vision-Language Models (VLMs) / Diffusion Models
- Proprietary / Open-Weight / Open-Source Models
- Multimodal Models / Unified Multimodal Models (UMMs)
- AI Agents / Context Engineering / Memory / Evaluation Harnesses / Scaffoldings
- (Synthetic) Datasets / Evaluation / Benchmarks
- Pre-training / Mid-training / Post-training
- Reinforcement Learning
- Test-time Scaling / Test-time Learning
- Representation Learning / Embeddings
- Self-Improving AI
- Transformer architectures (Attention, Positional Encoding, Residual Streams, etc.)

---

## Issue Notes and Granularity

Each Issue may contain:

- The maintainer’s understanding or interpretation of the work [^2]
- Initial impressions
- Links to explanatory SNS posts or discussions

The **level of detail varies** depending on available time and interest at the time of reading.  
Notes are managed using the following labels (not all Issues have been fully labeled yet because the maintainer have manually labeled it):

- [![Initial Impression Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Initial%20Impression%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Initial%20Impression%20Notes"): first impressions based on the abstract, related posts, or skimming
- [![One-Line Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/One-Line%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22One-Line%20Notes%22): a single key takeaway
- [![Surface-level Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Surface-level%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Surface-level%20Notes%22): a broad summary of the paper
- [![KeyPoint Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/KeyPoint%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22KeyPoint%20Notes%22): notes on multiple important technical points
- [![In-Depth Notes](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/In-Depth%20Notes)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22In-Depth%20Notes%22): details of the paper and multiple important technical points with the maintainer's own opinion
- [![Reference Collection](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Reference%20Collection)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Reference%20Collection%22): a collection of related links (e.g., explanatory posts)

---

## Label Taxonomy

Labels are broadly categorized and color-coded as follows:

- **Medium**: [![Blog](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Blog)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ABlog), [![Video](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Video)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AVideo), [![Slide](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Slide)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ASlide), ...

- **Research Field**: [![NLP](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/NLP)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ANLP), [![ComputerVision](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ComputerVision)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AComputerVision), [![SpeechProcessing](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/SpeechProcessing)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ASpeechProcessing), [![RecommenderSystems](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/RecommenderSystems)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ARecommenderSystems), ...

- **Task**: [![DocumentSummarization](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/DocumentSummarization)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ADocumentSummarization), [![MachineTranslation](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/MachineTranslation)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AMachineTranslation), [![Evaluation](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Evaluation)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AEvaluation), ...

- **Method**: [![LanguageModel](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/LanguageModel)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ALanguageModel), [![AIAgents](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/AIAgents)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AAIAgents), [``![ReinforcementLearning](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ReinforcementLearning)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AReinforcementLearning), ...

- **Fine-grained Category**: [![OpenWeight](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/OpenWeight)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AOpenWeight), [![AttentionSinks](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/AttentionSinks)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AAttentionSinks), [![Architecture](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Architecture)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AArchitecture), ...

- **Properties / Characteristics**: [![Controllable](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/Controllable)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AControllable), [![EfficiencyImprovement](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/EfficiencyImprovement)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AEfficiencyImprovement), [![LowResource](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/LowResource)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ALowResource), ...

- **Conference / Journal**: [![ACL](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/ACL)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3AACL), [![CVPR](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/CVPR)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ACVPR), [![TACL](https://img.shields.io/github/labels/AkihikoWatanabe/paper_notes/TACL)](https://github.com/AkihikoWatanabe/paper_notes/issues?q=is%3Aissue%20state%3Aopen%20label%3ATACL), ...


The above labels are just a few examples, and there are currently 600+ different labels in total. You can filter issues using these labels.

---

## Wiki and Interactive Access (DeepWiki)

In addition to Issue-based notes, this repository provides two complementary ways to explore and consume the collected information.

### [Wiki](https://github.com/AkihikoWatanabe/paper_notes/wiki): Personal Trend Notes

A Wiki is maintained to record **personal impressions of trends** observed while casually browsing papers and discussions on X.

- These notes reflect **subjective observations and interpretations**
- They may contain inaccuracies or biases
- Updates are **irregular and informal**

The Wiki is intended as a lightweight place to capture emerging ideas, trends, and intuitions that may not yet be fully formed.

---

### [DeepWiki](https://deepwiki.com/AkihikoWatanabe/paper_notes): Conversational Interface

This repository can also be explored via **DeepWiki**, which provides a **chat-based interface** for interacting with the contents of this repository.

Using DeepWiki, it may be easier to:

- Interactively extract information from Issues and notes
- Ask questions about specific papers, topics, or trends
- Navigate the repository in a conversational manner rather than browsing Issues manually

---

## Updates

**2026.01.20**
- Update README.md

**2025.10.17**  
- I created a [Wiki](https://github.com/AkihikoWatanabe/paper_notes/wiki) to jot down *personal impressions of trends* observed while casually browsing papers on X.  
- These are purely subjective notes and may contain inaccuracies. Updates will be irregular and informal.

**2025.08.05**  
- At present, the most convenient way to use this repository may be to extract knowledge interactively via its [DeepWiki](https://deepwiki.com/AkihikoWatanabe/paper_notes) interface.

**2025.07.19**  
- The following improvements were made:
  - Fixed degraded blog response time
  - Updated displayed blog content  
  - (A full redesign is still pending 🫠)

**2024.12.28**  
- Several months have passed since I first planned to redesign the blog.

**2024.09**
- I reorganized Issue notes into a blog-style format.  
- The blog is available [here](https://akihikowatanabe.github.io/paper_notes/).

**2017.12.28**
- I started this repository and created the first issue.

---

## Footnotes

[^1]: Metadata and abstracts are used in accordance with the **CC0 1.0 license** specified in the arXiv API terms of use.  
[^2]: Images and screenshots included in Issues or blog posts are, in principle, cited from the original sources (papers, articles, slides, etc.) linked within each Issue.
