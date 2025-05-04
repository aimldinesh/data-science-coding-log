# 🧲 Problem: Subarray Sum Equals K

- **Platform**: [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- **Submission**: [https://leetcode.com/problems/subarray-sum-equals-k/submissions/1625197142/](https://leetcode.com/problems/subarray-sum-equals-k/submissions/1625197142/)
- **Date Solved**: 2025-05-04
- **Tags**: Array, Hash Table, Prefix Sum
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an array of integers `nums` and an integer `k`, return the **total number of subarrays whose sum equals to `k`**.
---
## 🧪 Example

```python
Input:
nums = [1, 2, 3], k = 3

Output: 2
Explanation:
  - Subarrays: [1, 2], [3]
```
---

## 🚀 My Approach
We use a prefix sum + hashmap technique to solve this in one pass.
Idea:
  - Maintain a running sum curSum as we traverse the array.
  - For each index, we check if there exists a prefix sum such that curSum - k has occurred before.
  - If yes, that means the subarray from that previous index to the current one sums to k.
  - We track the count of each prefix sum using a hashmap.

---

## 💻 Code (Python)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # Stores count of valid subarrays
        curSum = 0  # Stores the cumulative sum
        prefixSum = {0: 1}  # HashMap to store prefix sum frequencies

        for n in nums:
            curSum += n  # Add current number to cumulative sum
            diff = curSum - k  # Find difference needed to form subarray sum = k
            
            # If this difference has been seen before, add its frequency to result
            res += prefixSum.get(diff, 0)
            
            # Update the prefix sum frequency
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res  # Return total count of valid subarrays

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Single pass through the array.
- **Space**: O(n)
   - Space for storing prefix sums in a hashmap.
