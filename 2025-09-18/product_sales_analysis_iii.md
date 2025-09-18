# 🧲 Problem: Product Sales Analysis III

- **Platform**: [LeetCode](https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/product-sales-analysis-iii/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/product-sales-analysis-iii/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-18
- **Tags**: MySQL, Database, Sorting, Grouping
- **Difficulty**: Medium

---

## 📌 Problem Statement
Table: **Sales**

| Column Name | Type  |
|-------------|-------|
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |

- `(sale_id, year)` is the **primary key** of this table.  
- `product_id` is a foreign key referencing the **Product** table.  
- Each row records a sale of a product in a given year.  
- A product may have multiple sales entries in the same year.  

Write a SQL query to **find all sales that occurred in the first year each product was sold**.  

- For each `product_id`, identify the **earliest year** it appears in the Sales table.  
- Return all sales entries for that product in that year.  
- Return a table with the following columns:  
  - `product_id`, `first_year`, `quantity`, and `price`.  
- Return the result in **any order**.  

---

## 📝 Example

**Input:**

Sales table:
| sale_id | product_id | year | quantity | price |
|---------|------------|------|----------|-------|
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

**Output:**

| product_id | first_year | quantity | price |
|------------|------------|----------|-------|
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |

---

## 🚀 Approach
1. **Identify the earliest year for each product**  
   - Use `MIN(year)` grouped by `product_id` to find the first year the product was sold.

2. **Join with the original table**  
   - Join this result back to the Sales table on both `product_id` and the identified `first_year`.  
   - This ensures we only select rows belonging to the first year.

3. **Select required columns**  
   - Return `product_id`, `first_year` (as alias of year), `quantity`, and `price`.

---

## 💻 SQL Query

```sql
SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT 
        product_id, 
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) t
ON s.product_id = t.product_id 
AND s.year = t.first_year;
```
---

## Query Explanation

- The subquery:finds the earliest year for each product.
```sql
   SELECT product_id, MIN(year) AS first_year
   FROM Sales
   GROUP BY product_id
```

- The main query:
  - Joins the subquery result with Sales (s) on product_id and matching first_year.
  - Ensures we only return sales rows from the first year of that product.

- Final result includes:
  - product_id → identifier of the product
  - first_year → the year the product was first sold
  - quantity, price → details of sales during that year

This guarantees all sales entries from the first year of each product are captured.
