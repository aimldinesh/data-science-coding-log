# 🧲 Problem: Monthly Transactions I

- **Platform**: [LeetCode](https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/monthly-transactions-i/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/monthly-transactions-i/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📝 Problem Statement  
You are given a table `Transactions` that contains information about incoming transactions.  

Write an SQL query to find, for each **month** and **country**:  
1. The **total number of transactions**.  
2. The **number of approved transactions**.  
3. The **total transaction amount**.  
4. The **total approved transaction amount**.  

- Return the result table in **any order**.  
- The `month` should be formatted as `YYYY-MM`.  

---

## 📊 Table Schema  

### Transactions  
| Column Name | Type    |  
|-------------|---------|  
| id          | int     |  
| country     | varchar |  
| state       | enum    |  
| amount      | int     |  
| trans_date  | date    |  

- `id` is the primary key.  
- `state` is an enum of type: `approved`, `declined`.  

---

## ✅ Example Input  

**Transactions Table:**  
| id  | country | state    | amount | trans_date |  
|-----|---------|----------|--------|------------|  
| 121 | US      | approved | 1000   | 2018-12-18 |  
| 122 | US      | declined | 2000   | 2018-12-19 |  
| 123 | US      | approved | 2000   | 2019-01-01 |  
| 124 | DE      | approved | 2000   | 2019-01-07 |  

---

## 🎯 Expected Output  

| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |  
|---------|---------|-------------|----------------|--------------------|-----------------------|  
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |  
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |  
| 2019-01 | DE      | 1           | 1              | 2000               | 2000                  |  

---

## 🛠️ Approach  

1. Extract the `month` from `trans_date` using `DATE_FORMAT(trans_date, '%Y-%m')`.  
2. Group data by **month** and **country**.  
3. Use **conditional aggregation**:  
   - `COUNT(id)` → Total number of transactions.  
   - `COUNT(CASE WHEN state = 'approved' THEN id END)` → Number of approved transactions.  
   - `SUM(amount)` → Total transaction amount.  
   - `SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END)` → Total approved transaction amount.  
4. Return results in any order.  

---

## 💡 SQL Query  

```sql
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(id) AS trans_count,
    COUNT(CASE WHEN state = 'approved' THEN id END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM 
    Transactions
GROUP BY 
    month, country;
```
---

## 🔎 Query Explanation

- DATE_FORMAT(trans_date, '%Y-%m') → Extracts the month in YYYY-MM format.
- COUNT(id) → Counts all transactions.
- COUNT(CASE WHEN state = 'approved' THEN id END) → Counts only approved transactions.
- SUM(amount) → Total amount of all transactions.
- SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) → Adds only approved transaction amounts.
- GROUP BY month, country → Ensures aggregation is done per month and country.
