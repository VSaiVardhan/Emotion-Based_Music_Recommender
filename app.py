import streamlit as st
import pandas as pd
import joblib
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load assets
model = joblib.load("emotion_predictor.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
songs_dataset_en = pd.read_csv("songs_dataset_en.csv")
songs_dataset_te = pd.read_csv("songs_dataset_te.csv")

# Set title and subtitle
st.set_page_config(page_title="Emotion-Based Music Recommender 🎵", layout="wide")
st.title("Emotion-Based Music Recommender 🎶")
st.markdown("Describe your mood and get the perfect song recommendations based on how you feel.")
st.markdown("Your current emotion is detected from what you type and then songs are recommended based on detected emotion.")

# Preprocess function
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    return ' '.join(tokens)

# Song recommendation based on predicted emotion
def get_songs_by_emotion(emotion, language):
    df = songs_dataset_te if language.lower() == "telugu" else songs_dataset_en
    return df[df['emotion_cluster'].str.lower() == emotion.lower()].sample(n=min(5, len(df)))

# UI Elements
language = st.selectbox("🌐 Select your preferred language:", ["English", "Telugu"])
user_input = st.text_area("🗣️ How are you feeling right now?", height=100)

if st.button("🎧 Recommend Songs"):
    if user_input.strip() == "":
        st.warning("Please enter your feelings to get recommendations.")
    else:
        clean = preprocess(user_input)
        vec = vectorizer.transform([clean])
        prediction = model.predict(vec)[0]

        st.success(f"🧠 Detected Emotion: **{prediction.upper()}**")

        st.markdown("---")
        st.subheader("🎵 Recommended Songs for You:")
        recommendations = get_songs_by_emotion(prediction, language)

        if recommendations.empty:
            st.info("No songs found for this emotion in the selected language.")
        else:
            for i, row in recommendations.iterrows():
                st.write(f"- **{row['song_title']}** — *{row['artist']}*")

st.markdown("---")
st.markdown(
    "Built by [VSaiVardhan](https://github.com/VSaiVardhan)",
    unsafe_allow_html=True
)

