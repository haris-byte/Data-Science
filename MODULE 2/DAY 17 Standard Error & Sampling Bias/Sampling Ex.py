import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Fake Ages of 10000 people
np.random.seed(42)
population = np.random.normal(loc=35, scale=10, size=10000)
# mean = 35, std = 10

print("\nExercise 1\n")
# Exercise 1 Random Sampling
#  - Randomly select 100 val from the population As Sample
#  - Print MEAN and STANDARD DEVIATION of both POPULATION and SAMPLE
sample = np.random.choice(population,size=100, replace=False)
print("Population Mean:", np.mean(population))
print("Population Std:", np.std(population))
print("Sample Mean:", np.mean(sample))
print("Sample Std:", np.std(sample))

print("\nExercise 2\n")
# Exercise 2 Compare Different Sample Size
#  - Take samples of size 10, 50, 100, 500
#  - Compare how close their means are to the true population mean
Sample_Size = [10, 50, 100, 500]

for size in Sample_Size:
    sample = np.random.choice(population,size=size)
    print(f'Sample Size: {size} -> Sample Mean: {np.mean(sample):.2f}')

print("\nExercise 3\n")
# Exercise 3 Sampling Distribution (CLT Preview)
#  - For sample size 30, take 100 samples and store the mean of each
#  - Plot histogram of those means
sample_mean = []
for _ in range(100):
    sample = np.random.choice(population, size=30)
    sample_mean.append(np.mean(sample))
plt.hist(sample_mean, color='red', bins=20)
plt.title("Sampling Distribution of the Mean (n=30)")
plt.show()

print("\nExercise 4\n")
# Exercise 4 Systematic Sampling
#  - Pick Every 50th element from the population sorted or unsorted 
step = 50 
systematic_sample = population[::step]
print("Systematic Sample Sizes:", len(systematic_sample))
print("Systematic Sample Mean:", np.mean(systematic_sample))

print("\nExercise 5\n")
# Exercise 5 Stratified Sampling 
#  - Simulate a population split into 2 groups: Adults (age > 30), Youth (age ≤ 30)
#  - Take 50 random samples from each group
df = pd.DataFrame({'Age': population})
group1 = df[df['Age']>30]
group2 = df[df['Age']<=30]

Strata_sample = pd.concat([
    group1.sample(n=50),
    group2.sample(n=50)
])

print(Strata_sample)
print("Stratafied Sample Mean:", Strata_sample['Age'].mean())