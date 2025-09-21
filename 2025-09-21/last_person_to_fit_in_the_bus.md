# 🧲 Problem: Last Person to Fit in the Bus

- **Platform**: [LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-21
- **Tags**: MySQL, Database, Select, Joins
- **Difficulty**: Medium

---


## 📌 Problem Statement  
Table: **Queue**

| Column Name | Type    |
|-------------|---------|
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |

- `turn` determines the order in which people board the bus (`turn = 1` boards first).  
- The bus has a **weight limit of 1000 kg**.  
- Only one person boards at a time.  
- Find the `person_name` of the **last person who can fit on the bus** without exceeding the limit.  

---

## 📝 Example  

**Input:**

| person_id | person_name | weight | turn |
|-----------|-------------|--------|------|
| 5         | Alice       | 250    | 1    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 2         | Marie       | 200    | 4    |
| 4         | Bob         | 175    | 5    |
| 1         | Winston     | 500    | 6    |

**Output:**

| person_name |
|-------------|
| John Cena   |

**Explanation:**  

| Turn | Name      | Weight | Cumulative Weight |
|------|-----------|--------|------------------|
| 1    | Alice     | 250    | 250              |
| 2    | Alex      | 350    | 600              |
| 3    | John Cena | 400    | 1000             | ← last person to board  
| 4    | Marie     | 200    | 1200             | cannot board  

---

## 🚀 Approach
1. Calculate the **cumulative sum of weights** in the order of `turn`.  
2. Identify rows where cumulative weight ≤ 1000.  
3. Select the **last person** in this filtered list.  
4. Use a **window function** (`SUM() OVER`) to compute the cumulative weight.  

---

## 💻 SQL Query

```sql
WITH cumsum AS (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM cumsum
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
```
---

## 🔎 Query Explanation

- SUM(weight) OVER (ORDER BY turn) → calculates cumulative weight as people board.
- WHERE total_weight <= 1000 → filters only those who can board.
- ORDER BY total_weight DESC LIMIT 1 → picks the last person to fit.
