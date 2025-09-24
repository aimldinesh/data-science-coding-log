# 🧲 Problem: Investments in 2016

- **Platform**: [LeetCode](https://leetcode.com/problems/investments-in-2016/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/investments-in-2016/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/investments-in-2016/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, Subquries
- **Difficulty**: Medium

---

## 📌 Problem Statement
We have one table:

### Insurance
| Column Name | Type  |
|-------------|-------|
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |

- `pid` is the primary key.  
- Each row represents a policyholder with total investment values (`tiv_2015`, `tiv_2016`) and their city coordinates (`lat`, `lon`).  

**Task:**  
Calculate the sum of `tiv_2016` for policyholders who meet both conditions:
1. Their `tiv_2015` value is **shared with at least one other policyholder**.  
2. Their `(lat, lon)` combination is **unique** in the table.  

Round the sum to **two decimal places**.

---

## 🚀 Approach
1. **Find duplicate `tiv_2015` values**  
   - Group by `tiv_2015` and keep only those with `COUNT(*) > 1`.  

2. **Find unique locations**  
   - Group by `(lat, lon)` and keep only those with `COUNT(*) = 1`.  

3. **Filter Insurance table**  
   - Keep records that satisfy both the duplicate `tiv_2015` and unique location conditions.  

4. **Sum `tiv_2016`**  
   - Round the result to 2 decimal places.  

---

## 💻 SQL Query
```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
```
---

## Query Explanation

1.Duplicate tiv_2015 check:Returns only tiv_2015 values shared by multiple policyholders.
```sql
SELECT tiv_2015
FROM Insurance
GROUP BY tiv_2015
HAVING COUNT(*) > 1
```

2.Unique (lat, lon) check: Returns only unique city coordinates.
```sql
SELECT lat, lon
FROM Insurance
GROUP BY lat, lon
HAVING COUNT(*) = 1
```
3.Final filter and sum:
  - Keep only rows satisfying both conditions.
  - SUM(tiv_2016) aggregates total investment in 2016.
  - ROUND(..., 2) ensures 2 decimal places in the result.
