# 🧲 Problem: Tuple with Same Product

- **Platform**: [LeetCode](https://leetcode.com/problems/tuple-with-same-product/description/)
- **Submission**: [https://leetcode.com/problems/tuple-with-same-product/submissions/1786296787/](https://leetcode.com/problems/tuple-with-same-product/submissions/1786296787/)
- **Date Solved**: 2025-09-29
- **Tags**: DSA, Math
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an integer array `nums` of **distinct** positive integers, return the number of tuples `(a, b, c, d)` such that:

- `nums[a] * nums[b] == nums[c] * nums[d]`, and  
- `a, b, c, d` are **distinct indices**.

Tuples are ordered — i.e., `(a,b,c,d)` is different from `(c,d,a,b)` and order inside a pair matters (so `(a,b,...)` and `(b,a,...)` are different tuples).

---

## 🔹 Example

**Example:**  
```text
Input: `nums = [2, 3, 4, 6]`  
All index pairs with product 12 are: `(0,3)` (2×6) and `(1,2)` (3×4).

From these two pairs we can form 8 ordered tuples:

(0,3,1,2), (3,0,1,2), (0,3,2,1), (3,0,2,1),
(1,2,0,3), (2,1,0,3), (1,2,3,0), (2,1,3,0)

Output:
So output = 8
```

---

## 🔹 Key Idea / Approach

- Consider all unordered index pairs `(i, j)` with `i < j` and compute their product `p = nums[i] * nums[j]`.
- Group pairs by product: for a given product `p`, suppose there are `t` distinct index-pairs whose product equals `p`.
- How many **ordered** tuples `(a,b,c,d)` can we produce from those `t` pairs?

  - Choose a first unordered pair (t choices) and a different second unordered pair (t - 1 choices) → `t * (t - 1)` ordered selections of pair *identities*.
  - For each selected pair identity, elements inside each pair can be ordered in 2 ways each (swap within pair): `2 * 2 = 4`.
  - Total from product `p` = `4 * t * (t - 1)`.

- Sum that value over all products `p`.

**Implementation detail:**  
- First pass: count occurrences `t` for every product (using a hashmap).
- Second pass (or inline): for each product with count `t`, add `4 * t * (t - 1)` to the answer.

This approach is `O(n^2)` time (to enumerate all pairs) and `O(n^2)` worst-case space (distinct products).

---

## 🔹 Key Idea / Approach

- Consider all unordered index pairs `(i, j)` with `i < j` and compute their product `p = nums[i] * nums[j]`.
- Group pairs by product: for a given product `p`, suppose there are `t` distinct index-pairs whose product equals `p`.
- How many **ordered** tuples `(a,b,c,d)` can we produce from those `t` pairs?

  - Choose a first unordered pair (t choices) and a different second unordered pair (t - 1 choices) → `t * (t - 1)` ordered selections of pair *identities*.
  - For each selected pair identity, elements inside each pair can be ordered in 2 ways each (swap within pair): `2 * 2 = 4`.
  - Total from product `p` = `4 * t * (t - 1)`.

- Sum that value over all products `p`.

**Implementation detail:**  
- First pass: count occurrences `t` for every product (using a hashmap).
- Second pass (or inline): for each product with count `t`, add `4 * t * (t - 1)` to the answer.

This approach is `O(n^2)` time (to enumerate all pairs) and `O(n^2)` worst-case space (distinct products).

---

## 🔹 Code (Python)

```python
from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Map product -> number of unordered pairs (i < j) producing that product
        prod_count = defaultdict(int)
        n = len(nums)
        
        # Count all pair-products
        for i in range(n):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]
                prod_count[p] += 1
        
        # For each product with t pairs, number of ordered tuples is 4 * t * (t - 1)
        res = 0
        for t in prod_count.values():
            if t > 1:
                res += 4 * t * (t - 1)
        
        return res
```
---

## 💡 Time and Space Complexity
- **Time**: O(n^2) 
    — we enumerate all pairs (i, j) once.
- **Space**: O(n^2) in the worst case 
    — number of distinct pair products can be O(n^2).
