# 🧮 Problem: Valid Anagram

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-anagram/)
- **Submission**: [https://leetcode.com/problems/valid-anagram/submissions/1067455989/](https://leetcode.com/problems/valid-anagram/submissions/1067455989/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA

---

## 📘 Problem Statement
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all original letters exactly once.

---

## 🔍 Example

### Example 1:
**Input:**  
`s = "anagram"`, `t = "nagaram"`  
**Output:**  
`True`

### Example 2:
**Input:**  
`s = "rat"`, `t = "car"`  
**Output:**  
`False`


---

## 🚀 Approach 1 : Using Dictionary (Manual Counting)
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

## 🔍 Example Walkthrough
```python
nput:
s = "listen", t = "silent"

Steps:
| Step      | String     | Frequency Count                                |
| --------- | ---------- | ---------------------------------------------- |
| Count `s` | `"listen"` | `{ 'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1 }` |
| Count `t` | `"silent"` | `{ 's':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1 }` |

- Since both dictionaries are identical → ✅ True

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Each string is traversed once
- **Space**: O(1)
   - At most 26 letters for lowercase English letters
 
---

## Approach 2: Using collections.Counter
- Instead of manually counting characters with dictionaries,
- we can use Python’s built-in Counter class (from the collections module),
- which automatically counts the frequency of each character.

## Code(Python)
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Compare the frequency count of both strings directly
        return Counter(s) == Counter(t)
```
---

## 🧠 Example Walkthrough
```python
Input:
s = "triangle", t = "integral"

Process:

Counter(s) → {'t':1, 'r':1, 'i':1, 'a':1, 'n':1, 'g':1, 'l':1, 'e':1}

Counter(t) → {'i':1, 'n':1, 't':1, 'e':1, 'g':1, 'r':1, 'a':1, 'l':1}

✅ Both are equal → returns True
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Counter internally iterates through each character once.
- **Space**: O(1)
   - Since only a fixed number of characters (26 lowercase letters) can appear.
