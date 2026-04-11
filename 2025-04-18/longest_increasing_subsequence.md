# 🧲 Problem: Longest Increasing Subsequence

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/longest-increasing-subsequence/submissions/1610219048/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/longest-increasing-subsequence/submissions/1610219048/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-18
- **Tags**: Array, Binary Search, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an integer array `nums`, return the length of the **longest strictly increasing subsequence**.

---
## Example
```python
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```
---

## 🚀 My Approach : Binary Search
This approach maintains a `tail` array that keeps the **smallest tail of all increasing subsequences** with different lengths. 

If an element is:
- **Greater than the last element** in `tail`, it extends the current longest increasing subsequence.
- **Smaller or equal to some element** in `tail`, we replace the **first element in `tail` greater than or equal to it**, keeping the subsequence valid but with a potentially smaller tail (for future extension).

---

### 🧠 Intuition

- Binary search is used to find the **appropriate position to replace** in the `tail` list.
- This does **not give the actual subsequence**, but the **length** is correct.



---

## 💻 Code (Python)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tail = [nums[0]]

        # Iterate through each element in the nums starting from the second element
        for i in range(1,n):
            # if the current element is greter than the last element in active list append it
            if nums[i] > tail[-1]:
                tail.append(nums[i])

            else:
                # if not , find the smallest element in the active list greater than equal to the current element
                c = self.ceilIndex(tail, nums[i])
                tail[c] = nums[i]

        # the length of the active list is the length of the longest increasing subsequence
        return len(tail)

    # helper function to find the smallest alement greter than or equal to x using binary search
    def ceilIndex(self,tail, x):
        # Initialize pointer for binary search
        l = 0
        r = len(tail) - 1

        # perform binary search
        while l < r:
            m = l + (r-l)//2
            if tail[m] >= x:
                r = m
            else:
                l = m + 1

        # return the index of the smallest element greater than or equal to x
        return r                            
           
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
   - For each of the n elements, we perform binary search in tail, which takes O(log n) time.
- **Space**: O(n)
   - In the worst case, tail can grow up to length n.


