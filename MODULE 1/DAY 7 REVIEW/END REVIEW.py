import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
df = pd.DataFrame(data)
plt.figure(figsize=(14,5))

plt.subplot(1,3, 1)
sns.barplot(data=df, x="day",y="tip",hue="day")

plt.subplot(1,3, 2)
sns.scatterplot(data=df,x="sex",y="tip",hue="sex")

plt.subplot(1,3, 3)
sns.heatmap(data=df.corr(numeric_only=True))
print(df.describe())
print(df.corr(numeric_only=True))
plt.show()