# 🧲 Problem: Biggest Single Number

- **Platform**: [LeetCode](https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/biggest-single-number/submissions/1776039620/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/biggest-single-number/submissions/1776039620/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-19
- **Tags**: MySQL, Database, Sorting, Grouping
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **MyNumbers**

| Column Name | Type |
|-------------|------|
| num         | int  |

- Each row contains a single number.  
- There is **no primary key**, and the table may contain duplicates.  

Write a SQL query to **find the largest number that only appears once** in the table.  
If no such number exists, return **null**.  

---

## 📝 Example

**Input:**

MyNumbers table:
| num |
|-----|
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |

**Output:**

| num |
|-----|
| 5   |

Explanation:  
- Numbers `8` and `3` appear more than once → not valid.  
- Numbers `1`, `4`, and `5` appear only once.  
- The largest among them is `5`.

---

## 🚀 Approach
1. **Count occurrences of each number**  
   - Use `GROUP BY num` with `HAVING COUNT(num) = 1` to filter numbers that appear only once.  

2. **Find the maximum among them**  
   - Use `MAX(num)` to get the largest number from the unique ones.  

---

## 💻 SQL Query

```sql
SELECT 
    MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);
```

---

## 🔎 Query Explanation

- The subquery:finds all numbers that appear only once.
```sql
SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1
```
- The outer query:selects the largest among those unique numbers.
```sql
SELECT MAX(num)
```
- If no number appears once, MAX() returns null, which satisfies the problem condition.

