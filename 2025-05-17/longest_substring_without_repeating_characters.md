# 🧲 Problem: Longest Substring Without Repeating Characters

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Submission**: [https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1636420373/](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1636420373/)
- **Date Solved**: 2025-05-17
- **Tags**: Hash Table, String, Sliding Window
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given a string `s`, find the length of the **longest substring** without repeating characters.

---

### 🔍 Examples

```python
Example 1:

Input: s = "abcabcbb"
Output: 

Explanation: The answer is "abc", with length 3.

Example 2:

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with length 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with length 3.
```
---

## 🚀 Approach : Sliding Window with HashSet
🧠 Intuition

Imagine a sliding window moving across the string. We expand it to the right greedily — but the moment we hit a duplicate character, we shrink from the left until the duplicate is gone. A set tracks what's currently inside the window, giving us O(1) duplicate checks.

📌 Approach

1. Use two pointers l and r to define a window
2. Expand r each iteration
3. If s[r] is already in charSet → shrink from left until it's removed
4. Add s[r] to set, update res = max(res, r - l + 1)

---

## 💻 Code (Python)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # To store unique characters in the current window
        l = 0            # Left pointer of the sliding window
        res = 0          # Stores the length of the longest substring found

        for r in range(len(s)):  # Right pointer moves through the string
            # If character is already in the set, shrink window from the left
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove leftmost character
                l += 1                # Move left pointer to the right

            # Add the current character to the set
            charSet.add(s[r])

            # Update result with the current window length
            res = max(res, r - l + 1)

        return res  # Return the length of the longest valid substring
```

---
🔍 Step-by-Step Execution

Input: s = "abcabcbb"

Initial State:
```python
charSet = {}
l = 0, res = 0
```
r=0 → s[r]='a'
```python
'a' not in set → add it
charSet = {'a'}
window = s[0:1] = "a"
res = max(0, 0-0+1) = 1
```
r=1 → s[r]='b'
```python
'b' not in set → add it
charSet = {'a','b'}
window = s[0:2] = "ab"
res = max(1, 1-0+1) = 2
```
r=2 → s[r]='c'
```python
'c' not in set → add it
charSet = {'a','b','c'}
window = s[0:3] = "abc"
res = max(2, 2-0+1) = 3
```
r=3 → s[r]='a'
```python
'a' IN set → shrink from left:
  remove s[0]='a', l=1
  charSet = {'b','c'}
'a' not in set now → add it
charSet = {'b','c','a'}
window = s[1:4] = "bca"
res = max(3, 3-1+1) = 3
```
r=4 → s[r]='b'
```python
'b' IN set → shrink from left:
  remove s[1]='b', l=2
  charSet = {'c','a'}
'b' not in set now → add it
charSet = {'c','a','b'}
window = s[2:5] = "cab"
res = max(3, 4-2+1) = 3
```
r=5 → s[r]='c'
```python
'c' IN set → shrink from left:
  remove s[2]='c', l=3
  charSet = {'a','b'}
'c' not in set now → add it
charSet = {'a','b','c'}
window = s[3:6] = "abc"
res = max(3, 5-3+1) = 3
```
r=6 → s[r]='b'
```python
'b' IN set → shrink from left:
  remove s[3]='a', l=4
  charSet = {'b','c'}  ← 'b' still in set!
'b' IN set → shrink again:
  remove s[4]='b', l=5
  charSet = {'c'}
'b' not in set now → add it
charSet = {'c','b'}
window = s[5:7] = "cb"
res = max(3, 6-5+1) = 3
```
r=7 → s[r]='b'
```pyython
'b' IN set → shrink from left:
  remove s[5]='c', l=6
  charSet = {'b'}  ← 'b' still in set!
'b' IN set → shrink again:
  remove s[6]='b', l=7
  charSet = {}
'b' not in set now → add it
charSet = {'b'}
window = s[7:8] = "b"
res = max(3, 7-7+1) = 3
```
---
✅ Final Answer
```python
return res = 3   →   "abc"
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each character is visited at most twice (once by r, once by l).
- **Space**: O(k)
    - Where k is the number of unique characters in the string (max 128 for ASCII).
