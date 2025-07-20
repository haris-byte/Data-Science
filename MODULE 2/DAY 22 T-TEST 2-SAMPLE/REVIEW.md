# DAY 22
Two-Sample t-Test with unequal variances (Welch’s t-test) is used to compare two sample means when population σ is unknown and both sample sizes might differ.
## KEY Concepts 
- comparison of two independent entity (Artifact) Crimson and Emarald to see if one artifact is significantly improves DPS over the other 
- Used Welch t-Test due to differnet Std Deviation
- Compute:
- - sample mean And Std Deviation
- - Standard Error Combining Two Sample
- - Degree of Freedom (Welch-Satterwaite equation)
- - one tailed p-value using scipy.stats.t.cdf
- Interpret P-value against a = 0.05 threshhold to either accept/reject the Null Hypothesis

## Results Of Data
- Crimson Mean: 2041.67
- Emerald Mean: 1964.86
- t-score: 1.52
- p-value: 0.06
By the Given Result I have concluded that the Emerald is Significantly better then Crimson
(Although I want Crimson to be winner.)