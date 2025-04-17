# 🧮 Problem: Median of Two Sorted Arrays

- **Platform**: [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1484468833/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1484468833/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.


---

## 🚀 My Approach: Merge and Sort
We can solve this problem by **merging both arrays**, sorting the result, and then finding the median.

### 🔸 Steps:

1. **Merge** the two input arrays into one.
2. **Sort** the merged array.
3. **Calculate Total Length** of the merged array.
4. **Determine Median**:
   - If total length is **odd**, return the middle element.
   - If total length is **even**, return the average of the two middle elements.


---

## 💻 Code (Python)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Merge the two arrays
        merged = nums1 + nums2
        
        # Step 2: Sort the merged array
        merged.sort()
        
        # Step 3: Calculate the total number of elements
        total = len(merged)
        
        # Step 4: Check if the total number of elements is odd or even
        if total % 2 == 1:
            # Odd case: Median is the middle element
            return float(merged[total // 2])
        else:
            # Even case: Median is the average of the two middle elements
            median1 = merged[total // 2 - 1]
            median2 = merged[total // 2]
            return (float(median1) + float(median2)) / 2.0

```

---

## 💡 Time and Space Complexity
- **Time**: O((m + n) log(m + n))
   - Merging arrays takes O(m + n)
   - Sorting takes O((m + n) log(m + n))
- **Space**: O(m + n), due to merged array
