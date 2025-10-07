# 🧲 Problem: Split Array Largest Sum

- **Platform**: [LeetCode](https://leetcode.com/problems/split-array-largest-sum/description/)
- **Submission**: [https://leetcode.com/problems/split-array-largest-sum/submissions/1663009005/](https://leetcode.com/problems/split-array-largest-sum/submissions/1663009005/)
- **Date Solved**: 2025-06-13
- **Tags**: Array, Binary Search, DP
- **Difficulty**: Hard

---

## ✅ Problem Statement
- You are given an integer array nums and an integer k.
- Split the array into k non-empty contiguous subarrays such that the largest sum among these subarrays is minimized.
- Return the minimum possible value of this largest sum.

### 🌰 Examples
```python
Example 1:
Input: nums = [7,2,5,10,8], k = 2  
Output: 18
Explanation:
We can split the array into two subarrays in multiple ways:

[7,2,5] and [10,8] → max sum = 18 ✅

[7,2] and [5,10,8] → max sum = 23

[7] and [2,5,10,8] → max sum = 25

Minimum possible largest subarray sum = 18

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9

Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

```
---

## 🚀 Approach : Binary Search
💡 Intuition
- We want to split the array such that the maximum subarray sum (among the splits) is as small as possible.
- The problem turns into:
    ➤ What is the minimum "largest subarray sum" achievable with at most k splits?
- We can apply binary search on the answer!


🚀 Approach
- The smallest possible largest subarray sum is the maximum element in the array.
- The largest possible largest subarray sum is the sum of the entire array.
- Use binary search between those two boundaries.
- For each mid, check if it's possible to split the array with that maximum subarray sum using a helper function.
- If it’s possible → try smaller values (search left).
- If not → we need larger value (search right).
---

## 💻 Code (Python)

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Helper function to check if we can split nums into ≤ k subarrays
        # such that the largest subarray sum is ≤ 'max_allowed_sum'
        def isPossible(max_allowed_sum):
            subarrays = 1
            current_sum = 0

            for num in nums:
                current_sum += num
                if current_sum > max_allowed_sum:
                    subarrays += 1
                    current_sum = num  # Start a new subarray
                    if subarrays > k:
                        return False  # Too many subarrays
            return True

        # Binary Search boundaries
        left, right = max(nums), sum(nums)  # Min and max possible largest subarray sum
        result = right

        # Binary Search to find minimum possible "largest subarray sum"
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                result = mid  # Try to minimize the result
                right = mid - 1
            else:
                left = mid + 1

        return result
```

---

## 💡 Time and Space Complexity
- **Time**: O(n * log(sum - max))
    - here n = len(nums),
    - sum = total sum of nums,
    - max = max element in nums
- **Space**: O(1)
    - Only constant extra space is used — no additional data structures or recursion stack.
