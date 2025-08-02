import numpy as np
from scipy.stats import chisquare
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Observed Pattern: count of items on 100 pulls 
Observed = np.array([3,22,75])

# Expected Pattern: Claim by the Devs 
expected = np.array([5,15,80])
category = ['5★', '4★', '3★']

# Chi-Square for the Goodness of FIt Test 
chi2, p = chisquare(f_obs=Observed,f_exp=expected)

print(f"Chi-Square Value: {chi2:.2f}")
print(f"P Value: {p:.2f}")

alpha = 0.05
if p < alpha:
    print("Rejected Null Hypothesis Observed do not match with expextion (Change)")
else:
    print("Accept Null Hypothesis Observed match with expextion (No Change)")

DF = pd.DataFrame({
    "Rarity": category*2,
    "Count": np.concatenate([Observed,expected]),
    "Type": ["Observed"]*3 + ["Expected"]*3
})
print(DF)

plt.figure(figsize=(8, 5))
sns.barplot(data=DF, x="Rarity", y="Count",hue="Type",palette=['skyblue','lightcoral'])
plt.title("Chi-Square Goodness of Fit: Gacha Drops")
plt.ylabel("Frequence")
plt.grid(True, axis="y", linestyle='--',alpha=0.5,color="green")
plt.tight_layout()
plt.show()