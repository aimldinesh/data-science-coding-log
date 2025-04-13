# 🧮 Problem: Search Insert Position

- **Platform**: [LeetCode](https://leetcode.com/problems/search-insert-position/)
- **Submission**: [https://leetcode.com/problems/search-insert-position/submissions/1605280184/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/search-insert-position/submissions/1605280184/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: DSA, Binary Search, Array

---

## ✅ Problem Statement
- Given a **sorted** array of distinct integers and a target value, return the **index** if the target is found. If not, return the index **where it would be inserted** in order.You must write an algorithm with **O(log n)** runtime complexity.

---

## 🚀 My Approach
- Since the array is sorted, I used **Binary Search**.
- Used `left` and `right` pointers to narrow down the search.
- If the target is found during search, return its index.
- If not found, `left` will be at the correct **insertion position**.
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

## 💡 Time and Space Complexity
- **Time**: O(logn), Binary search halves the search space each step.
- **Space**: O(1), Constant space used.
