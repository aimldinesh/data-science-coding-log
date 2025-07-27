# 🧮 Problem: Kth Missing Positive Number

- **Platform**: [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/kth-missing-positive-number/submissions/1483432687/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/kth-missing-positive-number/submissions/1483432687/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Given an integer array `arr` of sorted distinct positive integers and an integer `k`, you need to find the `k`-th missing positive integer.


---

## 🚀 My Approach
We can efficiently solve this problem using a **Binary Search** technique. Here's a step-by-step breakdown of the approach:

### 1. Initialize Two Pointers:
We begin by initializing two pointers: 
- `left` at the start (`0`) 
- `right` at the end (`len(arr) - 1`) of the array.

### 2. Binary Search:
We apply binary search to find the correct position in the array where the number of missing positive integers is just less than `k`.

For each middle element `arr[mid]`, we calculate the number of missing positive integers up to that point. The formula used is:

```python
missing = arr[mid] - mid - 1
- This formula works because the number of missing numbers before arr[mid] is essentially the difference between the value of arr[mid] and its index, minus one (since arrays are zero-indexed).

3. Adjust the Range:
 - If missing < k, we move the left pointer to mid + 1, because we need to find more missing numbers.

 - If missing >= k, we move the right pointer to mid - 1, because we need to find fewer missing numbers.

Once the binary search loop terminates, the result is calculated as right + k + 1. This formula gives the k-th missing number because after narrowing down the search space, right gives the last valid position, and adding k + 1 gives the exact number we're looking for.
```
---

## 💻 Code (Python)

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        # Binary search to find the correct position
        while left <= right:
            mid = (left + right) // 2
            # Calculate the number of missing elements until the current index
            missing = arr[mid] - mid - 1

            if missing < k:
                left = mid + 1  # Move right to find more missing numbers
            else:
                right = mid - 1  # Move left to find fewer missing numbers

        # The kth missing number is right + k + 1
        return right + k + 1

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
   - The binary search halves the search space in each iteration, making the time complexity logarithmic with respect to the size of the input array.
- **Space**: O(1)
   - The solution uses only a constant amount of extra space, as the solution operates in-place.
