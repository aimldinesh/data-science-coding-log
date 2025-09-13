# 🧲 Problem: Product Sales Analysis I

- **Platform**: [LeetCode](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/product-sales-analysis-i/submissions/1769224778/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/product-sales-analysis-i/submissions/1769224778/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-13
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

### 📄 Problem Statement  
Table: `Sales`  

| Column Name | Type    |
|-------------|---------|
| sale_id     | int     |
| product_id  | int     |
| year        | int     |
| quantity    | int     |
| price       | int     |

- `sale_id` is the primary key for this table.  
- Each row contains information about a sale of a product in a particular year.  

Table: `Product`  

| Column Name | Type    |
|-------------|---------|
| product_id  | int     |
| product_name | varchar |

- `product_id` is the primary key for this table.  
- Each row contains the product ID and product name.  

**Task:**  
Write an SQL query to report the `product_name`, `year`, and `price` for each sale.  

---

### 📝 Approach  
- We need to combine the `Sales` and `Product` tables using `product_id`.  
- Use an `INNER JOIN` since every sale must have a valid product.  
- Select `product_name`, `year`, and `price` from the joined tables.  

---

### 💻 Query  
```sql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p
  ON s.product_id = p.product_id;
```
### 🔍 Explanation

- JOIN Product p ON s.product_id = p.product_id → links sales with product names.
- SELECT p.product_name, s.year, s.price → fetches required columns.
- No filtering needed since all sales are valid.

✅ Simple join query combining two tables.
