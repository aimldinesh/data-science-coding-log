# 🧲 Problem: Remove Duplicates from Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1408230377/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1408230377/)
- **Date Solved**: 2025-05-09
- **Tags**: Array, Two Pointer, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
- Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

---
## Examples
```python
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
---

## 🧠 Intuition
- Since the array is sorted, all duplicates will be adjacent.
- Use two pointers:
   - r scans through the array.
   - l keeps track of the position where the next unique element should be placed.

## 🚀 My Approach
- Start with l = 1, since the first element is always unique.
- For every element from index 1 to end:
   - If the current element is different from the previous one:
        - Assign it to position l.
        - Increment l.
- The value of l will be the count of unique elements.

---

## 💻 Code (Python)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer 'l' to track the position of the next unique element
        l = 1
        
        # Start iterating from the second element (index 1) since the first element is always unique
        for r in range(1, len(nums)):
            # If the current element is different from the previous one, it's a unique element
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]  # Move the unique element to the 'l' position
                l += 1  # Increment 'l' to the next position for a unique element
        
        # Return 'l', which represents the length of the array with unique elements at the start
        return l       
        

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - We iterate through the array once using a single loop.
   - Each element is visited at most once, so the runtime scales linearly with the size of nums.
- **Space**: O(1)
   - The algorithm uses only constant extra space:
      - Two pointers (l and r).
   - No additional data structures are used.
