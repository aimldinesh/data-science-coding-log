# 🧮 Problem: Find K Closest Elements

- **Platform**: [LeetCode](https://leetcode.com/problems/find-k-closest-elements/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/find-k-closest-elements/submissions/1484317717/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-k-closest-elements/submissions/1484317717/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
Given a **sorted array** `arr`, an integer `k`, and a target integer `x`, return the `k` closest integers to `x` in the array.

### 📝 Conditions:
- The result should be sorted in **ascending order**.
- An integer `a` is closer to `x` than an integer `b` if:
  - `|a - x| < |b - x|`, or
  - `|a - x| == |b - x|` and `a < b`.

---
## Examples
```python
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```
---

## 🚀 My Approach 1 : Sorting Based on Distance
We can solve this using a **custom sort** based on absolute distance from `x`.

### 🔸 Steps:
1. Sort the array based on two keys:
   - Absolute difference from `x`: `abs(num - x)`
   - In case of a tie, the smaller value comes first: `num`
2. Select the **first `k` elements** after sorting.
3. Sort the selected `k` elements to return them in ascending order.


---

## 💻 Code (Python)

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort the array based on the absolute difference from x.
        # If two numbers have the same difference, sort them by their values.
        arr.sort(key=lambda num: (abs(num - x), num))
        
        # Select the first k elements after sorting by proximity
        closest = arr[:k]
        
        # Return the closest elements sorted in ascending order
        return sorted(closest)
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
  - Sorting the array: O(n log n)
  - Slicing first k elements: O(k)
  - Final sort of k elements: O(k log k) → negligible if k << n

- **Space**: O(1)
