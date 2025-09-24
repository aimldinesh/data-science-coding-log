# 🧲 Problem: Patients With a Condition

- **Platform**: [LeetCode](https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/patients-with-a-condition/submissions/1781239132/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/patients-with-a-condition/submissions/1781239132/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, String, Clause
- **Difficulty**: Easy

---

## 📌 Problem Statement
We have a table **Patients**:

| Column Name  | Type    |
|--------------|---------|
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |

- `patient_id` is the primary key.  
- `conditions` contains **0 or more medical condition codes** separated by spaces.  
- Each condition may represent a disease, and we are only interested in **Type I Diabetes** codes.  

**Task:**  
Find all patients who have **Type I Diabetes**.  
- The condition code for Type I Diabetes **always starts with `DIAB1`**.  
- Return `patient_id`, `patient_name`, and `conditions`.  
- Order of output does not matter.  

---

## 📝 Example
Input:

**Patients**
| patient_id | patient_name | conditions   |
|------------|--------------|--------------|
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |

Output:

| patient_id | patient_name | conditions   |
|------------|--------------|--------------|
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |

---

## 🚀 Approach
1. Use a **string pattern search** on the `conditions` column.  
2. Since `conditions` may contain multiple codes separated by spaces:
   - We must match any word that **starts with `DIAB1`**.  
3. SQL’s `LIKE` operator works here:
   - `'DIAB1%'` → matches any code starting with `DIAB1`.  
   - Need to check when it appears:
     - at the **start of the string**, or  
     - after a **space**.  

---

## 💻 SQL Query
```sql
SELECT 
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';
```
---

## 🔎 Query Explanation

- conditions LIKE 'DIAB1%' → finds patients where the first condition starts with DIAB1.
- conditions LIKE '% DIAB1%' → finds patients where a later condition starts with DIAB1 (preceded by a space).
- Combining both ensures we capture all cases.
- The output includes only patients who meet this condition.
