# 🧲 Problem: Classes With at Least 5 Students

- **Platform**: [LeetCode](https://leetcode.com/problems/classes-with-at-least-5-students/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/classes-with-at-least-5-students/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/classes-with-at-least-5-students/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-18
- **Tags**: MySQL,Database,Sorting, Grouping
- **Difficulty**: Easy

---


## 📌 Problem Statement
Table: **Courses**

| Column Name | Type    |
|-------------|---------|
| student     | varchar |
| class       | varchar |

- `(student, class)` is the **primary key**.  
- Each row indicates that the student is enrolled in the class.  

Write a SQL query to **find all the classes that have at least five students**.  
Return the result table in **any order**.  

---

## 📝 Example

**Input:**

Courses table:
| student | class   |
|---------|---------|
| A       | Math    |
| B       | Math    |
| C       | Math    |
| D       | Math    |
| E       | Math    |
| F       | Science |
| G       | Science |
| H       | Science |
| I       | Science |

**Output:**

| class |
|-------|
| Math  |

---

## 🚀 Approach
1. **Group students by class**  
   - Use `GROUP BY class` to collect students per class.

2. **Count the number of students in each class**  
   - Apply `COUNT(student)`.

3. **Filter classes with at least 5 students**  
   - Use `HAVING COUNT(student) >= 5`.

---

## 💻 SQL Query

```sql
SELECT 
    class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
```
---

## 🔎 Query Explanation

- GROUP BY class → groups rows by class.
- COUNT(student) → counts number of students in each class.
- HAVING COUNT(student) >= 5 → filters only classes with 5 or more students