# 🧲 Problem: Excel Sheet Column Title

- **Platform**: [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/description/)
- **Submission**: [https://leetcode.com/problems/excel-sheet-column-title/submissions/](https://leetcode.com/problems/excel-sheet-column-title/submissions/)
- **Date Solved**: 2025-09-27
- **Tags**: DSA, Math, String
- **Difficulty**: Easy

---

## 📌 Problem Statement
Given a positive integer `columnNumber`, return its corresponding Excel column title.

- Excel labels columns as:
  - 1 → A
  - 2 → B
  - ...
  - 26 → Z
  - 27 → AA
  - 28 → AB
  - and so on.

---
```text
Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

```
---

## 💡 Approach
1. Initialize an empty string `res`.
2. While `columnNumber > 0`:
   - Compute `offset = (columnNumber - 1) % 26` to find the letter index.
   - Append the corresponding character (`A` + offset) to `res`.
   - Update `columnNumber = (columnNumber - 1) // 26`.
3. Since characters are built in reverse, return `res[::-1]`.

---

## 🐍 Python Code

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            # Get current character (Excel is 1-indexed)
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)

            # Move to the next position
            columnNumber = (columnNumber - 1) // 26

        # Reverse the result since we built it backwards
        return res[::-1]
```

---

## 💡 Time and Space Complexity
- **Time**: O(log₍26₎ columnNumber)
    - Each step divides columnNumber by 26.
- **Space**: O(log₍26₎ columnNumber)
    - The result string length is proportional to the number of base-26 digits.
