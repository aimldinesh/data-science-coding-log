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
## 🧠 Intuition
- Start merging from the end to avoid overwriting elements in nums1.
- Use two pointers from the back of nums1 and nums2, and a third pointer to place elements from the back.
## 🚀 Approach
- Initialize a pointer last at the end of the merged array.
- Compare elements from the back of both arrays and place the larger one at last.
- After one array is exhausted, copy any remaining elements from nums2 (since nums1’s remaining elements are already in place).

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
Step-by-Step Walkthrough
Initial state:
```python
nums1 = [1, 2, 3, 0, 0, 0]   m=3
nums2 = [2, 5, 6]             n=3, last=5
```
----
```
Step  Compare                         Winner          nums1            m     n      last
1     nums1[2]=3 vs nums2[2]=6        6 wins          [1,2,3,0,0,6]     3     2       4
2     nums1[2]=3 vs nums2[1]=5        5 wins          [1,2,3,0,5,6]     3     1       3
3     nums1[2]=3 vs nums2[0]=2        3 wins          [1,2,3,3,5,6]     2     1       2
4     nums1[1]=2 vs nums2[0]=2        2 wins (nums2)  [1,2,2,3,5,6]     2     0       1
```
n=0 → main while loop ends ✅
No leftover n elements, so second while skips.
```
Final: [1, 2, 2, 3, 5, 6] ✅
```
---

Why the Second While Loop?
Handles leftover nums2 elements if nums1 runs out first.
```
nums1 = [4, 0, 0],  m=1
nums2 = [1, 2],     n=2

Step 1: 4 vs 2 → place 4 → [4,0,4]  m=0, n=2
# main loop ends (m=0)

Second loop kicks in:

→ place nums2[1]=2 → [4,2,4]
→ place nums2[0]=1 → [1,2,4]  ✅
```
Note: We never need a second loop for nums1 leftovers — they're already in place!

---

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
### Space: O(1) or O(m+n)
