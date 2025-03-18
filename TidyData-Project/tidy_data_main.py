#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#STEP 1: Load Data Set
#This step utilizes the pandas library to take the project's csv, located within the TidyData-Project folder,
#and put it into a data frame

olympic_df = pd.read_csv("TidyData-Project/2008_medalist_data.csv")
#print untidy data
print("Olympic 2008 Medals Untidy")
print(olympic_df)


#STEP 2: Switch Data Set into Melted Form (Long Form) and clean values
# Transitioned the data into a tidy and vertical format, removed blank values to make it easier to work with

df_olympic_melted = olympic_df.melt(id_vars=["medalist_name"], var_name="sport_gender", value_name="medal")
# Drop NaN values where no medals were received
df_olympic_melted = df_olympic_melted.dropna()
print("Olympic 2008 Medals Tidy and NaN Dropped")
print(df_olympic_melted)

#STEP 3: Separate sport and gender
# Information is currently difficult to work with because the two pieces are combined
# By using str.split, we can split apart the sport and gender and look at each individually
# Then, str.split, dashes were taken out of sport names
# str.title() was used to make sure all information was capitalized

df_olympic_melted[['gender', 'sport']] = df_olympic_melted['sport_gender'].str.split(pat="_",expand = True)
# Remove any extra spaces in sport names
df_olympic_melted['gender'] = df_olympic_melted['gender'].str.title()
df_olympic_melted['medal'] = df_olympic_melted['medal'].str.title()
df_olympic_melted['medalist_name'] = df_olympic_melted['medalist_name'].str.title()
df_olympic_melted['sport'] = df_olympic_melted['sport'].str.replace('_', ' ').str.title()
print("Olympic 2008 Medals Sports and Gender")
print(df_olympic_melted)

#STEP 4: Count medals by sport
# I wanted to look further at the number of medals per sport
# The groupby method allows one to group each sport by its medals, and the counts the number of medals
# The ascending=False allowed it to be sort from highest to lowest

df_medal_counts = df_olympic_melted.groupby("sport")['medal'].count().reset_index()
df_medal_counts = df_medal_counts.sort_values(by='medal', ascending=False)
print("Sorted Olympic 2008 Medals by Sport")
print(df_medal_counts)

#STEP 5: Look at sport type and gender correaltion with metals earned
# Created a pivot table that looks at the medal breakdown for each sport by gender to better show the information
#Uses the sport as the index

# Pivot table looking at medals, using sport as an index and gender as a column
medal_gender_pivot = pd.pivot_table(df_olympic_melted, values='medal', index='sport', columns='gender', aggfunc='count',fill_value=0)
print("\nPivot Table by Medal and Gender")
print(medal_gender_pivot)

#STEP 6: Evaluated different relevant pieces of information to see visual data correlations
# Specifically wanted to see the medal distribution by sport, and further by gender, so a stacked bar chart seemed best
#Then wanted to see what sports had the most medals to compare

# Makes a bar chart that shows each sport by gender and medal count
medal_gender_pivot.plot(kind='bar', stacked=True)
plt.ylabel("Number of Medals")
plt.title("Medal Distribution by Gender and Sport")
plt.show()

# Create a bar plot to see the top 10 sports with the most medals
plt.figure()
sns.barplot(x='medal', y='sport', data=df_medal_counts.head(10),palette="Set1",hue='sport')
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.title("Top 10 Sports with the Most Medals in 2008 Olympics")
#plt.show()
