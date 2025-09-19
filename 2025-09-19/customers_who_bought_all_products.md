# 🧲 Problem: Customers Who Bought All Products

- **Platform**: [LeetCode](https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/customers-who-bought-all-products/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/customers-who-bought-all-products/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-19
- **Tags**: MySQL, Database, Sorting, Grouping
- **Difficulty**: Medium

---

## 📌 Problem Statement
Table: **Customer**

| Column Name | Type |
|-------------|------|
| customer_id | int  |
| product_key | int  |

- `(customer_id, product_key)` is the **primary key**.  
- Each row shows that a customer purchased a particular product.  

Table: **Product**

| Column Name | Type |
|-------------|------|
| product_key | int  |

- `product_key` is the **primary key**.  
- Each row indicates an existing product.  

Write a SQL query to **find the customers who bought all the products available in the Product table**.  
Return the result table in **any order**.  

---

## 📝 Example

**Input:**

Customer table:
| customer_id | product_key |
|-------------|-------------|
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |

Product table:
| product_key |
|-------------|
| 5           |
| 6           |

**Output:**

| customer_id |
|-------------|
| 1           |
| 3           |

Explanation:  
- Products available = {5, 6}  
- Customer 1 bought {5, 6} → ✅  
- Customer 2 bought {6} only → ❌  
- Customer 3 bought {5, 6} → ✅  

---

## 🚀 Approach
1. **Count how many products exist in total**  
   - `SELECT COUNT(*) FROM Product`.

2. **Count distinct products bought by each customer**  
   - Use `GROUP BY customer_id` and `COUNT(DISTINCT product_key)`.

3. **Filter customers who bought all products**  
   - Compare their count with the total count of products.

---

## 💻 SQL Query

```sql
SELECT 
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM Product
);
```

---

## 🔎 Query Explanation

- COUNT(DISTINCT product_key) → ensures we only count unique products per customer.
- Subquery (SELECT COUNT(*) FROM Product) → gets total number of available products.
- HAVING ... = ... → filters only those customers who purchased all products.
