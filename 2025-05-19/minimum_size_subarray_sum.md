# 🧲 Problem: Minimum Size Subarray Sum

- **Platform**: [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/description/)
- **Submission**: [https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1638263836/](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1638263836/)
- **Date Solved**: 2025-05-19
- **Tags**: Array, Sliding Window, Two Pointers, Prefix Sum
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an array of positive integers `nums` and an integer `target`, return the **minimal length of a contiguous subarray** of which the sum is greater than or equal to `target`.If there is no such subarray, return 0.

---

### 🔍 Examples

```python
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length of 2.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```
---

## 🚀 Approach : Sliding Window
🔸 Idea:
- Use two pointers (l and r) to create a sliding window.
- Expand the window by moving the right pointer and adding nums[r] to the total.
- When the sum of the window is ≥ target, try to shrink the window from the left to find the minimal size.
- Keep track of the smallest valid window size encountered.

---

## 💻 Code (Python)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0  # Initialize left pointer and current total sum
        res = float("inf")  # Set result as infinity (to find minimum length)

        # Right pointer expands the window
        for r in range(len(nums)):
            total += nums[r]  # Add current number to total

            # Try shrinking the window from the left as long as total >= target
            while total >= target:
                res = min(res, r - l + 1)  # Update minimum length
                total -= nums[l]  # Remove the element at the left
                l += 1  # Move the left pointer forward

        # If no valid subarray found, return 0
        return 0 if res == float("inf") else res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each element is added and removed from the window at most once.
- **Space**: O(1)
    - Only pointers and a few variables used.
