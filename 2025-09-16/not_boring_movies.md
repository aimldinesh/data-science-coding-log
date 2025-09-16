# 🧲 Problem: Not Boring Movies

- **Platform**: [LeetCode](https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/not-boring-movies/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/not-boring-movies/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-16
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Cinema**

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| movie       | varchar |
| description | varchar |
| rating      | float   |

- `id` is the primary key.  
- Each row contains the movie name, its description, and its rating.  

Write a SQL query to report all movies with **odd `id` values** and a description that is **not "boring"**.  
- Return the result ordered by **rating in descending order**.  

---

## ✅ Approach
1. Use `WHERE` to filter:  
   - `id % 2 = 1` → odd IDs only.  
   - `description != 'boring'` → exclude boring movies.  
2. Use `ORDER BY rating DESC` to sort movies by rating.  

---

## ✅ SQL Query

```sql
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;
```
---

### ✅ Explanation

- id % 2 = 1 → ensures only odd IDs are selected.
- description != 'boring' → excludes boring movies.
- ORDER BY rating DESC → highest-rated movies appear first.
- SELECT * → returns all columns (id, movie, description, rating).

### 🔎 Step-by-Step

- Movie 1 (War) → odd id = ✅, description not boring = ✅ → included.
- Movie 2 (Science) → even id = ❌ → excluded.
- Movie 3 (Irish) → odd id = ✅, but description = boring ❌ → excluded.
- Movie 4 (Ice song) → even id = ❌ → excluded.
- Movie 5 (House card) → odd id = ✅, description not boring = ✅ → included.

Result sorted by rating → House card (9.1), War (8.9).
