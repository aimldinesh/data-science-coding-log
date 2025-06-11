# 🧲 Problem: Search in Rotated Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1660866790/](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1660866790/)
- **Date Solved**: 2025-06-11
- **Tags**: Binary Search, Array, Divide and Conquer
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given a rotated sorted array of distinct integers nums and a target value target.
- Return the index of target if it is in the array, otherwise return -1.
- You must solve it in O(log n) time.

### 🌰 Examples
```python
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
---

## 🚀 Approach : Binary Search
💡 Intuition
- The array was originally sorted but has been rotated at some pivot.
- That means at any point, one half is always sorted.

- We can use binary search:
     - At each step, check if the left half or right half is sorted.
     - Then check whether the target lies within the sorted part.
     - This narrows the search space to O(log n).

🚀 Approach
- Use two pointers left and right.
- While left <= right:
     - Find the mid index.
     - If nums[mid] == target, return mid.
     - Determine which half is sorted:
          - If nums[left] <= nums[mid], left half is sorted.
               - If target is in the left half → right = mid - 1
               - Else → left = mid + 1
          - Else, right half is sorted.
               - If target is in the right half → left = mid + 1
               - Else → right = mid - 1

- If the loop ends without finding the target, return -1.


---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            # If the target is found, return its index
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the left sorted part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target lies in the left half
                else:
                    left = mid + 1  # Target lies in the right half
            else:
                # Right half must be sorted
                # Check if target lies within the right sorted part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target lies in the right half
                else:
                    right = mid - 1  # Target lies in the left half

        # Target not found, return -1
        return -1
   
```
---
### 🧮 Step-by-step Execution Example
```python
Input: nums = [4,5,6,7,0,1,2], target = 0

🔁 Iteration 1:
- left = 0, right = 6, mid = 3 → nums[mid] = 7
- Left half is sorted (nums[left]=4 <= nums[mid]=7)
- Is target (0) in range [4..7]? ❌ No
- → Move to right half: left = mid + 1 = 4

🔁 Iteration 2:
- left = 4, right = 6, mid = 5 → nums[mid] = 1
- Right half is sorted (nums[mid]=1 <= nums[right]=2)
- Is target (0) in range [1..2]? ❌ No
- → Move to left half: right = mid - 1 = 4

🔁 Iteration 3:
- left = 4, right = 4, mid = 4 → nums[mid] = 0
- Found the target! ✅ Return 4

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
    - because binary search reduces the search space by half each time.
- **Space**: O(1)
    - constant space usage (no recursion or extra data structures).

---
