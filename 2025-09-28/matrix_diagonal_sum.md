# 🧲 Problem: Matrix Diagonal Sum

- **Platform**: [LeetCode](https://leetcode.com/problems/matrix-diagonal-sum/description/)
- **Submission**: [https://leetcode.com/problems/matrix-diagonal-sum/submissions/1784921610/](https://leetcode.com/problems/matrix-diagonal-sum/submissions/1784921610/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math, Matrix
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given a **square matrix** `mat` of size `n x n`.  
Return the sum of the matrix's **primary diagonal** and **secondary diagonal**.  

If `n` is odd, subtract the value at the center of the matrix (to avoid counting it twice).  

---

## 🔹 Example  

**Input**:  
```text

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
```
---
## 🔹 Approach  

1. Iterate through each row `r` of the matrix.  
2. Add:
   - `mat[r][r]` → element from **primary diagonal**  
   - `mat[r][n - r - 1]` → element from **secondary diagonal**  
3. If `n` is odd, subtract the middle element once (since it was counted twice).  

---

## 🔹 Python Code  

```python
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)

        for r in range(n):
            # Add primary diagonal element
            res += mat[r][r]
            # Add secondary diagonal element
            res += mat[r][n - r - 1]

        # Subtract center element if n is odd (to avoid double counting)
        return res - (mat[n // 2][n // 2] if n & 1 else 0)

```
---
### Step by step execution with example
```
Example:
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Goal: Find the sum of both diagonals.
```
Step-by-Step Execution:

1. Initialization:
```python
res, n = 0, len(mat)
# res = 0 (to store the sum)
# n = 3 (size of the matrix)
```
2.Loop through each row:
```python
for r in range(n):

→ Iterates from r = 0 to 2.
```

```python
➤ r = 1

Primary diagonal: mat[1][1] = 5

Secondary diagonal: mat[1][n-1-1] = mat[1][1] = 5

Both diagonals overlap (center element).

Add both: res += 5 + 5 = 10
(so far res = 4 + 10 = 14)


➤ r = 2

Primary diagonal: mat[2][2] = 9

Secondary diagonal: mat[2][0] = 7

Add both: res += 9 + 7 = 16
(total res = 14 + 16 = 30)

```

3. Avoid double counting center element
   + The center element mat[1][1] = 5 was counted twice (once in each diagonal).
   + Since n is odd (3), subtract it once:
```python
res - mat[n // 2][n // 2]
= 30 - mat[1][1]
= 30 - 5
= 25

```
✅ Final Answer: 25

---

## 💡 Time and Space Complexity
- **Time**: O(n) → we iterate once through all rows.
- **Space**: O(1) → no extra space used (just variables).
