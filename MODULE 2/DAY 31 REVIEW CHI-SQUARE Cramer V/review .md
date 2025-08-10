# Day 31 – Chi-Square Test for Independence (Two Case Studies)

## Concepts
- Performed **Chi-Square Test for Independence** on two datasets:
  1. **Anime Genre × Age Group**
  2. **Game Type × Device Used**
- Calculated **Cramér’s V** as an effect size measure.
- Visualized contingency tables with **heatmaps** for easy interpretation.

**Hypotheses:**
- **H₀ (Null Hypothesis):** Variables are independent (no relationship).
- **H₁ (Alternative Hypothesis):** Variables are dependent (relationship exists).

---

## Case 1 – Anime Genre × Age Group

| Anime Genre | Teen | Young Adult | Adult |
|-------------|------|-------------|-------|
| Action      | 50   | 40          | 30    |
| Adventure   | 30   | 50          | 20    |
| Comedy      | 20   | 30          | 25    |
| Drama       | 40   | 20          | 30    |
| Fantasy     | 60   | 70          | 40    |
| Horror      | 10   | 15          | 20    |
| Romance     | 25   | 35          | 15    |

---

## Case 2 – Game Type × Device Used

| Game Type | Mobile | PC | Console |
|-----------|--------|----|---------|
| RPG       | 40     | 35 | 20      |
| Shooter   | 15     | 30 | 25      |
| Puzzle    | 20     | 15 | 35      |
| Sports    | 25     | 20 | 30      |

---

## Results

| Test                             | Chi² Statistic | p-value | DOF | Cramér's V |
|----------------------------------|---------------:|--------:|----:|-----------:|
| Anime Genre × Age Group          |  32.39         | 0.0012  | 12  | 0.154      |
| Game Type × Device Used          |  22.21         | 0.0011  | 6   | 0.189      |

---

## Interpretation
- Both tests **reject H₀**, indicating significant associations exist.
- **Cramér’s V** quantifies the strength of the association (0 = no relationship, 1 = perfect relationship).
- Heatmaps clearly display where counts are higher or lower compared to expectations.

---

## Visualizations
Generated heatmaps for each contingency table:

1. **Anime Genre × Age Group**
2. **Game Type × Device Used**

```python
sns.heatmap(Table, annot=True, cmap='coolwarm', fmt='g')
sns.heatmap(Table2, annot=True, cmap='coolwarm', fmt='g')
