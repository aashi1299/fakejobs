import streamlit as st
import pickle
import requests
from bs4 import BeautifulSoup
import re

# Load trained model and vectorizer
with open("model/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("model/job_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Function to extract text from a job URL (basic/general-purpose)
def extract_job_text_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to extract paragraph or job description text
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])

        # Fallback: get all visible text
        if not text.strip():
            text = soup.get_text()

        # Clean text
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    except Exception as e:
        return f"Error extracting job text: {e}"

# Streamlit UI
st.set_page_config(page_title="Job Authenticity Checker", layout="centered")
st.title("🕵️ Job Authenticity Classifier")
st.markdown("Paste a job listing URL below and find out if it's real or potentially fake!")

job_url = st.text_input("🔗 Job Listing URL")

if job_url:
    with st.spinner("Extracting job details and running prediction..."):
        job_text = extract_job_text_from_url(job_url)

        if job_text.startswith("Error"):
            st.error(job_text)
        else:
            input_vector = vectorizer.transform([job_text])
            prediction = model.predict(input_vector)[0]
            prob = model.predict_proba(input_vector)[0][prediction]

            if prediction == 1:
                st.error(f"⚠️ This job posting appears to be **FAKE** (Confidence: {prob:.2%})")
            else:
                st.success(f"✅ This job posting appears to be **REAL** (Confidence: {prob:.2%})")

            if st.checkbox("🔍 View Extracted Text"):
                st.text_area("Extracted Job Description", job_text, height=300)
