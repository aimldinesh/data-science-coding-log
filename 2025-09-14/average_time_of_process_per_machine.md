# 🧲 Problem: Average Time of Process per Machine

- **Platform**: [LeetCode](https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/average-time-of-process-per-machine/submissions/1770471717/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/average-time-of-process-per-machine/submissions/1770471717/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-14
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📌 Problem  
Table: **Activity**  

| Column Name   | Type    | Description |
|---------------|---------|-------------|
| machine_id    | int     | The ID of the machine |
| process_id    | int     | The ID of the process |
| activity_type | enum    | Either `'start'` or `'end'` |
| timestamp     | float   | The time at which the activity happened |

- Each process has exactly one `'start'` and one `'end'` record for a machine.  
- We need to calculate the **average processing time** of each machine.  
- The result should be rounded to **3 decimal places**.  

---

## 💡 Approach  
1. Each process has a `start` and `end` event.  
2. Processing time = `end.timestamp - start.timestamp`.  
3. Perform a **self-join** on the `Activity` table:  
   - Match rows with the same `machine_id` and `process_id`.  
   - Pair `'start'` with `'end'`.  
4. Calculate the **average** of processing times per machine.  
5. Use `ROUND(..., 3)` to keep 3 decimal places.  

---

## ✅ SQL Query  

```sql
SELECT 
    s.machine_id,
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM Activity s
JOIN Activity e
  ON s.machine_id = e.machine_id
 AND s.process_id = e.process_id
WHERE s.activity_type = 'start'
  AND e.activity_type = 'end'
GROUP BY s.machine_id;
```
### 🔎 Query Explanation

- FROM Activity s JOIN Activity e:
  - We join the table with itself to pair start (s) and end (e) activities of the same process.

- ON s.machine_id = e.machine_id AND s.process_id = e.process_id:
  - Ensures we are comparing the same machine and the same process.

- WHERE s.activity_type = 'start' AND e.activity_type = 'end':
  - Filters so that s only takes 'start' rows and e only takes 'end' rows.

- e.timestamp - s.timestamp:
  - Gives the processing time for a single process.

- AVG(...):
  - Calculates the average processing time across all processes for each machine.

- ROUND(..., 3):
  - Rounds the average to 3 decimal places as required.

- GROUP BY s.machine_id:
  - Groups results by machine so each machine gets one row in the output.
