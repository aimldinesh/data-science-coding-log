# 🧮 Problem: Search in Rotated Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **Submission**: [https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1508345478/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1508345478/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-14
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Given a rotated sorted array `nums` of distinct integers and a target integer `target`, return the index of the target if it exists in the array. Otherwise, return `-1`.
- You must write an algorithm with a time complexity of O(log n).

---

## 🚀 My Approach
1. **Binary Search**: 
   - We will use binary search, but since the array is rotated, we need to adjust our search approach to handle the rotation.
   - We will check whether the left half or the right half is sorted and adjust the search space accordingly.
   - If the target is within the sorted half, we narrow our search to that half; otherwise, we search the other half.

2. **Key Observations**:
   - The array is split into two sorted subarrays due to the rotation.
   - Depending on whether the left or right half is sorted, we can figure out if the target lies in that half and adjust our search space.


---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # If we found the target, return the index
            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within the sorted left portion
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1  # Target is not in the left sorted half
                else:
                    right = mid - 1  # Target is in the left sorted half

            # Otherwise, the right half must be sorted
            else:
                # Check if the target lies within the sorted right portion
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1  # Target is not in the right sorted half
                else:
                    left = mid + 1  # Target is in the right sorted half

        # Target not found, return -1
        return -1
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), because we are performing binary search on the array, and the array is halved each time.
- **Space**: O(1), as we are using only a constant amount of extra space.
