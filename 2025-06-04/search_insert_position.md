# 🧲 Problem: Search Insert Position

- **Platform**: [LeetCode](https://leetcode.com/problems/search-insert-position/description/)
- **Submission**: [https://leetcode.com/problems/search-insert-position/submissions/1653900893/](https://leetcode.com/problems/search-insert-position/submissions/1653900893/)
- **Date Solved**: 2025-06-04
- **Tags**: Binary Search, Array
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be inserted in order.
- You must write an algorithm with O(log n) runtime complexity.

### 🌰 Example:
```python
Example 1:
nput: nums = [1, 3, 5, 6], target = 5
Output: 2

Example 2:
Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Example 3:
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
```
---

## 🚀 Approach : Binary Search
💡 Intuition:
- Since the array is sorted, we can use binary search to efficiently find the target, or determine where it should be inserted if not present.
- Binary search narrows the search space in half at each step, achieving logarithmic time.

🧠 Approach:
- Set two pointers: left = 0, right = len(nums) - 1.
- While left <= right:
     - Calculate mid = (left + right) // 2.
     - If nums[mid] == target, return mid.
     - If nums[mid] < target, search the right half: left = mid + 1.
     - If nums[mid] > target, search the left half: right = mid - 1.

- If the loop ends and target isn't found, return left (the insertion index).
---

## 💻 Code (Python)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return the index
            
            # If the middle element is less than the target, search in the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # If the middle element is greater than the target, search in the left half
            else:
                right = mid - 1
        
        # If the target is not found, return the insertion point (left)
        return left

```

---

## 💡 Time and Space Complexity
- **Time**: O(O(log n))
- **Space**: O(1)
