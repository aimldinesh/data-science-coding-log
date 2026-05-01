# 🧮 Problem: Search Insert Position

- **Platform**: [LeetCode](https://leetcode.com/problems/search-insert-position/)
- **Submission**: [https://leetcode.com/problems/search-insert-position/submissions/1605280184/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/search-insert-position/submissions/1605280184/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: DSA, Binary Search, Array

---

## ✅ Problem Statement
- Given a **sorted** array of distinct integers and a target value, return the **index** if the target is found. If not, return the index **where it would be inserted** in order.You must write an algorithm with **O(log n)** runtime complexity.

---
## Examples
```python
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

```
---

## 🚀 Approach : Binary Search
🧠 Intuition

Standard binary search with one extra insight — if the target isn't found, where would it go? When the loop exits, left has naturally moved to the exact position where target should be inserted to keep the array sorted. No extra logic needed.
```
nums = [1, 3, 5, 6],  target = 4

4 fits between 3 and 5 → insertion index = 2

After binary search exits:
  right → index 1 (points at 3, too small)
  left  → index 2 (points at 5, first element > target) ✅
```
📌 Approach

1. Binary search with left=0, right=n-1
2. At each mid:
   + nums[mid] == target → found → return mid
   + nums[mid] < target  → go right → left = mid + 1
   + nums[mid] > target  → go left → right = mid - 1

3. Loop exits → return left as insertion point

---

## 💻 Code (Python)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return the index
            
            # If the middle element is less than the target, search in the right half
            elif nums[mid] < target:
                left = mid + 1
            
            # If the middle element is greater than the target, search in the left half
            else:
                right = mid - 1
        
        # If the target is not found, return the insertion point (left)
        return left
```

---
## 🔍 Step-by-Step Execution

Input: nums = [1, 3, 5, 6], target = 4
```
Indices:  0  1  2  3
Values:   1  3  5  6
               ↑ insert here (index 2)
```

Iteration 1
```
left=0, right=3
mid = (0+3)//2 = 1
nums[1] = 3

3 < 4 → too small, go right
left = mid+1 = 2
```
Iteration 2
```
left=2, right=3
mid = (2+3)//2 = 2
nums[2] = 5

5 > 4 → too big, go left
right = mid-1 = 1
```
Loop ends: left=2 > right=1
```
return left = 2 ✅
```
---
### 📊 Trace Table — target = 4
```
Iter        left        right       mid       nums[mid]                vs target          Action   
1           0           3           1          3                       3 < 4 ❌           left=2
2           2           3           2          5                       5 > 4 ❌           right=1
```
```
return left = 2 ✅
```
---
### 🔍 All Cases Covered

Case 1 — Target Found: target = 5
```
Iter            left         right            mid        nums[mid]         Action
1               0            3                1          3                 3 < 5 → left=2
2               2            3                2          5                 5 == 5 → return 2 ✅
```


## 💡 Time and Space Complexity
- **Time**: O(logn), Binary search halves the search space each step.
- **Space**: O(1), Constant space used.
