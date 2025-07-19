# 📅 Day 19 - Hypothesis Testing (Z-Test)

Today I learned how to apply **Hypothesis Testing** using Z-tests to check whether a new weapon (e.g., Emerald of Genesis) actually improves damage performance compared to the population average.

🔍 Key Concepts:
- **Null Hypothesis (H₀)**: No change (weapon does not increase DPS).
- **Alternative Hypothesis (H₁)**: Weapon increases DPS.
- **Z-Score**: Measures how far the sample mean is from population mean in standard errors.
- **P-Value**: The probability of observing such a result if H₀ is true.

🧪 I simulated weapon data using NumPy, calculated Z-score and p-value, and drew a real conclusion:
- If p-value < 0.05, I rejected the null → weapon improves DPS.
- If p-value ≥ 0.05, not enough evidence to say the weapon is better.

⚔️ Final Verdict:
After testing, the p-value showed strong evidence to reject the null hypothesis, so I recommended using the new weapon. ✅

This builds my foundation for A/B testing, product decisions, and statistical modeling in real-world data science work.
