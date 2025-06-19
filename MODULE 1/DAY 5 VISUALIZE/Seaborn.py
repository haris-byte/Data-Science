import numpy as n
import pandas as p
import matplotlib.pyplot as pt
import seaborn as s

sdf = s.load_dataset("tips")

# Seaborn Example 

# Histtogram
print(sdf.to_string())
s.histplot(sdf["day"])
pt.title("DAY Histo")
pt.show()
s.histplot(data=sdf, x="total_bill", bins=30, kde=True, color="orange")
pt.show()

# boxplot
s.boxplot(x = "tip", y = "sex", data=sdf)
pt.title("Box")
pt.show()

Scores = [40, 45, 50, 55, 60, 65, 70, 75, 80, 100]
s.boxplot(data=Scores)
pt.title("Boxplot of Test Scores")
pt.show()

# countplot
s.countplot(data=sdf , x = "sex")
pt.show()
print(sdf.head())

# scatter plot 
s.scatterplot(x=sdf["tip"],y=sdf['total_bill'],data=sdf, hue="sex")
pt.show()
s.stripplot(x="sex", y="tip", data=sdf, hue="day", jitter=True)
pt.show()


# Heat Map
# This will show correlation between all numeric columns
s.heatmap(sdf.corr(numeric_only=True), annot=True, cmap="YlGnBu")
pt.title("Correlation Heatmap")
pt.show()
print(sdf.corr(numeric_only=True))

# PROJECT
# Distribution of total_bill
# Average tip by day
# Relationship between total_bill and tip (scatter)
# Heatmap of correlation matrix

# Distribution of total_bill
s.histplot(sdf["total_bill"])
pt.show()

# Average tip by day
s.barplot(x="day",y="tip", data=sdf)
pt.show()

# bill vs tip scat 
s.scatterplot(x="total_bill", y="tip", data=sdf)
pt.show()

s.heatmap(sdf.corr(numeric_only=True), annot=True)
s.set_theme(style="darkgrid")
pt.show()