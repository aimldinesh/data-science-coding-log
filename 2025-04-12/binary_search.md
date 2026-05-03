# 🧮 Problem: Binary Search

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/binary-search/submissions/1481236117/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/binary-search/submissions/1481236117/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-12
- **Tags**: DSA, Array, Binary Search

---

## ✅ Problem Statement
- Given a **sorted** array of integers `nums` and an integer `target`, return the **index** of `target` if it is in the array. If not, return `-1`.You must write an algorithm with **O(log n)** runtime complexity.

---
## Examples
```python
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```
---

## 🚀 Approach : Binary Search
🧠 Intuition

The array is sorted — so at any mid, you can immediately eliminate half the search space. If target < nums[mid], it can't be in the right half. If target > nums[mid], it can't be in the left half. Keep halving until found or exhausted.
```
nums = [1, 3, 5, 7, 9],  target = 7

mid=9 → too big  → go left
mid=3 → too small → go right
mid=7 → found ✅
```
📌 Approach

1. left=0, right=n-1
2. At each mid:
   + nums[mid] == target → return mid
   + nums[mid] > target  → right = mid - 1
   + nums[mid] < target  → left = mid + 1

3. Loop exits → return -1

---

## 💻 Code (Python)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # Binary search loop: continue while the search space is valid
        while left <= right:
            mid = (left + right) // 2  # Calculate mid index

            # If target is found at mid, return the index
            if nums[mid] == target:
                return mid
            # If target is smaller than mid element, search left half
            elif nums[mid] > target:
                right = mid - 1
            # If target is greater, search right half
            else:
                left = mid + 1

        # Target not found in the array
        return -1  
```

---
## 🔍 Step-by-Step Execution

Input: nums = [1, 3, 5, 7, 9, 11, 13], target = 7
```
Indices:  0  1  2  3  4   5   6
Values:   1  3  5  7  9  11  13
                  ↑ target
```
Iteration 1
```
left=0, right=6
mid = (0+6)//2 = 3
nums[3] = 7 == target ✅
return 3
```
Input: nums = [1, 3, 5, 7, 9, 11, 13], target = 6

Iteration 1
```
left=0, right=6
mid = (0+6)//2 = 3
nums[3] = 7 > 6
→ right = mid-1 = 2
```
Iteration 2
```
left=0, right=2
mid = (0+2)//2 = 1
nums[1] = 3 < 6
→ left = mid+1 = 2
```
Iteration 3
```
left=2, right=2
mid = (2+2)//2 = 2
nums[2] = 5 < 6
→ left = mid+1 = 3
```
Loop ends: left=3 > right=2
```
return -1 ✅
```
---
### 📊 Trace Table — target = 7 (found)
```
Iter      left       right        mid           nums[mid]               vs target        Action
1         0          6            3             7                       == 7 ✅         return 3
```
### 📊 Trace Table — target = 6 (not found)
```
Iter      left       right         mid          nums[mid]                vs target         Action
1         0          6             3            7                        7 > 6             right=2
2         0          2             1            3                        3 < 6             left=2
3         2          2             2            5                        5 < 6             left=3
```
```
left=3 > right=2 → return -1 ✅
```
---
### 💡 Search Space Visualised
```
nums = [1, 3, 5, 7, 9, 11, 13],  target=6

Iter 1:  [1  3  5  7  9  11  13]   mid=7 > 6 → cut right
                  ↑
Iter 2:  [1  3  5]                 mid=3 < 6 → cut left
             ↑
Iter 3:     [5]                    mid=5 < 6 → cut left
              ↑
          []                       empty → return -1
```
---

### 🔍 Edge Cases
```
python# Single element — found
nums=[5], target=5  →  mid=0, nums[0]==5  →  return 0 ✅

# Single element — not found
nums=[5], target=3  →  mid=0, nums[0]>3  →  right=-1
                    →  left=0 > right=-1  →  return -1 ✅

# Target at boundaries
nums=[1,3,5,7,9], target=1  →  return 0 ✅  (leftmost)
nums=[1,3,5,7,9], target=9  →  return 4 ✅  (rightmost)
```
---
### ✅ Final Answers
```
target=7  →  return 3   ✅  (found)
target=6  →  return -1  ✅  (not found)
```
---

## 💡 Time and Space Complexity
- **Time**: O(logn), Efficient search using binary strategy.
- **Space**: O(1), Only constant extra space is used.

---
### Common mistakes
```
  while left < right   → misses single element case
  left = mid           → infinite loop when left+1==right
  right = mid          → infinite loop when left+1==right
```
---

### 💡 Interview tip: 
Binary search looks simple but has subtle bugs. The three most common mistakes are using < instead of <=, using mid instead of mid±1 when updating pointers, and integer overflow on mid (use left + (right-left)//2 in languages without big integers like Java/C++).
