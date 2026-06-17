import streamlit as st
import pickle

# Load model
model = pickle.load(
    open("models/trained_model.pkl", "rb")
)

# Load vectorizer
vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

st.title("Twitter Sentiment Analysis")

tweet = st.text_area(
    "Enter Tweet",
    placeholder="Type your tweet here..."
)

if st.button("Analyze Sentiment"):

    if tweet.strip() != "":

        vector = vectorizer.transform([tweet])

        prediction = model.predict(vector)

        st.write("Prediction:", prediction[0])

    else:
        st.warning("Please enter a tweet.")

      
if prediction[0] == 0:
    st.write("Sadness")
if prediction[0] == 1:
    st.write("ANGER")
if prediction[0] == 2:
     st.write("love")
if prediction[0] == 3:
    st.write("Surprise")
if prediction[0] == 4:
    st.write("Fear")
else:
    st.write("Joy")
    