# 🧲 Problem: Append Characters to String to Make Subsequence

- **Platform**: [LeetCode](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/)
- **Submission**: [https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/submissions/1786922125/](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/submissions/1786922125/)
- **Date Solved**: 2025-09-30
- **Tags**: DSA, String, Two Pointer
- **Difficulty**: Medium

---

## ✅ Problem Statement
You are given two strings `s` and `t`.  
Your task is to determine the **minimum number of characters you need to append to the end of `s`** so that `t` becomes a subsequence of `s`.

A subsequence of a string is a new string generated from the original string with some characters (possibly none) deleted without changing the relative order of the remaining characters.

Return the minimum number of characters to append.

---

## 🔹 Example

**Example 1:**  
Input: `s = "coaching"`, `t = "coding"`  
Output: `1`  

Explanation: The longest prefix of `t` in `s` as a subsequence is `"coing"`.  
Remaining part of `t` = `"d"`.  
So, we need to append **1** character.  

---

**Example 2:**  
Input: `s = "abc"`, `t = "abc"`  
Output: `0`  

Explanation: `t` is already a subsequence of `s`. Nothing needs to be appended.  

---

**Example 3:**  
Input: `s = "z"`, `t = "abcde"`  
Output: `5` 

Explanation: No characters of `t` match in `s`.  
We must append all of `t` (5 characters).  

---

## 🔹 Approach
1. Use **two pointers** (`i` for `s`, `j` for `t`).  
2. Traverse both strings:
   - If `s[i] == t[j]`, move both pointers forward.  
   - Otherwise, only move `i`.  
3. After traversal:
   - `j` indicates how many characters of `t` matched inside `s`.  
   - Remaining = `len(t) - j`, which must be appended.  

---

## 🔹 Code (Python)

### ✨ Two-Pointer Solution
```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j
```
---
## One-Liner Solution
```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        it = iter(s)
        return len(t) - sum(ch in it for ch in t)
```
---
```text
Dry Run of One-Liner (Example: s = "coaching", t = "coding")

We create an iterator it = iter("coaching").
Now check each character of t sequentially:

ch = 'c': Is 'c' in iterator "coaching"? ✅ Yes → consume up to 'c'. (Matched count = 1)

ch = 'o': Is 'o' in remaining "oaching"? ✅ Yes → consume up to 'o'. (Matched count = 2)

ch = 'd': Is 'd' in remaining "aching"? ❌ No → cannot match. (Matched count = 2)

ch = 'i': Is 'i' in remaining "aching"? ✅ Yes → consume up to 'i'. (Matched count = 3)

ch = 'n': Is 'n' in remaining "ng"? ✅ Yes → consume up to 'n'. (Matched count = 4)

ch = 'g': Is 'g' in remaining "g"? ✅ Yes → consume 'g'. (Matched count = 5)

👉 Total matched = 5 out of 6.
So, result = len(t) - matched = 6 - 5 = 1.
```
---

## 💡 Time and Space Complexity
- **Time**: O(len(s) + len(t))
    - each char checked once.
- **Space**: O(1)
    - only pointers/iterator used.
