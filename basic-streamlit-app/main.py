#Import Streamlit and Pandas
import streamlit as st
import pandas as pd
# To run, open the console and type in streamlit run basic_streamlit_app/main.py

#Heading used for general info
st.title("Netflix Title Sorter")
st.write("This app allows you to sort through info about Netflix Movies and TV Shows")

#data set up
df = pd.read_csv("data/netflix_titles.csv")
netflix_df = df[["type", "title", "date_added", "release_year", "rating", "duration", "listed_in"]]

#Sort by content type
type = st.selectbox("Select a type of content:", netflix_df["type"].unique())
filtered_df = netflix_df[netflix_df["type"] == type]
st.write(f"Every {type} on Netflix:")
st.dataframe(filtered_df)

#Sort by rating
rating = st.selectbox("Select a rating of content:", netflix_df["rating"].unique())
rating_df = netflix_df[netflix_df["rating"] == rating]
st.write(f"Content that is rated {rating} on Netflix:")
st.dataframe(rating_df)

#select a year
year = st.slider('Select a release year to sort through content:', min_value=netflix_df["release_year"].min(), max_value=netflix_df["release_year"].max())
year_df = netflix_df[netflix_df["release_year"] == year]
st.write(f"Content that was released in {year} on Netflix:")
st.dataframe(year_df)


#show image
st.image('data/Netflix.jpg')

#fun element
st.balloons()