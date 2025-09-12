# 🧲 Problem: Article Views I

- **Platform**: [LeetCode](https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/article-views-i/submissions/1767890749/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/article-views-i/submissions/1767890749/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-12
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## ✅ Problem Statement
Table: `Views`  

| Column Name | Type    |
|-------------|---------|
| article_id  | int     |
| author_id   | int     |
| viewer_id   | int     |
| view_date   | date    |

- `(article_id, viewer_id, view_date)` is the primary key.  
- Each row of this table shows that a viewer viewed an article written by a certain author on a specific date.  

**Task:**  
Write an SQL query to find all the authors who **viewed at least one of their own articles**.  
Return the result table containing only `author_id`, sorted in **ascending order**.  

---

### 📝 Approach  
- A self-view happens when `author_id = viewer_id`.  
- Use a `WHERE` condition to filter such rows.  
- Use `DISTINCT` to avoid duplicates.  
- Use alias `AS id` to match required output column name.  
- Finally, `ORDER BY id ASC`.  

---

### 💻 Query  
```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
```

---

## 🔍 Explanation

- WHERE author_id = viewer_id → selects rows where authors view their own articles.
- DISTINCT → avoids duplicate author entries.
- AS id → renames the output column to match requirements.
- ORDER BY id ASC → sorts authors in ascending order.
