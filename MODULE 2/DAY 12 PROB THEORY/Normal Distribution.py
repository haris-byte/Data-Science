import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Normal distributed data
# relays on count how likely a value can occur 
# it tell the high probability according to data 

data = np.random.normal(loc=50, scale=10, size=1000)
print(data)
sns.histplot(data, kde=True)
plt.title("Normal Distribution (mean=50, std=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 👉 If you measure heights of people, IQ scores, errors in measurement, test scores in a big population:
# ✅ Most values cluster around the average (mean).
# ✅ Few values are much lower or higher.

# Mean (μ) → center.
# Standard deviation (σ) → width (spread).

# A Gaussian (Normal) distribution means:
# most data is around the average, fewer data points are far away, forming a bell curve.