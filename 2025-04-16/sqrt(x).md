# 🧮 Problem: Sqrt(x)

- **Platform**: [LeetCode](https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Implement a function that computes the square root of a non-negative integer `x`, and returns the integer part of the square root.


---
## Examples
```python
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```
---

## 🚀 Approach : Binary Search
🧠 Intuition

Square root is monotonically increasing — so binary search works perfectly. Search for the largest integer mid where mid² ≤ x. Since we want the floor of the square root, when there's no exact answer, right ends up pointing to the best integer answer.
```python
x = 8  →  √8 = 2.82...  →  floor = 2

Try mid=1 → 1²=1  < 8  → go right
Try mid=2 → 2²=4  < 8  → go right
Try mid=3 → 3²=9  > 8  → go left
→ right = 2 ✅
```
---

📌 Approach

1. Handle base case — x < 2 returns x directly
2. Binary search between left=0 and right=x
3. At each mid:
   - mid² == x → exact answer, return mid
   - mid² < x  → too small → left = mid + 1
   - mid² > x  → too big  → right = mid - 1

4. Loop exits when left > right → return right

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
