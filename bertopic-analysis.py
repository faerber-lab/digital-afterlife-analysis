from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

out_berttopic = "ENDEVR_btopic"

stop_words = stopwords.words("english")

vectorizer = CountVectorizer(stop_words=stop_words)
topic_model = BERTopic(vectorizer_model=vectorizer,
                       language="english",
                       verbose=True,
                       calculate_probabilities=False)
topics, probs = topic_model.fit_transform(df["clean"])

# topic_model = BERTopic(language="english", verbose=True, calculate_probabilities=False)
# topics, probs = topic_model.fit_transform(df["clean"])

df["topic"] = topics
topic_info = topic_model.get_topic_info()

print("\nTop 10 Topics:\n")
print(topic_info.head(10))

df.to_csv(out_berttopic+"_2.csv", index=False)
print("Done! BERTopic results saved to {out_berttopic} ")

# --- exploring top comments per topic ---
for i in topic_info.head(11)["Topic"]:
    if i == -1:  # -1 means outliers
        continue
    print(f"\n--- Topic {i}: {topic_model.get_topic(i)} ---")
    sample_comments = df[df["topic"] == i]["text"].head(6).tolist()
    for c in sample_comments:
        print("•", c[:500], "...\n")
