import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import numpy as np
import math

# Sample 1 DataFrame of anime genre × age group
data = {
    'Anime_Genre': ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance'],
    'Teen': [50, 30, 20, 40, 60, 10, 25],
    'Young_Adult': [40, 50, 30, 20, 70, 15, 35],
    'Adult': [30, 20, 25, 30, 40, 20, 15]
}
df = pd.DataFrame(data)
# Sample 2 DataFrame of game type × device used
data2 = {
    'Game_Type': ['RPG', 'Shooter', 'Puzzle', 'Sports'],
    'Mobile': [40, 15, 20, 25],
    'PC': [35, 30, 15, 20],
    'Console': [20, 25, 35, 30]
}
df2 = pd.DataFrame(data2)

# Contingency table for anime genre × age group
Table = df.pivot_table(index='Anime_Genre', values=['Teen', 'Young_Adult', 'Adult'], aggfunc='sum')
# Contingency table for game type × device used
Table2 = df2.pivot_table(index='Game_Type', values=['Mobile', 'PC', 'Console'], aggfunc='sum')

print("\n->Contingency Table for Anime Genre × Age Group:\n", Table)
print("\n->Contingency Table for Game Type × Device Used:\n", Table2)
# Chi-Square Test for Anime Genre × Age Group
chi2, p, dof, expected = chi2_contingency(Table)
chi2_2, p2, dof2, expected2 = chi2_contingency(Table2)
print("\n->Chi-Square Test for Anime Genre × Age Group:\n")
print(f"Chi-Square Statistic: {chi2},\n p-value: {p},\n Degrees of Freedom: {dof}")
print("\n->Chi-Square Test for Game Type × Device Used:\n")
print(f"Chi-Square Statistic: {chi2_2},\n p-value: {p2},\n Degrees of Freedom: {dof2}")

# Cramer_V (Effect Size) for Anime Genre × Age Group
n = Table.values.sum()
n2 = Table2.values.sum()
Cramer_V = math.sqrt(chi2 / (n * (min(Table.shape) - 1)))
Cramer_V2 = math.sqrt(chi2_2 / (n2 * (min(Table2.shape) - 1)))
print("\n->Cramer's V for Anime Genre × Age Group:\n", Cramer_V)
print("->Cramer's V for Game Type × Device Used:\n", Cramer_V2)

# Visualization of the contingency tables
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.heatmap(Table, annot=True, cmap='coolwarm', fmt='g')
plt.title('Anime Genre × Age Group Contingency Table')
plt.subplot(1, 2, 2)
sns.heatmap(Table2, annot=True, cmap='coolwarm', fmt='g')
plt.title('Game Type × Device Used Contingency Table')
plt.show()