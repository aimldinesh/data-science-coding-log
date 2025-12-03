# 🧮 Problem: Valid Perfect Square

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-perfect-square/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/valid-perfect-square/submissions/1608349630/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/valid-perfect-square/submissions/1608349630/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Given a positive integer `num`, write a function that returns `True` if `num` is a perfect square else `False`.

---
## Examples
```python
Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

```
---


## 🚀 My Approach
We can use **Binary Search** to efficiently check if there exists an integer `x` such that `x * x == num`.

- Set search boundaries: `left = 1`, `right = num`.
- While `left <= right`, calculate the mid and square it.
- If the square is equal to `num`, it's a perfect square.
- Otherwise, adjust the search space based on whether the square is less than or greater than `num`.


---

## 💻 Code (Python)

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:  # Handle small numbers
            return True

        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:  # Perfect square found
                return True
            elif square < num:  # Search in the right half
                left = mid + 1
            else:  # Search in the left half
                right = mid - 1

        return False  # No perfect square found

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), due to binary search.
- **Space**: O(1), no extra space used.
