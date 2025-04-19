# 🧲 Problem: Move Zeroes

- **Platform**: [LeetCode](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=programming-skills)
- **Submission**: [https://leetcode.com/problems/move-zeroes/submissions/1489409407/?envType=study-plan-v2&envId=programming-skills](https://leetcode.com/problems/move-zeroes/submissions/1489409407/?envType=study-plan-v2&envId=programming-skills)
- **Date Solved**: 2025-04-19
- **Tags**: Array, DSA, Two Pointer
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an integer array `nums`, move all zeroes to the end of the array without changing the relative order of the non-zero elements.You must do this in **place** by modifying the array.

---

## 🚀 My Approach : Two-pointer technique

### 💡 Key Insight:
- The idea is to maintain a pointer (`non_zero_index`) which will track the position where the next non-zero element should be placed.
- Traverse the array, and whenever a non-zero element is found, it is swapped with the element at `non_zero_index`, then increment `non_zero_index`.


---

## 💻 Code (Python)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer for the position of the next non-zero element
        non_zero_index = 0

        # Traverse the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the non-zero element with the element at non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Move the non_zero_index forward
                non_zero_index += 1
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the number of elements in the array, because we traverse the array once.
- **Space**: O(1), because we do not use any additional data structures.
