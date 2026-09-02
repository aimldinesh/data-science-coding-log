# 🧮 Problem: First Bad Version

- **Platform**: [LeetCode](https://leetcode.com/problems/first-bad-version/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/first-bad-version/submissions/1608253146/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/first-bad-version/submissions/1608253146/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version has some bugs.Your goal is to find the first bad version among n versions using the isBadVersion API.

---
## Examples
```
Example 1:
Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
```

## 🚀 Approach
- We use Binary Search to reduce the search space.
- If mid is a bad version, we move the right pointer to mid.
- If mid is not bad, we move the left pointer to mid + 1.
- The loop stops when left == right, which is the first bad version

---

## 💻 Code (Python)

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Versions start from 1

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # First bad version could be at mid or before
            else:
                left = mid + 1  # Bad version must be after mid

        return left  # Left will point to the first bad version

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), We use Binary Search, which repeatedly halves the search space, leading to logarithmic time complexity.
- **Space**: O(1), No extra space is used except for a few variables (left, right, mid), so it's constant space.
