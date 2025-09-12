# 🧲 Problem: Invalid Tweets

- **Platform**: [LeetCode](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/invalid-tweets/submissions/1767898487/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/invalid-tweets/submissions/1767898487/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-12
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

### 📄 Problem Statement  
Table: `Tweets`  

| Column Name | Type    |
|-------------|---------|
| tweet_id    | int     |
| content     | varchar |

- `tweet_id` is the primary key for this table.  
- Each row contains the ID of a tweet and the content of the tweet.  

**Task:**  
A tweet is considered **invalid** if the number of characters in `content` is **strictly greater than 15**.  
Write an SQL query to find the `tweet_id` of invalid tweets.  

---

### 📝 Approach  
- Use the `LENGTH()` function to count characters in `content`.  
- Filter rows where `LENGTH(content) > 15`.  
- Select only `tweet_id`.  

---

### 💻 Query  
```sql
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```
---

## 🔍 Explanation

- LENGTH(content) → counts the number of characters in each tweet.
- WHERE LENGTH(content) > 15 → keeps only invalid tweets.
- SELECT tweet_id → outputs the IDs of invalid tweets.

✅ Simple filtering with LENGTH() function.
