# 🧲 Problem: Largest Odd Number in String

- **Platform**: [LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/description/)
- **Submission**: [https://leetcode.com/problems/largest-odd-number-in-string/submissions/](https://leetcode.com/problems/largest-odd-number-in-string/submissions/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given a string `num`, representing a large integer.  
Return the **largest-valued odd integer** (as a string) that is a **non-empty substring** of `num`.  
Return an empty string `""` if no odd integer exists.

> Note: A substring is a contiguous sequence of characters within a string.

---

## 🔹 Examples

**Example 1:**  
Input: `num = "52"`  
Output: `"5"`  

Explanation: The non-empty substrings are `"5"`, `"2"`, and `"52"`. `"5"` is the only odd number.

**Example 2:**  
Input: `num = "4206"`  
Output: `""`  
Explanation: There are no odd numbers in `"4206"`.

**Example 3:**  
Input: `num = "35427"`  
Output: `"35427"`  
Explanation: `"35427"` is already an odd number.

---


---

## 🧠 Approach 1: Brute Force (Check All Substrings)

### 🔹 Idea:
Generate **all possible substrings**, check which are **odd numbers**, and return the **largest one**.

### 🔹 Steps:
1. Iterate through all possible substring start (`i`) and end (`j`) indices.
2. Convert each substring to an integer.
3. Check if the number is **odd** → last digit in `1, 3, 5, 7, 9`.
4. Keep track of the **largest odd number** found.
5. Return it as a string. If none found, return `""`.

---

### 🧾 Code (Brute Force Approach)
```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd = ""  # Store the largest odd substring

        # Generate all possible substrings
        for i in range(len(num)):
            for j in range(i + 1, len(num) + 1):
                sub = num[i:j]

                # Check if substring ends with an odd digit
                if int(sub[-1]) % 2 == 1:
                    # Update if this is a larger odd number
                    if max_odd == "" or int(sub) > int(max_odd):
                        max_odd = sub

        return max_odd
```

---

## 💡 Time and Space Complexity
- **Time**: O(n²)
    - Checking every substring
- **Space**: O(1) 
    - Only storing a few variables

---

## ⚡ Approach 2: Efficient Approach (Rightmost Odd Digit)

### Key Insight:
👉 The **largest odd number substring** always starts from the **beginning of the string**  
and ends at the **last odd digit** in `num`.

### Steps:
1. Traverse the string **from the end**.
2. Find the **first odd digit** (1, 3, 5, 7, or 9).
3. Return the substring from `0` to that index (inclusive).
4. If no odd digit is found, return an empty string `""`.

---

## ✅ Code Implementation (Efficient Approach)

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Traverse from the end of the string
        for i in range(len(num) - 1, -1, -1):
            # Check if current digit is odd
            if int(num[i]) % 2 == 1:
                # Return substring up to this index
                return num[:i + 1]
        # No odd number found
        return ""
```
---
### step by step execution with example
```python
Example: num = "35427"

Start from right:
  '7' → odd ✅
Return substring num[:5] → "35427"
Output: "35427"

---------------------

Example: num = "4206"

Check digits from end:
  '6' even
  '0' even
  '2' even
  '4' even
No odd found → return ""
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Single pass through the string
- **Space**: O(1) 
    - Constant extra space
---

## 🧩 Summary
| Approach    | Description                        | Time  | Space |
| ----------- | ---------------------------------- | ----- | ----- |
| Brute Force | Check all substrings               | O(n²) | O(1)  |
| Efficient   | Scan from right for last odd digit | O(n)  | O(1)  |

