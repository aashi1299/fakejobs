# 🕵️ Job Authenticity Classifier

A simple, open-source Streamlit app that predicts whether a job posting is **real or fake** using machine learning and NLP.

---

## 🔍 What It Does
- Accepts a job listing URL from the user
- Extracts the job description text from the page
- Uses a trained Logistic Regression model to classify the job as **REAL** or **FAKE**
- Displays the result with a confidence score

---

## 🧠 How It Works
1. **Dataset:** Trained on the [Fake Job Postings Dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
2. **Text Processing:** Combines job title, location, description, requirements, and company profile
3. **Vectorization:** TF-IDF vectorizer (5000 features)
4. **Model:** Logistic Regression trained on a balanced dataset
5. **Scraping:** Uses BeautifulSoup to extract job content from the provided URL

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/aashi1299/fakejobs
cd fakejobs
```

### 2. Install Dependencies
It's recommended to use a virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirement.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

## 📈 Model Performance
Trained on balanced data (upsampled minority class):
- **Accuracy:** 99.0%
- **Precision (Fake Jobs):** 98.2%
- **Recall (Fake Jobs):** 99.8%

---

## 📌 Notes
- Works best on sites with publicly viewable job descriptions (e.g., Indeed)
- Sites like LinkedIn may block scraping (use with caution)

---

## 📬 Contributing
Feel free to fork, tweak, and contribute! PRs welcome.

---

## 📜 License
MIT License © 2025 Aashi Sharma
