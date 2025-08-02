from scipy.stats import chi2_contingency
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Observed frequencies in a contingency table (cross tab)

# A 2D table (like gender × product choice(Tech Fashion Grocery)) 10 x 10.
observed = pd.DataFrame({
    'Product': ['Tech', 'Fashion', 'Grocery', 'Tech', 'Fashion', 'Grocery',
    'Tech', 'Fashion', 'Grocery', 'Tech'],
    'Gender': ['Male', 'Female'] * 5,
    'Count': [30, 10, 20, 25, 15, 5, 10, 30, 20, 15]
})
# convert into a pivot table cross tab (contgency table) 
table = observed.pivot_table(index='Gender', columns='Product')
# Display the contingency table
print("Contingency Table:")
print(table)
# Perform Chi-Square Test for Independence
chi2, p, dof, expected = chi2_contingency(table)
# Display the results
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2}")
print(f"P-Value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)
# Visualize the contingency table using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(table, annot=True, cmap='Blues')
plt.title('Contingency Table Heatmap')
plt.xlabel('Product')
plt.ylabel('Gender')
plt.show()
# Interpretation of results
if p < 0.05:
    print("Reject the null hypothesis: There is a significant association between gender and product choice.")
else:
    print("Fail to reject the null hypothesis: There is no significant association between gender and product choice.")
