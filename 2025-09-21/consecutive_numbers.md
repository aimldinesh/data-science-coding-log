# 🧲 Problem: Consecutive Numbers

- **Platform**: [LeetCode](https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/consecutive-numbers/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/consecutive-numbers/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-21
- **Tags**: MySQL, Database, Select, Joins
- **Difficulty**: Medium

---

## 📌 Problem Statement  
You are given a table `Logs` with a single column:  

- `num` → integer value representing a number in a log sequence.  

Find all numbers that appear **at least three times consecutively**.  

Return the result with a single column:  
- `"ConsecutiveNums"` → the number that appears 3 or more times in a row.

---

## 💡 Approach  
1. Use **window functions** (`LEAD` / `LAG`) to check consecutive rows.  
2. Compare the current row’s `num` with the next two rows (`LEAD(1)` and `LEAD(2)`).  
3. If all three values are the same → mark it as a consecutive number.  
4. Use `DISTINCT` to avoid duplicates.  

---

## 📝 Query  
```sql
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LEAD(num, 1) OVER (ORDER BY id) AS next1,
           LEAD(num, 2) OVER (ORDER BY id) AS next2
    FROM Logs
) t
WHERE num = next1 AND num = next2;
```
---

## 🔎 Query Explanation

- LEAD(num, 1) → fetches the next row’s number.
- LEAD(num, 2) → fetches the number two rows ahead.
- If num = next1 = next2, that means the number appears 3 consecutive times.
- DISTINCT ensures each qualifying number appears only once in the output.
