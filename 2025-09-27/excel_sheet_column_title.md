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

## 🧠 Intuition
Excel columns follow a base-26 system but with no zero — A=1, B=2, ... Z=26, AA=27. Unlike regular base conversion, there's no 0 digit. The trick is columnNumber - 1 before each modulo/division — this shifts the range from 1-26 to 0-25, making standard base-26 math work correctly.
```python
Regular base 26:   0-25  →  digits 0,1,...,25
Excel base 26:     1-26  →  digits A,B,...,Z  (no zero!)

Fix: subtract 1 before each operation to align them
```
## 📌 Approach

1. While columnNumber > 0:
   - offset = (columnNumber - 1) % 26 → current letter (0=A, 25=Z)
   - Append chr(ord('A') + offset) to res
   - columnNumber = (columnNumber - 1) // 26 → move left

2. Reverse res and return

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
### 🔍 Step-by-Step Execution

Example 1: columnNumber = 28 → expected "AB"

Iteration 1:
```python
offset      = (28-1) % 26  = 27 % 26 = 1
char        = chr(65 + 1)  = 'B'
res         = "B"
columnNumber = (28-1) // 26 = 27 // 26 = 1
```
Iteration 2:
```python
offset      = (1-1) % 26  = 0 % 26 = 0
char        = chr(65 + 0) = 'A'
res         = "BA"
columnNumber = (1-1) // 26 = 0 // 26 = 0
```
Loop ends: columnNumber = 0
```python
res[::-1] = "AB" ✅
```
---

Example 2: columnNumber = 701 → expected "ZY"

Iteration 1:
```python
offset      = (701-1) % 26  = 700 % 26 = 24
char        = chr(65 + 24)  = 'Y'
res         = "Y"
columnNumber = (701-1) // 26 = 700 // 26 = 26
```
Iteration 2:
```python
offset      = (26-1) % 26  = 25 % 26 = 25
char        = chr(65 + 25)  = 'Z'
res         = "YZ"
columnNumber = (26-1) // 26 = 25 // 26 = 0
```
Loop ends:
```python
res[::-1] = "ZY" ✅
```
---




## 💡 Time and Space Complexity
- **Time**: O(log₍26₎ columnNumber)
    - Each step divides columnNumber by 26.
- **Space**: O(log₍26₎ columnNumber)
    - The result string length is proportional to the number of base-26 digits.
