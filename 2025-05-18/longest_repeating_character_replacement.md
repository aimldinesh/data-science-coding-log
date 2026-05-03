# 🧲 Problem: Longest Repeating Character Replacement

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/description/)
- **Submission**: [https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1637272582/](https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1637272582/)
- **Date Solved**: 2025-05-18
- **Tags**: Hash Table, String, Sliding Window
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given a string `s` and an integer `k`. You can choose **at most k** characters from the string and change them to **any uppercase letter**.
- Return the length of the **longest possible substring** that contains only the same character after performing at most `k` replacements.

---

### 🔍 Examples

```python
Example 1:

Input: s = "ABAB", k = 2
Output: 4

Explanation: Replace the two 'A's or two 'B's to get "BBBB" or "AAAA".

Example 2:

Input: s = "AABABBA", k = 1
Output: 4

Explanation: Replace the third 'A' to get "AABBBBA", the longest is "ABBB".

```
---

## 🚀 Approach 1 : Brute Force + Frequency Count

🧠 Intuition

In any window, the most frequent character stays, and everything else gets replaced. So the number of replacements needed = window size - max frequency. If that's ≤ k, the window is valid. Try every possible window with two nested loops — brute force but clear.
```
s = "AABABBA",  k = 1

Window "AABA" → maxf=3(A), replacements=4-3=1 ≤ k ✅ valid, length=4
Window "ABAB" → maxf=2(A), replacements=4-2=2 > k ❌ invalid
```
📌 Approach

1. For every starting index i, expand j rightward
2. Track character frequencies in current window
3. At each step: replacements = (j - i + 1) - maxf
   + ≤ k → valid window → update res
   + > k → invalid → break inner loop (window can only get worse)

4. Return res

---

## 💻 Code (Python)

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0  # Store the length of the longest valid substring
        
        # Outer loop: start index of the window
        for i in range(len(s)):
            count, maxf = {}, 0  # count = frequency map, maxf = max frequency in window

            # Inner loop: end index of the window
            for j in range(i, len(s)):
                # Update character frequency
                count[s[j]] = 1 + count.get(s[j], 0)
                
                # Update max frequency in the current window
                maxf = max(maxf, count[s[j]])

                # Check if we can replace remaining characters (window size - max freq) <= k
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)  # Valid window, update result

        return res  # Return the length of the longest valid substring

```

---

## 💡 Time and Space Complexity
- **Time**: O(n² × 26) = O(n²)
     - Outer loop runs n times, inner loop up to n times.
     - Inside the inner loop, frequency map lookup and max are O(1) due to only 26 letters.
- **Space**: O(26) = O(1)
     - Only uses a dictionary for uppercase letter frequencies.

## 🚀 Approach 2 : Sliding Window + Character Frequency
🔸 Key Insight:
- The goal is to maintain the longest window such that we can convert all characters in that window to the most frequent character using at most k replacements.
🔸 Steps:
- Use a dictionary count to track the frequency of each character in the current window.
- If (window size - max frequency) exceeds k, shrink the window from the left.
- Update res with the length of the valid window.

---

## 💻 Code (Python)

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of characters in the current window
        res = 0     # Stores the length of the longest valid substring
        l = 0       # Left pointer of the window

        # Iterate through the string with right pointer `r`
        for r in range(len(s)):
            # Update frequency of the current character s[r]
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if the window is valid:
            # (window length - count of most frequent character) should be <= k
            # i.e., we can replace at most k characters to make all characters same
            while (r - l + 1) - max(count.values()) > k:
                # Shrink the window from the left
                count[s[l]] -= 1
                l += 1

            # Update the result with the size of the valid window
            res = max(res, r - l + 1)

        return res  # Return the length of the longest valid substring
```

---

## 💡 Time and Space Complexity
- **Time**: O(26 × n) = O(n)
     - Each character is processed once.
     - max(count.values()) is bounded by 26 (uppercase letters only).
- **Space**: O(26) = O(1)
     - Dictionary holds at most 26 characters.
