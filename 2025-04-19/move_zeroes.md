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
        # This pointer indicates the index where the next non-zero element should be placed
        non_zero_index = 0

        # Traverse the array using index i
        for i in range(len(nums)):
            
            # If the current element is non-zero
            if nums[i] != 0:
                
                # Swap the current non-zero element with the element
                # at non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                
                # Move non_zero_index forward,
                # since we have placed a non-zero correctly
                non_zero_index += 1

```

---
## Step by Step code execution with example
Input:
```python
nums = [0, 1, 0, 3, 12]
```
Execution:
| i | nums[i] | Action            | nums         | non_zero_index |
| - | ------- | ----------------- | ------------ | -------------- |
| 0 | 0       | skip              | [0,1,0,3,12] | 0              |
| 1 | 1       | swap with index 0 | [1,0,0,3,12] | 1              |
| 2 | 0       | skip              | [1,0,0,3,12] | 1              |
| 3 | 3       | swap with index 1 | [1,3,0,0,12] | 2              |
| 4 | 12      | swap with index 2 | [1,3,12,0,0] | 3              |

Output
```python
[1, 3, 12, 0, 0]
```
---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the number of elements in the array, because we traverse the array once.
- **Space**: O(1), because we do not use any additional data structures.
