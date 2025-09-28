# 🧲 Problem: Ugly Number

- **Platform**: [LeetCode](https://leetcode.com/problems/ugly-number/description/)
- **Submission**: [https://leetcode.com/problems/ugly-number/submissions/1785296132/](https://leetcode.com/problems/ugly-number/submissions/1785296132/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math
- **Difficulty**: Easy

---

# 263. Ugly Number

## ✅ Problem Statement
An **ugly number** is a positive integer whose **prime factors** are limited to **2, 3, and 5**.  

Given an integer `n`, return `True` if `n` is an **ugly number**, otherwise return `False`.

---

## 🔹 Examples

**Example 1:**  
Input: `n = 6`  
Output: `true`  
Explanation: 6 = 2 × 3  

**Example 2:**  
Input: `n = 1`  
Output: `true`  
Explanation: 1 is considered an ugly number by convention.  

**Example 3:**  
Input: `n = 14`  
Output: `false`  
Explanation: 14 = 2 × 7 (7 is not allowed).  

---

## 🔹 Approach

1. If `n <= 0`, return `False` (since only **positive** integers can be ugly numbers).  
2. Keep dividing `n` by **2, 3, and 5** as long as it is divisible.  
3. After removing all factors of 2, 3, and 5, check if the result is **1**.  
   - If yes → it's an ugly number.  
   - If not → it has some other prime factor → return False.  

---

## 🔹 Code (Python)

```python
class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Keep dividing n by 2, 3, and 5
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p  # divide out the factor completely

        # After removing factors of 2, 3, and 5, n should be 1
        return n == 1
```

---

## 💡 Time and Space Complexity
- **Time**:
    - In the worst case, we keep dividing by 2 until n = 1.
    - That takes O(logn).
- **Space**: O(1)
    - Only a few variables are used.
