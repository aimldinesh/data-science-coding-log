# 🧲 Problem: Delete Duplicate Emails

- **Platform**: [LeetCode](https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/delete-duplicate-emails/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/delete-duplicate-emails/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, self-join
- **Difficulty**: Easy

---

## 📌 Problem Statement
We have a table **Person**:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| email       | varchar |

- `id` is the primary key.  
- Each row represents a unique record of an email, but **duplicates may exist**.  
- The task is to **delete duplicate emails**, keeping only the one with the **smallest `id`** for each unique email.  

**Note:**  
- You must write a `DELETE` statement (not `SELECT`).  
- After deletion, the result will show the cleaned **Person** table.  
- Order of rows in the output does not matter.  

---

## 📝 Example
Input:

**Person**
| id | email            |
|----|------------------|
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |

Output:

| id | email            |
|----|------------------|
| 1  | john@example.com |
| 2  | bob@example.com  |

**Explanation:**  
- `john@example.com` is duplicated (id 1 & 3).  
- Keep the record with **id = 1** (smallest).  
- Delete record with **id = 3**.  

---

## 🚀 Approach
1. Identify duplicates using **email grouping**.  
2. For each `email`, determine the **smallest id**.  
3. Delete rows where `id` is **not equal to the smallest id** for that email.  

---

## 💻 SQL Query
```sql
DELETE p1
FROM Person p1
JOIN Person p2
  ON p1.email = p2.email
 AND p1.id > p2.id;
```

---

## 🔎 Query Explanation

- JOIN pairs rows with the same email.
- Condition p1.id > p2.id → keeps only the larger id duplicates.
- DELETE p1 → removes those duplicates, leaving only the smallest id.
- ✅ Final result: Table contains only unique emails with the smallest id preserved.
