# 🧲 Problem: Confirmation Rate

- **Platform**: [LeetCode](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/confirmation-rate/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/confirmation-rate/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-15
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Signups**
- `user_id INT PRIMARY KEY`
- `time_stamp DATETIME`

Table: **Confirmations**
- `user_id INT`
- `time_stamp DATETIME`
- `action ENUM('confirmed', 'timeout')`

Each user may request to confirm their signup via email.  
- A user can request multiple times.  
- Each request is recorded in the `Confirmations` table with an action of either:
  - `'confirmed'` → user successfully confirmed  
  - `'timeout'` → confirmation expired  

Write a SQL query to **find the confirmation rate of each user**.  

- Confirmation Rate =  
  **(# of confirmed actions) / (total # of actions)**  
- If a user did not request any confirmation, their confirmation rate is `0`.  
- The result should be **rounded to 2 decimal places**.  
- Return results **ordered by `user_id`**.  

---

## ✅ Approach
1. Use a **LEFT JOIN** between `Signups` and `Confirmations` to keep all users.  
2. Count:
   - Confirmed actions using `SUM(c.action = 'confirmed')`.  
   - Total actions using `COUNT(c.action)`.  
3. Divide `confirmed / total` to get confirmation rate.  
4. Use `IFNULL` for users with no confirmations → set rate to `0`.  
5. Round result to **2 decimal places**.  

---

## ✅ SQL Query

```sql
SELECT 
    s.user_id,
    ROUND(
        IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0),
        2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;
```
---

### ✅ Explanation

- LEFT JOIN → includes users even if they have no confirmation records.
- SUM(c.action = 'confirmed') → counts how many confirmations are successful (TRUE=1, FALSE=0).
- COUNT(c.action) → total attempts (confirmed + timeout).
- IFNULL(..., 0) → handles division by NULL for users with no confirmations.
- ROUND(..., 2) → ensures result is formatted to 2 decimal places.
- GROUP BY s.user_id → compute rates per user.

### Output Explanation

- User 2 → 1 confirmed / 1 total = 1.00
- User 3 → 0 confirmed / 2 total = 0.00
- User 6 → 0 confirmed / 0 total → 0.00
- User 7 → 3 confirmed / 3 total = 1.00
