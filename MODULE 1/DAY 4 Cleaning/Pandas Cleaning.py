import pandas as p
import numpy as n

a = p.Series([1,2,3], dtype=n.int64).reindex([0,1,2,3,4,5,6,7,8,9])
print (a)

# Exercise Practice

data = {
    "Name": ["Alice", "Bob", "Charlie", None, "Eve", "Alice"],
    "Age": [25, 30, n.nan, 22, 28, 25],
    "Score": [85, n.nan, 67, 90, None, 85],
    "City": ["Lahore", "Karachi", "Lahore", "Lahore", n.nan, "Lahore"]
}
df = p.DataFrame(data)

# Task 1 Missing Data
# count nulls
print(df.isnull().sum())
# Fill Age -> Median   Score -> Mean   City -> Unkonwon
df.fillna({"Age" : df["Age"].median()},inplace=True)
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["City"] = df["City"].fillna("Unknown")
df.dropna(subset=["Name"],inplace=True)

# Task 2 Duplicates
print(df.duplicated())
df = df.drop_duplicates()
# OR 
df.drop_duplicates(inplace=True)

# Task 3 Replacing / Renaming
df.replace({"Lahore":"LHR","Karachi":"Khi"},inplace=True)
df = df.rename(columns={"Score":"Exam Score"})

# Task 4 Indexing 
df = df.set_index("Name")
df = df.reset_index()
print(df)

# Project

# Drop any row where Title or Rating is missing
# Fill missing Votes with the average
# Add a new column "Blockbuster":
# If Votes >= 1,000,000 and Rating >= 8, then "Yes", else "No"
# Print summary stats using .describe()

data = {
    "Title": ["Inception", "Tenet", "Interstellar", "Dunkirk", None],
    "Year": [2010, 2020, 2014, 2017, 2019],
    "Rating": [8.8, 7.5, None, 7.9, 8.0],
    "Genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "War", "Sci-Fi"],
    "Votes": [2000000, 500000, 1500000, None, 800000]
}
movies = p.DataFrame(data)

movies = movies.dropna(subset=["Title","Rating"])

movies["Votes"] = movies["Votes"].fillna(movies["Votes"].mean())

movies["BlockBuster"] = n.where((movies["Votes"]>=1000000) & (movies["Rating"]>= 8),"Yes","No")
movies["BlockBuster"] = ((movies["Votes"]>=1000000)&(movies["Rating"]>=8)).map({True:"Yes",False:"No"})

print(movies)
print(movies.describe())