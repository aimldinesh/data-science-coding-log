# 🧲 Problem: Plus One

- **Platform**: [LeetCode](https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/plus-one/submissions/1618290400/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/plus-one/submissions/1618290400/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-04-26
- **Tags**: Array, Math, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
- You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer.The digits are ordered from most significant to least significant.You need to increment the integer by one and return the resulting array of digits.


---

## 🚀 Approach
- Start from the last digit and move backward.
- If the current digit is less than 9, simply add 1 and return the list immediately (no carry needed).
- If the digit is 9, set it to 0 and continue to the previous digit (carry the 1).
- If you finish processing all digits (meaning all were 9s), prepend a 1 at the beginning (e.g., [9,9,9] → [1,0,0,0]).

---

## 💻 Code (Python)

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)  # Get the length of the digits array

        # Traverse the list from the last digit to the first
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just add 1 and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, return the result

            # If the digit is 9, it becomes 0 and we continue to check the previous digit
            digits[i] = 0

        # If we have gone through all digits and they were all 9s, prepend 1 at the start
        return [1] + digits

```

---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the number of digits (because we may touch each digit once).
- **Space**: O(1), ignoring the input/output list (in-place modification except in the case of carry).
