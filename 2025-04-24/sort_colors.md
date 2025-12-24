# 🧲 Problem: Sort Colors

- **Platform**: [LeetCode](https://leetcode.com/problems/sort-colors/description/)
- **Submission**: [https://leetcode.com/problems/sort-colors/submissions/1616706458/](https://leetcode.com/problems/sort-colors/submissions/1616706458/)
- **Date Solved**: 2025-04-24
- **Tags**: Array, Two Pointers, Sorting
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent and in the order red (0), white (1), and blue (2).You must solve this problem **without using the library's sort function**.


---

## Examples
```
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
```
---

## 🚀 Approach : Dutch National Flag Algorithm
- Use three pointers: low, current, and high.
- Traverse the array:
   - If the element is 0, swap it with the element at low, and move both low and current.
   - If the element is 2, swap it with the element at high and decrement high.
   - If the element is 1, just move current.

---

## 💻 Code (Python)

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, current, high = 0, 0, len(nums) - 1

        while current <= high:
            if nums[current] == 0:
                # Swap current with low and move both pointers
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 2:
                # Swap current with high and move the high pointer
                nums[high], nums[current] = nums[current], nums[high]
                high -= 1
            else:  # nums[current] == 1
                # Just move the current pointer
                current += 1
               
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), single pass through the array
- **Space**: O(1), in-place sorting with constant space
