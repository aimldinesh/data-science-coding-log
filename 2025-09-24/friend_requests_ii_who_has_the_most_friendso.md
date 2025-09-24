# 🧲 Problem: Friend Requests II Who Has the Most Friendso

- **Platform**: [LeetCode](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database, CTE, Subquries
- **Difficulty**: Medium

---

## 📌 Problem Statement
We have one table:

### RequestAccepted
| Column Name  | Type |  
|--------------|------|  
| requester_id | int  |  
| accepter_id  | int  |  
| accept_date  | date |  

- `(requester_id, accepter_id)` is the **primary key**.  
- Each row represents a friendship acceptance between two users on a specific date.  
- Friendships are **bidirectional** (if A is a friend of B, then B is also a friend of A).  

**Task:**  
Find the person who has the most friends and the number of friends they have.  
- Only one person will have the maximum.  

---

## 🚀 Approach
1. **Expand bidirectional friendships**  
   - Use `UNION ALL` so that `(requester_id, accepter_id)` and `(accepter_id, requester_id)` are both included.  

2. **Count friends per user**  
   - Use `COUNT(DISTINCT friend_id)` grouped by user.  

3. **Get max friends**  
   - Sort by number of friends (`DESC`) and take the top 1.  

---

## 💻 SQL Query
```sql
WITH AllFriends AS (
    SELECT requester_id AS id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend_id
    FROM RequestAccepted
)
SELECT id, COUNT(DISTINCT friend_id) AS num
FROM AllFriends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```
---

## 🔎 Query Explanation

- CTE (AllFriends):
  - Expands each friendship into two rows so we treat it as bidirectional.

- COUNT(DISTINCT friend_id):
  - Ensures each friend is counted only once per user.

- ORDER BY num DESC LIMIT 1:
  - Returns the user with the most friends and their count.
