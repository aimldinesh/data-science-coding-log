# 🧲 Problem: Merge Strings Alternately

- **Platform**: [LeetCode](https://leetcode.com/problems/merge-strings-alternately/)
- **Submission**: [https://leetcode.com/problems/merge-strings-alternately/submissions/1627815529/](https://leetcode.com/problems/merge-strings-alternately/submissions/1627815529/)
- **Date Solved**: 2025-05-07
- **Tags**: String, Two Pointers
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the remaining letters at the end.

### 🔍 Examples

```python
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

---

## 🚀 My Approach
### 🧠 Intuition
  - Use a pointer to alternate between characters of both strings.
  - Once the shorter string is exhausted, append the remaining part of the longer string.
Steps:
  - Initialize an empty result string.
  - Use a loop to append one character from each string alternately.
  - After the loop, append the remainder of the longer string (if any).
  
---

## 💻 Code (Python)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""  # Initialize an empty result string
        i, n, m = 0, len(word1), len(word2)

        # Merge alternately
        while i < n and i < m:
            result += word1[i] + word2[i]
            i += 1

        # Append the remaining characters from the longer word
        return result + word1[i:] + word2[i:]
```

---

## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are lengths of word1 and word2.
- **Space**: O(1)
