# 🧮 Problem: Longest Common Prefix

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-common-prefix/)
- **Submission**: [https://leetcode.com/problems/longest-common-prefix/submissions/1602255574/](https://leetcode.com/problems/longest-common-prefix/submissions/1602255574/)
- **Date Solved**: 2025-04-10
- **Tags**: DSA

---

## ✅ Problem Statement
-Given an array of strings `strs`, write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.


---
## Examples
```python
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

````
---

# 🧠 Approach: Vertical Scanning (Character by Character)

### 🔹 Idea:
- Take the **first string** as the reference.
- Compare each character index `i` with all other strings.
- If:
  - any string ends OR  
  - characters mismatch → stop and return prefix so far.
- Otherwise, append the character to the prefix.

This is called **vertical scanning**.

---

### 🔹 Steps:
1. Initialize `res = ""`
2. For each character index `i` of the first string:
   - Compare that character across all strings.
3. If mismatch or out of bounds → return `res`
4. Else append the character to result
5. Return `res`

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
## Step-by-step code execution

Example 1 — ["flower", "flow", "flight"]

Initial values:

-  strs = ["flower","flow","flight"]
-  res = ""
-  first string = "flower", so range(len(strs[0])) → i = 0..5 (indices of "flower")

We go index by index (vertical scanning):

i = 0

- strs[0][0] = 'f'
- Loop through all strings s:
  - s = "flower" → i == len(s)? No. s[0] == 'f' equals strs[0][0]? Yes.
  - s = "flow" → i == len(s)? No. s[0] == 'f' equals 'f'? Yes.
  - s = "flight" → i == len(s)? No. s[0] == 'f' equals 'f'? Yes.
- All match → append 'f' to res.
- res = "f"

i = 1

- strs[0][1] = 'l'
- Check each string:
  - "flower"[1] = 'l' → match
  - "flow"[1] = 'l' → match
  - "flight"[1] = 'l' → match
- All match → append 'l'.
- res = "fl"

i = 2

- strs[0][2] = 'o'
- Check each string:
  - "flower"[2] = 'o' → match
  - "flow"[2] = 'o' → match
  - "flight"[2] = 'i' → mismatch ('i' != 'o')
- On mismatch the inner loop hits if s[i] != strs[0][i]: return res
- Function returns "fl" immediately.

Final returned value: "fl"


---

Example 2 — ["dog","racecar","car"]

Initial:

- strs = ["dog","racecar","car"]
- res = ""
- first string = "dog" → i = 0..2

i = 0

- strs[0][0] = 'd'
- Check:
  - "dog"[0] = 'd' → match
  - "racecar"[0] = 'r' → mismatch ('r' != 'd')
- Mismatch → immediate return res (res is currently "")
- Final returned value: ""

---

## 💡 Time and Space Complexity
- **Time**: O(S), where S is the sum of all characters in all strings (in the worst case).
- **Space**: O(1), extra space (result string grows with prefix but not counted as extra).
