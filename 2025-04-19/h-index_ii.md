# 🧲 Problem: H-Index II

- **Platform**: [LeetCode](https://leetcode.com/problems/h-index-ii/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/h-index-ii/submissions/1611514197/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/h-index-ii/submissions/1611514197/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-19
- **Tags**: Array, Binary Search, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an array of integers `citations` where `citations[i]` is the number of citations of the `i-th` paper, return the **h-index** of the researcher.

The **h-index** is the maximum value such that the researcher has published at least `h` papers with `h` or more citations.


---

## 🚀 My Approach : Binary Search
### 💡 Key Insight:
- The **h-index** is the largest integer `h` such that there are at least `h` papers with at least `h` citations.
- The array is sorted in ascending order of citations.
- We can use **binary search** to efficiently find the **h-index** by looking for the point where the number of citations is greater than or equal to `n - mid`, where `mid` is the middle index of the array.


---

## 💻 Code (Python)

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)  # Total number of papers
        left, right = 0, n - 1

        # Binary search to find the h-index
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] < n - mid:
                left = mid + 1  # Move to the right half
            else:
                right = mid - 1  # Move to the left half

        # The h-index is calculated as n - left
        return n - left
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), for binary search.
- **Space**: O(1), (constant space
