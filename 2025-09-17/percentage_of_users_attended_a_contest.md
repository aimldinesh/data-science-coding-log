# 🧲 Problem: Percentage of Users Attended a Contest

- **Platform**: [LeetCode](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/percentage-of-users-attended-a-contest/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/percentage-of-users-attended-a-contest/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📝 Problem Statement  
Write an SQL query to find the **percentage of users registered in each contest**, rounded to **two decimal places**.  

- Return the result table ordered by `percentage` in descending order.  
- If two contests have the same percentage, order them by `contest_id` in ascending order.  

### Table: Users  
| Column Name | Type    |  
|-------------|---------|  
| user_id     | int     |  
| user_name   | varchar |  

- `user_id` is the primary key.  

### Table: Register  
| Column Name | Type    |  
|-------------|---------|  
| contest_id  | int     |  
| user_id     | int     |  

- `(contest_id, user_id)` is the primary key.  

---

## ✅ Example Input  

**Users Table:**  
| user_id | user_name |  
|---------|-----------|  
| 6       | Alice     |  
| 2       | Bob       |  
| 7       | Alex      |  

**Register Table:**  
| contest_id | user_id |  
|------------|---------|  
| 215        | 6       |  
| 209        | 2       |  
| 208        | 2       |  
| 208        | 6       |  
| 209        | 7       |  
| 215        | 7       |  
| 208        | 7       |  

---

## 🎯 Expected Output  

| contest_id | percentage |  
|------------|------------|  
| 208        | 100.00     |  
| 215        | 66.67      |  
| 209        | 66.67      |  

---

## 🛠️ Approach  

1. First, count how many users registered in each contest (`COUNT(user_id)`).  
2. Get the **total number of users** from the `Users` table.  
3. Compute the percentage for each contest as:  
   - percentage = (number of users in contest / total users) * 100

4. Round the result to **two decimal places**.  
5. Sort the result by `percentage DESC`, and then by `contest_id ASC`.  

---

## 💡 SQL Query  

```sql
SELECT 
 r.contest_id,
 ROUND(COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM 
 Register r
GROUP BY 
 r.contest_id
ORDER BY 
 percentage DESC, r.contest_id ASC;
```
---

### 🔎 Query Explanation

- COUNT(r.user_id) → Counts the number of users who registered in a given contest.
- (SELECT COUNT(*) FROM Users) → Gets the total number of users in the system.
- ROUND(..., 2) → Rounds the percentage to two decimal places.
- GROUP BY r.contest_id → Ensures we calculate the percentage per contest.
- ORDER BY percentage DESC, contest_id ASC → Sorts contests by highest participation first, then by contest ID.
