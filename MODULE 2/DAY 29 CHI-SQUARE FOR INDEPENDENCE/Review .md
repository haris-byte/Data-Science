# Day 29 Chi-Square Test for Independence 
 
## Concepts:
Test 2 Variables are associated or not using contingency Table (matix of categories)
- H0: Null -> 2 Variables are independent (NO RelationShip)
- H1: Alt -> 2 Variables are dependent (RelationShip Exist)

## Task
Testing Weather the Gender of customer is independent of their product choices 
- Gender (Male, Female)
- Product (Tech, Fasion, Grocery)

## Methode Used
We used pivot table from pandas df
- pd.pivot_table : table = observed.pivot_table(values='Count', index='Gender', columns='Product')
- used chi-Square Contigency and found p-Value For hypothesis

## Results
- Contingency Table:
          Count
Product Fashion Grocery  Tech
Gender
Female     20.0     5.0  20.0
Male       15.0    20.0  20.0

-      Chi-Square Test Results:
- Chi-Square Statistic: 8.802308802308803
- P-Value: 0.012263175105213908
- Degrees of Freedom: 2
- Expected Frequencies: 
[[15.75 11.25 18.  ]
 [19.25 13.75 22.  ]]
