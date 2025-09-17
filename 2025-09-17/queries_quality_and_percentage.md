# 🧲 Problem: Queries Quality and Percentage

- **Platform**: [LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/queries-quality-and-percentage/submissions/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/queries-quality-and-percentage/submissions/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-17
- **Tags**: MySQL, Database
- **Difficulty**: Easy

---

## 📝 Problem Statement  
Write an SQL query to find each **query_name**'s:  
1. **Quality**: The average of `rating / position` for all its records, rounded to **two decimal places**.  
2. **Poor query percentage**: The percentage of queries with `rating < 3`, rounded to **two decimal places**.  

- Return the result table ordered by `quality` in descending order.  
- If two queries have the same quality, order them by `query_name` in ascending order.  

### Table: Queries  
| Column Name | Type    |  
|-------------|---------|  
| query_name  | varchar |  
| result      | varchar |  
| position    | int     |  
| rating      | int     |  

- `(query_name, result)` is the primary key.  
- `rating` is an integer between 1 and 5.  
- `position` is an integer between 1 and 500.  

---

## ✅ Example Input  

**Queries Table:**  
| query_name | result    | position | rating |  
|------------|-----------|----------|--------|  
| Dog        | Golden    | 1        | 5      |  
| Dog        | Retriever | 2        | 5      |  
| Dog        | Canine    | 3        | 4      |  
| Cat        | Kitten    | 1        | 4      |  
| Cat        | Meow      | 2        | 2      |  
| Cat        | Feline    | 3        | 3      |  

---

## 🎯 Expected Output  

| query_name | quality | poor_query_percentage |  
|------------|---------|------------------------|  
| Dog        | 2.50    | 0.00                   |  
| Cat        | 1.50    | 33.33                  |  

---

## 🛠️ Approach  

1. **Quality Calculation**:  
   - For each query, calculate `(rating / position)` and take the average across all rows.  
   - Use `AVG(rating * 1.0 / position)` for precision.  
   - Round to **two decimal places**.  

2. **Poor Query Percentage**:  
   - Count how many queries have `rating < 3` for each `query_name`.  
   - Divide it by the total number of queries for that `query_name`.  
   - Multiply by 100 to get the percentage.  
   - Round to **two decimal places**.  

3. **Sorting**:  
   - Order by `quality DESC`.  
   - If tied, order by `query_name ASC`.  

---

## 💡 SQL Query  

```sql
SELECT 
    query_name,
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM 
    Queries
GROUP BY 
    query_name
ORDER BY 
    quality DESC, query_name ASC;
```

---

## 🔎 Query Explanation

- AVG(rating * 1.0 / position) → Calculates the quality score by averaging (rating / position).
- SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) → Counts poor queries (rating < 3).
- COUNT(*) → Total queries per query_name.
- ROUND(..., 2) → Ensures both quality and percentage are rounded to 2 decimal places.
- GROUP BY query_name → Aggregates results per query.
- ORDER BY quality DESC, query_name ASC → Sorts by quality first, then alphabetically.

This query returns each query_name with its quality and poor query percentage.
