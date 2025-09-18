# 🧲 Problem: Number of Unique Subjects Taught by Each Teacher

- **Platform**: [LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/submissions/1774550054/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/submissions/1774550054/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-18
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## Problem Statement
Table: **Teacher**

| Column Name | Type    |
|-------------|---------|
| teacher_id  | int     |
| subject_id  | int     |
| dept_id     | int     |

- This table has no primary key and may contain duplicate rows.
- Each row indicates that a teacher teaches a subject in a department.

Write an SQL query to report the number of **unique subjects** each teacher teaches.  
Return the result table in any order.

---

## Example 1

**Input**
Teacher table:  
| teacher_id | subject_id | dept_id |
|------------|------------|---------|
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |

**Output**
| teacher_id | cnt |
|------------|-----|
| 1          | 2   |
| 2          | 4   |

**Explanation**
- Teacher 1 teaches subject `2` in two different departments but it should be counted only once.  
  Unique subjects = {2, 3} → count = 2.  
- Teacher 2 teaches subjects {1, 2, 3, 4} → count = 4.  

---

## Approach
1. Group data by `teacher_id`.  
2. Use `COUNT(DISTINCT subject_id)` to ensure each subject is counted only once per teacher (even if repeated across departments).  
3. Return `teacher_id` and count.  

---

## SQL Query

```sql
SELECT 
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```
---

## Query Explanation

- COUNT(DISTINCT subject_id) counts unique subjects taught by each teacher.
- GROUP BY teacher_id ensures the count is calculated per teacher.
- Final output returns teacher’s ID and their unique subject count.
