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
```
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

---
## 🥉 Approach 2: Brute Force (Using Index Checks)
- 🔹 Idea
- We will:
  - Use two pointers i and j for word1 and word2.
  - Pick characters alternately using conditions.
  - Stop when both strings are completely used.

- 🧠 Step-by-Step Logic
  - Initialize i = 0, j = 0, and res = ""
  - Loop while either i < len(word1) or j < len(word2)
  - Add one character from word1 (if available)
  - Add one character from word2 (if available)
  - Increment i and j accordingly
  - Return the merged result

---
## Code(Python)
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers and result string
        i, j = 0, 0
        res = ""
        
        # Loop until both strings are exhausted
        while i < len(word1) or j < len(word2):
            # If word1 still has characters, take one
            if i < len(word1):
                res += word1[i]
                i += 1
            
            # If word2 still has characters, take one
            if j < len(word2):
                res += word2[j]
                j += 1
        
        # Return the merged string
        return res
```
## step by step with example
```python
Input:
word1 = "abc"
word2 = "pqr"

Steps:
res = ""
→ add 'a' + 'p' → "ap"
→ add 'b' + 'q' → "apbq"
→ add 'c' + 'r' → "apbqcr"
Output = "apbqcr"

✅ Output: "apbqcr"
```
---

## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are lengths of word1 and word2.
- **Space**: O(n + m)

---

## 🥈 Approach 3: Efficient (Using List + Join)
- Instead of concatenating strings repeatedly (which is slow because strings are immutable in Python),
- we’ll use a list to collect characters and then "".join() at the end.
- Also, we can directly use slicing for leftover parts.

- 💡 Logic
  - Create an empty list merged = []
  - Use a loop for the common part (min_len = min(len(word1), len(word2)))
  - Append one character from word1 and one from word2
  - After the loop, append the remaining characters (if any)
  - Return "".join(merged)
---
## Code(Python)
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create an empty list to store merged characters
        merged = []

        # Find minimum length between both strings
        min_len = min(len(word1), len(word2))

        # Merge alternately up to the shortest string
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        
        # Append leftover characters from longer string
        merged.append(word1[min_len:])
        merged.append(word2[min_len:])

        # Join list into final merged string
        return "".join(merged)

```
---
## step by step with example
```python
input:
word1 = "ab"
word2 = "pqrs"

Steps:
min_len = 2
merged = ['a','p','b','q']
leftover from word2 = "rs"
merged = ['a','p','b','q','r','s']

Output = "apbqrs"
```
---
## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are lengths of word1 and word2.
- **Space**: O(n + m)
- More efficient than the brute-force because of list usage (no repeated string concatenation).

---
## 🥇 Approach 4: Pythonic (Using zip_longest)
- 🔹 Idea
- We can use:
```python
from itertools import zip_longest
```
- to pair characters from both strings, even when they’re of unequal length.Then, we join all characters alternately using a generator expression.

- 🧠 Step-by-Step Logic
   - Import zip_longest
   - Use zip_longest(word1, word2, fillvalue="") to handle uneven string lengths
   - For each pair (a, b), combine them as a + b
   - Finally, "".join() everything into a single string

---
## Code(Python)
```python
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # zip_longest pairs characters from both strings
        # fillvalue="" ensures that extra characters from the longer string are kept
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

```
---
## step by step with example
```python
input:
word1 = "abcd"
word2 = "pq"

| Step | a   | b   | Result   |
| ---- | --- | --- | -------- |
| 1    | 'a' | 'p' | "ap"     |
| 2    | 'b' | 'q' | "apbq"   |
| 3    | 'c' | ''  | "apbqc"  |
| 4    | 'd' | ''  | "apbqcd" |

✅ Output: "apbqcd"
```
---

## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are lengths of word1 and word2.
- **Space**: O(n + m)
- ✅ Simplest and most Pythonic way to merge alternately.

---

## 🏁 Summary of All Approaches
| Approach | Method                     | Time     | Space    | Notes                                               |
| -------- | -------------------------- | -------- | -------- | --------------------------------------------------- |
| 1        | Brute Force (manual loops) | O(n + m) | O(n + m) | Simple logic but slower due to string concatenation |
| 2        | Efficient (list + join)    | O(n + m) | O(n + m) | Faster, good balance                                |
| 3        | Pythonic (`zip_longest`)   | O(n + m) | O(n + m) | Clean, concise, interview-friendly ✅                |

