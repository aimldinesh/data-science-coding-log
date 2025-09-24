# 🧲 Problem: Movie Rating

- **Platform**: [LeetCode](https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/movie-rating/submissions/1780921629/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/movie-rating/submissions/1780921629/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-24
- **Tags**: MySQL, Database
- **Difficulty**: Medium

---

## 📌 Problem Statement
We have three tables:

### Movies
| Column Name | Type    |
|-------------|---------|
| movie_id    | int     |
| title       | varchar |

### Users
| Column Name | Type    |
|-------------|---------|
| user_id     | int     |
| name        | varchar |

### MovieRating
| Column Name | Type    |
|-------------|---------|
| movie_id    | int     |
| user_id     | int     |
| rating      | int     |
| created_at  | date    |

- `movie_id` and `user_id` together form the primary key in `MovieRating`.  
- Each row records a rating given by a user for a movie.  

**Task:**
1. Find the name of the user who rated the greatest number of movies.  
   - In case of tie → return lexicographically smaller name.  
2. Find the movie title with the **highest average rating in February 2020**.  
   - In case of tie → return lexicographically smaller title.  

Return results in **two rows**:  
- First row = user’s name  
- Second row = movie title  

---

## 🚀 Approach
1. **Find user with max ratings:**
   - Count how many ratings each user has given (`COUNT(*)` grouped by `user_id`).  
   - Join with `Users` table to get user names.  
   - Sort by `COUNT DESC, name ASC` and take the top one.

2. **Find movie with max average rating in Feb 2020:**
   - Filter `MovieRating` for dates between `'2020-02-01'` and `'2020-02-29'`.  
   - Compute average rating per movie.  
   - Join with `Movies` table to get movie titles.  
   - Sort by `AVG(rating) DESC, title ASC` and take the top one.

3. **Union the results** (user + movie) into one column `results`.

---

## 💻 SQL Query
```sql
(
    SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(mr.movie_id) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title AS results
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);
```

---

## 🔎 Query Explanation

- First part:
  - COUNT(mr.movie_id) → how many ratings each user gave.
  - ORDER BY COUNT DESC, name ASC → ensures we pick the top rater (tie broken by name).

- Second part:
  - Filter February ratings.
  - AVG(mr.rating) → average per movie.
  - ORDER BY AVG DESC, title ASC → ensures we pick the top movie (tie broken by title).

- UNION ALL → Combines both results into one column, exactly as required.
