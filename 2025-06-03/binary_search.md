# 🧲 Problem: Binary Search

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-search/description/)
- **Submission**: [https://leetcode.com/problems/binary-search/submissions/1652773834/](https://leetcode.com/problems/binary-search/submissions/1652773834/)
- **Date Solved**: 2025-06-03
- **Tags**: Binary Search, Array
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an array of integers nums which is sorted in ascending order, and an integer target, return the index of target if it is in the array.If not, return -1.
- You must write an algorithm with O(log n) runtime complexity.

### 🌰 Example:
```python
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation:nums[4] == 9, so return 4.
```
 ---

## 🚀 Approach
💡 Intuition:
- Since the array is sorted, we can efficiently find the target using Binary Search instead of checking each element one by one.
- Binary search reduces the search range by half in each iteration, achieving logarithmic time complexity.

🧠 Approach:
- Set two pointers: left = 0, right = len(nums) - 1.
- While left <= right:
     - Compute mid = (left + right) // 2.
     - If nums[mid] == target, return mid.
     - If nums[mid] > target, move right = mid - 1.
     - If nums[mid] < target, move left = mid + 1.

- If loop ends, target is not in the array → return -1.

---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1

        # Continue searching while the left pointer does not cross the right
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid
            # If the middle element is greater than the target, 
            # narrow the search to the left half
            elif nums[mid] > target:
                right = mid - 1
            # If the middle element is less than the target,
            # narrow the search to the right half
            else:
                left = mid + 1

        # If the loop ends, the target is not in the list
        return -1

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
    - Because the search space is halved each time.
- **Space**: O(1)
    - Only a few pointers (left, right, mid) are used regardless of input size.
