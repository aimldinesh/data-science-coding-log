# 🧲 Problem: The Number of Employees Which Report to Each Employee

- **Platform**: [LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-20
- **Tags**: MySQL, Database, select, joins
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Employees**

| Column Name | Type    |
|-------------|---------|
| employee_id | int     |
| name        | varchar |
| reports_to  | int     |
| age         | int     |

- `employee_id` is unique for each employee.  
- `reports_to` stores the `employee_id` of the manager they report to.  
- If `reports_to` is `NULL`, the employee does not report to anyone.  
- A **manager** is an employee who has at least **1 direct report**.  

Write a SQL query to report:
- The `employee_id` and `name` of each manager.  
- The **number of employees** who report directly to them (`reports_count`).  
- The **average age** of those reports (`average_age`), rounded to the nearest integer.  

Return the result ordered by `employee_id`.  

---

## 📝 Example

**Input:**

Employees table:  
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |

**Output:**

| employee_id | name    | reports_count | average_age |
|-------------|---------|---------------|-------------|
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |

---

## 🚀 Approach
1. Use a **self-join**:  
   - `e1` → employees (reports).  
   - `e2` → managers.  
   - Condition: `e1.reports_to = e2.employee_id`.  

2. Group by manager’s ID and name.  

3. Use aggregations:  
   - `COUNT(e1.employee_id)` → number of direct reports.  
   - `ROUND(AVG(e1.age), 0)` → average age of reports.  

4. Order by `employee_id`.  

---

## 💻 SQL Query

```sql
SELECT 
    e2.employee_id,
    e2.name,
    COUNT(e1.employee_id) AS reports_count,
    ROUND(AVG(e1.age), 0) AS average_age
FROM Employees e1
JOIN Employees e2
    ON e1.reports_to = e2.employee_id
GROUP BY e2.employee_id, e2.name
ORDER BY e2.employee_id;
```

---

## 🔎 Query Explanation

- JOIN connects each employee with their manager.
- COUNT(e1.employee_id) counts how many people report to each manager.
- AVG(e1.age) calculates the average age of those direct reports.
- ROUND(..., 0) ensures the average is rounded to the nearest integer.
- GROUP BY groups results by manager.
- ORDER BY e2.employee_id sorts managers by ID.
