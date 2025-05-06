# 🧲 Problem: First Missing Positive

- **Platform**: [LeetCode](https://leetcode.com/problems/first-missing-positive/description/)
- **Submission**: [https://leetcode.com/problems/first-missing-positive/submissions/1626916119/](https://leetcode.com/problems/first-missing-positive/submissions/1626916119/)
- **Date Solved**: 2025-05-06
- **Tags**: Array, Hash Table, In-Place, Cyclic Sort
- **Difficulty**: Hard

---

## ✅ Problem Statement
- Given an unsorted integer array `nums`, return the **smallest missing positive integer**.You must implement an algorithm that runs in **O(n)** time and uses **constant extra space**.

```python
Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

```
---

## 🧠 Intuition

- We're looking for the first **positive integer not present** in the array.
- We explore two methods:
  1. An **Optimal In-Place Cyclic Sort** method that meets the problem's constraints.
  2. A simple **HashSet-based** approach.



## 🚀 Approach 1 : Cyclic Sort Style
### Step 1: Index Placement  
- For every number, if it's in the range `[1, n]`, place it at index `num - 1` using swapping.

### Step 2: Detection  
- After rearrangement, if `nums[i] != i + 1`, then `i + 1` is the missing positive number.

### Step 3: If All In Place  
- If all positions are correctly placed, return `n + 1`.
---

## 💻 Code (Python)

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Put each number in its correct index position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Identify the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # This index + 1 is the missing number

        # Step 3: If all values are in place, return n + 1
        return n + 1
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Each element is swapped at most once.
- **Space**: O(1)
   - Sorting is done in-place with no extra storage used.

---

## 🚀 Approach 2 :  HashSet
Steps:
  1. Add all elements of `nums` into a set for fast lookup.
  2. Start from `1` and incrementally check if each positive number exists in the set.
  3. The first one that doesn't exist is the missing positive number.

## 💻 Code (Python)

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        positive = 1

        while True:
            if positive not in num_set:
                return positive
            positive += 1
```
---

## 💡 Time and Space Complexity
- **Time**: O(n + k)
   - O(n) to build the set.
   - In the worst case, we might check up to k numbers where k is the smallest missing positive.
- **Space**: O(n)
   - For storing the set.

---
