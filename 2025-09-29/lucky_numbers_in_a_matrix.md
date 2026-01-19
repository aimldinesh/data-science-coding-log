# 🧲 Problem: Lucky Numbers in a Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/)
- **Submission**: [https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/1786269909/](https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/1786269909/)
- **Date Solved**: 2025-09-29
- **Tags**: DSA, Math, Matrix
- **Difficulty**: Easy

---

## ✅ Problem Statement
Given an `m x n` matrix of distinct numbers, return all **lucky numbers**.

A **lucky number** is an element of the matrix that is:
- The **minimum** element in its row, and
- The **maximum** element in its column.

---

## 🔹 Examples

**Example 1:** 
```text 
Input:

matrix = [[3,7,8],
          [9,11,13],
          [15,16,17]]

Output: [15]  

Explanation:  
- Row minimums: [3, 9, 15]  
- Column maximums: [15, 16, 17]  
- Intersection = [15]
``` 
---
**Example 2:** 
```text 
Input: 
matrix = [[1,10,4,2],
          [9,3,8,7],
          [15,16,17,12]] 

Output: [12]  
```
---
**Example 3:** 
```text 
Input: 
matrix = [[7,8],
          [1,2]] 

Output: [7] 
```
---
## 🔹 Approach

1. Compute the **minimum value of each row**.  
2. Compute the **maximum value of each column**.  
3. The lucky numbers are the **intersection** of these two sets.  

---

## 🔹 Code (Python)

```python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find minimum of each row
        row_mins = {min(row) for row in matrix}
        
        # Step 2: Find maximum of each column (transpose with zip)
        col_maxs = {max(col) for col in zip(*matrix)}
        
        # Step 3: Intersection → lucky numbers
        return list(row_mins & col_maxs)

```
---

## 💡 Time and Space Complexity
- **Time**: 
    - Finding row minimums = O(m * n)
    - Finding column maximums = O(m * n)
    - Overall = O(m * n)

- **Space**:
    - Storing row mins + col maxs = O(m + n)
