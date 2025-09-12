# 🧲 Problem: Recyclable and Low Fat Products

- **Platform**: [LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/1767843746/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/1767843746/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-12
- **Tags**: SQL
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: `Products`  

| Column Name | Type    |
|-------------|---------|
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |

- `product_id` is the primary key for this table.  
- `low_fats` is an ENUM of type (`'Y'`, `'N'`) where `'Y'` means this product is low fat.  
- `recyclable` is an ENUM of type (`'Y'`, `'N'`) where `'Y'` means this product is recyclable.  

**Task:**  
Write an SQL query to find the IDs of products that are both **low fat** and **recyclable**.  
Return the result table in **any order**. 

---

## 🚀 Approach
- The table `Products` has information about each product with two binary attributes:  
  - `low_fats` (`'Y'`/`'N'`)  
  - `recyclable` (`'Y'`/`'N'`)  
- We need to find the `product_id` of products that are **both low fat and recyclable**.  
- Use a simple `WHERE` filter with conditions on both columns.

---

## 💻 Query

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';
```

---

## 🔍 Explanation
- WHERE low_fats = 'Y' → filters only low-fat products.
- AND recyclable = 'Y' → keeps only those that are also recyclable.
- The SELECT product_id outputs the required IDs.
- ✅ Simple filter query using multiple conditions in WHERE.
