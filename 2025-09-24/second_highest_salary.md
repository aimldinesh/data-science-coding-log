# 🧲 Problem: Second Highest Salary

- **Platform**: [LeetCode](https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/second-highest-salary/submissions/1781278709/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/second-highest-salary/submissions/1781278709/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, Findow Function, Subqueries
- **Difficulty**: Medium

---

## Problem Statement
We need to query the **second highest distinct salary** from the `Employee` table.  
- If there is **no second highest salary** (i.e., only one distinct salary exists), we must return `NULL`.

### Table: Employee
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
```
- id is the primary key (column with unique values).
- Each row of this table contains information about the salary of an employee.

### Example 1

#### Input:
```text
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
#### Output:
```text
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```
---

### Example 2

#### Input:
```text
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
```
### Output:
```text
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```
---

## ✅ Approach 1: Using LIMIT + OFFSET
```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

--- 

### Explanation:

- DISTINCT salary → removes duplicates.
- ORDER BY salary DESC → sorts salaries from highest to lowest.
- LIMIT 1 OFFSET 1 → skips the highest salary and picks the next one.
- If no row exists, it returns NULL.

---

## ✅ Approach 2: Using Window Function (DENSE_RANK)
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) t
WHERE rnk = 2;
```
---

### Explanation:

- DENSE_RANK() assigns ranks starting from highest salary.
- Rank 1 = highest salary, Rank 2 = second highest.
- Filter rows where rnk = 2.
- MAX(salary) ensures we return one row even if multiple employees share the same second highest salary.
- If no second highest exists, returns NULL.

---

## ✅ Approach 3: Using Subquery with MAX and <
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary) FROM Employee
);
```

---

### Explanation:

- First find the highest salary.
- Then select the maximum salary that is less than the highest salary.
- If only one salary exists, returns NULL.