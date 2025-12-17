# 🧲 Problem: Number of Subsequences That Satisfy the Given Sum Condition

- **Platform**: [LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/submissions/1611462462/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/submissions/1611462462/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-19
- **Tags**: Array, Sorting, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
You are given an array of integers `nums` and an integer `target`.
Return the number of **non-empty subsequences** such that the **sum of the minimum and maximum elements** in the subsequence is **less than or equal to target**.

As the answer may be large, return it modulo **10⁹ + 7**.

---
## Examples
```python
Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
```
---

## 🚀 My Approach : Two Pointers + Precomputed Powers of 2
### 💡 Key Insight:
- Sort the array to handle min/max efficiently.
- For each valid pair `(left, right)` where `nums[left] + nums[right] <= target`, 
  all subsequences between `left` and `right` are valid.
  - Count of such subsequences = `2^(right - left)`
- Use two pointers: 
  - Move `left` when condition is satisfied.
  - Move `right` when it's not.

---

## 💻 Code (Python)

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        # Sort the array
        nums.sort()
        
        # Precompute powers of 2 modulo MOD
        n = len(nums)
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD
        
        # Two-pointer approach
        left, right = 0, n - 1
        count = 0
        
        while left <= right:
            # If the smallest + largest <= target, count valid subsequences
            if nums[left] + nums[right] <= target:
                count += power[right - left]
                count %= MOD
                left += 1
            else:
                # Reduce the largest element
                right -= 1
        
        return count
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
   - Sorting: O(n log n)
   - Two-pointer traversal: O(n)
- **Space**: O(n)
   - For the precomputed power array
