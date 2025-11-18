# 🧮 Problem: Concatenation of Array

- **Platform**: [LeetCode](https://leetcode.com/problems/concatenation-of-array/)
- **Submission**: [https://leetcode.com/problems/concatenation-of-array/submissions/1601284485/](https://leetcode.com/problems/concatenation-of-array/submissions/1601284485/)
- **Date Solved**: 2025-04-09
- **Tags**: DSA, Array, Concatenation

---

## ✅ Problem Statement
Given an integer array `nums` of length `n`, return an array `ans` of length `2n` such that `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n`.

---
## Examples:
```python
Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

```
---

## 🚀 My Approach
- First, get the length of the original array `n`.
- Create a new list `ans` of size `2n`, initialized with zeros.
- Iterate through the original array and place elements at both the original and `+n` indices in `ans`.
- Return `ans` after the loop completes.

---

## 💻 Code (Python)

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the input list

        # Create a new list 'ans' with size double the input, initialized with 0s
        ans = [0] * (2 * n)

        # Loop through each index of the original list
        for i in range(n):
            ans[i] = nums[i]         # Place the element at the current index
            ans[i + n] = nums[i]     # Place the same element at the next half (for concatenation)

        return ans  # Return the new concatenated list
```

---

## 💡 Time and Space Complexity

- **Time**: O(n), Looping through the array once.
- **Space**: O(n), Creating a new array of size 2n.
