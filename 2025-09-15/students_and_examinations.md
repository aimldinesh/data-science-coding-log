# 🧲 Problem: Students and Examinations

- **Platform**: [LeetCode](https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/students-and-examinations/submissions/1771634819/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/students-and-examinations/submissions/1771634819/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-15
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: **Students**  

| Column Name | Type    |
|-------------|---------|
| student_id  | int     |
| student_name| varchar |

- `student_id` is the primary key.  

---

Table: **Subjects**  

| Column Name | Type    |
|-------------|---------|
| subject_name| varchar |

- `subject_name` is the primary key.  

---

Table: **Examinations**  

| Column Name | Type    |
|-------------|---------|
| student_id  | int     |
| subject_name| varchar |

- Records which student attended which subject exam.  

---

👉 Write a SQL query to find the **number of times each student attended each exam**.  
- Output should include **all students and all subjects**, even if a student never attended that subject (attendance = 0).  
- Sort by `student_id` and `subject_name`.  

---

## 💡 Approach  
1. Generate all possible pairs of `(student_id, subject_name)` using **CROSS JOIN** between `Students` and `Subjects`.  
2. Use a **LEFT JOIN** with `Examinations` to count how many times each student attended that subject exam.  
3. Use `COUNT(e.subject_name)` to get the number of times attended (0 if never attended).  
4. Sort by `student_id`, then by `subject_name`.  

---

## ✅ SQL Query  

```sql
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
  ON s.student_id = e.student_id
 AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
```

---

### Query Explanation

- CROSS JOIN:
  - Produces every possible combination of students and subjects.

- LEFT JOIN Examinations:
  - Keeps all student–subject pairs, even if the student never attended that subject exam.

- COUNT(e.subject_name):
  - Counts how many times the student attended the exam (0 if no match).

- GROUP BY:
  - Groups by each student and subject combination to aggregate the count.

- ORDER BY s.student_id, sub.subject_name:
  - Orders output by student and subject as required.
