# 🧲 Problem: 4Sum

- **Platform**: [LeetCode](https://leetcode.com/problems/4sum/description/)
- **Submission**: [https://leetcode.com/problems/4sum/submissions/1631939141/](https://leetcode.com/problems/4sum/submissions/1631939141/)
- **Date Solved**: 2025-05-12
- **Tags**: Array, Two Pointer, Sorting
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an array nums of n integers, return all unique quadruplets [a, b, c, d] such that:
  - a + b + c + d == target
  - No duplicate quadruplets in the result.
---
## 🧠 Intuition
- We need to find all unique combinations of 4 numbers that sum up to a given target.
- Sorting helps simplify duplicate handling and efficient pointer-based techniques.

## 🚀 Approach 1 : Brute Force (Using 4 Loops)
🔹 Steps:
  - Sort the array.
  - Use four nested loops to try every combination of 4 elements.
  - If their sum equals the target, store the result in a set to avoid duplicates.
  - Convert the set back to a list before returning.

---

## 💻 Code (Python)

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Get the length of the input array
        n = len(nums)
        
        # Sort the array to ensure that we can find valid quadruplets more efficiently
        nums.sort()
        
        # Initialize an empty set to store the unique quadruplets (using set to avoid duplicates)
        res = set()

        # Iterate over all possible quadruplets (4 elements)
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        # Check if the sum of the current quadruplet equals the target
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            # Add the quadruplet to the set (to avoid duplicate quadruplets)
                            res.add((nums[a], nums[b], nums[c], nums[d]))

        # Convert the set of quadruplets to a list and return it
        return list(res)

```

---

## 💡 Time and Space Complexity
- **Time**: O(n ^4)
    - O(n⁴) — 4 nested loops
    - Very slow for large arrays
- **Space**: O(n)
    - to store unique results in a set

---
## 🚀 Approach 2 : Two Pointers (Optimized O(n³))
🔹 Steps:
   - Sort the array to enable two-pointer optimization and simplify duplicate checks.
   - Fix the first two elements with nested loops (i, j).
   - Use two pointers (left, right) to find the remaining two numbers.
   - Skip duplicates using while loops.
   - If the current sum matches the target, add the combination to the result list.

---

## 💻 Code (Python)

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array to enable two-pointer technique and duplicate handling
        nums.sort()
        res, quad = [], []  # res will hold the final result, quad holds the current combination

        # Recursive kSum function that generalizes the solution for k numbers
        def kSum(k, start, target):
            # Base case: 2Sum problem using two pointers
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    current_sum = nums[l] + nums[r]
                    if current_sum < target:
                        l += 1  # Need a larger sum
                    elif current_sum > target:
                        r -= 1  # Need a smaller sum
                    else:
                        # Found a valid pair, add the full combination to the result
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # Skip duplicate elements
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            # Recursive case: reduce kSum to (k-1)Sum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicates to avoid duplicate combinations
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])  # Choose current number
                kSum(k - 1, i + 1, target - nums[i])  # Recursive call
                quad.pop()  # Backtrack to explore other possibilities

        # Start the recursion with k = 4
        kSum(4, 0, target)
        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n^3)
    - two nested loops + two-pointer traversal
- **Space**: O(1)extra space (excluding output)
