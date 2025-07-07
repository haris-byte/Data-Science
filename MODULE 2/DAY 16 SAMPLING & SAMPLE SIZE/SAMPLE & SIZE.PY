import numpy as np
import matplotlib.pyplot as plt 

# Dps Values of wuthering waves rovers build
population_dps = np.random.exponential(scale=2000, size=100000)

sample_size = [5, 10, 30, 100, 500]
sample_mean = []

for size in sample_size:
    mean = []
    for _ in range(300):
        sample = np.random.choice(population_dps, size=size)
        mean.append(np.mean(sample))
    sample_mean.append(mean)

# ploting the Sample 
plt.figure(figsize=(14,10))
for h, size in enumerate(sample_size):
    plt.subplot(3, 2, h+1)
    plt.hist(sample_mean[h], bins=20, color='violet')
    plt.title(f'Sampl Size = {size}')
    plt.axvline(np.mean(population_dps), color='red', linestyle='dashed', label='True Mean')
    plt.legend()
plt.tight_layout()
plt.show()

