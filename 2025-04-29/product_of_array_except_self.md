# 🧲 Problem: Product of Array Except Self

- **Platform**: [LeetCode](https://leetcode.com/problems/product-of-array-except-self/description/)
- **Submission**: [https://leetcode.com/problems/product-of-array-except-self/submissions/1621010256/](https://leetcode.com/problems/product-of-array-except-self/submissions/1621010256/)
- **Date Solved**: 2025-04-29
- **Tags**: Array, Prefix Sum, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` **except** `nums[i]`.
**You must solve it without using division and in O(n) time.**
---

## 🧪 Examples

**Example 1**:
- Input: `nums = [1,2,3,4]`
- Output: `[24,12,8,6]`

**Example 2**:
- Input: `nums = [-1,1,0,-3,3]`
- Output: `[0,0,9,0,0]`

---

## 🚀 Approach
1. **Prefix pass**:
   - Traverse from left to right, maintaining a running product of all elements before the current index.
   - Store this in the result array.

2. **Postfix pass**:
   - Traverse from right to left, maintaining a running product of all elements after the current index.
   - Multiply this with the values already stored in the result array from the prefix pass.

3. The final result array contains the product of all elements except the current one, without using division and in O(n) time.


---

## 💻 Code (Python)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize the result list (res) with 1's. 
        # This list will hold the final products.
        res = [1] * (len(nums))
        
        # Step 2: Calculate the prefix products (product of all elements to the left of each element).
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix          # Store current prefix in result
            prefix *= nums[i]        # Update prefix

        # Step 3: Calculate the postfix products (product of all elements to the right of each element).
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # Multiply with current postfix
            postfix *= nums[i]       # Update postfix
        
        # Step 4: Return the final result
        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n
    - One pass for prefix, one pass for postfix
- **Space**: O(1)
    - Result array is not counted as extra space (as per problem statement)
