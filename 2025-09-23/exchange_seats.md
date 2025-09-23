# 🧲 Problem: Exchange Seats

- **Platform**: [LeetCode](https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/exchange-seats/submissions/1780227669/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/exchange-seats/submissions/1780227669/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-23
- **Tags**: MySQL, Database, Subquries
- **Difficulty**: Medium

---

## 📌 Problem Statement
We are given a `Seat` table:

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| student     | varchar |

- `id` is the primary key and starts from 1, incrementing continuously.  
- Each row represents the student assigned to a seat.  

**Task:** Swap the seat `id` of every two consecutive students.  
- If the number of students is odd, the last student remains unchanged.  
- Return the table ordered by `id`.

---

## 🚀 Approach
1. We need to **swap students in pairs**:
   - Student at **odd id** should take the seat of the **next (id+1)**.
   - Student at **even id** should take the seat of the **previous (id-1)**.
   - If the last row is odd and has no partner → keep as is.
2. Use a `CASE` expression to remap the `id` for each student:
   - If `id` is odd **and not the last row** → new id = `id + 1`.
   - If `id` is even → new id = `id - 1`.
   - If last student is odd → keep same `id`.
3. Order results by `id` to preserve final sequence.

---

## 💻 SQL Query

```sql
SELECT
    CASE
        WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM Seat)
            THEN id + 1
        WHEN id % 2 = 0
            THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;
```

---

## 🔎 Query Explanation

- id % 2 = 1 AND id != (SELECT MAX(id) FROM Seat) → For odd ids (except the last one if odd), assign them the next id.
- id % 2 = 0 → For even ids, assign them the previous id.
- ELSE id → Keeps the last student unchanged if total students count is odd.
- Final ORDER BY id ensures ascending order of seat IDs.
