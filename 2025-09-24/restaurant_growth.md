# 🧲 Problem: Restaurant Growth

- **Platform**: [LeetCode](https://leetcode.com/problems/restaurant-growth/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/restaurant-growth/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/restaurant-growth/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, self-joins, window function, cte
- **Difficulty**: Medium

---

## Problem Statement
We are given a `Customer` table:

| Column Name | Type |
|-------------|------|
| customer_id | int  |
| name        | varchar |
| visited_on  | date |
| amount      | int  |

- Each row records a customer's visit date and amount spent.
- We must calculate a **7-day rolling window average** of daily spending.
- Only return results starting from the **7th day onward**.

---

## Approach1 (Without Window Functions)
1. First, calculate **daily total spending** from the `Customer` table using `GROUP BY visited_on`.
2. For each day `d`, find all daily totals where `visited_on` is between `d - 6` and `d` (7 days inclusive).
3. Use a **self-join** to aggregate those totals:
   - Sum over the 7-day window → `amount_sum`.
   - Divide by 7 to get `average_amount`.
4. Filter out the first 6 days since they don’t form a complete 7-day window.

---

## SQL Query
```sql
WITH Daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT 
    a.visited_on,
    SUM(b.amount) AS amount,
    ROUND(SUM(b.amount) / 7, 2) AS average_amount
FROM Daily a
JOIN Daily b
    ON b.visited_on BETWEEN DATE_SUB(a.visited_on, INTERVAL 6 DAY) AND a.visited_on
GROUP BY a.visited_on
HAVING COUNT(b.visited_on) = 7
ORDER BY a.visited_on;
```

---

## Query Explanation
- Daily CTE: Summarizes all spending per day.
```sql
SELECT visited_on, SUM(amount) AS amount
FROM Customer
GROUP BY visited_on
```
- Self-Join: For each date a.visited_on, join with all rows b within the last 7 days.
```sql
ON b.visited_on BETWEEN DATE_SUB(a.visited_on, INTERVAL 6 DAY) AND a.visited_on
```

- SUM(b.amount) → total spending in the 7-day window.
- ROUND(SUM(b.amount)/7,2) → average spending in the 7-day window.
- HAVING COUNT(b.visited_on) = 7 ensures we only include complete 7-day windows.
- ORDER BY a.visited_on gives ascending chronological order.

---
## Approach2(using window function)
1. **Aggregate Daily Totals**  
   Since multiple customers may visit on the same day, group by `visited_on` to compute the daily spending total.  

2. **Apply Window Functions**  
   Use `SUM()` and `AVG()` with a **sliding 7-day window** (`ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`) to calculate:
   - Total amount in the last 7 days.  
   - Average amount in the last 7 days (rounded to 2 decimal places).  

3. **Filter Only Complete 7-Day Windows**  
   Use `ROW_NUMBER()` to track row order and keep only those where at least 7 days of data exist (`rn >= 7`).  

4. **Order the Result** by `visited_on`.  

---

## Query (MySQL 8+)
```sql
WITH Daily AS (
  SELECT visited_on, SUM(amount) AS amount
  FROM Customer
  GROUP BY visited_on
),
Rolling AS (
  SELECT
    visited_on,
    SUM(amount) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(
      AVG(amount) OVER (
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
      ), 2
    ) AS average_amount,
    ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
  FROM Daily
)
SELECT visited_on, amount, average_amount
FROM Rolling
WHERE rn >= 7
ORDER BY visited_on;
```
---

## Query Explanation

1.Daily CTE:Aggregates total spending per day.
```sql
SELECT visited_on, SUM(amount) AS amount
FROM Customer
GROUP BY visited_on
```
2.Rolling CTE
  - SUM(amount) OVER (...) → rolling 7-day sum.
  - AVG(amount) OVER (...) → rolling 7-day average.
  - ROW_NUMBER() → assigns order so we know when at least 7 days have passed.

3.Final Selection
  - Keep only rows where rn >= 7 → ensures complete 7-day windows.
  - Output columns: visited_on, total amount, and rounded average_amount.
