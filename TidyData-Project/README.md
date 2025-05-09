### Olympic Medalist Data App
_An interactive data visualization app for exploring 2008 Olympic medalist trends using pandas, matplotlib, seaborn, and Streamlit_

This project is an interactive data application that processes, cleans, and visualizes medalist data from the 2008 Summer Olympics. Using **Python**, **pandas**, and **Streamlit**, users can gain insights into sports, medal distributions, and gender comparisons through dynamic visualizations and pivot tables.

---

## 🚀 Project Overview

Olympic data often comes in untidy formats, with columns and values that are difficult to work with for analysis. This app uses **tidy data principles** to reshape, clean, and analyze data from the 2008 Olympic Games. The app reveals medal patterns by:
- Gender
- Sport
- Medal type (gold, silver, bronze)

It also includes interactive visualizations that show top sports, distribution by gender, and medal type counts.

This app demonstrates how **data wrangling and visualization tools** can be used to turn raw information into compelling insights.

---

## 🛠️ App Features

- 📥 **Data Loading:** Load raw CSV medalist data
- 🧹 **Data Cleaning:** 
  - Remove NaNs
  - Separate sport and gender from merged columns
  - Format text to title case
- 🔁 **Pivot Tables:**
  - Medals by sport and gender
  - Medal types by sport
- 📊 **Visualizations:**
  - Top 10 sports by total medals
  - Gender comparisons across sports
  - Medal type counts by sport and across all events
- 🧠 **Insights:**
  - Bronze medals were more common
  - Sports with more medals show more gender balance

**Example Insight**

A bar plot shows that in sports with many medals, male and female athletes received awards at a more even rate — indicating greater representation.

---

## ⚙️ Setup & Installation

Install the required libraries:
- pandas
- matplotlib
- seaborn
- streamlit

Use the console to install:
```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install streamlit
```

### To run the app:
```bash
streamlit run /Users/brynnwilary/Desktop/WILARY-PYTHON-PORTFOLIO/OlympicMedalistApp/main.py
```

(Or replace the file path with wherever your app is stored.)

---

## References:
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf)
- [Matplotlib Docs](https://matplotlib.org/stable/users/index.html)
- [Seaborn Docs](https://seaborn.pydata.org/)
- [Streamlit Docs](https://docs.streamlit.io/)

## Exploratory Data Analysis & Visualization:

**Top 10 Sports** by medal count
![alt text](image-1.png)

**Medal Gender Distribution** across all sports
![alt text](image-2.png)

**Medal Type Distribution**
![alt text](image.png)

## Pivot Table:
Two **pivot tables** were created to provide a clearer look at the data and to be used with the visuals. Both were indexed by sport, but one looked at the gender breakdown of medals earned and the other looked at the breakdown of the type of medal received.

## Instructions:
1. Clone the repository and install dependencies (`pip install pandas matplotlib seaborn`)
2. Run the Jupyter Notebook step by step
3. Review visualizations and pivot table insights
