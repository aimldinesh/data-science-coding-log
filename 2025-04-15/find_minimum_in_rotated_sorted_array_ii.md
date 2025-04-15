# 🧮 Problem: Find Minimum in Rotated Sorted Array II

- **Platform**: [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/1607520420/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/1607520420/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-15
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Given a rotated sorted array nums that may contain duplicates, find the minimum element.You must decrease the overall complexity to better than linear time if possible.

---

## 🚀 My Approach
- Binary Search with Duplicates:
  - Use binary search to minimize the search space.
  - If nums[mid] == nums[right], the side where the minimum lies is uncertain. Reduce the search space by shrinking both ends.
  - If nums[mid] > nums[right], the minimum is in the right half.
  - Otherwise, the minimum is in the left half.

- Handles Duplicates:

  - Special handling is added when nums[left] == nums[mid] == nums[right] — increment the left pointer to continue the search.



---

## 💻 Code (Python)

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  # Initialize pointers
        mid = 0  # Variable to store mid index

        while left < right:  # Continue until the search space reduces to one element
            mid = (left + right) // 2  # Compute the middle index

            if nums[mid] == nums[right]:  # Handle duplicates
                if nums[mid] == nums[left]:  # Check for duplicates on both sides
                    left = left + 1
                else:  # Left side is sorted
                    right = mid
            elif nums[mid] > nums[right]:  # Minimum lies in the right half
                left = mid + 1
            else:  # Minimum lies in the left half
                right = mid

        return nums[left]  # Return the minimum element

```

---

## 💡 Time and Space Complexity
- **Time**: Worst case O(n), due to duplicates. Best/average case O(log n).
- **Space**: O(1), only constant extra space used.
