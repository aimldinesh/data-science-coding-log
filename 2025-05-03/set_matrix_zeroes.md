# 🧲 Problem: Set Matrix Zeroes

- **Platform**: [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/set-matrix-zeroes/submissions/1624157679/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/set-matrix-zeroes/submissions/1624157679/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-05-03
- **Tags**: Matrix, Simulation, In-Place
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an `m x n` integer matrix, if an element is 0, set its entire row and column to 0.You must do it **in-place**.
---

## 🧪 Example

```python
Input:
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

## 🚀 Approach
- Use the first row and first column as markers to track rows and columns that need to be zeroed.
- First, check if the first row or first column contains a 0 and store that info in flags.
- Then iterate through the matrix and for every cell that is 0, mark the first cell of that row and column as 0.
- Iterate through the rest of the matrix again and set any cell to 0 if its row or column is marked.
- Finally, use the stored flags to zero out the first row and/or first column, if necessary.

---

## 💻 Code (Python)

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Check if the first row and first column have any zeros
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

        # Use the first row and column as markers to mark zeroes
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Set matrix[i][j] to 0 if the corresponding row or column is marked
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

```

---

## 💡 Time and Space Complexity
- **Time**: O(m * n)
  - Full traversal of matrix for marking and updating.
- **Space**: O(1)
  - Done in-place with only a couple of boolean flags for the first row/column.
