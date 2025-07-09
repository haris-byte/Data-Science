import numpy as np
import matplotlib.pyplot as plt

# Concept 2: Sampling Bias
#  - Is my sample representative of the population?
#  - Only sampling high DPS players
#  - Only including players from Reddit or Twitter
#  - Ignoring low-rank or F2P users

# Full Wuthering Waves DPS data
population_dps = np.random.exponential(scale=2000, size=100000)

# Biased sampling: only high DPS players
biased_sample = population_dps[population_dps > 6000]  # cherry-picked
random_sample = np.random.choice(population_dps, size=1000)
print("Biased Sample Mean:", np.mean(biased_sample))
print("True Population Mean:", np.mean(population_dps))
print("Random Sample Mean:", np.mean(random_sample))

# Plot Standard Error vs Sample Size
plt.figure(figsize=(10,4))

# For Random Sampling
plt.subplot(1,2, 1)
plt.hist(random_sample, bins=30, color='skyblue')
plt.title("Random Sample (Fair)")

# For Biased Sampling
plt.subplot(1, 2, 2)
plt.hist(biased_sample, bins=30, color='salmon')
plt.title("Biased Sample (High DPS Only)")

plt.tight_layout()
plt.show()
