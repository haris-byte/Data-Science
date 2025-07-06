import numpy as np

Data = np.random.normal(loc = 100, scale=20, size=200)
mean = np.mean(Data)
std = np.std(Data)

x = 70
z = (x - mean) / std
print(f"Z-Score for Value: {x} is {z:.2f}")

# Remember !!
#  - If z=0, value = mean.
#  - If z=2, value is 2 std devs above mean (in ~95% band).
#  - how many std devs from mean 
#  - for anomaly detection & feature scaling