# 🧲 Problem: Max Consecutive Ones

- **Platform**: [LeetCode](https://leetcode.com/problems/max-consecutive-ones/solutions/)
- **Submission**: [https://leetcode.com/problems/max-consecutive-ones/submissions/1786965051/](https://leetcode.com/problems/max-consecutive-ones/submissions/1786965051/)
- **Date Solved**: 2025-09-30
- **Tags**: DSA, Array, Math, Two Pointer
- **Difficulty**: Easy

---

# ✅ Problem Statement  

You are given a **binary array** `nums` (containing only `0` and `1`).  
Return the **maximum number of consecutive 1's** in the array.  

---

## 🔹 Example  
```text
Input:  
nums = [1,1,0,1,1,1]
Output:3

Explanation:
The first two `1`s form a sequence of length 2.  
The next three `1`s form a sequence of length 3.  
Hence, the maximum consecutive ones = `3`.  
```
---

## 🚀 Approach
1. Initialize two variables:  
   - `count` → to store the current streak of consecutive `1`s.  
   - `max_count` → to store the maximum streak so far.  

2. Traverse the array:  
   - If the element is `1`, increase `count` and update `max_count`.  
   - If the element is `0`, reset `count` to `0`.  

3. Return `max_count` as the result.  

---

## 💻 Code (Python)

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0         # Current consecutive ones
        max_count = 0     # Maximum consecutive ones found

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)  # Update max if current streak is larger
            else:
                count = 0  # Reset current streak on zero

        return max_count
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - single pass through the array
- **Space**: O(1)
    - only constant extra space used
