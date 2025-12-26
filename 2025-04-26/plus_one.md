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
## Examples
```python
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```
---

## 🚀 Approach
🧠 Intuition

We simulate how addition works manually:

+ Start from the last digit
+ If the digit is less than 9, simply add 1 and return
+ If the digit is 9, it becomes 0 and we carry over to the next digit
+ If all digits are 9, we add 1 at the front

🧩 Algorithm

1. Traverse the array from right to left
2. If the current digit is < 9, increment it and return the array
3. Otherwise, set it to 0 and continue
4. If all digits were 9, return [1] + digits
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
## 🔍 Example 1 (With Carry Propagation)

Input
```
digits = [1, 2, 9, 9]
```
✅ Step-by-Step Execution

Initial state:
```
digits = [1, 2, 9, 9]
n = 4
```

🔁 Loop Iteration (Right to Left)

Iteration 1

+ i = 3
+ digits[3] = 9
+ Since 9 == 9, set it to 0
```
digits → [1, 2, 9, 0]
```
Iteration 2

+ i = 2
+ digits[2] = 9
+ Again, set it to 0
```
digits → [1, 2, 0, 0]
```
Iteration 3

+ i = 1
+ digits[1] = 2 (< 9)
+ Add 1 → digits[1] = 3

Return result immediately
```
Final Output → [1, 3, 0, 0]
```
✅ Output
```
[1, 3, 0, 0]
```
---
## 🔍 Example 2 (All digits are 9)

Input
```
digits = [9, 9, 9]
```
🔁 Execution
| Index | Value | Action   |
| ----- | ----- | -------- |
| 2     | 9     | set to 0 |
| 1     | 9     | set to 0 |
| 0     | 9     | set to 0 |

After loop:
```
digits = [0, 0, 0]
```

Since all digits were 9, we add 1 at the beginning.

✅ Output
```
[1, 0, 0, 0]
```
---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the number of digits (because we may touch each digit once).
- **Space**: O(1), ignoring the input/output list (in-place modification except in the case of carry).
