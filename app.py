import streamlit as st
import joblib

# Load pipeline
pipeline = joblib.load("fake_news_pipeline.pkl")

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

st.title("📰 Fake News Detection App")
st.write("Enter any news article below and check whether it is **Fake** or **Real**.")

# User input
user_input = st.text_area("Paste news content here...", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text before predicting.")
    else:
        # Direct prediction (pipeline does preprocessing + vectorization + model)
        prediction = pipeline.predict([user_input])[0]

        if prediction == 0:
            st.error("❌ This news is likely **Fake**.")
        else:
            st.success("✅ This news is likely **Real**.")
