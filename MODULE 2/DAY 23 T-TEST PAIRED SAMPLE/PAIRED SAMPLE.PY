# Paired T-Testing for Hypothesis Test 
import numpy as np
from scipy.stats import ttest_rel

# Task 
# You want to test whether the “Crimson Star” artifact 
# boosts damage for the same character after equipping it.

# Simulated DPS before and After equiping "Crimson Star" (same character)
np.random.seed(42)
before = np.random.normal(loc=1950, scale=250, size= 30 )
after = before + np.random.normal(loc=120, scale=100, size=30)

# paired T-test
t_score, p_value = ttest_rel(after, before)

# Results
print(f"Mean Before: {np.mean(before):.2f}")
print(f"Mean After: {np.mean(after):.2f}")
print(f"t-score: {t_score:.3f}")
print(f"p-value: {p_value:.5f}")

# Hypothesis test conclusion
alpha = 0.05
if p_value < alpha:
    print("Reject H₀: Crimson Star significantly boosts DPS!")
else:
    print("Fail to reject H₀: No strong evidence of DPS improvement.")