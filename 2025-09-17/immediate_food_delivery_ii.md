# 🧲 Problem: Immediate Food Delivery II

- **Platform**: [LeetCode](https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/immediate-food-delivery-ii/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/immediate-food-delivery-ii/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## Problem Statement
Table: **Delivery**

| Column Name                 | Type    |
|-----------------------------|---------|
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |

- `delivery_id` is the column of unique values of this table.  
- The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).  

- If the customer's preferred delivery date is the same as the order date, then the order is called **immediate**; otherwise, it is called **scheduled**.  
- The **first order** of a customer is the order with the earliest order date that the customer made.  
- It is guaranteed that a customer has precisely one first order.  

Write a solution to find the **percentage of immediate orders in the first orders of all customers**, rounded to 2 decimal places.  

### Example 1:
**Input:**  
Delivery table:  
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|-------------|-------------|------------|-----------------------------|
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |

**Output:**  
| immediate_percentage |
|-----------------------|
| 50.00                |

**Explanation:**  
- Customer 1’s first order → delivery_id 1 → scheduled.  
- Customer 2’s first order → delivery_id 2 → immediate.  
- Customer 3’s first order → delivery_id 5 → scheduled.  
- Customer 4’s first order → delivery_id 7 → immediate.  

So, half the customers have immediate first orders → **50.00%**.

---

## Approach
1. Find the **first order** for each customer (minimum `order_date`).  
2. Check if this first order is **immediate** (`order_date = customer_pref_delivery_date`).  
3. Count the immediate first orders and divide by the total number of customers.  
4. Round the result to 2 decimal places.  

---

## SQL Query
```sql
SELECT 
    ROUND(
        SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*), 2
    ) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) f
ON d.customer_id = f.customer_id AND d.order_date = f.first_order_date;
```
---

## Query Explanation

- Subquery f:
  - Finds the first order date for each customer using MIN(order_date).
- Join Delivery with f:
  - Ensures we only look at the first orders of each customer.
- CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END:
  - Checks whether the first order is immediate.
- SUM(...) / COUNT(*):
  - Computes the percentage of immediate first orders among all customers.
- ROUND(..., 2):
  - Rounds the result to 2 decimal places.
