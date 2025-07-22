# After performing ANOVA (which tells if there is a difference 
# between group means), Tukey’s HSD tells which specific 
# pairs of groups are significantly different.

import numpy as np
import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

# Simulate DPS data for 3 artifact groups
np.random.seed(42)
crimson_dps = np.random.normal(loc=2100, scale=250, size=30)
emerald_dps = np.random.normal(loc=2000, scale=240, size=30)
azure_dps = np.random.normal(loc=1950, scale=230, size=30)

# Combine into DataFrame 
dps_data = pd.DataFrame({
    'DPS': np.concatenate([crimson_dps, emerald_dps, azure_dps]),
    'Artifact': ['Crimson']*30 + ['Emerald']*30 + ['Azure']*30
})
print(dps_data)

# one way Anova 
f_stat, p_value = f_oneway(crimson_dps,emerald_dps,azure_dps)
print(f"ANOVA F-Statistics: {f_stat:.2f}, p-value: {p_value:.4f}")

# Tukey's HSD 
tukey = pairwise_tukeyhsd(endog=dps_data['DPS'], groups=dps_data['Artifact'],alpha=0.05)

tukey.plot_simultaneous(comparison_name='Crimson')
plt.title("Tukey HSD - Artifact DPS Comparison")
plt.grid(True)
plt.show()