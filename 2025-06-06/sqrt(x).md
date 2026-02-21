# 🧲 Problem: Sqrt(x)

- **Platform**: [LeetCode](https://leetcode.com/problems/sqrtx/description/)
- **Submission**: [https://leetcode.com/problems/sqrtx/submissions/1655737451/](https://leetcode.com/problems/sqrtx/submissions/1655737451/)
- **Date Solved**: 2025-06-06
- **Tags**: Binary Search, Math
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a non-negative integer `x`, compute and return the **square root of `x`**. Since the return type is an integer, the **decimal digits are truncated**, and only the **integer part** of the result is returned.

### 🌰 Examples
```python
Example 1:

Input: x = 4
Output: 2
Explanation: √4 = 2

Example 2:

Input: x = 8
Output: 2
Explanation: √8 ≈ 2.828... → Truncate to 2
```

---

## 🚀 Approach 1 : Brute Force
💡 Intuition
- The square root of a number x lies between 1 and x.
- We can iterate from 1 up to x, and for each i, check if i * i > x.
- The previous i that satisfied i * i ≤ x will be the correct result.

🚶 Approach: Linear Scan
- Start a loop from i = 1 up to x.
- For each i, compute i * i.
    - If i * i > x, then return the previous value i - 1 as the square root.
- If loop ends (when x is 1), return the last value of res.
---

## 💻 Code (Python)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Special case: square root of 0 is 0
        if x == 0:
            return 0

        res = 1  # Initialize result
        # Loop from 1 to x to find the integer square root
        for i in range(1, x + 1):
            if i * i > x:
                # If i squared exceeds x, the previous i (stored in res) is the answer
                return res
            res = i  # Update result to current i

        return res  # Handles perfect squares like x = 1

```

---

## 💡 Time and Space Complexity
- **Time**: O(√x)
    - In the worst case, we iterate up to √x times until i*i > x.
- **Space**: O(1)
    - Constant extra space usage — no additional data structures are used.

---
## 🚀 Approach 2 :  Binary Search
💡 Intuition
- We want to find the **largest integer** `r` such that `r * r ≤ x`.  
- This is a **monotonic condition**, which makes **Binary Search** a suitable approach.

🧠 Approach:
1. Initialize two pointers: `left = 0`, `right = x`.
2. Use binary search to find the integer whose square is closest to `x` but not more than `x`.
3. For each `mid` value:
   - If `mid * mid == x`: return `mid`.
   - If `mid * mid < x`: move right and store `mid` as a potential result.
   - If `mid * mid > x`: move left.
4. After the loop, return the last stored valid `mid` (`res`).

---

## 💻 Code (Python)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize binary search boundaries
        left, right = 0, x
        res = 0  # To store the result (integer part of sqrt)

        while left <= right:
            mid = left + ((right - left) // 2)  # Avoid overflow (better than (left + right)//2)

            if mid ** 2 > x:
                # If mid squared is too large, move left
                right = mid - 1
            elif mid ** 2 < x:
                # If mid squared is too small, move right
                left = mid + 1
                res = mid  # Store potential answer
            else:
                # Found exact square root
                return mid

        # Return the integer part of the square root
        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(log x)
    - Uses binary search to reduce the range logarithmically.
- **Space**: O(1)
    - Constant space usage — no additional data structures.

---
## 🚀 Approach 3 : In-Built Function

---

## 💻 Code (Python)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
```

---

## 💡 Time and Space Complexity
- **Time**: O(1)
- **Space**: O(1)
