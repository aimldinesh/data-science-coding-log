# 🧲 Problem: Search a 2D Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/description/)
- **Submission**: [https://leetcode.com/problems/search-a-2d-matrix/submissions/1656509637/](https://leetcode.com/problems/search-a-2d-matrix/submissions/1656509637/)
- **Date Solved**: 2025-06-07
- **Tags**: Binary Search, Matrix
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given an m x n integer matrix with the following properties:
     - Each row is sorted in ascending order.
     - The first integer of each row is greater than the last integer of the previous row.
- Task: Write a function to determine if a given target value exists in the matrix.

### 🌰 Example
```python
Example 1:
Input: 
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3

Output: True

Example 2:
Input: 
matrix = [[1]]
target = 2

Output: False
```
---

## 🚀 Approach : 2-Level Binary Search
💡 Intuition
- The matrix can be visualized as a flattened sorted array.
- First, identify which row the target could be in using binary search on rows.
- Then perform binary search within that row to check if the target exists.

🚀 Approach: 2-Level Binary Search
- Binary Search over Rows:
     - Each row is sorted and non-overlapping.
     - Use binary search to find the row where target lies between the first and last element.

- Binary Search in Identified Row:
     - Perform binary search in the selected row to find the target
---

## 💻 Code (Python)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 1: Binary search to find the correct row
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # If target is greater than the last element of the row,
            # it must be in a lower row
            if target > matrix[row][-1]:
                top = row + 1
            # If target is less than the first element of the row,
            # it must be in an upper row
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break  # Target must be within this row
        
        # If the correct row was not found
        if not (top <= bottom):
            return False
        
        # Step 2: Binary search within the identified row
        row = (top + bottom) // 2
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            # Move right if target is greater
            if target > matrix[row][mid]:
                left = mid + 1
            # Move left if target is smaller
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True  # Found the target

        return False  # Target not found
```

---

## 💡 Time and Space Complexity
- **Time**: O(log m + log n)
    - Binary search over rows + binary search over columns
- **Space**: O(1)
    - No extra space used beyond a few pointers
