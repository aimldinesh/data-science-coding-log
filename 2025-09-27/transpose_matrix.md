# 🧲 Problem: Transpose Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/transpose-matrix/description/)
- **Submission**: [https://leetcode.com/problems/transpose-matrix/submissions/](https://leetcode.com/problems/transpose-matrix/submissions/)
- **Date Solved**: 2025-09-27
- **Tags**: DSA, Math, Matrix
- **Difficulty**: Easy

---

## 📌 Problem Statement
Given a 2D integer matrix, return the **transpose** of the matrix.  
The transpose of a matrix is obtained by swapping rows with columns.

Formally:
- If the input matrix has dimensions `m x n`,  
- The transpose will have dimensions `n x m`,  
- Each element `matrix[r][c]` becomes `res[c][r]`.

---
# ✅ Example usage:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Output: [[1, 4],
           [2, 5],
           [3, 6]]

Example 2:
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

Output: [[1,4,7],
         [2,5,8],
         [3,6,9]]
```
---

## 💡 Approach
1. Find the number of rows (`ROWS`) and columns (`COLS`) of the input matrix.
2. Initialize an empty result matrix `res` of size `COLS x ROWS`, filled with zeros.
3. Iterate over every cell `(r, c)` in the input:
   - Assign `res[c][r] = matrix[r][c]`.
4. Return the result matrix.

This approach builds a **new transposed matrix** rather than modifying in place.

---

## 💻 Code (Python)

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Step 1: Get the number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 2: Initialize result matrix with dimensions COLS x ROWS
        res = [[0] * ROWS for _ in range(COLS)]

        # Step 3: Fill the result by swapping row and column indices
        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]

        # Step 4: Return the transposed matrix
        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(ROWS × COLS)
    - Each element is visited exactly once.
- **Space**: O(ROWS × COLS)
    - New matrix is created to store the transpose.
