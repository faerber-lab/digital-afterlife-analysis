# sentiment-analysis.py
import pandas as pd
from transformers import pipeline

# Models
MODEL_SENT = "cardiffnlp/twitter-roberta-base-sentiment-latest"
MODEL_EMO = "cardiffnlp/twitter-roberta-large-emotion-latest"

# Label maps
id2label_sent = { "0": "Negative", "1": "Neutral", "2": "Positive" }
id2label_emo = {
    "0": "anger", "1": "anticipation", "2": "disgust", "3": "fear",
    "4": "joy", "5": "love", "6": "optimism", "7": "pessimism",
    "8": "sadness", "9": "surprise", "10": "trust"
}

def get_prediction(text, pipe, label_map):
    try:
        result = pipe(text[:256])[0]
        label_id = result["label"].replace("LABEL_", "")
        label_name = label_map.get(label_id, result["label"])
        return label_name, float(result["score"])
    except Exception:
        return None, None

def analyze_sentiment(input_file="ENDEVR_clean.csv", output_sent="ENDEVR_sent.csv", output_emo="ENDEVR_emo.csv"):
    df = pd.read_csv(input_file)

    # Sentiment
    sent_pipe = pipeline("sentiment-analysis", model=MODEL_SENT)
    df[["sent_label", "sent_score"]] = df["clean"].apply(
        lambda x: pd.Series(get_prediction(x, sent_pipe, id2label_sent))
    )
    df.to_csv(output_sent, index=False)
    print(f"✅ Sentiment predictions saved to '{output_sent}'")

    # Emotion
    emo_pipe = pipeline("sentiment-analysis", model=MODEL_EMO)
    df[["emo_label", "emo_score"]] = df["clean"].apply(
        lambda x: pd.Series(get_prediction(x, emo_pipe, id2label_emo))
    )
    df.to_csv(output_emo, index=False)
    print(f"✅ Emotion predictions saved to '{output_emo}'")

if __name__ == "__main__":
    analyze_sentiment()
