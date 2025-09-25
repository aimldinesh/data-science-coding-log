# 🧲 Problem: Department Top Three Salaries

- **Platform**: [LeetCode](https://leetcode.com/problems/department-top-three-salaries/description/)
- **Submission**: [https://leetcode.com/problems/department-top-three-salaries/submissions/](https://leetcode.com/problems/department-top-three-salaries/submissions/)
- **Date Solved**: 2025-09-25
- **Tags**: MySQL, Database, Window Function, Joins
- **Difficulty**: Hard

---

# 185. Department Top Three Salaries

## 📌 Problem  
We are given two tables:

### Employee
| Column Name  | Type    |
|--------------|---------|
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |

- `id` is the primary key.  
- `departmentId` is a foreign key referencing `Department.id`.  
- Each row contains an employee's ID, name, salary, and department ID.

### Department
| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |

- `id` is the primary key.  
- Each row contains a department ID and name.  

---

### Task  
Find the employees who are **high earners** in each department.  
- A high earner is an employee with a salary in the **top three distinct salaries** in their department.  
- Return:  
  - Department name  
  - Employee name  
  - Employee salary  

---

## 🧠 Approach  

1. **Join Employee with Department** → so we can return department names.  
2. Use `DENSE_RANK()` (not `ROW_NUMBER()`) over `(departmentId ORDER BY salary DESC)` to assign a salary rank **within each department**.  
   - `DENSE_RANK()` ensures that if multiple employees share the same salary, they get the same rank.  
   - Example: if two employees earn the same highest salary, both get rank 1, and the next salary gets rank 2.  
3. Filter results where the salary rank ≤ 3 (top 3 salaries only).  

---
## Example 1:

**Input:** 
**Employee table:**
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
**Department table:**
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
**Output:**
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
**Explanation:** 
- In the IT department:
  - Max earns the highest unique salary
  - Both Randy and Joe earn the second-highest unique salary
  - Will earns the third-highest unique salary

- In the Sales department:
  - Henry earns the highest salary
  - Sam earns the second-highest salary
  - There is no third-highest salary as there are only two employees
---

## ✅ SQL Query  

```sql
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT 
        id,
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
) e
JOIN Department d 
    ON e.departmentId = d.id
WHERE e.salary_rank <= 3;
```
---

## 🎯 Explanation

- The subquery assigns a salary rank for each employee within their department.

- DENSE_RANK() handles duplicates correctly:
  - If two employees share the same salary, they are tied at the same rank.
  - The next unique salary gets the next rank (no gaps).
- The main query joins with Department to return department names.
- The WHERE clause ensures only top 3 distinct salaries per department are returned.
