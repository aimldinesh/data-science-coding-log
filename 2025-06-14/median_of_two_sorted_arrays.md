# 🧲 Problem: Median of Two Sorted Arrays

- **Platform**: [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
- **Submission**: [https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1663870360/](https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1663870360/)
- **Date Solved**: 2025-06-14
- **Tags**: Array, Brute Force, Binary Search
- **Difficulty**: Hard

---

## ✅ Problem Statement
- Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
- You must solve the problem in O(log (m+n)) time complexity ideally.

### 🌰 Examples
```python
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: The merged array is [1, 2, 3], and the median is 2.

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: The merged array is [1, 2, 3, 4], median is (2 + 3)/2 = 2.5

```

---

## 🚀 Approach : Brute Force
💡 Intuition
- The median is the middle value in an ordered list.
- If total elements = odd → median is the middle element
- If even → median is the average of the two middle elements.

🐢 Brute-Force Approach
- Merge both arrays.
- Sort the merged array.
- If the length is odd → return middle element.
- If even → return average of the two middle elements.

---

## 💻 Code (Python)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Merge the two arrays
        merged = nums1 + nums2
        
        # Step 2: Sort the merged array
        merged.sort()
        
        # Step 3: Total number of elements
        total = len(merged)
        
        # Step 4: Find median
        if total % 2 == 1:
            # Odd number of elements
            return float(merged[total // 2])
        else:
            # Even number of elements
            median1 = merged[total // 2 - 1]
            median2 = merged[total // 2]
            return (float(median1) + float(median2)) / 2.0

```

---

## 💡 Time and Space Complexity
- **Time**: O((m + n) log(m + n))
    - Because of the .sort() on the merged array of size m + n.
- **Space**: O(m + n)
    - Since we create a new list merged.
