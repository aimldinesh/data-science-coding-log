# 🧲 Problem: Product Price at a Given Date

- **Platform**: [LeetCode](https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/product-price-at-a-given-date/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/product-price-at-a-given-date/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-21
- **Tags**: MySQL, Database,Select, Joins
- **Difficulty**: Medium

---


## 📌 Problem Statement
Table: **Products**

| Column Name | Type |
|-------------|------|
| product_id  | int  |
| new_price   | int  |
| change_date | date |

- `(product_id, change_date)` is the primary key.  
- Each row indicates the price of a product changed to `new_price` on `change_date`.  
- Initially, all products have a price of **10**.  

Write a SQL query to find the **price of each product on 2019-08-16**.  
Return the result table with columns: `product_id`, `price`.  
The order of rows does not matter.

---

## 📝 Example

**Input:**

Products table:  

| product_id | new_price | change_date |
|------------|-----------|-------------|
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |

**Output:**

| product_id | price |
|------------|-------|
| 1          | 35    |
| 2          | 50    |
| 3          | 10    |

---

## 🚀 Approach
1. For each product, find the **latest price change on or before `2019-08-16`**.  
2. If no change exists before that date, the product retains its **initial price = 10**.  
3. Use a **window function** (`ROW_NUMBER()`) or a **correlated subquery** to pick the latest change per product.  

---

## 💻 SQL Query (Using ROW_NUMBER)

```sql
WITH latest_price AS (
    SELECT 
        product_id,
        new_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT 
    p.product_id,
    COALESCE(l.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id FROM Products
) p
LEFT JOIN latest_price l
    ON p.product_id = l.product_id AND l.rn = 1;
```

## 🔎 Query Explanation

- latest_price CTE:
  - Partitions by product_id and orders changes by change_date DESC.
  - ROW_NUMBER() = 1 gives the latest price on or before 2019-08-16.

- COALESCE(l.new_price, 10):
  - Returns the latest price if it exists.
  - If not, defaults to 10.

- LEFT JOIN with distinct products:
  - Ensures we include all products, even those without any changes before 2019-08-16.

- Final result gives each product_id with its correct price on 2019-08-16.
