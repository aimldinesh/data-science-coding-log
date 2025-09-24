# 🧲 Problem: Fix Names in a Table

- **Platform**: [LeetCode](https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/fix-names-in-a-table/submissions/1781228099/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/fix-names-in-a-table/submissions/1781228099/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, String, Regex
- **Difficulty**: Easy

---

## 📌 Problem Statement
We have a table **Users**:

| Column Name | Type    |
|-------------|---------|
| user_id     | int     |
| name        | varchar |

- `user_id` is the primary key.  
- `name` contains only alphabetic characters, but may have **mixed uppercase/lowercase letters**.  

**Task:**  
Fix the names so that:
- The **first character** is uppercase.  
- The **remaining characters** are lowercase.  

Return the result ordered by **user_id**.

---

## 📝 Example
Input:

**Users**
| user_id | name  |
|---------|-------|
| 1       | aLice |
| 2       | bOB   |

Output:

| user_id | name  |
|---------|-------|
| 1       | Alice |
| 2       | Bob   |

---

## 🚀 Approach
1. Extract the **first character** using `LEFT(name, 1)` and convert it to uppercase (`UPPER`).  
2. Extract the **remaining substring** using `SUBSTRING(name, 2)` and convert it to lowercase (`LOWER`).  
3. Combine both parts using `CONCAT`.  
4. Order results by `user_id`.  

---

## 💻 SQL Query
```sql
SELECT 
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)), 
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;
```
---

## 🔎 Query Explanation

- LEFT(name, 1) → first character of the name.
- UPPER(LEFT(name, 1)) → ensures the first character is uppercase.
- SUBSTRING(name, 2) → extracts the rest of the string.
- LOWER(SUBSTRING(name, 2)) → ensures all remaining characters are lowercase.
- CONCAT(...) → combines the two parts into the corrected name.
- ORDER BY user_id → ensures the output is sorted by user IDs.
