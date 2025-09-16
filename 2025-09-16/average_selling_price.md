# 🧲 Problem: Average Selling Price

- **Platform**: [LeetCode](https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/average-selling-price/submissions/1772304351/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/average-selling-price/submissions/1772304351/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-16
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📌 Problem Statement
Tables: **Prices** and **UnitsSold**

**Prices**
| Column Name | Type |
|-------------|------|
| product_id  | int  |
| start_date  | date |
| end_date    | date |
| price       | int  |

- `(product_id, start_date, end_date)` is the primary key.  
- Each row represents the price of a product for the given date range.  

**UnitsSold**
| Column Name | Type |
|-------------|------|
| product_id  | int  |
| purchase_date | date |
| units       | int  |

- `(product_id, purchase_date)` is the primary key.  
- Each row represents the number of units sold for a product on a given date.  

Write a SQL query to **find the average selling price for each product**.  
- The average selling price is calculated as:  
  **(Total price of product × units sold) / (Total units sold)**  

Return the result table with columns:  
- `product_id`  
- `average_price` (rounded to 2 decimal places)  

---

## ✅ Approach 1
1. Join `Prices` and `UnitsSold` on `product_id`.  
2. Ensure `purchase_date` lies between `start_date` and `end_date`.  
3. Compute total revenue = `SUM(units * price)`.  
4. Compute total units = `SUM(units)`.  
5. Divide revenue by units to get average price.  
6. Round to 2 decimal places.  

---

## ✅ SQL Query

```sql
SELECT 
    u.product_id,
    ROUND(SUM(u.units * p.price) / SUM(u.units), 2) AS average_price
FROM UnitsSold u
JOIN Prices p
  ON u.product_id = p.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id;
```
---

### ✅ Explanation

- JOIN → ensures we pick the correct price based on product and valid date range.
- SUM(u.units * p.price) → calculates total revenue for the product.
- SUM(u.units) → calculates total units sold.
- Division → revenue ÷ total units = average selling price.
- ROUND(..., 2) → formats result to 2 decimal places.
- GROUP BY u.product_id → one row per product.

---

## ✅ Approach 2
1. Aggregate revenue and units by joining `UnitsSold` -> `Prices` on `product_id` and purchase date between `start_date` and `end_date`.  
2. Compute `total_revenue = SUM(units * price)` and `total_units = SUM(units)` per product.  
3. Start from the **distinct product list in `Prices`** and LEFT JOIN the aggregated results so products with zero sales are still present.  
4. Use `NULLIF(total_units, 0)` to avoid division by zero and `COALESCE(..., 0)` to produce `0` when there are no sales.  
5. Round the result to 2 decimal places and order by `product_id`.

---

## ✅ SQL Query

```sql
WITH agg AS (
  SELECT 
    u.product_id,
    SUM(u.units * p.price) AS total_revenue,
    SUM(u.units) AS total_units
  FROM UnitsSold u
  JOIN Prices p
    ON u.product_id = p.product_id
   AND u.purchase_date BETWEEN p.start_date AND p.end_date
  GROUP BY u.product_id
)
SELECT 
  p.product_id,
  ROUND(
    COALESCE(agg.total_revenue / NULLIF(agg.total_units, 0), 0),
    2
  ) AS average_price
FROM (
  SELECT DISTINCT product_id
  FROM Prices
) p
LEFT JOIN agg
  ON p.product_id = agg.product_id
ORDER BY p.product_id;
```

---

### 🔎 Query Explanation

- The agg CTE computes total revenue and total units for products that actually have matching sold rows and price intervals.
- The outer query enumerates all distinct product_ids from Prices (so products with no sales are included).
- COALESCE(agg.total_revenue / NULLIF(agg.total_units, 0), 0):
  - NULLIF(..., 0) prevents division-by-zero (returns NULL if total_units = 0).
  - COALESCE(..., 0) converts that NULL into 0 for products with no sales/matches.
- ROUND(..., 2) formats the average to 2 decimal places.
- ORDER BY p.product_id returns deterministic ordering.

--- 

### 🔎 Step-by-Step

- Product 1:
  - (100 × 5) + (15 × 20) = 500 + 300 = 800 total revenue
  - Total units = 100 + 15 = 115
  - Average = 800 / 115 = 6.67

- Product 2:
  - (200 × 15) = 3000 revenue
  - Total units = 200
  - Average = 3000 / 200 = 15.00