# 🧲 Problem: Find Followers Count

- **Platform**: [LeetCode](https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/find-followers-count/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/find-followers-count/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-18
- **Tags**: MySQL, Database, Sorting, Grouping
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Followers**

| Column Name | Type |
|-------------|------|
| user_id     | int  |
| follower_id | int  |

- `(user_id, follower_id)` is the **primary key**.  
- Each row represents that the `follower_id` follows the `user_id`.  

Write a SQL query to **find the number of followers for each user**.  
Return the result table ordered by `user_id` in **ascending order**.  

---

## 📝 Example

**Input:**

Followers table:
| user_id | follower_id |
|---------|-------------|
| 1       | 3           |
| 2       | 3           |
| 2       | 4           |

**Output:**

| user_id | followers_count |
|---------|-----------------|
| 1       | 1               |
| 2       | 2               |

---

## 🚀 Approach
1. **Group records by `user_id`**  
   - Since we need followers count per user, group on `user_id`.

2. **Count distinct followers**  
   - Use `COUNT(follower_id)` to count number of followers for each user.  
   - Distinct isn’t required here because `(user_id, follower_id)` is already unique.

3. **Sort the output**  
   - Order by `user_id ASC`.

---

## 💻 SQL Query

```sql
SELECT 
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```

---

## Query Explanation

- GROUP BY user_id → groups rows by user.
- COUNT(follower_id) → counts how many followers each user has.
- ORDER BY user_id → ensures ascending order of users in the output.
