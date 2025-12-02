# 🧮 Problem: Search a 2D Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/search-a-2d-matrix/submissions/1608303300/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/search-a-2d-matrix/submissions/1608303300/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Write an efficient algorithm to search for a value in a 2D matrix. This matrix has the following properties:
  - Integers in each row are sorted from left to right.
  - The first integer of each row is greater than the last integer of the previous row.

---
## Examples
```python
Example1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```
---

## 🚀 My Approach: Binary Search in Two Phases
- Binary search to find the correct row where the target could exist (based on first and last elements of each row).
- Binary search within that row to find the actual target.

---

## 💻 Code (Python)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # Binary search to find the correct row
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break  # Target is within the range of this row
        
        if not (top <= bottom):
            return False  # Target not in any valid row
        
        # Binary search within the identified row
        row = (top + bottom) // 2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False

```

---

## 💡 Time and Space Complexity
- **Time**: O(log m + log n), where, m = number of rows, n = number of columns
- **Space**: O(1)
