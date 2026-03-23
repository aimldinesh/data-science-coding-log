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

## Step-by-Step Execution

Input Matrix:
```python
1  2  3
4  5  6
7  8  9
```
```python
left=0, right=3, top=0, bottom=3
res=[]
```
🔁 Iteration 1
Pass 1 → Left to Right range(0, 3) → row top=0
```python
matrix[0][0]=1, matrix[0][1]=2, matrix[0][2]=3
res = [1, 2, 3]
top += 1  →  top=1
```
Pass 2 ↓ Top to Bottom range(1, 3) → col right-1=2
```python
matrix[1][2]=6, matrix[2][2]=9
res = [1, 2, 3, 6, 9]
right -= 1  →  right=2
````
🔍 Boundary Check: left(0) < right(2) and top(1) < bottom(3) → ✅ continue

Pass 3 ← Right to Left range(1, -1, -1) → row bottom-1=2
```python
matrix[2][1]=8, matrix[2][0]=7
res = [1, 2, 3, 6, 9, 8, 7]
bottom -= 1  →  bottom=2
```
Pass 4 ↑ Bottom to Top range(1, 0, -1) → col left=0
```python
matrix[1][0]=4
res = [1, 2, 3, 6, 9, 8, 7, 4]
left += 1  →  left=1
```
State after iteration 1:
```python
left=1, right=2, top=1, bottom=2
res = [1, 2, 3, 6, 9, 8, 7, 4]
```
🔁 Iteration 2

Pass 1 → Left to Right range(1, 2) → row top=1
```python
matrix[1][1]=5
res = [1, 2, 3, 6, 9, 8, 7, 4, 5]
top += 1  →  top=2
```

Pass 2 ↓ Top to Bottom range(2, 2) → empty range, nothing added
```python
right -= 1  →  right=1
```
🔍 Boundary Check: left(1) < right(1) → ❌ BREAK

✅ Final Result
```python
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```
---

📊 Element-by-Element Trace Table
```python
Step     Direction         Index      Value         res
1        →                 [0][0]      1            [1]
2        →                 [0][1]      2            [1,2]
3        →                 [0][2]      3            [1,2,3]
4        ↓                 [1][2]      6            [1,2,3,6]
5        ↓                 [2][2]      9            [1,2,3,6,9]
6        ←                 [2][1]      8            [1,2,3,6,9,8]
7        ←                 [2][0]      7            [1,2,3,6,9,8,7]
8        ↑                 [1][0]      4            [1,2,3,6,9,8,7,4]
9        →                 [1][1]      5            [1,2,3,6,9,8,7,4,5]
```
---

## 💡 Time and Space Complexity
- **Time**: O(m * n)
    - Every element is visited once.
- **Space**: O(1)
    - Result list doesn't count as extra space in complexity analysis.
