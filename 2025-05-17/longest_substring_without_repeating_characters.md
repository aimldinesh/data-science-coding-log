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
Output: 3
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
🔸 Steps:
- Use two pointers (l and r) to maintain a window of non-repeating characters.
- Use a set charSet to store characters in the current window.
- If a repeating character is found at r, shrink the window from the left until the character is removed.
- Update the maximum length (res) during each iteration.

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

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each character is visited at most twice (once by r, once by l).
- **Space**: O(k)
    - Where k is the number of unique characters in the string (max 128 for ASCII).
