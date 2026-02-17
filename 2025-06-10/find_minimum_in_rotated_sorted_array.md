# 🧲 Problem: Find Minimum in Rotated Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1659809903/](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1659809903/)
- **Date Solved**: 2025-06-10
- **Tags**: Binary Search, Array
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given a rotated sorted array nums of distinct integers. Your task is to find the minimum element in the array.
- You must solve it in O(log n) time.

### Examples
```python
Example 1:
input: nums = [3,4,5,1,2]

Output: 1

Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]

Output: 0

Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]

Output: 11

Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

```

---

## 🚀 Approach : Binart Search
💡 Intuition
- The array was originally sorted, but has been rotated. So:
- One part of the array is sorted (in increasing order).
- The minimum element is the pivot point — the place where the rotation happened.
- We can use binary search to find this pivot efficiently.

🚀 Approach
- Use two pointers: left = 0, right = len(nums) - 1.
- While left < right:
     - Find mid = (left + right) // 2.
     - If nums[mid] > nums[right], the minimum must be in the right half (excluding mid).
     - Else, the minimum is in the left half (including mid).

- When the loop ends, left == right and points to the minimum element.
---

## 💻 Code (Python)

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize binary search pointers
        left, right = 0, len(nums) - 1

        # Binary search continues until the range is narrowed to one element
        while left < right:
            mid = (left + right) // 2  # Compute the middle index

            # If mid element is greater than the rightmost element,
            # the minimum is in the right half (excluding mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Else, the minimum is in the left half (including mid)
                right = mid

        # After the loop, left == right and points to the minimum element
        return nums[left]
```

---
### 🧮 Step-by-Step Execution:
- Let's track:
    - left, mid, right pointers
    - values at these positions
    - decision made in each step

```python
- Input: nums = [4, 5, 6, 7, 0, 1, 2]

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[right]` | Decision                                             |
| ---- | ------ | ------- | ----- | ----------- | ------------- | ---------------------------------------------------- |
| 1    | 0      | 6       | 3     | 7           | 2             | `7 > 2` → `min` in right half → `left = mid + 1 = 4` |
| 2    | 4      | 6       | 5     | 1           | 2             | `1 < 2` → `min` in left half → `right = mid = 5`     |
| 3    | 4      | 5       | 4     | 0           | 1             | `0 < 1` → `min` in left half → `right = mid = 4`     |

- Loop exits when left == right == 4. So
Return nums[4] = 0

```
---


## 💡 Time and Space Complexity
- **Time**: O(log n)
- **Space**: O(1)

---

## 🚀 Approach : Brute Force
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
```
---
## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(1)

---

