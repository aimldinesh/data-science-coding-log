# 🧮 Problem: Valid Anagram

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-anagram/)
- **Submission**: [https://leetcode.com/problems/valid-anagram/submissions/1067455989/](https://leetcode.com/problems/valid-anagram/submissions/1067455989/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA

---

## ✅ Problem Statement
Check if two strings are anagrams of each other. An anagram is formed by rearranging the letters of another string, using all original letters exactly once.


---

## 🚀 My Approach
1. First, check if both strings are of the same length. If not, return False.
2. Use two dictionaries to count the frequency of each character in both strings.
3. Compare both dictionaries — if equal, they are anagrams.

---

## 💻 Code (Python)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length
        if len(s) != len(t):
            return False

        # Use dictionaries to count character frequencies in both strings  
        s_count = {}
        t_count = {}

        #Count characters in string s
        for char in s:
            s_count[char] = s_count.get(char,0) + 1
        # count character i string t
        for char in t:
            t_count[char] = t_count.get(char,0) + 1

        # compare both dictonories
        return s_count == t_count
        
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(1),(since character set is limited)
