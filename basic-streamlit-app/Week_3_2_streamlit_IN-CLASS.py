# Import the Streamlit library
import streamlit as st

# Display a simple text message
st.write("Hello")
st.markdown("# This is my first streamlit app!")

# Display a large title on the app

# ------------------------

# INTERACTIVE BUTTON
# ------------------------
if st.button("Click me!"):
    st.write("You clicked the button! Good job!")
else:
    st.write("I dare you to click this button...")

# Create a button that users can click.
# If the button is clicked, the message changes.

# ------------------------
# COLOR PICKER WIDGET
# ------------------------

# Creates an interactive color picker where users can choose a color.
# The selected color is stored in the variable 'color'.
color = st.color_picker("Pick a color", "#00f900")
# Display the chosen color value
st.write(f"You picked: {color}")
# ------------------------
# ADDING DATA TO STREAMLIT
# ------------------------

# Import pandas for handling tabular data
st.subheader("Now, let's look at some data!")
# Display a section title
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie', 'David'], # Column of names
'Age': [25, 30, 35, 40], # Column of ages
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'] # Column of cities
})
# Create a simple Pandas DataFrame with sample data
st.write("Here's a simple table:")

# Display a descriptive message

# Display the dataframe in an interactive table.
# Users can scroll and sort the data within the table.
st.dataframe(df)
# ------------------------
# Create a dropdown (selectbox) for filtering the DataFrame by city.
# The user selects a city from the unique values in the "City" column.
city = st.selectbox("Select a city", df["City"].unique())
# Create a filtered DataFrame that only includes rows matching the selected city.
filtered_df = df[df["City"] == city]
# Display the filtered results with an appropriate heading.
st.write(f"People in {city}:")
st.dataframe(filtered_df) # Show the filtered table
# ------------------------
# NEXT STEPS & CHALLENGE
# ------------------------
# Play around with more Streamlit widgets or elements by checking the
documentation:
# https://docs.streamlit.io/develop/api-reference
# Use the cheat sheet for quick reference:
# https://cheat-sheet.streamlit.app/
### Challenge:
# Modify the dataframe (add new columns or different data).1️⃣
# Add an input box for users to type names and filter results.2️⃣
# Make a simple chart using st.bar_chart().3️⃣
