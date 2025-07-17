import numpy as np
import matplotlib.pyplot as plt

# Population Dps
Population_dps = np.random.exponential(scale=2000, size=100000)
True_Mean = np.mean(Population_dps)

# Take a random Sample
sample = np.random.choice(Population_dps, size=100)
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Standard Error 
SE = sample_std / np.sqrt(len(sample))

# 95% Confidence Interval 
C1_Positive = sample_mean + 1.96 * SE
C1_Negative = sample_mean - 1.96 * SE
print(f"Sample Mean {sample_mean}")
print(f"Confidence Interval {C1_Negative} - {C1_Positive}")
print(f"The Original Population Mean {True_Mean}")

# - If the population mean lies inside the CI → your sample was good
# - If outside → sample was unlucky or biased


# now ploting 50 different samples 

ci_bounds = []
for _ in range(50):
    sample = np.random.choice(Population_dps, size=100)
    m = np.mean(sample)
    se = np.std(sample)/np.sqrt(len(sample))
    CI = (m - 1.96*(se), m + 1.96*(se))
    ci_bounds.append(CI)

# Ploting CI 
plt.figure(figsize=(10, 6))
count_contain = 0
for i, (Low, High) in enumerate(ci_bounds):
    Check = (Low <= True_Mean <= High)
    if Check:
        count_contain +=1
    color = "green" if Check else "red"
    plt.plot([Low, High], [i, i], color = color,linewidth=2)
print(f"{count_contain}/50 intervals captured the true mean")
plt.axvline(np.mean(Population_dps),color="blue", linestyle="--", label="True Mean")
plt.title("50 Confidence Intervals (Green = Captures True Mean)")
plt.xlabel("DPS")
plt.ylabel("Sample #")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()