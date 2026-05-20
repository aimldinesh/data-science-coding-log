# 🧮 Problem: Search in Rotated Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **Submission**: [https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1508345478/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1508345478/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-14
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Given a rotated sorted array `nums` of distinct integers and a target integer `target`, return the index of the target if it exists in the array. Otherwise, return `-1`.
- You must write an algorithm with a time complexity of O(log n).

---
## Examples
```python
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
```
---

## 🚀 Approach

🧠 Intuition
A rotated sorted array is two sorted subarrays joined together. At any mid, one half is always fully sorted. Use that guaranteed sorted half to check if the target lies within it — if yes, search there; if no, search the other half.
```
[4, 5, 6, 7, 0, 1, 2]   target = 0
left half [4,5,6,7] → sorted ✅ → 0 not in [4..7] → go right
right half [0,1,2]  → sorted ✅ → 0 in [0..2]     → go left
```

📌 Approach

1. Standard binary search with left=0, right=n-1
2. If nums[mid] == target → return mid
3. Check which half is sorted:
   + nums[left] <= nums[mid] → left half is sorted
     + Target in [nums[left]..nums[mid]] → go left
     + Else → go right

   + Else → right half is sorted
     + Target in [nums[mid]..nums[right]] → go right
     + Else → go left

4. Return -1 if not found
---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # If we found the target, return the index
            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within the sorted left portion
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1  # Target is not in the left sorted half
                else:
                    right = mid - 1  # Target is in the left sorted half

            # Otherwise, the right half must be sorted
            else:
                # Check if the target lies within the sorted right portion
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1  # Target is not in the right sorted half
                else:
                    left = mid + 1  # Target is in the right sorted half

        # Target not found, return -1
        return -1
```

---
## 🔍 Step-by-Step Execution
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Indices:  0  1  2  3  4  5  6
Values:   4  5  6  7  0  1  2
                        ↑ target
```
Iteration 1
```
left=0, right=6
mid = (0+6)//2 = 3
nums[3] = 7 ≠ 0

nums[left]=4 <= nums[mid]=7 → left half [4,5,6,7] is sorted ✅
target=0 > nums[mid]=7?  → No
target=0 < nums[left]=4? → Yes ❌ target NOT in left half
→ left = mid+1 = 4
```
Iteration 2
```
left=4, right=6
mid = (4+6)//2 = 5
nums[5] = 1 ≠ 0

nums[left]=0 <= nums[mid]=1 → left half [0,1] is sorted ✅
target=0 > nums[mid]=1?  → No
target=0 < nums[left]=0? → No ✅ target IS in left half
→ right = mid-1 = 4
```
Iteration 3
```
left=4, right=4
mid = (4+4)//2 = 4
nums[4] = 0 == target ✅
→ return 4
```
---
### 📊 Trace Table
```
Iter        left      right     mid      nums[mid]       Sorted Half        Target in Range?      Action 
1           0         6         3        7               Left [4..7] ✅     0 < 4 ❌             left=4
2           4         6         5        1               Left [0..1] ✅     0 in [0..1] ✅       right=4
3           4         4         4        0               —                   0 == target ✅       return 4
```
---
### 🔍 Case 2 — Target Not Found
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3

Iter       left      right      mid      nums[mid]       Sorted Half         Target in Range?       Action
1          0         6          3        7               Left [4..7] ✅      3 < 4 ❌              left=4
2          4         6          5        1               Left [0..1] ✅      3 > 1 ❌              left=6
3          6         6          6        2               Left [2..2] ✅      3 > 2 ❌              left=7
```
```
left=7 > right=6 → loop exits
return -1 ✅
```
---
### 💡 The Core Logic Visualised
```
Rotated array always looks like one of these:

Case A: left half sorted        Case B: right half sorted
   ↗ pivot                              pivot ↘
  /         \                          /         \
 /    ↘       \                       /    ↗      \
nums[left]<=nums[mid]            nums[left]>nums[mid]

   ┌──────┐ ┌──┐                  ┌──┐ ┌──────┐
   │sorted│ │  │                  │  │ │sorted│
   └──────┘ └──┘                  └──┘ └──────┘
   check here first               check here first
```
---
### 💡 Why nums[left] <= nums[mid] (not strict <)?
```
# Equal handles the case where left == mid (2-element array)
nums = [3, 1],  target = 1
left=0, right=1, mid=0

nums[left]=3 <= nums[mid]=3 → True (equal case)
→ correctly identifies left half as sorted [3]
→ 1 not in [3..3] → go right → finds 1 at index 1 ✅
```
---
### ✅ Final Answers
```
target=0  →  return 4   ✅
target=3  →  return -1  ✅
```
---

## 💡 Time and Space Complexity
- **Time**: O(log n), because we are performing binary search on the array, and the array is halved each time.
- **Space**: O(1), as we are using only a constant amount of extra space.

---
### Interview Tip: 
The key insight examiners listen for is "one half is always guaranteed to be sorted in a rotated array" — that's what makes binary search still applicable. Without stating that, the solution looks like magic. With it, the logic flows naturally.
