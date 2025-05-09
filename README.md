This portfolio will be used to highlight my projects from the Elements of Computing 2 class.

## 🎬 Netflix Title Sorter App - Basic Streamlit App

This project is an interactive Streamlit application that allows users to filter and explore Netflix’s catalog by **type**, **rating**, and **release year**. Using data visualization and user input widgets, this app makes it easy to sort through streaming content and identify shows or movies based on viewer preferences.

---

### 📌 Project Overview

The Netflix Title Sorter provides a clean interface for interacting with a dataset of Netflix titles. Users can select filters to dynamically update results and better understand the platform’s content offerings.

Users can:
- Choose between **Movies** and **TV Shows**
- Filter content by **rating category** (e.g., PG, R, TV-MA)
- Select a **specific release year** using an interactive slider
- View an image banner for a polished user interface
- Celebrate their search results with fun **balloon animations**

> This tool is especially useful for users who want to browse Netflix titles by specific categories without using the Netflix interface.

---

### 🎯 Class Connection

This app was developed for my **Elements of Computing 2** course at the University of Notre Dame. It allowed me to:
- Learn the **basics of Streamlit and Python-based web apps**
- Practice working with real-world datasets and user input handling
- Develop **data filtering techniques** using **Pandas**
- Combine interactive visuals with functionality for a user-first experience

This project serves as a foundational example of data app development, helping me build core programming and design skills.

---

### 🚀 App Features

- 🎥 **Content Type Selector:** Filter between Movies and TV Shows  
- 📊 **Rating Filter:** Sort titles by audience rating category  
- 📅 **Release Year Slider:** Narrow content by year of release  
- 🖼️ **Visuals:** Includes a banner image and celebratory animations  
- 🔄 **Live Data Display:** Updates dynamically based on selections  

---

### 🛠️ Technologies Used

- `Python`
- `Streamlit`
- `Pandas`
- CSV-based data: [`netflix_titles.csv`](https://www.kaggle.com/datasets/shivamb/netflix-shows)  

---

_TLDR Description:_ _This app helps users sort Netflix content by type, rating, and release year using an interactive Streamlit interface._


## 🏅 Tidy Data Analysis - 2008 Olympic Medalists

This project analyzes data from the **2008 Olympic Games** using **tidy data principles** to reshape, clean, and explore medalist trends across sports and gender categories. It applies core concepts in **data wrangling**, **pivoting**, and **visualization** using `pandas`, `matplotlib`, and `seaborn`.

---

### 📌 Project Overview

The dataset initially contains wide-format data with merged gender-sport columns and several `NaN` values. The project goes through multiple steps:
- Tidying the dataset into long form with meaningful column separation
- Cleaning and standardizing entries
- Creating pivot tables to summarize medals by gender and type
- Using grouped aggregations to reveal trends
- Visualizing medal counts by sport, gender, and medal type

Users can follow the entire transformation process from raw CSV to cleaned and visually insightful analysis.

---

### 🎯 Class Connection

This project was created for my **Elements of Computing 2** course at the University of Notre Dame. It allowed me to:
- Work deeply with **pandas** for data transformation and aggregation
- Practice the **Tidy Data** standard by reshaping wide-form tables
- Improve data storytelling through **pivot tables** and **bar plots**
- Learn how to draw meaningful conclusions from grouped and cleaned data

This analysis demonstrates foundational data analysis skills and the ability to present findings clearly and effectively.

---

### 🚀 Project Features

- 📊 **Data Reshaping:** Convert wide-form data to long-form using `melt()`
- 🔍 **NaN Removal:** Clean dataset to keep only meaningful values
- 🧹 **Column Separation:** Split combined sport-gender labels into usable columns
- 🔄 **Standardization:** Capitalize and clean text fields consistently
- 📑 **Pivot Tables:** Summarize medals by sport, gender, and medal type
- 📈 **Visualizations:** 
  - Top 10 sports by medal count
  - Medal distribution by gender
  - Total medal type counts
  - Medal type breakdown by sport

---

### 🛠️ Technologies Used

- `Python`
- `Pandas`
- `Matplotlib`
- `Seaborn`
- Data source: [`2008_medalist_data.csv`](your/dataset/path)

---

_TLDR Description:_ _This project cleans and analyzes 2008 Olympic medal data to evaluate distribution by sport, gender, and medal type through pivot tables and visualizations._


## Named Entity Recognition App - Streamlit
This project is an interactive web-based application that allows users to explore **Named Entity Recognition (NER)** by defining their own entity labels and identifying custom patterns in user-submitted text. Built using the **spaCy** NLP library and the **Streamlit** framework, this app allows me to utilize basic machine learning principles.


### 📌 Project Overview
Named Entity Recognition is a task of **Natural Language Processing (NLP)**, where entities such as names, organizations, dates, and locations are identified in text. This app demonstrates **spaCy’s rule-based `EntityRuler`**, allowing users to create and visualize their own NER patterns and labels.

Users can:
- Input their own sentence or paragraph
- Define multiple entity labels (like "names", "subjects", "events")
- Select specific words that belong to each label
- View real-time visualizations of their tagged text using spaCy's `displacy`

---

### 🎯 Class Connection
This app was developed as part of my **Elements of Computing 2** course at the University of Notre Dame. It showcases my ability to:
- Work with advanced libraries like **spaCy**
- Design **user-driven interfaces** with **Streamlit**
- Combine **data logic, NLP, and interactivity** in one cohesive application
- Explain complex tools in an intuitive, visual way

This project also builds on my interest in **user-centric technology design**, and represents a meaningful step toward developing tools that make machine learning more understandable and hands-on for a broader audience.

---

### 🚀 App Features

- 📝 **Text Input:** Enter any sentence, paragraph, or list
- 🏷️ **Label Creation:** Add multiple custom entity labels and assign patterns
- 📌 **Pattern Matching:** Select specific words from your input for each label
- ✨ **Visual Output:** View entity-tagged text with color-coded highlights


## 📈 Stock Analysis App - Streamlit

This project is an interactive web-based application that allows users to analyze and compare publicly traded companies based on ticker symbols or company names. Built using **Streamlit** and financial data libraries, this app offers a dynamic way to explore key stock metrics across different sectors and exchanges.

---

### 📌 Project Overview

The Stock Analysis App allows users to conduct basic financial research and comparisons in an intuitive interface. By entering a company name or stock ticker, users can access key financial data and evaluate performance from multiple perspectives.

Users can:
- Input a company name or ticker (e.g., `TSLA`, `Apple`)
- View key details like company name, exchange, sector, market cap, and EBITDA
- Select additional analyses from:
  - Peer companies in the same market
  - Sector-level comparisons
  - Exchange-wide insights
  - Company-specific deep dives

> The app organizes data clearly for individual and comparative analysis using dropdowns and clean layout sections.

---

### 🎯 Class Connection

This app was developed as part of my **Elements of Computing 2** course at the University of Notre Dame. It demonstrates my ability to:
- Work with **financial data APIs and data visualization tools**
- Build responsive, user-driven web applications with **Streamlit**
- Structure complex datasets into digestible insights
- Highlight performance trends across markets in an accessible format

The project reflects my growing interest in **financial analytics** and in making data-rich tools more navigable and understandable for users of all backgrounds.

---

### 🚀 App Features

- 🔍 **Search Functionality:** Enter ticker or company name to start analysis  
- 📊 **Key Stats Panel:** View exchange, market cap, sector, EBITDA, and more  
- 🧩 **Dynamic Comparison Tools:**
  - Compare within exchange
  - Filter by sector or market cap tier
  - Deep-dive into company-specific metrics  
- 📈 **Visual Feedback:** Interactive layout with labeled sections and financial highlights

