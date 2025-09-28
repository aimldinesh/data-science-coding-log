# 🧲 Problem: Sum of Square Numbers

- **Platform**: [LeetCode](https://leetcode.com/problems/sum-of-square-numbers/description/)
- **Submission**: [https://leetcode.com/problems/sum-of-square-numbers/submissions/1785320932/](https://leetcode.com/problems/sum-of-square-numbers/submissions/1785320932/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given a non-negative integer `c`, determine if there exist two integers `a` and `b` such that:  

\[
a^2 + b^2 = c
\]

---

## 🔹 Examples

**Example 1:**  
Input: `c = 5`  
Output: `true`  
Explanation: 1² + 2² = 5  

**Example 2:**  
Input: `c = 3`  
Output: `false`  
Explanation: No integers `a` and `b` exist such that a² + b² = 3.  

---

## 🔹 Approach

We use the **two-pointer technique**:

1. Initialize `left = 0` and `right = int(sqrt(c))`.  
   - Because `a` and `b` cannot be larger than `sqrt(c)`.  
2. Compute `total = left² + right²`.  
   - If `total == c` → return `True`.  
   - If `total > c` → decrease `right` (to reduce sum).  
   - If `total < c` → increase `left` (to increase sum).  
3. Repeat until `left > right`.  
4. If no match found → return `False`.

---

## 🔹 Code (Python)

```python
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Two-pointer approach
        left, right = 0, int(sqrt(c))

        while left <= right:
            total = left * left + right * right

            if total > c:
                # Too large, decrease right
                right -= 1
            elif total < c:
                # Too small, increase left
                left += 1
            else:
                # Found: left^2 + right^2 == c
                return True

        # No such pair found
        return False
```
---

## 💡 Time and Space Complexity
- **Time**: 
    - At most, left and right move across 0 → sqrt(c).
    - Complexity = O(√c).
- **Space**: O(1)
    - Only constant extra space is used.
