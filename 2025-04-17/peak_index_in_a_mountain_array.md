# 🧮 Problem: Peak Index in a Mountain Array

- **Platform**: [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA
- **Difficulty**: Medium
- **Code Review**: [https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search)
---

## ✅ Problem Statement
Given a **mountain array**, which is an array where:
- The array has at least **3 elements**.
- The elements strictly **increase** and then strictly **decrease**.
  
Find the index of the **peak element** (the element where the array stops increasing and starts decreasing).


---

## 🚀 My Approach:Binary Search
We can solve this problem using **Binary Search** to efficiently find the peak element.

### 🔸 Observations:
- The peak element is the highest value, and it will always have values less than itself both before and after it.
- The array strictly increases and then decreases, so it guarantees a unique peak element.

### 🔸 Steps:
1. Initialize two pointers: `left = 0` and `right = len(arr) - 1`.
2. Run a binary search:
   - Compute `mid = (left + right) // 2`.
   - Compare `arr[mid]` with `arr[mid + 1]`:
     - If `arr[mid] < arr[mid + 1]`: The peak is on the **right**, so update `left = mid + 1`.
     - If `arr[mid] > arr[mid + 1]`: The peak is at `mid` or on the **left**, so update `right = mid`.
3. When the loop ends, `left` will be pointing to the peak element, so return `left`.



---

## 💻 Code (Python)

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with its next element
            if arr[mid] < arr[mid + 1]:
                left = mid + 1  # Peak is to the right
            else:
                right = mid  # Peak is at mid or to the left
        
        # Left points to the peak index
        return left
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), Binary search takes logarithmic time.
- **Space**: O(1), Only a constant amount of space is used.
