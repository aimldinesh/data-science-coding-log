# 🧮 Problem: Contains Duplicate

- **Platform**: [LeetCode](https://leetcode.com/problems/contains-duplicate/)
- **Submission**: [https://leetcode.com/problems/contains-duplicate/submissions/1586471444/](https://leetcode.com/problems/contains-duplicate/submissions/1586471444/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA, Array, HashSet, Sorting, Duplicate

---

## ✅ Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

---

## 🚀 My Approach 1: Using Hash Set (Efficient Time)
- Use a set to store seen numbers.
- If a number appears again, return `True`.
- Otherwise, return `False`.

---

## 💻 Code (Python)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## 🚀 My Approach 2: Using Sorting (Efficient Space)
- Sort the array.
- Check if any adjacent elements are equal.

## 💻 Code (Python)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

---

## 💡 Time and Space Complexity
- **Time**: O(nlogn)
- **Space**: O(1) or O(n) (depends on sorting implementation)

---
