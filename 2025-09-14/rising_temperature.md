# 🧲 Problem: Rising Temperature

- **Platform**: [LeetCode](https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/rising-temperature/submissions/1770460790/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/rising-temperature/submissions/1770460790/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-14
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

### 📄 Problem Statement  
Table: `Weather`  

| Column Name | Type |
|-------------|------|
| id          | int  |
| recordDate  | date |
| temperature | int  |

- `id` is the primary key for this table.  
- Each row contains information about the temperature on a certain day.  

**Task:**  
Write an SQL query to find the IDs of all dates’ records with higher temperatures compared to the previous day (yesterday).  

---

### 📝 Approach  
- We need to compare each day’s temperature with the **previous day’s temperature**.  
- Use a **self-join** on the `Weather` table:  
  - Match `w1.recordDate = w2.recordDate + 1`.  
- Select `w1.id` where `w1.temperature > w2.temperature`.  

---

### 💻 Query  
```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```
---

### 🔍 Explanation

- JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 → matches each date with its previous day.
- WHERE w1.temperature > w2.temperature → keeps only days hotter than yesterday.
- SELECT w1.id → returns the IDs of such days.

✅ Uses self-join and date difference to compare consecutive days.