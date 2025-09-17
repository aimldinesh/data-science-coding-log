# 🧲 Problem: Project Employees I

- **Platform**: [LeetCode](https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/project-employees-i/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/project-employees-i/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📝 Problem Statement  
Write an SQL query that reports all the **projects** with the **average employee experience** rounded to **2 decimal places**.  

- `experience_years` is the number of years the employee has worked in the company.  
- The result table should contain `project_id` and `average_years`.  
- Return the result table ordered by `project_id`.  

### Table: Project  
| Column Name  | Type    |  
|--------------|---------|  
| project_id   | int     |  
| employee_id  | int     |  

- `(project_id, employee_id)` is the primary key.  

### Table: Employee  
| Column Name      | Type    |  
|------------------|---------|  
| employee_id      | int     |  
| name             | varchar |  
| experience_years | int     |  

- `employee_id` is the primary key.  

---

## ✅ Example Input  

**Project Table:**  
| project_id | employee_id |  
|------------|-------------|  
| 1          | 1           |  
| 1          | 2           |  
| 1          | 3           |  
| 2          | 1           |  
| 2          | 4           |  

**Employee Table:**  
| employee_id | name  | experience_years |  
|-------------|-------|------------------|  
| 1           | Khaled| 3                |  
| 2           | Ali   | 2                |  
| 3           | John  | 1                |  
| 4           | Doe   | 2                |  

---

## 🎯 Expected Output  

| project_id | average_years |  
|------------|---------------|  
| 1          | 2.00          |  
| 2          | 2.50          |  

---

## 🛠️ Approach  

1. We need to calculate the **average experience of employees per project**.  
2. Since `experience_years` is available in the **Employee** table, we must join it with the **Project** table using `employee_id`.  
3. After joining, we group the results by `project_id`.  
4. Use `AVG()` to calculate the average experience per project.  
5. Use `ROUND(..., 2)` to ensure the average is displayed with **2 decimal places**.  

---

## 💡 SQL Query  

```sql
SELECT 
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM 
    Project p
JOIN 
    Employee e
ON 
    p.employee_id = e.employee_id
GROUP BY 
    p.project_id;
```
---

### 🔎 Query Explanation

- JOIN Project p and Employee e → Matches employees with their projects using employee_id.
- AVG(e.experience_years) → Calculates the average years of experience for employees working on each project.
- ROUND(..., 2) → Ensures the average is formatted to 2 decimal places.
- GROUP BY p.project_id → Groups results by project so that we get one row per project.
