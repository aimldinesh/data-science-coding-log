# 🧲 Problem: Game Play Analysis IV

- **Platform**: [LeetCode](https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/game-play-analysis-iv/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/game-play-analysis-iv/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## Problem Statement
Table: **Activity**

| Column Name | Type    |
|-------------|---------|
| player_id   | int     |
| device_id   | int     |
| event_date  | date    |
| games_played| int     |

- `(player_id, event_date)` is the primary key.
- For each player, find whether they logged in **the day after their first login**.
- Return the fraction of players who did, rounded to 2 decimal places, column name `fraction`.

---

## Approach
1. For each player find their **first login date** (`MIN(event_date)`).  
2. For each player check whether there exists a record for `first_login + 1 day`.  
3. Compute the fraction as `(#players_with_next_day_login) / (total_players)`.  
4. Round to 2 decimal places.

---

## Correct SQL Query

```sql
SELECT
  ROUND(
    AVG(
      CASE
        WHEN EXISTS (
          SELECT 1
          FROM Activity a2
          WHERE a2.player_id = f.player_id
            AND a2.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY)
        ) THEN 1 ELSE 0 END
    ), 2
  ) AS fraction
FROM (
  SELECT player_id, MIN(event_date) AS first_login
  FROM Activity
  GROUP BY player_id
) f;

```

---

## Query Explanation

- The inner subquery f finds the first login date per player_id.
- For each f.player_id we use a correlated EXISTS(...) to check if that player has any record with event_date = first_login + 1 day.
- CASE WHEN EXISTS(...) THEN 1 ELSE 0 END yields 1 (next-day login) or 0 (no next-day login) per player.
- AVG(...) over these 0/1 values gives the fraction of players who logged in the next day.
- ROUND(..., 2) formats the result to 2 decimal places.
