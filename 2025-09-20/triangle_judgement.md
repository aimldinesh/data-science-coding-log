# 🧲 Problem: Triangle Judgement

- **Platform**: [LeetCode](https://leetcode.com/problems/triangle-judgement/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/triangle-judgement/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/triangle-judgement/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-20
- **Tags**: MySQL, Database, triangle, Math
- **Difficulty**: Easy

---


## 📌 Problem Statement  
You are given a table `Triangle` with three columns: `x`, `y`, and `z`, representing the lengths of the sides of a triangle.  
Write a query to determine whether these values can form a valid triangle.  
A valid triangle must satisfy the following **triangle inequality conditions**:
- `x + y > z`
- `y + z > x`
- `x + z > y`

Return each row with an additional column `"triangle"` that outputs:
- `"Yes"` if the values can form a triangle
- `"No"` otherwise

---

## 💡 Approach  
1. Use the **triangle inequality theorem** to check if the three sides can form a valid triangle.  
2. Apply a `CASE WHEN` statement in the query:  
   - If all three inequalities are satisfied → return `"Yes"`.  
   - Else → return `"No"`.  

---

## 📝 Query  
```sql
SELECT x, y, z,
       CASE
           WHEN x + y > z AND y + z > x AND x + z > y THEN 'Yes'
           ELSE 'No'
       END AS triangle
FROM Triangle;
```
---

## 🔎 Query Explanation

- x + y > z, y + z > x, and x + z > y are checked for each row.
- CASE assigns "Yes" only if all conditions are met.
- If any condition fails, "No" is returned.
- This ensures only valid triangles are marked "Yes".