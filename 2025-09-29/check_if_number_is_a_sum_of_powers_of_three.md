# 🧲 Problem: Check if Number is a Sum of Powers of Three

- **Platform**: [LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/)
- **Submission**: [https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/submissions/1786280868/](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/submissions/1786280868/)
- **Date Solved**: 2025-09-29
- **Tags**: DSA, Math
- **Difficulty**: Medium

---


## ✅ Problem Statement
Given an integer `n`, return `True` if it can be represented as the **sum of distinct powers of three**.  
Otherwise, return `False`.

---

## 🔹 Examples

**Example 1:**  
Input: `n = 12`  
Output: `true`  
Explanation: 12 = 3¹ + 3² = 3 + 9  

**Example 2:**  
Input: `n = 91`  
Output: `true`  
Explanation: 91 = 3⁰ + 3² + 3⁴ = 1 + 9 + 81  

**Example 3:**  
Input: `n = 21`  
Output: `false`  

---

## 🔹 Approach

This is essentially checking whether `n` has a **valid base-3 representation** where all digits are either `0` or `1` (no `2`s).  

Reason:
- Each digit in base-3 corresponds to a power of three.
- If a digit is `2`, it means we are trying to use the same power of three twice, which is **not allowed**.

### Steps:
1. While `n > 0`:
   - If `n % 3 == 2`, return `False` (invalid, since digit = 2).  
   - Otherwise, divide `n //= 3`.  
2. If loop finishes, return `True`.

---

## 🔹 Code (Python with Comments)

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Convert number into base 3 and check digits
        while n > 0:
            if n % 3 == 2:  # digit '2' not allowed
                return False
            n //= 3
        return True

```
---

## 🔹 Example Walkthrough
```text
Example 1:

n = 12

Step 1: Convert 12 into base 3.

 12 ÷ 3 = 4 remainder 0
 4 ÷ 3 = 1 remainder 1
 1 ÷ 3 = 0 remainder 1

So, 12 = (110)_3.

Step 2: Check digits: 110 has only 0 or 1. ✅
So, 12 = 3² + 3¹ = 9 + 3.
Answer = True

----
Example 2:

n = 21

Step 1: Convert 21 into base 3.

  21 ÷ 3 = 7 remainder 0
  7 ÷ 3 = 2 remainder 1
  2 ÷ 3 = 0 remainder 2

So, 21 = (210)_3.

Step 2: Check digits: 210 has a 2. ❌
That means we’d need 2*(3²) = 18 in the sum, which repeats a power. Not allowed.
Answer = False

```
---

## 💡 Time and Space Complexity
- **Time**: O(log₃ n)
    - We divide n by 3 each step.
- **Space**: O(1)
    - Constant extra memory.
