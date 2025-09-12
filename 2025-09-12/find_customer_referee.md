# 🧲 Problem: Find Customer Referee

- **Platform**: [LeetCode](https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/find-customer-referee/submissions/1767869806/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/find-customer-referee/submissions/1767869806/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-12
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: `Customer`  

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| referee_id  | int     |

- `id` is the primary key for this table.  
- Each row of this table indicates the ID of a customer, their name, and the ID of the customer who referred them.  

**Task:**  
Write an SQL query to report the names of customers **who are not referred by the customer with id = 2**.  
Return the result table in **any order**.  

---

## 🚀 Approach
- We need all customers where `referee_id != 2` **or** `referee_id IS NULL` (not referred by anyone).  
- Use a `WHERE` condition with `<>` for not equal, and handle `NULL` explicitly.  

---

## 💻 Query

```sql
SELECT name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;
```

---

## 🔍 Explanation
- referee_id <> 2 → excludes customers who were referred by customer id = 2.
- OR referee_id IS NULL → includes customers without any referee.
- SELECT name → returns only the customer names as required.
✅ Handles both non-referrals and different referees.
