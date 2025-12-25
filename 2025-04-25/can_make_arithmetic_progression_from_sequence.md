# 🧲 Problem: Can Make Arithmetic Progression From Sequence

- **Platform**: [LeetCode](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/1617397065/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/1617397065/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-04-25
- **Tags**: Array, Sorting, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
Given an array of numbers `arr`, return `True` if the array can be rearranged to form an **arithmetic progression**. Otherwise, return `False`.
> An arithmetic progression is a sequence of numbers such that the difference between consecutive elements is constant.
---
## Examples
```
Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
```
---

## 🚀 Approach
- Sort the array.
- Compute the common difference using the first two elements.
- Iterate through the array and check if each consecutive difference equals the common difference.
- If all differences match, return True; otherwise, return False

---

## 💻 Code (Python)

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array to check consecutive differences
        arr.sort()

        # Calculate the common difference from the first two terms
        diff = arr[1] - arr[0]

        # Check the difference for all consecutive terms
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False  # Not an arithmetic progression

        return True  # All differences match
             
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n), due to sorting
- **Space**: O(1), no extra space used
