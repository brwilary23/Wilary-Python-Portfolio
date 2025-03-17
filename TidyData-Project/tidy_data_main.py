#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#STEP 1: Load Data Set
olympic_df = pd.read_csv("TidyData-Project/2008_medalist_data.csv")
#print untidy data
print("Olympic 2008 Medals Untidy")
print(olympic_df)


#STEP 2: Switch Data Set into Melted Form (Long Form) and clean values
df_olympic_melted = olympic_df.melt(id_vars=["medalist_name"], var_name="sport_gender", value_name="medal")
# Drop NaN values where no medals were received
df_olympic_melted = df_olympic_melted.dropna()
print("Olympic 2008 Medals Tidy and NaN Dropped")
print(df_olympic_melted)

#STEP 3: Separate sport and gender
df_olympic_melted[['gender', 'sport']] = df_olympic_melted['sport_gender'].str.split(pat="_",expand = True)
# Remove any extra spaces in sport names
df_olympic_melted['sport'] = df_olympic_melted['sport'].str.replace('_', ' ').str.title()
print("Olympic 2008 Medals Sports and Gender")
print(df_olympic_melted)

#STEP 4: Count medals by sport
df_medal_counts = df_olympic_melted.groupby("sport")['medal'].count().reset_index()
df_medal_counts = df_medal_counts.sort_values(by='medal', ascending=False)
print("Sorted Olympic 2008 Medals by Sport")
print(df_medal_counts)

#STEP 5: Look at sport type and medal correaltion
#Create a pivot table
medal_sport_pivot = pd.pivot_table(df_olympic_melted, values='medal', index='gender', columns='sport', aggfunc='count',fill_value=0)
print("Pivot Table by Medal and Sport")
print(medal_sport_pivot)
# Create a bar plot to see the top 10 sports with the most medals
plt.figure(figsize=(15, 6))
sns.barplot(x='medal', y='sport', data=df_medal_counts.head(10),palette="Set1",hue='sport')
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.title("Top 10 Sports with the Most Medals in 2008 Olympics")
#plt.show()

#STEP 6: Create a pivot table
# Pivot table for sport by gender
medal_gender_pivot = pd.pivot_table(df_olympic_melted, values='medal', index='sport', columns='gender', aggfunc='count',fill_value=0)
print("Pivot Table by Medal and Gender")
print(medal_gender_pivot)
# Makes a bar chart that shows each sport by gender and medal count
medal_gender_pivot.plot(kind='bar', figsize=(12, 10), stacked=True)
plt.ylabel("Number of Medals")
plt.title("Medal Distribution by Gender and Sport")
plt.show()