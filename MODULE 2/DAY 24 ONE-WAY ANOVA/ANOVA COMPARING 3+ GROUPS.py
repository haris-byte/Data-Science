import numpy as np
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
np.random.seed(42)
# simulated Dps For each individual weapon Three Groups 
crimson_dps = np.random.normal(loc=2100, scale=250, size=25)
emerald_dps = np.random.normal(loc=2000, scale=250, size=25)
void_dps = np.random.normal(loc=1950, scale=250, size=25)
# Trying ANOVA Analysis of Varianca 
# by using f_oneway 
f_state, p_value = f_oneway(crimson_dps,void_dps,emerald_dps)
# Print F & P
print(f"F-statistic: {f_state:.2f}")
print(f"p-value: {p_value:.4f}")
if p_value < 0.05:
    print("Rejected H0: At least one weapon is significantly Different DPS from the others")
else:
    print("Accept H1: There is no evidence there is any difference among the items")
plt.boxplot([crimson_dps,emerald_dps,void_dps],label=["Crimson","Emerald","Void"])
plt.title("DPS Comparison of 3 Weapons")
plt.ylabel("DPS")
plt.grid(True)
plt.show()