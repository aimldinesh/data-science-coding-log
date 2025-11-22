# 🧮 Problem: Binary Search

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/binary-search/submissions/1481236117/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/binary-search/submissions/1481236117/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-12
- **Tags**: DSA, Array, Binary Search

---

## ✅ Problem Statement
- Given a **sorted** array of integers `nums` and an integer `target`, return the **index** of `target` if it is in the array. If not, return `-1`.You must write an algorithm with **O(log n)** runtime complexity.

---
## Examples
```python
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```
---

## 🚀 My Approach
- Since the array is sorted, I used **Binary Search**.
- I maintained two pointers: `left` and `right`.
- I repeatedly calculated the middle index `mid`, and compared `nums[mid]` with the `target`.
- If found, I returned `mid`.
- If the `target` was smaller, I searched the **left** subarray.
- If larger, I searched the **right** subarray.

---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # Binary search loop: continue while the search space is valid
        while left <= right:
            mid = (left + right) // 2  # Calculate mid index

            # If target is found at mid, return the index
            if nums[mid] == target:
                return mid
            # If target is smaller than mid element, search left half
            elif nums[mid] > target:
                right = mid - 1
            # If target is greater, search right half
            else:
                left = mid + 1

        # Target not found in the array
        return -1  
```

---

## 💡 Time and Space Complexity
- **Time**: O(logn), Efficient search using binary strategy.
- **Space**: O(1), Only constant extra space is used.
