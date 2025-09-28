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

## 🔹 Approach

1. **Observation:**  
   - The largest odd-valued substring is always obtained by **trimming the rightmost even digits** from the number until the last digit is odd.  

2. **Steps:**  
   - Start from the end of the string.  
   - Remove digits from the end while the last digit is even.  
   - Return the resulting string.  
   - If all digits are even, return an empty string `""`.

3. **Why it works:**  
   - Any prefix of the string that ends with an odd digit forms a contiguous odd substring.  
   - To get the **largest value**, we keep as many digits from the start as possible.

---

## 🔹 Code (Python)

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Start from the end and trim even digits
        i = len(num) - 1
        while i >= 0 and int(num[i]) % 2 == 0:
            i -= 1
        # If no odd digit found, return empty string
        return num[:i+1]

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - We may need to check each digit from the end once.
- **Space**: O(1) 
    - No extra space is used aside from pointers and slicing.
