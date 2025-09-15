# 🧲 Problem: Employee Bonus

- **Platform**: [LeetCode](https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/employee-bonus/submissions/1771605367/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/employee-bonus/submissions/1771605367/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-15
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: **Employee**  

| Column Name | Type    |
|-------------|---------|
| empId       | int     |
| name        | varchar |

Table: **Bonus**  

| Column Name | Type    |
|-------------|---------|
| empId       | int     |
| bonus       | int     |

- `empId` is the primary key of **Employee**.  
- `empId` in **Bonus** is a foreign key referencing **Employee(empId)**.  
- Each employee may or may not have a bonus.  

👉 Write a SQL query to report the **name and bonus amount** of each employee whose bonus is **less than 1000** or is **NULL**.  

---

## 💡 Approach  
1. Use a **LEFT JOIN** so that employees without a bonus are still included.  
2. Select employees where `bonus < 1000` **or** `bonus IS NULL`.  
3. Return the employee’s name and their bonus.  

---

## ✅ SQL Query  

```sql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
  ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```
---
### Query Explanation

- FROM Employee e LEFT JOIN Bonus b:
  - Ensures all employees are included, even if they don’t have a bonus record.

- ON e.empId = b.empId:
  - Matches employees with their corresponding bonus.

- WHERE b.bonus < 1000 OR b.bonus IS NULL:
  - Filters only employees with bonuses less than 1000 or with no bonus assigned.

- SELECT e.name, b.bonus:
  - Returns the employee’s name and bonus value (if exists, else NULL).
