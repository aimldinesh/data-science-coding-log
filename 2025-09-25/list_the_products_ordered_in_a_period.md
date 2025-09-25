# 🧲 Problem: List the Products Ordered in a Period

- **Platform**: [LeetCode](https://leetcode.com/problems/list-the-products-ordered-in-a-period/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/list-the-products-ordered-in-a-period/submissions/1781946707/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/list-the-products-ordered-in-a-period/submissions/1781946707/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-25
- **Tags**: MySQL, Database, Joins
- **Difficulty**: Easy

---

## 📌 Problem Statement
We are given two tables:

### **Products**
| Column Name      | Type    |
|------------------|---------|
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |

- `product_id` is the **primary key**.  
- This table contains information about the company's products.  

### **Orders**
| Column Name   | Type    |
|---------------|---------|
| product_id    | int     |
| order_date    | date    |
| unit          | int     |

- `product_id` is a **foreign key** referencing `Products.product_id`.  
- The table may contain duplicates.  
- Each row records the number of units of a product ordered on a specific date.  

**Task:**  
Return the names of products and the total units ordered in **February 2020**, but only include products that have at least **100 units** ordered in that month.  

---

## 📝 Example
**Input:**

**Products**
| product_id | product_name          | product_category |
|------------|-----------------------|------------------|
| 1          | Leetcode Solutions    | Book             |
| 2          | Jewels of Stringology | Book             |
| 3          | HP                    | Laptop           |
| 4          | Lenovo                | Laptop           |
| 5          | Leetcode Kit          | T-shirt          |

**Orders**
| product_id | order_date | unit |
|------------|------------|------|
| 1          | 2020-02-05 | 60   |
| 1          | 2020-02-10 | 70   |
| 2          | 2020-01-18 | 30   |
| 2          | 2020-02-11 | 80   |
| 3          | 2020-02-17 | 2    |
| 3          | 2020-02-24 | 3    |
| 4          | 2020-03-01 | 20   |
| 4          | 2020-03-04 | 30   |
| 4          | 2020-03-04 | 60   |
| 5          | 2020-02-25 | 50   |
| 5          | 2020-02-27 | 50   |
| 5          | 2020-03-01 | 50   |

**Output:**
| product_name       | unit |
|--------------------|------|
| Leetcode Solutions | 130  |
| Leetcode Kit       | 100  |

---

## 🚀 Approach
1. **Filter Orders for February 2020:**  
   - Extract only rows where `order_date` falls between `'2020-02-01'` and `'2020-02-29'`.  

2. **Aggregate units per product:**  
   - Use `SUM(unit)` to calculate the total units sold in February 2020 for each product.  

3. **Apply filter:**  
   - Keep only products where total units `>= 100`.  

4. **Join with Products table:**  
   - Get the product names using `JOIN`.  

---

## 💻 SQL Query
```sql
SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Orders o
JOIN Products p
    ON o.product_id = p.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;
```

---

## ✅ Explanation

- WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29' → restricts to February 2020.
- SUM(o.unit) → total units per product.
- GROUP BY p.product_id, p.product_name → ensures correct aggregation.
- HAVING SUM(o.unit) >= 100 → filters only products with at least 100 units.
- The final output includes product_name and aggregated unit.
