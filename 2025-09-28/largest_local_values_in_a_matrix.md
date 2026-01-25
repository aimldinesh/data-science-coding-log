# 🧲 Problem: Largest Local Values in a Matrix

- **Platform**: [LeetCode](https://leetcode.com/problems/largest-local-values-in-a-matrix/description/)
- **Submission**: [https://leetcode.com/problems/largest-local-values-in-a-matrix/submissions/1785010909/](https://leetcode.com/problems/largest-local-values-in-a-matrix/submissions/1785010909/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math, Matrix
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given an `n x n` integer matrix `grid`.  

Return a matrix `res` of size `(n-2) x (n-2)` where each element `res[i][j]` is the **largest value** in the `3 x 3` submatrix of `grid` starting at position `(i, j)`.

Formally:  
\[
res[i][j] = \max \{ grid[r][c] \mid i \le r < i+3, j \le c < j+3 \}
\]

---

## 🔹 Example

**Example 1:**  

Input:  
```python
grid = [
  [9, 9, 8, 1],
  [5, 6, 2, 6],
  [8, 2, 6, 4],
  [6, 2, 2, 2]
]

Output:
[
  [9, 9],
  [8, 6]
]

```
---
### Explanation:

- The top-left 3x3 submatrix max: [[9,9,8],[5,6,2],[8,2,6]] → 9
- Top-right 3x3 submatrix max: [[9,8,1],[6,2,6],[2,6,4]] → 9
- Bottom-left 3x3 submatrix max: [[5,6,2],[8,2,6],[6,2,2]] → 8
- Bottom-right 3x3 submatrix max: [[6,2,6],[2,6,4],[2,2,2]] → 6

---

## 🔹 Approach

- Create a result matrix of size (N-2) x (N-2).
- Loop through each possible top-left position (i, j) of a 3x3 submatrix.
- For each 3x3 submatrix, find the maximum value by iterating through its 9 elements.
- Store the maximum in res[i][j].
- Return the res matrix.

## 💻 Code (Python)

```python
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        # Initialize result matrix of size (N-2) x (N-2) with zeros
        res = [[0] * (N - 2) for _ in range(N - 2)]

        # Iterate over all possible top-left positions of 3x3 submatrices
        for i in range(N - 2):
            for j in range(N - 2):
                # Check all elements inside the current 3x3 submatrix
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        # Update res[i][j] with the maximum value found
                        res[i][j] = max(res[i][j], grid[r][c])

        # Return the final result matrix
        return res

```

---
## Step by Step Code execution with example

Example input (we'll trace this)
```python
grid = [
  [9, 9, 8, 1],
  [5, 6, 2, 6],
  [8, 2, 6, 4],
  [6, 2, 2, 2]
]
```
- N = 4
- Output size = (N-2) x (N-2) = 2 x 2
- Initial res:
```python
res = [
  [0, 0],
  [0, 0]
]

```
We will iterate i = 0..1, j = 0..1. For each (i,j) we inspect the 3×3 window with top-left at (i,j).

#### Trace — detailed iteration

1) i = 0, j = 0
   - 3×3 window covers rows 0..2 and cols 0..2:
```python
[9, 9, 8]
[5, 6, 2]
[8, 2, 6]
```
We iterate r = 0..2, c = 0..2 and keep res[0][0] = max(...)

Step-by-step updates for res[0][0] (starting 0):
```python
compare with grid[0][0] = 9 → res[0][0] = max(0,9) = 9

grid[0][1] = 9 → res[0][0] = max(9,9) = 9

grid[0][2] = 8 → res[0][0] = max(9,8) = 9

grid[1][0] = 5 → res[0][0] = max(9,5) = 9

grid[1][1] = 6 → res[0][0] = max(9,6) = 9

grid[1][2] = 2 → res[0][0] = max(9,2) = 9

grid[2][0] = 8 → res[0][0] = max(9,8) = 9

grid[2][1] = 2 → res[0][0] = max(9,2) = 9

grid[2][2] = 6 → res[0][0] = max(9,6) = 9
```
After finishing this window:
```python
res = [
  [9, 0],
  [0, 0]
]
```
2) i = 0, j = 1

3×3 window covers rows 0..2 and cols 1..3:
```python
[9, 8, 1]
[6, 2, 6]
[2, 6, 4]

```
Update res[0][1]:

Start res[0][1] = 0
```python
grid[0][1] = 9 → res[0][1] = 9

grid[0][2] = 8 → max(9,8) = 9

grid[0][3] = 1 → max(9,1) = 9

grid[1][1] = 6 → max(9,6) = 9

grid[1][2] = 2 → max(9,2) = 9

grid[1][3] = 6 → max(9,6) = 9

grid[2][1] = 2 → ...

grid[2][2] = 6 → ...

grid[2][3] = 4 → ...
```
All keep it at 9.

After finishing:
```python
res = [
  [9, 9],
  [0, 0]
]
```
3) i = 1, j = 0

3×3 window covers rows 1..3 and cols 0..2:
```python
[5, 6, 2]
[8, 2, 6]
[6, 2, 2]

```
Update res[1][0]:

Start res[1][0] = 0
```python
grid[1][0] = 5 → res[1][0] = 5

grid[1][1] = 6 → res[1][0] = 6

grid[1][2] = 2 → res[1][0] = 6

grid[2][0] = 8 → res[1][0] = 8 ← new max

grid[2][1] = 2 → res[1][0] = 8

grid[2][2] = 6 → res[1][0] = 8

grid[3][0] = 6 → res[1][0] = 8

grid[3][1] = 2 → res[1][0] = 8

grid[3][2] = 2 → res[1][0] = 8
```
After finishing:
```python
res = [
  [9, 9],
  [8, 0]
]
```
4) i = 1, j = 1

3×3 window covers rows 1..3 and cols 1..3:
```python
[6, 2, 6]
[2, 6, 4]
[2, 2, 2]

```
Update res[1][1]:

Start res[1][1] = 0
```python
grid[1][1] = 6 → res[1][1] = 6

grid[1][2] = 2 → res[1][1] = 6

grid[1][3] = 6 → res[1][1] = max(6,6) = 6

grid[2][1] = 2 → ...

grid[2][2] = 6 → res[1][1] = max(6,6) = 6

grid[2][3] = 4 → ...

grid[3][1] = 2 → ...

grid[3][2] = 2 → ...

grid[3][3] = 2 → ...
```
Final res[1][1] = 6.

After finishing:
```python
res = [
  [9, 9],
  [8, 6]
]
```
Final output
```python
[[9, 9],
 [8, 6]]
```

---

## 💡 Time and Space Complexity
- **Time**: O(N^2)
    - Outer loops: (N-2)^2 ≈ N^2
    - Inner loops over 3x3 submatrix: 9 operations → constant
- **Space**: O(N^2)
    - Result matrix of size (N-2) x (N-2)
