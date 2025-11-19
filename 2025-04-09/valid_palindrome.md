# 🧮 Problem: Valid Palindrome

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-palindrome/description/)
- **Submission**: [https://leetcode.com/problems/valid-palindrome/submissions/1414342918/](https://leetcode.com/problems/valid-palindrome/submissions/1414342918/)
- **Date Solved**: 2025-04-09
- **Tags**: DSA

---

## ✅ Problem Statement
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

A palindrome is a word, phrase, or sequence that reads the same backward as forward after removing non-alphanumeric characters and converting all letters to lowercase.

---
## Examples:
```python
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```


---

## 🚀 My Approach 1: String Reversal
1. Loop through each character in the string.
2. Keep only the alphanumeric characters and convert them to lowercase.
3. Compare the cleaned string to its reversed version using slicing (`[::-1]`).

---

## 💻 Code (Python)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), One pass to clean the string, one pass to reverse and compare.
- **Space**: O(n), Extra space for the cleaned string.

---

## 🚀 My Approach 2: Two Pointers 
1. Loop through the original string and build a cleaned version that only contains lowercase alphanumeric characters.
2. Use two pointers: one starting from the beginning (`l`) and one from the end (`r`) of the cleaned string.
3. If at any point `res[l] != res[r]`, return `False`.
4. If all characters match, return `True`.

---

## 💻 Code (Python)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        l = 0
        r = len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), One pass to filter, one pass for two-pointer check.
- **Space**: O(n), For storing the cleaned string.
