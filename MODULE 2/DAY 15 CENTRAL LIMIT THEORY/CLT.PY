# CLT:
# No matter what the original data looks like, the average of many random samples will follow a normal distribution.

import numpy as np
import matplotlib.pyplot as plt

# Non Normal Data
Data = np.random.exponential(scale=2, size=10000)

# sample Means
smpl_Mean = []

for _ in range(1000): # 1000 Samples
    sample = np.random.choice(Data, size=30) 
    # Randomly Select 30 Values for sample
    smpl_Mean.append(np.mean(sample))

# NOW PLOTING ORIGINAL & SAMPLE MEANS
plt.figure(figsize=(12, 5))

plt.subplot(1,2,1)
plt.hist(Data, bins=40, color='orange')
plt.title("Original (Skewed) Data")

plt.subplot(1,2,2)
plt.hist(smpl_Mean, bins=30, color='green')

plt.tight_layout()
plt.show()

# If you take repeated random samples from any population (no matter if it’s skewed, weird, non-normal), and calculate the mean of each sample, then the distribution of those sample means will be: