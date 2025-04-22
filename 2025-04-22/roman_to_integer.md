# 🧲 Problem: Roman to Integer

- **Platform**: [LeetCode](https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/roman-to-integer/submissions/1614371167/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/roman-to-integer/submissions/1614371167/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-04-22
- **Tags**: Hash Table, Math, String
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a string `s` representing a Roman numeral, convert it to its corresponding integer value.

### Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Some examples of subtractive notation:
- `IV` = 4 (5 - 1)
- `IX` = 9 (10 - 1)
- `XL` = 40 (50 - 10)
- `XC` = 90 (100 - 10)
- `CD` = 400 (500 - 100)
- `CM` = 900 (1000 - 100)

### 🧪 Example:

```python
Input: s = "MCMXCIV"
Output: 1994

Explanation:
M = 1000  
CM = 900  
XC = 90  
IV = 4  
Total = 1000 + 900 + 90 + 4 = 1994

---

## 🚀 My Approach
- Create a dictionary that maps each Roman numeral to its integer value.
- Traverse the string s from left to right:
 - If the current numeral is less than the next one, subtract it (subtractive notation).
 - Otherwise, add it to the result.
- Return the accumulated result.

---

## 💻 Code (Python)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral to integer mapping
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        res = 0

        # Traverse the string
        for i in range(len(s)):
            # Subtractive case
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the length of the input string s, since we traverse it once
- **Space**: O(1), constant space used for the dictionary and variables
