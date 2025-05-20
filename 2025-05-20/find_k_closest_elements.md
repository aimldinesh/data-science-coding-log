# 🧲 Problem: Find K Closest Elements

- **Platform**: [LeetCode](https://leetcode.com/problems/find-k-closest-elements/description/)
- **Submission**: [https://leetcode.com/problems/find-k-closest-elements/submissions/1639291387/](https://leetcode.com/problems/find-k-closest-elements/submissions/1639291387/)
- **Date Solved**: 2025-05-20
- **Tags**: Array, Binary Search, Two Pointers, Sorting
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given a **sorted** array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array.The result should also be **sorted in ascending order**.
- An integer `a` is closer to `x` than an integer `b` if:
    - `|a - x| < |b - x|`, or  
    - `|a - x| == |b - x|` and `a < b`

---

### 🔍 Examples

```python
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

```
---

## 🚀 My Approach
🔸 Intuition:
- The array is sorted, and the k closest elements must appear in a contiguous subarray of size k.This allows us to apply binary search to find the starting index of that subarray.

🔸 Steps:
- Define the search range as left = 0 and right = len(arr) - k, since the window of size k must end before len(arr).
- Perform binary search on this range:
    - Calculate mid-point: mid = (left + right) // 2
    - Compare the distances:
       - If x - arr[mid] > arr[mid + k] - x, then the right side is closer → move left = mid + 1
       - Else, the left side is closer or equally close → move right = mid
- When binary search ends, left will be the starting index of the closest subarray.
- Return the subarray: arr[left:left + k]

---

## 💻 Code (Python)

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search on the window's starting index
        left, right = 0, len(arr) - k  # We need a window of size k

        while left < right:
            mid = (left + right) // 2

            # Compare distance between x and arr[mid] vs arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1  # Move right: arr[mid] is farther
            else:
                right = mid     # Move left: arr[mid + k] is farther

        # The window [left, left + k) contains the k closest elements
        return arr[left : left + k]
        
```

---

## 💡 Time and Space Complexity
- **Time**: O(log(n - k))
    - Binary search on the starting index of the window.
- **Space**: O(1)
    - Constant extra space (excluding result).
