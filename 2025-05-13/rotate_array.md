# 🧲 Problem: Rotate Array

- **Platform**: [LeetCode](https://leetcode.com/problems/rotate-array/description/)
- **Submission**: [https://leetcode.com/problems/rotate-array/submissions/1632882867/](https://leetcode.com/problems/rotate-array/submissions/1632882867/)
- **Date Solved**: 2025-05-13
- **Tags**: Array, Two Pointers, In-place, Reversal
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
🧾 Examples:

```python
Example 1:
Input:  nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]  
Explanation:  
rotate 1 step  -> [7,1,2,3,4,5,6]  
rotate 2 steps -> [6,7,1,2,3,4,5]  
rotate 3 steps -> [5,6,7,1,2,3,4]  

Example 2: 
Input:  nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]  
Explanation:  
rotate 1 step  -> [99,-1,-100,3]  
rotate 2 steps -> [3,99,-1,-100]  
```
---
## 🧠 Intuition
- To rotate the array to the right by k positions:
    - The last k elements come to the front.
    - The rest shift to the right.
    - We can achieve this efficiently using array reversal.

## 🚀 Approach: Reverse In-Place (O(1) Space)
🔸 Steps:
     - Normalize k using modulo to ensure it's within array bounds.
     - Reverse the entire array.
     - Reverse the first k elements.
     - Reverse the remaining n - k elements.

---

## 💻 Code (Python)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Ensure k is within bounds of the array
        k = k % len(nums)

        # Step 1: Reverse the entire array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: Reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: Reverse the remaining elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each element is visited at most twice during the reverse steps.
- **Space**: O(1)
    - The rotation is done in-place, with no extra space used.
