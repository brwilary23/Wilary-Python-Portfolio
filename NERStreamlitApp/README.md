### Named Entity Recognition (NER) App Project
_A customizable Named Entity Recognition (NER) app using spaCy and Streamlit for interactive text analysis_
This project is a custom Named Entity Recognition (NER) application using Python, spaCy, and Streamlit. This app will allow users to upload their own text data, define custom entity labels and rules using spaCy’s EntityRuler, and view highlighted entities in the output.

## 🚀 Project Overview
Named Entity Recognition is a type of Natural Language Processing (NLP) that involves identifying and categorizing key information (entities) in text. This includes the names of people, places, and organizations. Some labels are built into the system, but others can be added based on what a user wants for a given text. 

This app demonstrates **spaCy’s rule-based EntityRuler**, allowing users to:
- Choose their own labels (e.g., "classes", “names”)
- Pick patterns directly from their inputted text
- Instantly display results using spaCy's `displacy` rendering tool

## 🛠️ App Features
- Write your own text to be entered into the app
- Create your own entity labels
- Tag labels directly from your input
- Create multiple label and pattern combinations
- See your information visualized using displacy
- Add as many labels and patterns as you want

**Example Input Sentence**

From the text input:
`"Brynn is in coding with Ceci and Jack, finance with Reagan, and theology with Alice and Carina."`

You can create...
- A `"names"` label with `"Brynn", "Ceci", "Jack", "Reagan", "Alice", "Carina"`
- A `"classes"` label with `"coding", "finance", "theology"`

## ⚙️ Setup & Installation
Install the required libraries
- spacy
- streamlit
- pandas
- re

You can do this through installations in the console: 
pip install spacy
pip install streamlit 
pip install pandas 
python -m spacy download en_core_web_sm

#### To run the app you must use the following format to open streamlit:
streamlit run /Users/brynnwilary/Desktop/WILARY-PYTHON-PORTFOLIO/NERStreamlitApp/main.py

AKA streamlit run/The location of your file on your computer

## References
- [spaCy Documentation](https://spacy.io/usage)
- [EntityRuler Guide](https://spacy.io/usage/rule-based-matching#entityruler)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Visual Example
