#IMPORT NECESSARY PROGRAMS
#import pandas
import pandas as pd
#import streamlit
import streamlit as st
#import spacy and displacy from spacy
import spacy
from spacy import displacy
#set up nlp
nlp = spacy.load('en_core_web_sm')
#import re - used to separate sentence wout punctuation
import re

#TO RUN MUST USE: streamlit run /Users/brynnwilary/Desktop/WILARY-PYTHON-PORTFOLIO/NERStreamlitApp/main.py

#BASIC STREAMLIT SETUP
st.title("Named Entity Recognition App")
st.write("This app allows you to explore Named Entity Recognition with your own label and patterns from user-submitted text.")

#text area where text to be analyzed by system can be inputted
text = "This is a sample sentence"
text = st.text_area("Enter in the text you want to be put through the Name Entity Recognition software:")
st.write(text)

#split text into words
st.write("Enter Label and Pattern 1: ")
words = re.findall(r"[\w']+|[.,!?;]", text)
label = st.text_input("Enter the label name for the pattern you are trying to find: ")
pattern_list = st.multiselect("Enter the words from the given string that belong to the above label", options=words)
lp1 = []
for x in pattern_list:
    lp1.append({"label":label, "pattern":x})

# ask if want to do it again
continuous = st.selectbox("Do you want to add another label?", options=["","Yes","No"])

#copies the above pattern to create a bigger list with all of the potential keys and labels in individual lists
counter = 1
list_sublists =[lp1]
if continuous == "Yes":
    while continuous == "Yes":
        counter += 1
        st.write("Enter Label and Pattern " + str(counter) + ":")
        label1 = st.text_input(f"Enter the label name for pattern #{counter} you are trying to find: ", key=f"label{counter}")
        pattern_list1 = st.multiselect(f"Enter the words from the given string that belong to label #{counter}", options=words, key=f"pattern{counter}")
        
        lp = []
        for x1 in pattern_list1:
            lp.append({"label": label1, "pattern": x1})  # ✅ This is the fix

        list_sublists.append(lp)
        continuous = st.selectbox(f"Do you want to add label #{counter+1}?", options=["", "Yes", "No"], key=f"continue{counter}")

#CREATE AN NER
#uses the for loop to add all of the rules
#make sure there isn't an eror in putting in ruler
if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
    try:
        ruler = nlp.get_pipe("entity_ruler")
    except Exception:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
    for sublist in list_sublists:
        ruler.add_patterns(sublist)
else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
    ruler = nlp.add_pipe("entity_ruler")
    for sublist in list_sublists:
        ruler.add_patterns(sublist)
    ner = nlp.add_pipe("ner")

#test entity ruler
doc1 = nlp(text)
show = displacy.render(doc1, style="ent", jupyter=False)
st.markdown(show, unsafe_allow_html=True)



