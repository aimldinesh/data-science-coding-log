# 🧲 Problem: Two Sum II - Input Array Is Sorted

- **Platform**: [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
- **Submission**: [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1630156821/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1630156821/)
- **Date Solved**: 2025-05-10
- **Tags**: Array, Two Pointer, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given a sorted array of integers numbers and an integer target, return the indices of the two numbers such that they add up to target.
- Indices should be 1-based and exactly one solution exists.

---

## 🧠 Intuition
- Since the input array is sorted, we can use the two-pointer technique:
   - One pointer from the start (l)
   - One pointer from the end (r)
- Adjust the pointers based on the sum relative to the target.

## 🚀 Approach : Two Pointer
- Initialize two pointers: l = 0 (start), r = len(numbers) - 1 (end).
- While l < r:
   - If numbers[l] + numbers[r] == target, return [l + 1, r + 1].
   - If sum < target, move l to the right to increase the sum.
   - If sum > target, move r to the left to decrease the sum.

---

## 💻 Code (Python)

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: 'l' starting at the beginning and 'r' starting at the end
        l = 0
        r = len(numbers) - 1

        # Iterate while the left pointer is less than the right pointer
        while l < r:
            # Calculate the sum of the current left and right pointers
            currsum = numbers[l] + numbers[r]

            # If the current sum is less than the target, move the left pointer to the right
            if currsum < target:
                l += 1
            # If the current sum is greater than the target, move the right pointer to the left
            elif currsum > target:
                r -= 1
            # If the current sum equals the target, return the 1-based indices of the two numbers
            else:
                return (l + 1, r + 1)  # 1-based indexing as required by the problem
       
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - We traverse the array at most once using two pointers.
- **Space**: O(1)
    - No extra space is used.
