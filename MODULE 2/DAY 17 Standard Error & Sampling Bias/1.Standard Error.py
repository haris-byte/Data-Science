import numpy as np
import matplotlib.pyplot as plt

#  Concept 1: Standard Error (SE)
#   - How far do sample means usually fall from the population mean?
#   - It’s like standard deviation of the sample means
#   - Smaller SE = more trust in your sample average

# Formula
#  - Standard Error (SE) = std(sample) / sqrt(n)

# Wuwa DPS Data Set 
population_dps = np.random.exponential(scale=2000, size=100000)

# Sample Size for Sampling
sample_size = [10, 50 , 200, 600, 5000, 10000, 20000]
standard_err = []

# Loop for Sampling Each individual sample size
for size in sample_size:
    sample_mean = []
    for _ in range(400):
        sample =  np.random.choice(population_dps, size=size)
        sample_mean.append(np.mean(sample))

    se = np.std(sample_mean)
    standard_err.append(se)
    print(f"Sample Size: {size}, Standard Error {se:2f}")

plt.figure(figsize=(8,5))
plt.plot(sample_size, standard_err, marker='H', color='red')
plt.title("Standard Error Vs Sampe Size")
plt.xlabel("Sample Size")
plt.ylabel("Standard Error")
plt.grid(True)
plt.legend()
plt.show()
