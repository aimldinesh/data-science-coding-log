# 🧲 Problem: Count Salary Categories

- **Platform**: [LeetCode](https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/count-salary-categories/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/count-salary-categories/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-21
- **Tags**: MySQL, Database, Select, Joins
- **Difficulty**: Medium

---

## 📌 Problem Statement  
Table: **Accounts**

| Column Name | Type |
|-------------|------|
| account_id  | int  |
| income      | int  |

- `account_id` is the primary key.  
- Each row contains the monthly income of one bank account.  

Write a SQL query to calculate the **number of accounts in each salary category**:

- `"Low Salary"` → income < 20000  
- `"Average Salary"` → income between 20000 and 50000 inclusive  
- `"High Salary"` → income > 50000  

The result must include **all three categories**, even if the count is 0.  

Return columns:  
- `category`  
- `accounts_count`  

---

## 📝 Example

**Input:**

Accounts table:

| account_id | income |
|------------|--------|
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |

**Output:**

| category       | accounts_count |
|----------------|----------------|
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |

**Explanation:**  
- Low Salary: account 2 (12747)  
- Average Salary: no accounts  
- High Salary: accounts 3, 6, 8  

---

## 🚀 Approach
1. Categorize each account using a **CASE WHEN** expression based on `income`.  
2. Use **GROUP BY** on the category to count accounts.  
3. To ensure all categories appear, create a **derived table with all categories** and **LEFT JOIN** the counts.  

---

## 💻 SQL Query

```sql
WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
),
income_counts AS (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY category
)
SELECT c.category,
       COALESCE(ic.accounts_count, 0) AS accounts_count
FROM categories c
LEFT JOIN income_counts ic
    ON c.category = ic.category;
```
---

## 🔎 Query Explanation

- categories CTE → ensures all three salary categories exist.
- income_counts CTE → counts the number of accounts in each category using CASE WHEN.
- LEFT JOIN → merges counts with all categories.
- COALESCE → replaces NULL with 0 if no accounts exist in a category.
