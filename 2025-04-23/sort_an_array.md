# 🧲 Problem: Sort an Array

- **Platform**: [LeetCode](https://leetcode.com/problems/sort-an-array/description/)
- **Submission**: [https://leetcode.com/problems/sort-an-array/submissions/1615600197/](https://leetcode.com/problems/sort-an-array/submissions/1615600197/)
- **Date Solved**: 2025-04-23
- **Tags**: Array, Merge Sort, Quick Sort
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an array of integers nums, sort the array in ascending order and return it.
- You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

---
## Examples
```python
Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.

```
---

## 🚀 Approach 1 : Merge Sort
- Merge Sort is a classic divide-and-conquer sorting algorithm:
   - Divide the array recursively into two halves until each subarray contains only one element.
   - Merge the sorted halves back together by comparing elements and building a sorted array.
### Why Merge Sort?
- Merge Sort guarantees O(n log n) time complexity.
- It’s stable and works well for large datasets.
- Useful when random access is allowed and memory is not a constraint.

---

## 💻 Code (Python)

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Function to merge two sorted subarrays
        def merge(arr, low, mid, high):
            left = arr[low:mid + 1]    # Left half
            right = arr[mid + 1:high + 1]  # Right half

            i, j, k = 0, 0, low

            # Merge elements back into original array in sorted order
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy remaining elements of left half (if any)
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            # Copy remaining elements of right half (if any)
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        # Recursive merge sort function
        def mergeSort(arr, l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)       # Sort left half
            mergeSort(arr, m + 1, r)   # Sort right half
            merge(arr, l, m, r)        # Merge both halves

        # Call merge sort on entire array
        mergeSort(nums, 0, len(nums) - 1)
        return nums
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
   - The array is recursively divided (log n) and each merge operation takes linear time (n).
- **Space**: O(?)
   - Additional space is used to create subarrays (left and right) during merging.
