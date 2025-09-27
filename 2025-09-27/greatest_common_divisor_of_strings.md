# 🧲 Problem: Greatest Common Divisor of Strings

- **Platform**: [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)
- **Submission**: [https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/](https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/)
- **Date Solved**: 2025-09-27
- **Tags**: DSA, Math, String
- **Difficulty**: Easy

---

## 📌 Problem Statement
For two given strings `str1` and `str2`, return the **greatest common divisor (GCD) string**.

A string `x` is a divisor of string `y` if and only if:
- `y = x + x + ... + x` (concatenated some number of times).

The GCD string is the **largest string** that can divide both `str1` and `str2`.

---
## ✅ Example:
```text
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
```
---

## 💡 Approach
1. Define a helper function `isDivisor(l)`:
   - Check if a prefix of length `l` can fully divide both strings.
   - Verify lengths are divisible by `l`.
   - Verify repeated prefix reconstructs both strings.
2. Iterate from `min(len1, len2)` down to 1:
   - First valid divisor found is the answer.
3. If none found, return `""`.

---

## 🐍 Python Code

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # Helper to check if prefix of length l divides both strings
        def isDivisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Try all possible prefix lengths (largest first)
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""
```
---
## 🧮 Example Dry Run
```text
Input:
str1 = "ABCABC"
str2 = "ABC"

1.len1=6, len2=3, min=3
2.Try l=3: prefix = "ABC"

   len1 % 3 == 0 ✅
   len2 % 3 == 0 ✅

   "ABC" * 2 == "ABCABC" ✅
   "ABC" * 1 == "ABC" ✅

   → Return "ABC"

✅ Output: "ABC"
```
---

## 💡 Time and Space Complexity
- **Time**:
    - Checking divisibility requires repeating prefix strings → O(n + m) per check.
    - At most min(n, m) checks.
    - Worst case: O((n + m) * min(n, m)).
- **Space**: O(n + m)
    - For temporary string constructions during prefix checks.

