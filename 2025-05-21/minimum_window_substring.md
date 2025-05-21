# 🧲 Problem: Minimum Window Substring

- **Platform**: [LeetCode](https://leetcode.com/problems/minimum-window-substring/description/)
- **Submission**: [https://leetcode.com/problems/minimum-window-substring/submissions/1640324905/](https://leetcode.com/problems/minimum-window-substring/submissions/1640324905/)
- **Date Solved**: 2025-05-21
- **Tags**: Hash Table, String, Sliding Window, Two Pointers
- **Difficulty**: Hard

---

## ✅ Problem Statement
- Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.
- If there is no such substring, return the empty string `""`.

---

### 🔍 Examples

```python
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
```
---

## 🚀 Approach : Sliding Window + Hash Map
🧠 Intuition:
- We want to find the smallest substring in s that contains all characters from t (including duplicates).
- This is a classic case for the sliding window technique with frequency tracking using hash maps.

🔸 Steps:
- Create frequency map of characters in t called countT.
- Use two pointers l and r to represent the sliding window.
- Expand the window by moving the right pointer r, and track characters in the current window using window.
- When the current window contains all required characters:
     - Try to shrink the window from the left (move l) while maintaining validity.
     - Update the smallest valid window seen so far.
- Return the result window, or "" if no such window exists.

---

## 💻 Code (Python)

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, there's no need to search
        if t == "":
            return ""

        # Step 1: Create a frequency map of characters in t
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'have' tracks how many unique characters are satisfied in current window
        # 'need' is total number of unique characters in t
        have, need = 0, len(countT)

        # res stores the best window [start, end]; resLen stores its length
        res, resLen = [-1, -1], float('infinity')
        l = 0  # Left pointer of the sliding window

        # Step 2: Expand the window with the right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # Add current character to window count

            # If this character meets the required count, increase 'have'
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 3: Try to contract the window while all characters are satisfied
            while have == need:
                # Update the result if this window is smaller than previous best
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
```

---

## 💡 Time and Space Complexity
- **Time**: O(n + m) 
    Where:
       - n = len(s) (length of the input string s)
       - m = len(t) (length of the string t)
    Breakdown:
       - Building countT:
            - Takes O(m) time (we iterate over t once to build the frequency map).
       - Sliding window over s:
            - Each character is visited at most twice (once by the right pointer r, once by the left pointer l).
            - So total window movement = O(n).
       - Inside the window:
            - Operations like window[c] += 1, countT[c], and comparisons are all O(1) due to hash maps.
   ✅ Total Time = O(n + m)

- **Space**: O(m)
    Breakdown:
        - countT dictionary:
            - Stores the frequency of each character in t, so size = O(m) at most.
        - window dictionary:
            - At most stores m unique characters at a time from t, so also O(m).

    ✅ Total Space = O(m)
     
