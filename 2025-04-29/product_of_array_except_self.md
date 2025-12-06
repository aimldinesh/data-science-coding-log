# 🧲 Problem: Product of Array Except Self

- **Platform**: [LeetCode](https://leetcode.com/problems/product-of-array-except-self/description/)
- **Submission**: [https://leetcode.com/problems/product-of-array-except-self/submissions/1621010256/](https://leetcode.com/problems/product-of-array-except-self/submissions/1621010256/)
- **Date Solved**: 2025-04-29
- **Tags**: Array, Prefix Sum, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` **except** `nums[i]`.
- **You must solve it without using division and in O(n) time.**
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

## 🚀 Approach 2 : Prefix & Suffix
🧠 Intuition
We don’t need to compute the product of all elements separately for each index, nor do we need additional prefix/suffix arrays.

Instead, we can build the solution in two efficient passes using only:
 - A prefix running product, and
 - A postfix running product

How it works:

1. First Pass (Prefix)
   - For each index i, store the product of all elements to the left of i in res[i].
   - Maintain a running prefix value and update it as we move forward.

2. Second Pass (Postfix)
   - For each index i, multiply res[i] by the product of all elements to the right of i.
   - Maintain a running postfix and update it as we move backward.

This approach effectively computes:
```python
res[i] = (product of all left elements) * (product of all right elements)
```
And because we reuse the res array and only keep two integers (prefix, postfix), the extra space used is O(1).

🛠 Algorithm

1. Initialize the result array res with all values set to 1.
2. Set prefix = 1.
3. First pass (Left → Right):
   - For every index i:
     - Set res[i] = prefix.
     - Update prefix *= nums[i].

4. Set postfix = 1.
5. Second pass (Right → Left):
   - For every index i:
     - Multiply res[i] by postfix.
     - Update postfix *= nums[i].

6. Return res.

---

## 💻 Code (Python)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Step 1: initialize result with 1s

        # Step 2: prefix pass (compute product of all left-side elements)
        prefix = 1
        for i in range(n):
            res[i] = prefix      # store product of all elements to the left
            prefix *= nums[i]    # update prefix by multiplying current element

        # Step 3: postfix pass (compute product of all right-side elements)
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix     # multiply with right-side product
            postfix *= nums[i]    # update postfix

        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(n
  - One left-to-right pass
  - One right-to-left pass
- **Space**: O(1)
    - Output array is not considered extra space per LeetCode rules
    - Only two variables: prefix and postfix
