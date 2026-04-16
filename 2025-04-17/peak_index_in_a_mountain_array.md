# 🧮 Problem: Peak Index in a Mountain Array

- **Platform**: [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1484279758/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA
- **Difficulty**: Medium
---

## ✅ Problem Statement
Given a **mountain array**, which is an array where:
- The array has at least **3 elements**.
- The elements strictly **increase** and then strictly **decrease**.
  
Find the index of the **peak element** (the element where the array stops increasing and starts decreasing).


---
## Examples
```python
Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
```
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
## 🔍 Step-by-Step Execution
```
Input: arr = [0, 2, 4, 6, 3, 1] → n=6
Indices:  0  1  2  3  4  5
Values:   0  2  4  6  3  1
                  ↑ peak at index 3
```

Iteration 1
```
left=0, right=5
mid = (0+5)//2 = 2

arr[2]=4 < arr[3]=6 → still climbing ✅
left = mid+1 = 3
```
Iteration 2
```
left=3, right=5
mid = (3+5)//2 = 4

arr[4]=3 < arr[5]=1 → descending ❌
right = mid = 4
```
Iteration 3
```
left=3, right=4
mid = (3+4)//2 = 3

arr[3]=6 > arr[4]=3 → descending ❌
right = mid = 3
```

Loop ends: left=3 == right=3
```
return left = 3 ✅
```
💡 Why This Works
```
Left of peak:   arr[mid] < arr[mid+1]  →  safe to discard left half
Right of peak:  arr[mid] > arr[mid+1]  →  safe to discard right half
At peak:        arr[mid] > arr[mid+1]  →  right=mid, eventually left==right==peak
```
```
        🏔️
       /    \
      /      \          arr[mid] < arr[mid+1] → go right →
     /        \
────/────mid───\────
              ← arr[mid] > arr[mid+1] → go left
```
✅ Final Answer
```
return left = 3   →   arr[3] = 6  (peak)
```
---

## 💡 Time and Space Complexity
- **Time**: O(log n), Binary search takes logarithmic time.
- **Space**: O(1), Only a constant amount of space is used.
