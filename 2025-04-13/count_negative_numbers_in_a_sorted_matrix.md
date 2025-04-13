# 🧮 Problem: Count Negative Numbers in a Sorted Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
- **Submission**: [https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/1605339028/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/1605339028/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Given a `m x n` matrix `grid` of integers where each row is sorted in non-increasing order, count the total number of negative numbers in the matrix.


---

## 🚀 My Approach
- Since each row is sorted in **non-increasing** order, we can use **binary search** to find the **first negative number** in each row.
- Once we have the index of the first negative number, all elements to the right of it will also be negative.
- The number of negatives in that row = `len(row) - index`.
- Add this for all rows to get the final count.

---

## 💻 Code (Python)

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        # Helper function to find index of first negative number in a row using binary search
        def first_negative_index(row):
            left, right = 0, len(row) - 1

            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    # If mid element is negative, look to the left for earlier negative
                    right = mid - 1
                else:
                    # If mid element is non-negative, search in the right half
                    left = mid + 1

            # 'left' is now the index of the first negative number
            return left

        count = 0
        for row in grid:
            # Get the index of the first negative number in this row
            index = first_negative_index(row)

            # All elements from 'index' to end of row are negative
            count += len(row) - index

        return count
```

---

## 💡 Time and Space Complexity
- **Time**: O(m * log n), where m is number of rows, n is number of columns
- **Space**: O(1), No extra space used apart from variables.
