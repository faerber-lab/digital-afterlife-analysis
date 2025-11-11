from transformers import pipeline

out_sent = "ENDEVR_sent"
out_emo = "ENDEVR_emo"

model_emo_rlarge = "cardiffnlp/twitter-roberta-large-emotion-latest"
model_emo_rbase = "cardiffnlp/twitter-roberta-base-emotion-latest"
model_sent_rbase = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model_emo_dbertbase ="bhadresh-savani/distilbert-base-uncased-emotion"

sentiment_model = pipeline(
    "sentiment-analysis",
    model=model_sent_rbase
)

## sentiment analysis
id2label_sent = { 
    "0": "Negative", "1": "Neutral", "2": "Positive"
}

def get_sentiment_hf(text):
    try:
        result = sentiment_model(text[:256])[0]   # truncate to 512 tokens
        label_id = result["label"].replace("LABEL_", "")  # extract numeric ID
        label_name = id2label_sent.get(label_id, result["label"])  # map to emotion
        return label_name, float(result["score"])
        # return result["label"], float(result["score"])
    except:
        return None, None

df[["hf_label", "hf_score"]] = df["clean"].apply(lambda x: pd.Series(get_sentiment_hf(x)))
print(df["hf_label"].value_counts())
df.to_csv(out_sent+".csv", index=False)
print(f"✅ Predictions saved as {out_sent}.csv")

## emotion label classification

id2label = { 
    "0": "anger", "1": "anticipation", "2": "disgust", "3": "fear",
    "4": "joy", "5": "love", "6": "optimism", "7": "pessimism",
    "8": "sadness", "9": "surprise", "10": "trust" 
}

def get_emotion_hf(text):
    try:
        result = sentiment_model(text[:256])[0]  # truncate to 256 tokens
        label_id = result["label"].replace("LABEL_", "")  # extract numeric ID
        label_name = id2label.get(label_id, result["label"])  # map to emotion
        return label_name, float(result["score"])
    except:
        return None, None

df[["hf_label", "hf_score"]] = df["clean"].apply(lambda x: pd.Series(get_emotion_hf(x)))
print(df["hf_label"].value_counts())
df.to_csv(out_emo+".csv", index=False)
print(f"✅ Predictions saved as {out_sent}.csv")
