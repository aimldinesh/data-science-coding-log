# 🧲 Problem: Spiral Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/spiral-matrix/submissions/1623669109/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/spiral-matrix/submissions/1623669109/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-05-02
- **Tags**: Matrix, Math, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

---

## 🧪 Example

```python
Input:
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

```
---

## 🚀 My Approach
- Use four pointers to represent the current bounds:
   - top, bottom for row boundaries
   - left, right for column boundaries
- Traverse:
   - From left to right along the top row
   - From top to bottom along the right column
   - From right to left along the bottom row
   - From bottom to top along the left column
- After each traversal, shrink the boundaries inward.
- Repeat until the bounds cro

---

## 💻 Code (Python)

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []  # Initialize the result list

        # Define the boundaries
        left, right = 0, len(matrix[0])  # Columns
        top, bottom = 0, len(matrix)     # Rows

        while left < right and top < bottom:
            # Traverse from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check boundaries before next direction
            if not (left < right and top < bottom):
                break

            # Traverse from right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

```
---

## 💡 Time and Space Complexity
- **Time**: O(m * n)
    - Every element is visited once.
- **Space**: O(1)
    - Result list doesn't count as extra space in complexity analysis.
