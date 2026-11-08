# 🧲 Problem: Score of a String

- **Platform**: [LeetCode](https://leetcode.com/problems/score-of-a-string/description/)
- **Submission**: [https://leetcode.com/problems/score-of-a-string/submissions/1786897984/](https://leetcode.com/problems/score-of-a-string/submissions/1786897984/)
- **Date Solved**: 2025-09-30
- **Tags**: DSA, String
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given a string `s`.  
The **score** of the string is defined as the sum of the absolute differences between the ASCII values of **adjacent characters**.

Formally:  
\[
\text{score}(s) = \sum_{i=0}^{n-2} | \text{ord}(s[i]) - \text{ord}(s[i+1]) |
\]

Return the score of the string.

---

## 🔹 Example

**Example 1:**  
Input: `s = "hello"`  
Step-by-step:  
- |h - e| = |104 - 101| = 3  
- |e - l| = |101 - 108| = 7  
- |l - l| = |108 - 108| = 0  
- |l - o| = |108 - 111| = 3  

Total = 3 + 7 + 0 + 3 = **13**

Output: `13`

---

**Example 2:**  
Input: `s = "zaz"`  

- |z - a| = |122 - 97| = 25  
- |a - z| = |97 - 122| = 25  

Total = 25 + 25 = **50**

Output: `50`

---

## 🔹 Approach
1. Initialize a variable `res = 0` to store score.  
2. Iterate through string from index `0` to `n-2`.  
3. For each adjacent pair `(s[i], s[i+1])`, add `abs(ord(s[i]) - ord(s[i+1]))` to `res`.  
4. Return `res`.

---

## 🔹 Code (Python)

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))
        return res
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - single pass over string.
- **Space**: O(1)
    - only uses a few variables.
