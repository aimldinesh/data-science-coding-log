# 🧲 Problem: Valid Sudoku

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-sudoku/description/)
- **Submission**: [https://leetcode.com/problems/valid-sudoku/submissions/1621929486/](https://leetcode.com/problems/valid-sudoku/submissions/1621929486/)
- **Date Solved**: 2025-04-30
- **Tags**: Array, Hash Table, Matrix
- **Difficulty**: Medium

---

## ✅ Problem Statement
Determine if a 9 × 9 Sudoku board is valid.

Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.

---

## 🚀 Approach
- Use three dictionaries of sets to keep track of the numbers seen in:
  - Each **row**
  - Each **column**
  - Each **3x3 sub-grid**
- For each filled cell:
  - Check if the number is already present in the corresponding row, column, or square.
  - If yes, return `False` immediately.
  - Otherwise, add it to the sets for that row, column, and square.
- If no duplicate is found, return `True`.

---

## 💻 Code (Python)

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to track seen numbers in rows, columns, and 3x3 squares.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Key for squares will be (row//3, col//3)

        # Iterate through each cell in the 9x9 Sudoku board.
        for r in range(9):
            for c in range(9):
                # Skip empty cells represented by ".".
                if board[r][c] == ".":
                    continue
                
                # Check if the current number is already in the current row, column, or 3x3 square.
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # If found in any, the board is invalid.
                
                # Add the current number to the corresponding row, column, and square sets.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no conflicts are found, return True (valid Sudoku).
        return True  
```

---

## 💡 Time and Space Complexity
- **Time**: O(1)
   - Always a fixed 9x9 grid, constant operations for each cell.
- **Space**: O(1)
   - Even though sets are used, they hold at most 81 elements total, which is constant space.
