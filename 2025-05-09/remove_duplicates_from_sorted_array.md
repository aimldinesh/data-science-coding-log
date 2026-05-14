# 🧲 Problem: Remove Duplicates from Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1408230377/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1408230377/)
- **Date Solved**: 2025-05-09
- **Tags**: Array, Two Pointer, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
- Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

---
## Examples
```python
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
---
##  🚀 Approach : Brute Force (Using Set + Sorted)

🧠 Intuition
Use a set to track seen elements, collect all unique values in order, then write them back into the array.

## 💻 Code (Python)
```
def removeDuplicates(self, nums: List[int]) -> int:
    unique = sorted(set(nums))   # get unique elements in sorted order
    
    for i, val in enumerate(unique):
        nums[i] = val            # overwrite array from start
    
    return len(unique)
```
---
Walkthrough: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```
set(nums)      = {0, 1, 2, 3, 4}
sorted(...)    = [0, 1, 2, 3, 4]

Write back:
  nums[0]=0, nums[1]=1, nums[2]=2, nums[3]=3, nums[4]=4

nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
return 5 ✅
```
---
## ## 💡 Time and Space Complexity
- **Time**: O(n log n)
- **Space**: O(n), uses extra space

---



## 🚀 Approach : Two Pointer(Optimal)
🧠 Intuition

The array is already sorted — so duplicates are always adjacent. Use two pointers: r scans every element, l marks where the next unique element should be written. Whenever r finds something different from its previous element, it's a new unique — write it at l and advance l.
```
nums = [1, 1, 2, 2, 3]

r scans →  finds new unique → writes at l
                                        l moves →
Result: [1, 2, 3, _, _]   return l=3
```

📌 Approach

1. Start l=1 — index 0 is always unique, no need to check
2. r iterates from index 1 to end
3. If nums[r] != nums[r-1] → new unique found:
   + Write nums[r] at nums[l]
   + Increment l

4. Return l — count of unique elements
---

## 💻 Code (Python)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer 'l' to track the position of the next unique element
        l = 1
        
        # Start iterating from the second element (index 1) since the first element is always unique
        for r in range(1, len(nums)):
            # If the current element is different from the previous one, it's a unique element
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]  # Move the unique element to the 'l' position
                l += 1  # Increment 'l' to the next position for a unique element
        
        # Return 'l', which represents the length of the array with unique elements at the start
        return l       
        

```

---

### 🔍 Step-by-Step Execution

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```
Indices:  0  1  2  3  4  5  6  7  8  9
Values:   0  0  1  1  1  2  2  3  3  4
```

r=1 → nums[1]=0, nums[0]=0
```
0 == 0 → duplicate, skip
l=1
```
r=2 → nums[2]=1, nums[1]=0
```
1 != 0 → unique ✅
nums[1] = 1
l=2
array: [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
```
r=3 → nums[3]=1, nums[2]=1
```
1 == 1 → duplicate, skip
l=2
```
r=4 → nums[4]=1, nums[3]=1
```
1 == 1 → duplicate, skip
l=2
```
r=5 → nums[5]=2, nums[4]=1
```
2 != 1 → unique ✅
nums[2] = 2
l=3
array: [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
```
r=6 → nums[6]=2, nums[5]=2
```
2 == 2 → duplicate, skip
l=3
```
r=7 → nums[7]=3, nums[6]=2
```
3 != 2 → unique ✅
nums[3] = 3
l=4
array: [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
```
r=8 → nums[8]=3, nums[7]=3
```
3 == 3 → duplicate, skip
l=4
```
r=9 → nums[9]=4, nums[8]=3
```
4 != 3 → unique ✅
nums[4] = 4
l=5
array: [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
```
---
### 📊 Trace Table
```
r          nums[r]          nums[r-1]         Unique?            nums[l] =         l           Array (first l elements)
1          0                0                 ❌                 —                 1           [0]
2          1                0                 ✅                 nums[1]=1         2           [0,1]
3          1                1                 ❌                 —                 2           [0,1]
4          1                1                 ❌                 —                 2           [0,1]
5          2                1                 ✅                 nums[2]=2         3           [0,1,2]
6          2                2                 ❌                 —                 3           [0,1,2]
7          3                2                 ✅                 nums[3]=3         4           [0,1,2,3]
8          3                3                 ❌                 —                 4           [0,1,2,3]
9          4                3                 ✅                 nums[4]=4         5           [0,1,2,3,4]
```
---
### 💡 Two Pointer Visualised
```
Initial:
  0  0  1  1  1  2  2  3  3  4
  ↑l
     ↑r

r=2 finds 1 (new):        r=5 finds 2 (new):
  0  1  1  1  1  ...        0  1  2  1  1  ...
     ↑l                           ↑l
        ↑r                              ↑r

Final:
  0  1  2  3  4  |  2  2  3  3  4
  ───────────────   (don't care)
      l=5 ↑
```
---
### 🔍 Edge Cases
```
# All duplicates
nums = [1, 1, 1, 1]  →  l=1  →  return 1  →  [1] ✅

# No duplicates
nums = [1, 2, 3, 4]  →  l=4  →  return 4  →  [1,2,3,4] ✅

# Two elements, same
nums = [1, 1]        →  l=1  →  return 1  →  [1] ✅

# Two elements, different
nums = [1, 2]        →  l=2  →  return 2  →  [1,2] ✅
```
---
### ✅ Final Answer
```
return l = 5
nums[:5] = [0, 1, 2, 3, 4] ✅
```
## 💡 Time and Space Complexity
- **Time**: O(n)
   - We iterate through the array once using a single loop.
   - Each element is visited at most once, so the runtime scales linearly with the size of nums.
- **Space**: O(1)
   - The algorithm uses only constant extra space:
      - Two pointers (l and r).
   - No additional data structures are used.
