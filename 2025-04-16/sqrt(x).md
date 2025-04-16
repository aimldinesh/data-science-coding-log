# 🧮 Problem: Sqrt(x)

- **Platform**: [LeetCode](https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Implement a function that computes the square root of a non-negative integer `x`, and returns the integer part of the square root.


---

## 🚀 My Approach
We can use **Binary Search** to find the integer part of the square root efficiently.

- For `x = 0` or `x = 1`, the square root is `x` itself.
- Otherwise, initialize a search range from `0` to `x`.
- While `left <= right`, calculate the middle point `mid` and square it.
- If `mid^2 == x`, then `mid` is the exact square root.
- If `mid^2 < x`, then search in the right half of the range.
- If `mid^2 > x`, then search in the left half of the range.
- When the loop exits, `right` points to the largest integer such that `right^2 <= x`.


---

## 💻 Code (Python)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle base cases for small inputs
        if x < 2:  # For x = 0 or 1, the square root is x itself
            return x

        # Initialize the search range
        left, right = 0, x

        while left <= right:
            # Find the middle of the current range
            mid = (left + right) // 2
            square = mid * mid  # Calculate the square of mid

            if square == x:  # If mid squared equals x, we've found the exact square root
                return mid
            elif square < x:  # If mid squared is less than x, move to the right half
                left = mid + 1
            else:  # If mid squared is greater than x, move to the left half
                right = mid - 1

        # When the loop exits, right points to the largest integer such that right^2 <= x
        return right

```

---

## 💡 Time and Space Complexity
- **Time**: O(log x), due to the binary search.
- **Space**: O(1), no extra space used.
