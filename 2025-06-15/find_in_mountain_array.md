# 🧲 Problem: Find in Mountain Array

- **Platform**: [LeetCode](https://leetcode.com/problems/find-in-mountain-array/description/)
- **Submission**: [https://leetcode.com/problems/find-in-mountain-array/submissions/1665036487/](https://leetcode.com/problems/find-in-mountain-array/submissions/1665036487/)
- **Date Solved**: 2025-06-15
- **Tags**: Binary Search, Divide and Conquer, Mountain Array
- **Difficulty**: Hard

---

## ✅ Problem Statement
- You're given a mountain array, i.e., an array that increases strictly to a peak element and then decreases strictly. You can only access the array using an interface:
```python
class MountainArray:
    def get(index: int) -> int
    def length() -> int

```
- You are given a target integer. Your task is to return the index of the target in the array or -1 if it's not present.

### 📌 Examples
```python
Example 1:

Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
```
---

## 🚀 Approach : Brute Force

## 💻 Code (Python)

```python
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()  # Get the length of the mountain array

        # Iterate through every index of the mountain array
        for i in range(n):
            if mountainArr.get(i) == target:  # If current element equals the target
                return i  # Return its index immediately
        
        return -1  # If target not found in the entire array

```

---

## 💡 Time and Space Complexity & Drawbacks
- **Time**: O(n)
    - Worst case, it checks every element.
- **Space**: O(1)
    - Constant space used.
- Inefficient for large arrays, especially since MountainArray.get() is a costly API (can only be called a limited number of times in real interview settings like LeetCode hard problems).

---
## 🚀 Approach : Binary search
💡 Intuition
- Since the array first increases and then decreases:
    - We can find the peak using binary search.
    - Then, we apply binary search in the increasing and decreasing parts separately.

- Why? Because:
    - Left side is strictly increasing → regular binary search.
    - Right side is strictly decreasing → modified binary search.

🧠 Approach
- To solve the problem efficiently, we break it into three parts using binary search

✅ Step 1: Find the Peak Element (Maximum Element)
- A mountain array first increases then decreases.
- Use binary search to find the peak index where arr[i-1] < arr[i] > arr[i+1].
- Compare arr[m-1], arr[m], and arr[m+1]:
    - If in increasing slope (left < mid < right), move left to mid + 1.
    - If in decreasing slope (left > mid > right), move right to mid - 1.
    - If peak found (left < mid > right), break and store peak = mid.

✅ Step 2: Binary Search on the Left Side (Increasing Part)
- Perform regular binary search in range [0, peak].
- Since the left side is strictly increasing:
    - If arr[mid] < target: move left = mid + 1.
    -If arr[mid] > target: move right = mid - 1.
    - If arr[mid] == target: return mid.

✅ Step 3: Binary Search on the Right Side (Decreasing Part)
- If the target wasn't found in step 2, perform binary search in range [peak, end].
- Since the right side is strictly decreasing:
    - If arr[mid] > target: move left = mid + 1.
    - If arr[mid] < target: move right = mid - 1.
    - If arr[mid] == target: return mid.

Step 4: Return -1 if Not Found
    - If the target is not found in both left and right parts, return -1.
---

## 💻 Code (Python)

```python
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Step 1: Find the peak index (maximum value in the mountain array)
        l, r = 1, length - 2  # We start from 1 and end at length-2 because the peak can't be at the edges
        while l <= r:
            m = (l + r) // 2
            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m + 1)

            if left < mid < right:
                # Still in the increasing slope
                l = m + 1
            elif left > mid > right:
                # In the decreasing slope
                r = m - 1
            else:
                # Found the peak
                break

        peak = m  # Store peak index

        # Step 2: Binary search on the left (increasing) side of the peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1  # Move right in increasing part
            elif val > target:
                r = m - 1  # Move left
            else:
                return m  # Target found

        # Step 3: Binary search on the right (decreasing) side of the peak
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1  # Move right because values decrease
            elif val < target:
                r = m - 1  # Move left
            else:
                return m  # Target found

        # If target is not found in either part
        return -1
      
        
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
    - Peak finding: O(log n)
    - Binary search (twice): O(log n)
    - Total: O(log n)
- **Space**: O(1)
    - only pointers used

---
