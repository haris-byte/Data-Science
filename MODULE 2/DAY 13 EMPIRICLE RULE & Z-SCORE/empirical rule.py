import numpy as n
import seaborn as see
import matplotlib.pyplot as mt

# DATA GENERATION 
Data = n.random.normal(loc = 50, scale=10, size=200)
mean = n.mean(Data)
std = n.std(Data)

print(f"Mean : {mean:.2f} \nstd : {n.std(Data)}")

# Ploting DATA
see.histplot(Data, kde=True)
mt.axvline(mean, color='black', linestyle="dashed", linewidth=1.5,label='Mean')

# Ploting 1σ, 2σ, 3σ lines
for i in range(1,4):
    mt.axvline(mean + i*std,color='red',linestyle='dashed',linewidth=2)
    mt.axvline(mean - i*std,color='red',linestyle='dashed',linewidth=2)
mt.legend()
mt.title("Normal distribution using Empirical Rule (68-95-99.7%)")

# Actually according to my point of view Emperical rule:
#  - the standard deviation of data multiplied with 
#  - 1σ will contain 68% of whole data
#  - 2σ will contain 95% of whole data
#  - 3σ will contain 99.7% of whole data
#  - For Auto Scaling and Checking Outliers in data
#  - in program we showed each line by loop using axvline func (axis-vertical-line)