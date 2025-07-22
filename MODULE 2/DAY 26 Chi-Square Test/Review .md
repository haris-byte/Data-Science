# Day 26 – Chi-Square Test: Gacha Banner vs Rarity

## Scenario:
Check if 5 star drop rarity is affected by banner type in gacha pulls (Standard vs Limited).

## Concepts:
- if two catagorical variable are related or independent 
- Chi-Square Test for Independence
- Compared 5★, 4★, 3★ counts between banners
- Used `chi2_contingency()` for observed vs expected frequencies

## Result:
- Chi-Square value and p-value indicate if rarity is dependent
- In our simulation, p < 0.05 → Banner type **affects** rarity!

## Learning:
Chi-Square helps test categorical relationships.  
Useful in marketing, behavior, AB testing, or game design.
