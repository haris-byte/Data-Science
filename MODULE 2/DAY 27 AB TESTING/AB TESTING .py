import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Observed Value 
# rows Click no_click
# col group_a group_b
Observation = np.array([[60, 90],
                        [340, 290]])

chi2, p, dof, expectation = chi2_contingency(Observation)

print("Chi-Square value:", round(chi2, 2))
print("P-value:", round(p,4))
aplha = 0.05

if p < aplha:
    print("Statistically Significant: New design Improves Clicks")
else:
    print("No Significant Difference")

# vISUALS 
labels = ['Old Design', 'New Design']
clicks = [60, 90]
noclicks = [340, 290]

x= np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, clicks, width, label='Clicks', color='green')
ax.bar(x + width/2, noclicks, width, label='No Clicks', color='red')

ax.set_ylabel('Number of Users')
ax.set_title('A/B Test: Clicks on Old vs New Design')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()