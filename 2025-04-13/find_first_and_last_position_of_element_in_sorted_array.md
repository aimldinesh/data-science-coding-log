# 🧮 Problem: Find First and Last Position of Element in Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- **Submission**: [https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1605353741/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1605353741/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Given an array of integers `nums` sorted in non-decreasing order, and a target value `target`, return the starting and ending position of `target` in the array.If `target` is not found in the array, return `[-1, -1]`.

---
```python
## Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

```
---

## 🚀 Approach : Binary Search
🧠 Intuition
When a target appears multiple times, standard binary search stops at any occurrence. To find the first and last positions, run binary search twice with different biases — once pushing left to find the leftmost, once pushing right to find the rightmost. The key trick: don't stop when you find the target, keep searching in the biased direction.
```
nums = [5, 7, 7, 8, 8, 10]  target = 8

Standard search → lands on index 3 or 4 (unpredictable)
Left  biased    → always lands on index 3 (first 8)
Right biased    → always lands on index 4 (last 8)
```
---
📌 Approach

1. Call binSearch twice — once with leftBias=True, once with leftBias=False
2. Inside binSearch:
   + Standard binary search until target == nums[mid]
   + On match → record i = mid but don't stop
     + leftBias=True  → right = mid - 1 (keep searching left)
     + leftBias=False → left = mid + 1  (keep searching right)

3. Return [leftmost_index, rightmost_index]

## 💻 Code (Python)

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the leftmost and rightmost positions of the target
        left = self.binSearch(nums, target, True)  # Left biased search
        right = self.binSearch(nums, target, False)  # Right biased search
        return [left, right]

    def binSearch(self, nums, target, leftBias):
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        i = -1  # Default value if target is not found

        # Binary search loop
        while left <= right:
            mid = (left + right) // 2  # Calculate middle index
            
            if target > nums[mid]:  # Target is on the right side
                left = mid + 1
            elif target < nums[mid]:  # Target is on the left side
                right = mid - 1
            else:
                i = mid  # Record current index of target
                
                # Adjust search bounds based on bias
                if leftBias:  # Move left for leftmost target
                    right = mid - 1
                else:  # Move right for rightmost target
                    left = mid + 1
        return i  # Return the leftmost or rightmost index of the target based on bias

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), Two binary searches → O(log n) + O(log n) = O(log n)
- **Space**: O(1), Constant space used.
