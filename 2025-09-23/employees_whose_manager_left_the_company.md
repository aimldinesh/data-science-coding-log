# 🧲 Problem: Employees Whose Manager Left the Company

- **Platform**: [LeetCode](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/employees-whose-manager-left-the-company/submissions/1779773308/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/employees-whose-manager-left-the-company/submissions/1779773308/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-23
- **Tags**: MySQL, Database, Subquries
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Employees**

| Column Name  | Type    |
|--------------|---------|
| employee_id  | int     |
| name         | varchar |
| manager_id   | int     |
| salary       | int     |

- `employee_id` is the primary key.  
- `manager_id` is the id of the employee's manager (may be `NULL` if they have no manager).  
- When a manager leaves, their row is removed from the table, but their reports still keep the `manager_id`.

Find IDs of employees whose salary is **strictly less than 30000** and whose **manager left the company** (i.e., `manager_id` is not present in the Employees table).  
Return the result ordered by `employee_id`.

---

## 🚀 Approach
1. Filter employees by `salary < 30000`.  
2. Exclude employees with `manager_id IS NULL` (they never had a manager).  
3. Use a `LEFT JOIN` (or `NOT EXISTS`) to check whether the `manager_id` exists in the Employees table.  
4. If the join finds no manager (`m.employee_id IS NULL`), that manager left — include the employee.

---

## 💻 SQL Query

```sql
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m
    ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL      -- exclude employees who never had a manager
  AND m.employee_id IS NULL         -- manager row not found => manager left
ORDER BY e.employee_id;
```
#### Alternative (using NOT EXISTS)
```sql
SELECT e.employee_id
FROM Employees e
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND NOT EXISTS (
      SELECT 1
      FROM Employees m
      WHERE m.employee_id = e.manager_id
  )
ORDER BY e.employee_id;
```
---

## 🔎 Query Explanation

- e.salary < 30000 → candidates by salary.
- e.manager_id IS NOT NULL → exclude people who never had a manager (manager_id NULL).
- LEFT JOIN Employees m ON e.manager_id = m.employee_id → tries to find the manager row.
- m.employee_id IS NULL → manager row not found, meaning the manager left the company.
- Ordering by employee_id matches the required output format.
