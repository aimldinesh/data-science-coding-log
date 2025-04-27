# 🧲 Problem: Repeated Substring Pattern

- **Platform**: [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/repeated-substring-pattern/submissions/1619184889/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/repeated-substring-pattern/submissions/1619184889/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-04-27
- **Tags**: String, Math, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
For example:
 - s = "abab" → True ("ab" + "ab")
 - s = "aba" → False
 - s = "abcabcabcabc" → True ("abc" + "abc" + "abc" + "abc")

---

## 🚀 My Approach
 - Step 1: Concatenate the string with itself: doubled = s + s.
 - Step 2: Remove the first and last characters from the doubled string: modified = doubled[1:-1].
 - Step 3: Check if the original string s is a substring of modified.
 - If yes, s can be constructed by repeating a substring.
 - Otherwise, it cannot.

---

## 💻 Code (Python)

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Concatenate the string with itself
        doubled = s + s

        # Remove the first and last character
        modified = doubled[1:-1]

        # Check if s exists inside modified string
        return s in modified

```

---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the length of the string s.
- **Space**: O(n), extra space for the concatenated string.
