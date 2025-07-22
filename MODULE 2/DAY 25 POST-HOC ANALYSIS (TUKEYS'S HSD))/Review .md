# Day 25 – Tukey’s HSD: Comparing Artifact DPS

## Scenario:
Tested if there’s a significant DPS difference between 3 artifacts: Crimson, Emerald, Azure.

## Concepts:
- Used ANOVA to detect group difference
- Applied Tukey’s HSD to find which artifacts differ
- Visualized with plot_simultaneous()

## Result:
- ANOVA showed p < 0.05 → difference exists
- Tukey revealed that Crimson > Azure, and other pair results
- Conclusion: Crimson is statistically stronger than Azure; Emerald is close

## Learning:
Tukey’s HSD is essential after ANOVA to dig deeper into group-level differences.
