# 🧲 Problem: Customer Who Visited but Did Not Make Any Transactions

- **Platform**: [LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/1769232553/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/1769232553/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-13
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

### 📄 Problem Statement  
Table: `Visits`  

| Column Name | Type |
|-------------|------|
| visit_id    | int  |
| customer_id | int  |

- `visit_id` is the primary key for this table.  
- This table contains information about the customers who visited the mall.  

Table: `Transactions`  

| Column Name   | Type |
|---------------|------|
| transaction_id| int  |
| visit_id      | int  |
| amount        | int  |

- `transaction_id` is the primary key for this table.  
- Each row contains information about a transaction made during a visit.  

**Task:**  
Write an SQL query to find the IDs of customers who visited the mall but **did not make any transactions**.  
Return the result table containing `customer_id` and the **count of visits** without transactions.  

---

### 📝 Approach  
- Start with the `Visits` table (all visits).  
- Use a **LEFT JOIN** with `Transactions` on `visit_id`.  
- Customers with `transaction_id IS NULL` are visits without transactions.  
- Group by `customer_id` and count such visits.  

---

### 💻 Query  
```sql
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
  ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```
---

### 🔍 Explanation

- LEFT JOIN → keeps all visits, even if no matching transaction exists.
- WHERE t.transaction_id IS NULL → filters visits without transactions.
- GROUP BY v.customer_id → groups visits per customer.
- COUNT(v.visit_id) → counts visits without transactions.

✅ Correctly outputs customers who visited but didn’t buy anything.
