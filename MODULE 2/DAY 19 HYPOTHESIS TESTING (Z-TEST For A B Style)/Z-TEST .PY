import numpy as np
from scipy.stats import norm

# Assumed Population Mean 
Population_Dps_Mean = 2000

# Sample from new weapon DPS Sata (Simulated) 
sample = np.random.normal(loc=2100, scale=300, size=50)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Standard Error 
SE = sample_std / np.sqrt(len(sample))

# Z-Score 
Z = (sample_mean - Population_Dps_Mean / SE)

# One-Tailed p-value 
p_value = 1 - norm.cdf(Z)

print(f"Sample Mean: {sample_mean}")
print(f"Z_scre: {Z}")
print(f"P-Value: {p_value}")

# Conclusion of all Calculation 
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The new weapon increases DPS")
else:
    print("Fail to reject the null: No evidence the weapon increases DPS")
