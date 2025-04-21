# 🧲 Problem: Remove Element

- **Platform**: [LeetCode](https://leetcode.com/problems/remove-element/description/)
- **Submission**: [https://leetcode.com/problems/remove-element/submissions/1613144650/](https://leetcode.com/problems/remove-element/submissions/1613144650/)
- **Date Solved**: 2025-04-21
- **Tags**: Array, Two Pointer, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**. The function should return the new length of the array after removal.

- Do **not** allocate extra space — modify `nums` in-place with `O(1)` extra memory.


---

## 🚀 Approach 1 : Brute Force
- Create a temporary list (`temp`) to store elements not equal to `val`.
- Copy elements from `temp` back to `nums`.
- Return the length of the filtered list.

---

## 💻 Code (Python)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute Force
        temp = []
        for num in nums:
            if num == val:
                continue
            temp.append(num)

        # Copy back the filtered elements to original list
        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), one pass to filter, another to copy back.
- **Space**: O(n), due to the use of extra temporary list.

---
## 🚀 Approach 2 : Efficient : Two-Pointer
- Use a pointer `k` to track the index where the next non-`val` element should go. Iterate through the array, and whenever a value is not equal to `val`, move it to `nums[k]` and increment `k`.


---

## 💻 Code (Python)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Efficient Two-Pointer approach
        # k is the position where the next non-val element should be placed
        k = 0
        
        for i in range(len(nums)):
            # If the current element is not equal to the value to be removed
            if nums[i] != val:
                # Move the current element to index k
                nums[k] = nums[i]
                k += 1  # Increment k to the next position

        # k is the number of elements not equal to val (i.e., the new length of the array)
        return k

```

---

## 💡 Time and Space Complexity
- **Time**: O(n), single pass through the array.
- **Space**: O(1), in-place operation with no extra space used. 
