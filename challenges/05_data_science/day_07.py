import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")
    model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
    ])
    model.fit(df['comment'], df['label'])
    return model

model = load_model()

st.title("Youtube comment classifier")
st.write("Classify your comment as Toxic or supportive")
user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]
    if prediction == "toxic":
        st.error("This comment is likely **Toxic**")
    else:
        st.success("This comment is **Supportive**")

