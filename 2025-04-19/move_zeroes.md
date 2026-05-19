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
## Examples
```python
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
```
---

## 🚀 Approach : Two-pointer technique

🧠 Intuition
Use two pointers — non_zero_index marks where the next non-zero should land, i scans every element. Whenever i finds a non-zero, swap it to non_zero_index position and advance non_zero_index. Zeros naturally bubble to the back as non-zeros get swapped forward.
```
nums = [0, 1, 0, 3, 12]

i finds 1  → swap with position 0 → [1, 0, 0, 3, 12]
i finds 3  → swap with position 1 → [1, 3, 0, 0, 12]
i finds 12 → swap with position 2 → [1, 3, 12, 0, 0] ✅
```
 Approach

1. non_zero_index = 0 — next position to place a non-zero
2. Scan every index i:
   + nums[i] != 0 → swap nums[i] with nums[non_zero_index]
   + Increment non_zero_index

3. Zeros fill the tail naturally after all swaps

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
### 🔍 Step-by-Step Execution

Input: nums = [0, 1, 0, 3, 12]
```
Indices:  0  1  2  3   4
Values:   0  1  0  3  12
```

i=0 → nums[0]=0
```
0 == 0 → skip
non_zero_index = 0
nums = [0, 1, 0, 3, 12]
```
i=1 → nums[1]=1
```
1 != 0 → swap nums[1] and nums[0]
nums = [1, 0, 0, 3, 12]
non_zero_index = 1
```
i=2 → nums[2]=0
```
0 == 0 → skip
non_zero_index = 1
nums = [1, 0, 0, 3, 12]
```
i=3 → nums[3]=3
```
3 != 0 → swap nums[3] and nums[1]
nums = [1, 3, 0, 0, 12]
non_zero_index = 2
```
i=4 → nums[4]=12
```
12 != 0 → swap nums[4] and nums[2]
nums = [1, 3, 12, 0, 0]
non_zero_index = 3
```
---
### 📊 Trace Table
```
i        nums[i]            non_zero_index             swap?              nums after
0        0                  0                          ❌                 [0, 1, 0, 3, 12]
1        1                  0                          ✅swap(1,0)        [1, 0, 0, 3, 12]
2        0                  1                          ❌                 [1, 0, 0, 3, 12]
3        3                  1                          ✅ swap(3,1)       [1, 3, 0, 0, 12]
4        12                 2                          ✅ swap(4,2)       [1, 3, 12, 0, 0]
```
---
### 💡 Two Pointer Visualised
```
[0,  1,  0,  3,  12]
 ↑nz
 ↑i   → 0, skip

[0,  1,  0,  3,  12]
 ↑nz
     ↑i  → 1≠0, swap → nz moves

[1,  0,  0,  3,  12]
     ↑nz
         ↑i  → 0, skip

[1,  0,  0,  3,  12]
     ↑nz
             ↑i  → 3≠0, swap → nz moves

[1,  3,  0,  0,  12]
         ↑nz
                 ↑i → 12≠0, swap → nz moves

[1,  3,  12,  0,  0]
             ↑nz     ← all zeros pushed to tail ✅

```
---
### 🔍 Edge Cases
```
# All zeros
nums = [0, 0, 0]
→ i never swaps → non_zero_index stays 0
→ nums = [0, 0, 0] ✅

# No zeros
nums = [1, 2, 3]
→ every element swaps with itself (i == non_zero_index)
→ nums = [1, 2, 3] ✅  (unchanged)

# Single element
nums = [0] → nums = [0] ✅
nums = [1] → nums = [1] ✅

# Zeros at end already
nums = [1, 2, 0, 0]
→ 1 swaps with itself, 2 swaps with itself
→ nums = [1, 2, 0, 0] ✅  (no unnecessary moves)
```
---
## ✅ Final Answer
```
return None
nums = [1, 3, 12, 0, 0] ✅  (modified in-place)
```
---

## 💡 Time and Space Complexity
- **Time**: O(n), where n is the number of elements in the array, because we traverse the array once.
- **Space**: O(1), In-place swaps, no extra array

---
## 🆚 Alternative — Two Pass (Write then Fill)
```
# Pass 1: overwrite from front with non-zeros
def moveZeroes(self, nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    # Pass 2: fill remaining positions with zeros
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
```
---
```
Pass 1: [1, 3, 12, 3, 12]  ← non-zeros written forward
Pass 2: [1, 3, 12,  0,  0] ← tail filled with zeros ✅
```
---
```
Approach               Time                Swaps                     Notes
Swap (optimal)         O(n)                Minimum swaps             Preserves relative order
Two pass               O(n)                No swaps                  Writes, then fills zeros
```
---
### 💡 Interview tip: 

This is the same slow-fast pointer pattern as Remove Duplicates and Remove Element — non_zero_index is the slow write pointer, i is the fast read pointer. Recognising this family of problems and stating the pattern out loud is what separates strong candidates.
