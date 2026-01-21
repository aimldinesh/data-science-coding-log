# 🧲 Problem: Spiral Matrix III

- **Platform**: [LeetCode](https://leetcode.com/problems/spiral-matrix-iii/description/)
- **Submission**: [https://leetcode.com/problems/spiral-matrix-iii/submissions/1785394363/](https://leetcode.com/problems/spiral-matrix-iii/submissions/1785394363/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math, Spiral Matrix
- **Difficulty**: Medium

---

## ✅ Problem Statement
You are given the dimensions of a grid (`rows x cols`) and a starting position `(rStart, cStart)`.  

Return the sequence of coordinates visited in **spiral order** starting from `(rStart, cStart)` **until all cells are visited**.

---

## 🔹 Examples
**Example 1:** 
```text 
Input: `rows = 1, cols = 4, rStart = 0, cStart = 0`  
Output: `[[0,0],[0,1],[0,2],[0,3]]`
```
---

**Example 2:** 
```text 
Input: rows = 5, cols = 6, rStart = 1, cStart = 4

Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

```
---

## 🔹 Approach

1. Define directions in order: **right → down → left → up**.  
   - directions = [[0,1], [1,0], [0,-1], [-1,0]]
2. Start from `(rStart, cStart)`.  
3. Use a **step counter**:
- Move 1 step right, then 1 step down.  
- Increase steps → 2 steps left, 2 steps up.  
- Increase steps → 3 steps right, 3 steps down, and so on.  
4. Continue until we have collected all `rows * cols` cells that fall inside the grid.  
5. Return the result list.

---

## 🔹 Code (Python)

```python

class Solution:
 def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
     # Directions: right, down, left, up
     directions = [[0,1],[1,0],[0,-1],[-1,0]]

     res = []
     r, c = rStart, cStart  # starting point
     steps = 1              # number of steps to take in each direction
     i = 0                  # index for directions

     while len(res) < rows * cols:
         # Each loop expands the spiral (two directions per cycle)
         for _ in range(2):
             dr, dc = directions[i]
             for _ in range(steps):
                 # Only add valid coordinates inside the grid
                 if 0 <= r < rows and 0 <= c < cols:
                     res.append([r, c])
                 # Move to the next cell
                 r, c = r + dr, c + dc
             # Move to next direction
             i = (i + 1) % 4
         # After two directions, increase step size
         steps += 1

     return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(rows×cols)
    - Each valid cell is added exactly once.
- **Space**: O(rows×cols)
    - To store the result coordinates.
