# Day 21 - One Sample t-Test (When Population σ is Unknown)

## Goal
Determine whether a **new artifact "Crimson Star"** improves player DPS in Wuthering Waves, using a **one-sample t-test**, because population standard deviation (σ) is unknown.

---

## Scenario

A new artifact *Crimson Star* claims to increase the average DPS.  
To test this, we:
- Simulated population DPS (from older artifacts)
- Sampled DPS from Crimson Star
- Applied **t-test** to verify the claim

---

## Test Applied: One-Sample t-Test (Right-Tailed)

- Used when **population σ is unknown**
- Small sample size (n = 25)
- One-tailed test to check **if Crimson Star performs better**

---

## Results

| Metric                     | Value       |
|----------------------------|-------------|
| Population Mean (σ unknown)| ~2003.61    |
| Sample Mean (Crimson Star) | ~2129.75    |
| Sample Std Deviation       | ~281.25     |
| Degrees of Freedom (df)    | 24          |
| **t-score**                | **1.956**   |
| **p-value**                | **0.0315**  |

---

## Conclusion

-  **p < 0.05** → **Reject Null Hypothesis**
-  Evidence suggests that the new artifact **does improve DPS**
-  **Crimson Star is recommended** based on statistical testing

---

## Key Concepts Learned

- **One-Sample t-Test** is used when:
  - Population standard deviation is **not known**
  - Sample size is small
- Importance of:
  - **Degrees of Freedom**
  - How sample variance affects test statistics
---
