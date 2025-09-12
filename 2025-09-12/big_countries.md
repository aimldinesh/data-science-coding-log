# 🧲 Problem: Big Countries

- **Platform**: [LeetCode](https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/big-countries/submissions/1767877855/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/big-countries/submissions/1767877855/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-12
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: `World`  

| Column Name | Type    |
|-------------|---------|
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |

- `name` is the primary key for this table.  
- Each row contains information about a country.  

**Task:**  
A country is considered **big** if:  
- It has an area of at least **3,000,000 km²**, or  
- It has a population of at least **25,000,000**.  

Write an SQL query to output the `name`, `population`, and `area` of the big countries.  


---

## 🚀 Approach
 Apply a filter using `WHERE` with an `OR` condition:  
  - `area >= 3000000`  
  - `population >= 25000000`  
- Select only the required columns: `name`, `population`, `area`.  

---

## 💻 Query

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
```

---

## 🔍 Explanation
- WHERE area >= 3000000 → selects all large-area countries.
- OR population >= 25000000 → includes countries with large populations.
- Final SELECT outputs only the requested fields.

✅ Simple filter query using multiple conditions with OR.
