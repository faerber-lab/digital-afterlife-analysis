# Supplementary Materials
## Between Death and Data: Algorithmic Afterlives and the Ethics of Digital Continuity (2025)

This repository contains the data and code accompanying the paper "_Between Death and Data: Algorithmic Afterlives and the Ethics of Digital Continuity._"
The analysis explores public perceptions and emotional responses to AI-mediated interactions with digital representations of the deceased, based on a dataset of YouTube comments.

## Overview

We analyzed a total of **3,574 comments** from the YouTube documentaries:

- **ENDRV:** ["Living Forever Through AI: Digital Immortality and the Future of Death (2023)"](https://www.youtube.com/watch?v=LTduwK0-sGI), Access date: 2025-11-11  
- **GUARDIAN:** ["Back from the dead: could AI end grief? (2024)"](https://www.youtube.com/watch?v=5udOx8-QxtE), Access date: 2025-11-12
- **ABC News:** ["Generative AI helps grieving family remember their daughter (2024)"](https://www.youtube.com/watch?v=0JTzrYarcJw), Access date: 2025-11-12

Our analysis combined the following:

- **Sentiment Analysis** using fine-tuned LLMs (RoBERTa)
- **Unsupervised Topic Modeling** with BERTopic

## Explore the Full Analysis

First, install all dependencies by running:

```
pip install -r requirements.txt
```
To perform the full data processing and analysis, run [`pipeline.ipynb`](pipeline.ipynb) in Jupyter Notebook or Jupyter Lab. 

To download and analyze comments from your own YouTube video, change the YouTube URL in the notebook as shown below:
```
URL = "https://www.youtube.com/watch?v=5udOx8-QxtE" # Change this to your desired video URL
```
This will automatically retrieve comments from the specified video and integrate them into the analysis pipeline.

To visualize the analysis results, run the [`visualization.ipynb`](visualization.ipynb).

## Repository Contents

| File | Description |
|------|-------------|
| `data/` | The dataset contains the downloaded YouTube comments, and the results of the analysis. |
| `src/` | Python scripts for data processing and analysis: |
| &nbsp;&nbsp;`crawling.py` | Script for scraping YouTube comments. |
| &nbsp;&nbsp;`preprocess.py` | Script for cleaning and preparing text data for analysis. |
| &nbsp;&nbsp;`sentiment-analysis.py` | Script for performing sentiment analysis using fine-tuned LLMs. |
| &nbsp;&nbsp;`bertopic-analysis.py` | Script for topic modeling with BERTopic. |
| `pipeline.ipynb` | Jupyter notebook demonstrating the full analysis pipeline. |
| `visualization.ipynb` | Jupyter notebook for visualizing the analysis results. |
| `requirements.txt` | List of required Python packages for running the analysis. |



## License

This repository is released under the MIT License.
