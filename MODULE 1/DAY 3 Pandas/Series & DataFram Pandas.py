import pandas as p
import numpy as n
# Series
DATA = n.arange(4,100,10)
ser = p.Series(DATA)
print(ser)
# DataFrame
data = {
    'Games':['Genshin','Honkai',"Wuwa"],
    'Update':[5.6,3.7,2.4]
}
datF = p.DataFrame(data)
print(datF)
# Using List
Ls = p.Series([1,2,3,4])
Ldf = p.DataFrame([[1,2,3],[9,8,7]], columns=['a','b','c'])
print(Ls,"\n",Ldf) 
Ddf = p.DataFrame({
    "Character":["Cartehia","Charlota","Jinshi"],
    "Level":[00,80,10]
})
print(Ddf)

# Exercise

# 1.Create a Series from a list, numpy array, and dictionary.
# List 
Ls = p.Series([1,2,3,4])
print(Ls)
# numpy array
arr = n.array(['a','a','s','h'])
Narr = p.Series(arr)
print(Narr)
# dict 
DS = p.Series({'a':100,"2nd":200,"3rd":300})
print(DS)

# 2.Access elements by index and by label.
print(Ls[2])
print(Narr[2])
print(DS['2nd'])

# 3.Create a DataFrame from a dictionary with at least 3 columns (e.g. Name, Age, Score).
DataF = p.DataFrame({
    "Name":["Charlota","Jinshi","Cartethia"],
    "Age":[24,19,22],
    "Level":[80,50,20]
})
print(DataF)

# 4.Selecting rows and columns using .loc[] and .iloc[].
print(DataF.loc[1])
print(DataF.loc[[0,2],["Name","Level"]])

print(DataF.iloc[0])
print(DataF.iloc[[1,2],[0,1]])


# 5.Filtering rows based on a condition (e.g. age > 20).

print(DataF[ DataF["Age"] > 20 ])
# 6.Mean, median, and standard deviation of a numeric column.

print(f"    ~Score~    \nMean -> {DataF["Level"].mean()}\nMedian -> {DataF["Level"].median()}\nStandard Deviation -> {DataF['Level'].std()}")

# Project
#  Create a DataFrame for 5 students with columns: Name, Math, Science, English.
# ✅ Calculate:

# Each student’s average score.

# Overall subject averages.
# ✅ Add a new column: Pass/Fail (Pass if average >= 40).
# ✅ Print the DataFrame.
StudentData = {
    "Name" : ["Xiao","Kazuha","Ayaka","Furina","Kokomia"],
    "Math" : [10,30,90,70,80],
    "Science" : [5,70,98,67,60],
    "English" : [60,68,99,76,89]
}
Stu_DF = p.DataFrame(StudentData)
Stu_DF["Average"] = Stu_DF[['Math', 'Science', 'English']].mean(axis=1)
# using iloc
Stu_DF["Average-re"] = Stu_DF.iloc[:, 1:4].mean(axis=1)
Stu_DF["Pass/Fail"] = Stu_DF["Average"].apply(lambda x: "Pass" if x > 40 else "Fail")
Stu_DF["Pass/Fail-re"] = n.where(Stu_DF["Average"] >= 40, "Pass", "Fail")

print("Stats -> ",Stu_DF.describe())
print("Head -> ",Stu_DF.head())