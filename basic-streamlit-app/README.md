### Netflix Title Sorter App
_An interactive Streamlit app for exploring Netflix's catalog by content type, rating, and release year_

This project is a lightweight data exploration tool built with **Python**, **pandas**, and **Streamlit**. It allows users to interact with Netflix’s content library by sorting and filtering through shows and movies based on type, rating, and year of release.

---

## 🚀 Project Overview

The Netflix dataset includes hundreds of titles, ranging from feature films to TV series, each with attributes like genre, rating, and release year. This app offers an intuitive interface for exploring that content in real time. Users can select filters to:
- Compare ratings
- Focus on specific content types (Movie vs TV Show)
- View content released in a particular year

It’s a great example of how **data filtering and UI design** can make large datasets more accessible and user-friendly.

---

## 🛠️ App Features

- 🔍 **Select Content Type:** Filter between “Movie” and “TV Show”
- 🎯 **Filter by Rating:** Choose from Netflix ratings like PG, R, TV-MA, etc.
- 📅 **Choose Release Year:** Use a slider to select any year from the dataset
- 📊 **Live Data Table:** View dynamically filtered content
- 🖼️ **Netflix Logo Display:** Appends a visual image of the brand for polish
- 🎈 **Fun UI Element:** A `st.balloons()` animation adds light interactivity

**Example Use Case**

A user interested in PG-rated movies from 2010 can:
- Select “Movie” from the type dropdown
- Choose “PG” from the rating menu
- Slide to “2010” using the year slider
- Instantly see a table of results filtered by all three criteria

---

## ⚙️ Setup & Installation

Install the required libraries:
- pandas
- streamlit

Use the console to install:
```bash
pip install pandas
pip install streamlit
```

### To run the app:
```bash
streamlit run /Users/brynnwilary/Desktop/WILARY-PYTHON-PORTFOLIO/NetflixSorterApp/main.py
```

(Replace the file path above with the correct location on your computer.)

---

## References
- [Netflix Titles Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [pandas Documentation](https://pandas.pydata.org/)

---

## Visual Example

<img width="500" alt="Netflix Streamlit App Example" src="https://github.com/user-attachments/assets/netflix-app-example.png" />
