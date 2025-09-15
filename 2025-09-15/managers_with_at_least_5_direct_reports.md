# 🧲 Problem: Managers with at Least 5 Direct Reports

- **Platform**: [LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/managers-with-at-least-5-direct-reports/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-15
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: **Employee**  

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |

- `id` is the primary key.  
- `managerId` is the `id` of another employee in the same table (self-referencing).  
- Each employee has at most one manager.  

👉 Write a SQL query to find the **names of managers** who have **at least 5 direct reports**.  

---

## 💡 Approach  
1. Since `managerId` points to another employee’s `id`, we can **group by managerId**.  
2. Count how many employees report to each manager.  
3. Use `HAVING COUNT(*) >= 5` to filter managers with 5 or more direct reports.  
4. Join back with `Employee` to get the **manager’s name**.  

---

## ✅ SQL Query  

```sql
SELECT m.name
FROM Employee e
JOIN Employee m
  ON e.managerId = m.id
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;
```

---

### 🔎 Query Explanation

- JOIN Employee m ON e.managerId = m.id:
  - Joins employees (e) with their managers (m).

- GROUP BY m.id, m.name:
  - Groups data by each manager to aggregate the number of direct reports.

- COUNT(e.id):
  - Counts how many employees directly report to each manager.

- HAVING COUNT(e.id) >= 5:
  - Filters only those managers with at least 5 direct reports.

- SELECT m.name:
  - Returns the names of qualifying managers.

### Output Explanation
- Manager John (id=1) has 5 direct reports → Dan, James, Amy, Anne, Ron.
- No other manager meets the criteria.
- Hence, only John is returned.
