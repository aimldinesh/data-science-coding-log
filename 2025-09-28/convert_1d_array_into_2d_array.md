# 🧲 Problem: Convert 1D Array Into 2D Array

- **Platform**: [LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/description/)
- **Submission**: [https://leetcode.com/problems/convert-1d-array-into-2d-array/submissions/1785033316/](https://leetcode.com/problems/convert-1d-array-into-2d-array/submissions/1785033316/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math, Matrix
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given a **1D integer array** `original` and two integers `m` and `n`.  

Construct and return a **2D array** with `m` rows and `n` columns using all elements from `original` in **row-major order**.  

- If it is **impossible** to construct such a 2D array, return an **empty 2D array** `[]`.

---

## 🔹 Examples
```text
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
Example 2:

Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.
Example 3:

Input: original = [1,2], m = 1, n = 1
Output: []
Explanation: There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.



## 🚀 My Approach
- Check feasibility
  - The total number of elements len(original) must equal m * n.
  - If not, return [].

- Construct 2D array
  - Iterate m times (for each row).
  - Slice n elements from original for each row.
  - Append each row to the result list.

- Return the constructed 2D array.

---

## 💻 Code (Python)

```python
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to construct the 2D array
        if len(original) != m * n:
            return []

        res = []

        # Construct each row
        for r in range(m):
            start = r * n             # Start index of the current row
            end = start + n           # End index of the current row
            res.append(original[start:end])  # Slice the elements for this row

        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(m⋅n)
    - Each element is visited once during slicing.
- **Space**: O(m⋅n)
    - The result 2D array stores all elements.
