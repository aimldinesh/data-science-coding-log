# 🧲 Problem: User Activity for the Past 30 Days I

- **Platform**: [LeetCode](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/user-activity-for-the-past-30-days-i/submissions/1774565093/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/submissions/1774565093/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-18
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## Problem Statement
Table: **Activity**

| Column Name   | Type    |
|---------------|---------|
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |

- This table may contain duplicate rows.  
- `activity_type` is one of: **('open_session', 'end_session', 'scroll_down', 'send_message')**.  
- Each row records a user activity in a given session and date.  
- Each session belongs to exactly one user.  

Write a solution to find the **daily active user count** for the 30-day period ending **2019-07-27** (inclusive).  
- A user is considered active on a day if they made **at least one activity** on that day.  
- Return the result table in any order.  
- Ignore days with zero active users.

---

## Example

**Input**

Activity table:  

| user_id | session_id | activity_date | activity_type |
|---------|------------|---------------|---------------|
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |

**Output**

| day        | active_users |
|------------|--------------|
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |

**Explanation**

- On **2019-07-20** → users {1, 2} were active → 2 users.  
- On **2019-07-21** → users {2, 3} were active → 2 users.  
- The date **2019-06-25** is outside the 30-day window, so it is ignored.  

---

## Approach
1. Restrict results to the **30-day window** between `'2019-06-28'` and `'2019-07-27'`.  
   - Use `WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'`.  
2. Count **distinct users per date** with `COUNT(DISTINCT user_id)`.  
   - Prevents counting multiple activities from the same user on the same day.  
3. Group by `activity_date` to aggregate counts by day.  
4. Rename `activity_date` column to `day` to match expected output.

---

## SQL Query

```sql
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) 
                        AND '2019-07-27'
GROUP BY activity_date;
```
---

## Query Explanation

- DATE_SUB('2019-07-27', INTERVAL 29 DAY) → gets start date of 30-day window (2019-06-28).
- WHERE activity_date BETWEEN ... → filters activities to only this period.
- COUNT(DISTINCT user_id) → ensures each user is counted once per day, even if multiple actions.
- GROUP BY activity_date → computes per-day active user counts.
- Final output shows day and number of active_users.
✅ Correctly returns daily active users in the last 30 days.