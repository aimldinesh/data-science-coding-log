# 🧲 Problem: Group Sold Products By The Date

- **Platform**: [LeetCode](https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/group-sold-products-by-the-date/submissions/1781927623/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/group-sold-products-by-the-date/submissions/1781927623/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-25
- **Tags**: MySQL, Database, String
- **Difficulty**: Easy

---

## 📌 Problem Statement
We are given the table **Activities**:

| Column Name | Type    |
|-------------|---------|
| sell_date   | date    |
| product     | varchar |

- The table does **not** have a primary key (it may contain duplicates).  
- Each row represents the product name and the date it was sold.  

**Task:**  
For each date, find:
1. The number of **distinct products** sold (`num_sold`).  
2. The list of product names sold on that date, sorted **lexicographically**, concatenated with commas.  

Return the result ordered by `sell_date`.

---

## 📝 Example
**Input:**

**Activities**
| sell_date  | product     |
|------------|-------------|
| 2020-05-30 | Headphone   |
| 2020-06-01 | Pencil      |
| 2020-06-02 | Mask        |
| 2020-05-30 | Basketball  |
| 2020-06-01 | Bible       |
| 2020-06-02 | Mask        |
| 2020-05-30 | T-Shirt     |

**Output:**
| sell_date  | num_sold | products                     |
|------------|----------|------------------------------|
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |

---

## 🚀 Approach
1. **Remove duplicates:**  
   Use `DISTINCT` to ensure repeated products on the same date are counted only once.  

2. **Count unique products:**  
   Use `COUNT(DISTINCT product)` for `num_sold`.  

3. **Concatenate sorted product names:**  
   Use:
   - `GROUP_CONCAT(DISTINCT product ORDER BY product)` in MySQL.  
   - `STRING_AGG(product, ',' ORDER BY product)` in PostgreSQL / SQL Server.  

4. **Group by date:**  
   Group results by `sell_date` and order ascending.

---

## 💻 SQL Query (MySQL)
```sql
SELECT 
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```
---

## ✅ Explanation

- COUNT(DISTINCT product) → counts unique products per date.
- GROUP_CONCAT(DISTINCT product ORDER BY product) → builds a comma-separated sorted list of product names.
- GROUP BY sell_date → ensures results are aggregated per date.
- ORDER BY sell_date → returns rows sorted by date.
