# 🧲 Problem: Replace Employee ID With The Unique Identifier

- **Platform**: [LeetCode](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/1769216056/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/1769216056/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-13
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

### 📄 Problem Statement  
Table: `Employees`  

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |

`id` is the primary key for this table.  
Each row of this table contains the ID and name of an employee.  

Table: `EmployeeUNI`  

| Column Name  | Type    |
|--------------|---------|
| id           | int     |
| unique_id    | int     |

- `(id, unique_id)` is the primary key for this table.  
- Each row contains an employee’s ID and their corresponding unique identifier.  

**Task:**  
Write an SQL query to show the `unique_id` of each user along with the `name` from the `Employees` table.  
If an employee does not have a `unique_id`, still include their `name` with `NULL` for `unique_id`.  

---

### 📝 Approach  
- We need to combine two tables: `Employees` and `EmployeeUNI`.  
- Use a **LEFT JOIN** to keep all employees even if they don’t have a matching unique ID.  
- Select `unique_id` (from `EmployeeUNI`) and `name` (from `Employees`).  

---

### 💻 Query  
```sql
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
```
--- 

### 🔍 Explanation

- FROM Employees e → start with the Employees table.
- LEFT JOIN EmployeeUNI eu ON e.id = eu.id → bring in unique IDs if available, otherwise NULL.
- SELECT eu.unique_id, e.name → return required columns.

✅ Ensures all employees are listed even without a unique identifier.
