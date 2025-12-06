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
##  Approach 1 : Brute Force
🧠 Intuition

- The most direct way to solve the problem is to follow the definition:
- For each index i in the array:
  - Compute the product of all elements except nums[i].

- This means:
  - For every element, we perform a full traversal of the array.
  - We skip the element at the current index.
  - Multiply all the others.

- Although this approach is simple and easy to understand, it is inefficient, because for every index we re-scan the whole array —resulting in O(n²) time.

🛠 Algorithm

1. Let n be the length of nums.
2. Create a result array res of size n.
3. For each index i from 0 to n - 1:
   - Set a running product prod = 1.
   - Loop through all indices j from 0 to n - 1:
     - If i != j, multiply prod by nums[j].
   - Store prod into res[i].
4. Return the result array res.
----
## Code(Python)
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # output array to store product for each index

        # For each element in the array
        for i in range(n):
            prod = 1  # running product for this index

            # Multiply all elements except nums[i]
            for j in range(n):
                if i == j:
                    continue  # skip the current index element
                prod *= nums[j]

            res[i] = prod  # store computed product
        
        return res
```
---
## 💡 Time and Space Complexity
- **Time**: O(n²)
    -  For each index, we traverse the entire array.
- **Space**: O(1)
    - extra space (ignoring output array).
 
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
