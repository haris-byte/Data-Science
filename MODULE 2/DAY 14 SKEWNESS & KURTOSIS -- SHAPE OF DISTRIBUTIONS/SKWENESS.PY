import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Sample Distribution
data = np.random.normal(0, 1, 100)
Skew_data = np.random.exponential(scale=2, size=100)

# Description stats
print("Normal Skew:", skew(data))
print("\nSkewed Skew:", skew(Skew_data))

# Plot 
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.hist(data, bins=13, color='skyblue')
plt.title("Normal Distribution")

plt.subplot(1, 2, 2)
plt.hist(Skew_data, bins=30, color='salmon')
plt.title("Right-Skewed Distribution")
plt.tight_layout()
plt.show()

# SKEWNESS OF DATA (Asymmetry of Data)
#  - It tells you if your data is symmetrical or lopsided.
#  - Skewness = 0 → Perfectly symmetric (like normal distribution).
#  - Positive Skew (> 0) → Long right tail (e.g., income, house prices).
#  - Negative Skew (< 0) → Long left tail (e.g., exam scores where most did well).

