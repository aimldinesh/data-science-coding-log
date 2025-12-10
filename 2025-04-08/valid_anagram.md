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
**Output:** `True`

### Example 2:
**Input:**  
`s = "rat"`, `t = "car"`  
**Output:** `False`


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

---
## Approach 3: Hash Table using Array
🧠 Intuition

Since the problem states that both strings contain only lowercase English letters (a–z), we can use a fixed-size array of length 26 instead of a hash map.

Why this works:

- Each character 'a' to 'z' can be mapped to an index 0–25 using:
```python
index = ord(char) - ord('a')
```
- As we iterate through both strings at the same time:
  - We increment the count for each character in s
  - We decrement the count for each character in t

- For the strings to be anagrams:
  - Every increment must be matched by a decrement
  - So all 26 frequency counts must end at zero

This approach is efficient because:
  - It uses constant extra space (size 26)
  - It avoids expensive hash map operations
  - It runs in O(n) time

🛠 Algorithm

1. If lengths of s and t differ, return False immediately.
2. Create a frequency array count of size 26, initialized to zeros.
3. Iterate through both strings simultaneously:
   - For each character s[i], increment count[index]
   - For each character t[i], decrement count[index]

4. After processing both strings:
   - Check whether all values in count are zero
   - If any value is non-zero → frequency mismatch → return False
5. If the entire array contains zeros, return True.

---

## Code(Python)
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Step 1: If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Frequency array for characters 'a' to 'z'
        count = [0] * 26

        # Step 3: Process both strings simultaneously
        for i in range(len(s)):
            # Increment for s[i]
            count[ord(s[i]) - ord('a')] += 1
            
            # Decrement for t[i]
            count[ord(t[i]) - ord('a')] -= 1

        # Step 4: Check if all counts became zero
        for val in count:
            if val != 0:
                return False

        return True

```
---


## 💡 Time and Space Complexity
- **Time**: O(n)
   - We loop through the strings once.
- **Space**: O(1)
   - Fixed array of size 26 → constant space.

