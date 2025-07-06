import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Sample Distribution
data = np.random.normal(0, 1, 100)
Skew_data = np.random.exponential(scale=2, size=100)

# Description stats
print("Normal Skew:", skew(data))
print("Normal Kurtosis:", kurtosis(data))
# pd.skew() & pd.kurt() can be used
print("\nSkewed Skew:", skew(Skew_data))
print("Skewed Kurtosis:", kurtosis(Skew_data))

# Plot 
# 1 GRAPH
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1)
plt.hist(data, bins=13, color='skyblue')
plt.title("Normal Distribution")

# 2 GRAPH
plt.subplot(1, 2, 2)
plt.hist(Skew_data, bins=30, color='salmon')
plt.title("Right-Skewed Distribution")
plt.tight_layout()
plt.show()

# Kurtosis (Tailedness / Peakedness)
#  - It tells you how heavy or light the tails are compared to a normal distribution.
#  - Kurtosis = 0 (in scipy.stats.kurtosis()) → Same as normal distribution
#  - Positive Kurtosis (> 0) → Heavy tails, more outliers, sharper peak.
#  - Negative Kurtosis (< 0) → Light tails, fewer outliers, flatter peak.
#  - How extreme or outlier-prone is my data?