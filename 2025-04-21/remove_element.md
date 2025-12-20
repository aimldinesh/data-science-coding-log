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

## 🚀 Approach: Brute Force (Using Extra Array)
🔹 Intuition

The simplest way to remove all occurrences of a given value val from the array is to:

+ Create a new temporary list
+ Copy only those elements that are not equal to val
+ Overwrite the original array with these filtered elements

This approach is straightforward and easy to understand, though it uses extra space.

🧩 Algorithm

1. Initialize an empty list temp.
2. Traverse the array nums:
   + If the current element is equal to val, skip it.
   + Otherwise, append it to temp.
     
3. Copy elements from temp back into nums (in-place update).
4. Return the length of temp (number of elements not equal to val).
---

## 💻 Code (Python)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Step 1: Create a temporary list to store elements != val
        temp = []

        # Step 2: Traverse original array
        for num in nums:
            # Skip elements equal to val
            if num == val:
                continue
            # Keep valid elements
            temp.append(num)

        # Step 3: Copy filtered elements back to nums
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Step 4: Return new length of the array
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
