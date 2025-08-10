# DAY 30: Correlation Analysis (Pearson & Spearman)

## Concepts 
Correlation measures the strength and direction of the relationship between two numeric variables.

- **Range:** `-1` to `+1`
  - `+1`: Perfect positive correlation (both increase together)
  - `-1`: Perfect negative correlation (one increases, other decreases)
  - `0`: No relationship

---

## Types of Correlation
| Method      | Description                                   | When to Use                                    |
|-------------|-----------------------------------------------|------------------------------------------------|
| **Pearson** | Measures linear correlation between variables | Data is normally distributed and linear        |
| **Spearman**| Measures monotonic correlation (rank-based)   | Data not normal, contains outliers, or ranked  |

---

## Hypothesis
- **H₀ (Null):** No correlation between the variables.
- **H₁ (Alternative):** Significant correlation exists.

## Results
- Pearson (Attack vs Crit_Damage): 0.97 → Very strong positive correlation (p < 0.05)
- Spearman (Attack vs Substat): 0.97 → Very strong monotonic relationship (p < 0.05)
- Heatmap shows all variables are strongly positively correlated.