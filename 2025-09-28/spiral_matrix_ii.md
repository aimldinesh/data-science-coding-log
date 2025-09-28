# 🧲 Problem: Spiral Matrix II

- **Platform**: [LeetCode](https://leetcode.com/problems/spiral-matrix-ii/description/)
- **Submission**: [https://leetcode.com/problems/spiral-matrix-ii/submissions/](https://leetcode.com/problems/spiral-matrix-ii/submissions/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math, Matrix, Two Pointer
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given a positive integer `n`, generate an `n x n` matrix filled with elements from `1` to `n²` in **spiral order**.

---

## 🔹 Examples
```text
**Example 1:**  
Input: `n = 3`  
Output: 

[[1, 2, 3],
[8, 9, 4],
[7, 6, 5]]

**Example 2:**  
Input: `n = 1`  
Output:

[[1]]
```
---

## 🔹 Approach

We simulate the process of filling the matrix in spiral order:

1. Initialize 4 boundaries: `left, right, top, bottom`.  
2. Use a variable `val = 1` to track the current number.  
3. Fill in **four steps** repeatedly until the boundaries meet:
   - Fill **top row** left → right  
   - Fill **right column** top → bottom  
   - Fill **bottom row** right → left  
   - Fill **left column** bottom → top  
4. After each step, adjust the respective boundary (`top++, right--, bottom--, left++`).  
5. Continue until `val > n²`.


---

## 💻 Code (Python)

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize n x n matrix with 0s
        mat = [[0] * n for _ in range(n)]
        
        # Boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        # Start filling numbers from 1 to n^2
        val = 1

        while left <= right and top <= bottom:
            # 1. Fill top row
            for c in range(left, right + 1):
                mat[top][c] = val
                val += 1
            top += 1

            # 2. Fill right column
            for r in range(top, bottom + 1):
                mat[r][right] = val
                val += 1
            right -= 1

            # 3. Fill bottom row (if still valid)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    mat[bottom][c] = val
                    val += 1
                bottom -= 1

            # 4. Fill left column (if still valid)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    mat[r][left] = val
                    val += 1
                left += 1

        return mat

```

---

## 💡 Time and Space Complexity
- **Time**: O(n2)
    - We fill every cell exactly once.
- **Space**: O(1) (ignoring output matrix).
    - Only a few pointers are used.
