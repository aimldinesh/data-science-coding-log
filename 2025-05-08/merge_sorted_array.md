# 🧲 Problem: Merge Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- **Submission**: [https://leetcode.com/problems/merge-sorted-array/submissions/1628515387/](https://leetcode.com/problems/merge-sorted-array/submissions/1628515387/)
- **Date Solved**: 2025-05-08
- **Tags**: Array, Two Pointers , DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of initialized elements in `nums1` and `nums2`, respectively.
Merge `nums2` into `nums1` as one sorted array **in-place**.

### 🔍 Example

```python
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]
```
---
## 🚀 Approach

🧠 Intuition
Merging from the front would overwrite unprocessed elements in nums1. Instead, merge from the back — the end of nums1 has n empty slots, so writing the largest elements there first never overwrites anything needed. Compare the largest unplaced elements from both arrays and place the bigger one at last.
```
nums1 = [1, 3, 5, _, _, _]   m=3
nums2 = [2, 4, 6]             n=3

Merge from back →
  compare 5 vs 6 → place 6 at last
  compare 5 vs 4 → place 5
  compare 3 vs 4 → place 4
  ... and so on
```
## 📌 Approach

1. Start last = m + n - 1 (last index of nums1)
2. Compare nums1[m-1] vs nums2[n-1] — place the larger at nums1[last]
3. Decrement the pointer of whichever array was used, and last
4. If nums2 has leftovers → copy them in (nums1 leftovers are already in place)

---
### Key Insight: Fill from the Back
  - If we fill from the front, we'd overwrite values in nums1 we haven't used yet.
  - Filling from the back is safe — the empty zeros are at the end!
```python
nums1 = [1, 2, 3, | 0, 0, 0]
                    ↑ safe to overwrite
```
Three Pointers
```python
nums1 = [1, 2, 3, 0, 0, 0]
                          ↑ last  (m+n-1 = 5)
              ↑ m pointer (m-1 = 2)

nums2 = [2, 5, 6]
                ↑ n pointer (n-1 = 2)
```
---

## 💻 Code (Python)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start merging from the end
        last = m + n - 1

        # Compare elements from the back of both arrays
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If any elements remain in nums2, copy them
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

```

---
### 🔍 Step-by-Step Execution

Input:
```
nums1 = [1, 2, 3, 0, 0, 0]   m=3
nums2 = [2, 5, 6]             n=3
last  = 5
```
```
Indices:  0  1  2  3  4  5
nums1:    1  2  3  _  _  _
nums2:    2  5  6
```

Step 1: m=3, n=3, last=5
```
nums1[2]=3  vs  nums2[2]=6
6 > 3 → nums1[5] = 6
n=2, last=4
nums1 = [1, 2, 3, 0, 0, 6]
```
Step 2: m=3, n=2, last=4
```
nums1[2]=3  vs  nums2[1]=5
5 > 3 → nums1[4] = 5
n=1, last=3

nums1 = [1, 2, 3, 0, 5, 6]
```

Step 3: m=3, n=1, last=3
```
nums1[2]=3  vs  nums2[0]=2
3 > 2 → nums1[3] = 3
m=2, last=2

nums1 = [1, 2, 3, 3, 5, 6]
```
Step 4: m=2, n=1, last=2
```
nums1[1]=2  vs  nums2[0]=2
2 == 2 → nums2 wins (else branch) → nums1[2] = 2
n=0, last=1

nums1 = [1, 2, 2, 3, 5, 6]
```
Loop ends: n=0 → exit while loop
```
No remaining nums2 elements
nums1 = [1, 2, 2, 3, 5, 6] ✅
```

---
### 💡 Why No Need to Handle nums1 Leftovers?
```
If nums2 runs out first (n=0):
  Remaining nums1 elements are already in their correct position
  No copying needed ✅

If nums1 runs out first (m=0):
  Remaining nums2 elements must be copied into nums1
  The second while loop handles this ✅

nums1 = [4, 5, 6, _, _, _]    nums2 = [1, 2, 3]
  → nums2 runs out first                 → nums1 leftover stays ✅

nums1 = [1, 2, 3, _, _, _]    nums2 = [4, 5, 6]
  → nums1 runs out first       → copy remaining nums2 into front ✅
```
---
### 🔍 Edge Cases
```
# nums1 is empty (m=0)
nums1=[0,0,0], m=0, nums2=[1,2,3], n=3
→ first while skipped entirely
→ second while copies all nums2
→ nums1=[1,2,3] ✅

# nums2 is empty (n=0)
nums1=[1,2,3], m=3, nums2=[], n=0
→ both while loops skipped
→ nums1=[1,2,3] unchanged ✅

# All nums2 smaller than nums1
nums1=[4,5,6,_,_,_], m=3, nums2=[1,2,3], n=3
→ nums1 elements placed first at back
→ second while copies 1,2,3 into front ✅
```
---
### ✅ Final Answer
```
nums1 = [1, 2, 2, 3, 5, 6] ✅  (sorted in-place)
```

## 💡 Time and Space Complexity
- **Time**: O(m + n)
   - We traverse each element of nums1 and nums2 at most once.
   - In the worst case, we might need to check all m and n elements.
   - So total work done is linear with respect to the size of both arrays.
- **Space**: O(1)
   - The merging is done in-place, i.e., within the given nums1 array.
   - No extra arrays or data structures are used.
   - Thus, the algorithm uses constant additional space.

---
## Sorting
```python
nums1[m:] = nums2[:n]   # Step 1: Replace zeros with nums2 values
nums1.sort()             # Step 2: Sort the whole array
```

---

### Step-by-Step Example
```
nums1 = [1, 2, 3, 0, 0, 0],  m = 3
nums2 = [2, 5, 6],            n = 3
```

**Step 1: `nums1[m:] = nums2[:n]`**
```
nums1[3:] = nums2[:3]

Before: [1, 2, 3, | 0, 0, 0]
                     ↑ slice replaced
After:  [1, 2, 3, | 2, 5, 6]
```

**Step 2: `nums1.sort()`**
```
Before: [1, 2, 3, 2, 5, 6]
After:  [1, 2, 2, 3, 5, 6] ✅
```

---

### Complexity

### Time: O((m+n) log(m+n))
```
nums1[m:] = nums2[:n]  → O(n)         slice assignment
nums1.sort()           → O((m+n) log(m+n))  Timsort on full array
                                  ↑
                            dominates overall
```
### Space: O(1) or O(m+n)

---
### 💡 Interview tip: 

The key insight interviewers listen for is "merge from the back to avoid overwriting unprocessed elements". The naive approach of merging from the front and shifting elements right is O(m×n) — recognising that the empty slots at the end of nums1 let us merge in O(1) space is what makes this solution elegant.

