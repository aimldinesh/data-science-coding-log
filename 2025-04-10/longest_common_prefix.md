# 🧮 Problem: Longest Common Prefix

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-common-prefix/)
- **Submission**: [https://leetcode.com/problems/longest-common-prefix/submissions/1602255574/](https://leetcode.com/problems/longest-common-prefix/submissions/1602255574/)
- **Date Solved**: 2025-04-10
- **Tags**: DSA

---

## ✅ Problem Statement
*Given an array of strings `strs`, write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.
*

---

## 🚀 My Approach
- I loop through each character index of the **first string** in the list.
- For each index, I compare the character in the same position across **all other strings**.
- If any string:
  - Does not have a character at that index (index out of range), or
  - Has a different character at that position  
  Then I **return the prefix found so far**.
- If all characters match, I add that character to the result.

---

## 💻 Code (Python)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize the result string to store the common prefix

        # Loop through each character index of the first string
        for i in range(len(strs[0])):
            # Compare the character at index 'i' in all strings
            for s in strs:
                # If the index is out of range for any string or characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    return res  # Return the prefix found so far

            # If all strings have the same character at index 'i', add to result
            res += strs[0][i]

        return res  # Return the complete common prefix

```

---

## 💡 Time and Space Complexity
- **Time**: O(S), where S is the sum of all characters in all strings (in the worst case).
- **Space**: O(1), extra space (result string grows with prefix but not counted as extra).
