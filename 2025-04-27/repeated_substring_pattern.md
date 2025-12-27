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
## Examples
```
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```
---

## 🧠 Approach: String Doubling Trick

🔹 Intuition:

+ If a string s is made by repeating a substring, then:
  + s will appear inside (s + s)[1:-1]

Why?

+ Concatenating s + s creates overlapping patterns.
+ Removing the first and last character prevents matching the original string directly.
+ If s still exists inside this trimmed string → it is repeating.

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
