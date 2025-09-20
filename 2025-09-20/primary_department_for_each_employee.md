# 🧲 Problem: Primary Department for Each Employee

- **Platform**: [LeetCode](https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/primary-department-for-each-employee/submissions/1777017971/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/primary-department-for-each-employee/submissions/1777017971/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-20
- **Tags**: MySQL, Database, Select, Joins
- **Difficulty**: Easy

---

## 📌 Problem Statement
Table: **Employee**

| Column Name   | Type    |
|---------------|---------|
| employee_id   | int     |
| department_id | int     |
| primary_flag  | enum    |

- `employee_id` is not the primary key.  
- Each employee may belong to more than one department.  
- `primary_flag` is an ENUM of type: `'Y'` or `'N'`.  
   - `'Y'` → the department is the primary department of the employee.  
   - `'N'` → the department is a secondary department.  
- Each employee has exactly one primary department.  
- If an employee belongs to only one department, that department is their primary by default.  

Write a SQL query to report each employee’s **primary department id**.  

Return the result table in any order.  

---

## 📝 Example

**Input:**

Employee table:  
| employee_id | department_id | primary_flag |
|-------------|---------------|--------------|
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |

**Output:**

| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |

---

## 🚀 Approach
1. Check if an employee has multiple departments:  
   - If yes → select the one with `primary_flag = 'Y'`.  
   - If no → select that only department.  

2. Use `WHERE primary_flag = 'Y' OR` ensure single department employees are included.  

3. Return only `employee_id` and `department_id`.  

---

## 💻 SQL Query

```sql
SELECT 
    employee_id,
    department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
        SELECT employee_id
        FROM Employee
        GROUP BY employee_id
        HAVING COUNT(department_id) = 1
    );
```
---

## 🔎 Query Explanation

- primary_flag = 'Y' → captures employees’ marked primary departments.
- The subquery:finds employees with only one department.
```sql
SELECT employee_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1
```
- The outer query includes both cases using OR.
- Final output: each employee’s correct primary department.
