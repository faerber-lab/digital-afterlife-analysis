# Between Death and Data: Algorithmic Afterlives and the Ethics of Digital Continuity

This repository contains the data and code for the paper: **“Between Death and Data: Algorithmic Afterlives and the Ethics of Digital Continuity.”** The study examines public perceptions and emotional responses to AI-mediated interactions with representations of the deceased, using data from YouTube comments.

## Overview

We analyzed **2,637 comments** from the YouTube documentary *“Living Forever Through AI: Digital Immortality and the Future of Death”* (ENDEVR). Our methodology combined:

- **Sentiment Analysis** using fine-tuned large language models (LLMs)
- **Unsupervised Topic Modeling** with BERTopic

## Repository Contents

| File | Description |
|------|-------------|
| `crawl.py` | Script for scraping YouTube comments. |
| `preprocess.py` | Script for cleaning and preparing text data for analysis. |
| `sentiment-analysis.py` | Script for performing sentiment analysis using fine-tuned LLMs. |
| `bertopic-analysis.py` | Script for topic modeling with BERTopic. |
| `pipeline.ipynb` | Jupyter notebook demonstrating the full analysis pipeline. |


## Explore the Full Analysis

Open `pipeline.ipynb` in Jupyter Notebook or Jupyter Lab.

## Data

The dataset contains YouTube comments collected in accordance with YouTube’s Terms of Service. The preprocessed data used in the analyses is included in the repository.

## License

This repository is released under the MIT License.
