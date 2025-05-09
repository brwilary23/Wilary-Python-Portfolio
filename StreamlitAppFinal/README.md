# 📈 Stock Analysis App

The **Stock Analysis App** is an interactive web application built with Streamlit that allows users to analyze S&P 500 company stocks. Users can compare financial metrics—such as stock price, market cap, EBITDA, and revenue growth—against market, sector, and exchange averages.

![App Screenshot](./Screenshot%202025-05-08%20at%208.16.46%E2%80%AFPM.png)

---

## 🔧 Features

- **Interactive Sidebar Search**  
  Select stock symbols or search by company name. Instantly view key company fundamentals.

- **Comparative Analysis Charts**  
  Compare a stock’s metrics to market, sector, and exchange benchmarks with interactive visualizations.

- **Auto-Generated Investment Summary**  
  Get a narrative summary of how a stock is performing relative to its peers.

- **Streamlit Controls**  
  Clean layout with toggles for additional data and deep dives.

- **NLP Symbol Matching with spaCy**  
  Enhances the search experience using named entity recognition (NER).

---

## 📁 Project Structure

```
StreamlitAppFinal/
├── main.py                                 # main Streamlit application
├── sp500_companies.csv                     # dataset of S&P 500 companies
├── Screenshot 2025-05-08 at 8.16.46 PM.png # UI screenshot
├── README.md                               # project documentation
```

---

## ▶️ Getting Started

### 1. Install Dependencies

```bash
pip install streamlit pandas numpy plotly pydeck spacy
python -m spacy download en_core_web_sm
```

### 2. Run the App Locally

```bash
streamlit run main.py
```

### 3. Deploy Online (optional)

- Push to GitHub
- Deploy on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📊 Metrics Analyzed

- **Company Metrics**
  - Market Capitalization
  - EBITDA
  - Revenue Growth

- **Comparison Categories**
  - S&P 500 Market Average
  - Sector Average
  - Exchange Average

---

## ✅ Requirements Fulfilled

- ✔️ Interactive frontend with charts and data
- ✔️ Backend logic for filtering and comparisons
- ✔️ Clear, user-friendly design
- ✔️ Deployment-ready structure

---

## 🧠 Built With

- [Streamlit](https://streamlit.io)
- [pandas](https://pandas.pydata.org/)
- [spaCy](https://spacy.io/)
- [plotly](https://plotly.com/python/)
