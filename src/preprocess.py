import json, re, string
import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

input_data = "ENDEVR.json"

data = []
with open(input_data, "r") as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                data.append(json.loads(line))
            except:
                pass

df = pd.DataFrame(data)
print(f"Loaded {len(df)} comments")
df = df.dropna(subset=["text"])
df["text"] = df["text"].astype(str)

def clean_text(txt):
    txt = txt.lower()
    txt = re.sub(r"http\S+|www\S+", "", txt)
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    txt = re.sub(r"\s+", " ", txt)
    return txt.strip()

df["clean"] = df["text"].apply(clean_text)
print (df["clean"][5])
