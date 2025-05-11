# 🧲 Problem: Merge Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/merge-sorted-array/submissions/1628515387/](https://leetcode.com/problems/merge-sorted-array/submissions/1628515387/)
- **Date Solved**: 2025-05-08
- **Tags**: Array, Two Pointers , DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of initialized elements in `nums1` and `nums2`, respectively.
Merge `nums2` into `nums1` as one sorted array **in-place**.

### 🔍 Example

```python
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]
```
---
## 🧠 Intuition
- Start merging from the end to avoid overwriting elements in nums1.
- Use two pointers from the back of nums1 and nums2, and a third pointer to place elements from the back.
## 🚀 Approach
- Initialize a pointer last at the end of the merged array.
- Compare elements from the back of both arrays and place the larger one at last.
- After one array is exhausted, copy any remaining elements from nums2 (since nums1’s remaining elements are already in place).

---

## 💻 Code (Python)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start merging from the end
        last = m + n - 1

        # Compare elements from the back of both arrays
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If any elements remain in nums2, copy them
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

```

---

## 💡 Time and Space Complexity
- **Time**: O(m + n)
   - We traverse each element of nums1 and nums2 at most once.
   - In the worst case, we might need to check all m and n elements.
   - So total work done is linear with respect to the size of both arrays.
- **Space**: O(1)
   - The merging is done in-place, i.e., within the given nums1 array.
   - No extra arrays or data structures are used.
   - Thus, the algorithm uses constant additional space.
