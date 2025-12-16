# 🧲 Problem: Russian Doll Envelopes

- **Platform**: [LeetCode](https://leetcode.com/problems/russian-doll-envelopes/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/russian-doll-envelopes/submissions/1611444026/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/russian-doll-envelopes/submissions/1611444026/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-19
- **Tags**: Array, Binary Search, Sorting
- **Difficulty**: Hard

---

## ✅ Problem Statement
Given a list of envelopes where each envelope is represented as `[width, height]`, you can put one envelope into another **only if both the width and height of one envelope are strictly less than the other**.
Return the **maximum number of envelopes** you can Russian doll (put one inside another).


---
## Examples
```python
Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
```
---

## 🚀 My Approach : Sorting + Longest Increasing Subsequence (LIS)
### 💡 Key Insight:
- We cannot apply LIS directly on both dimensions.
- So we **sort envelopes** by:
  - **Width (ascending)**
  - **Height (descending)** for same width to avoid falsely nesting same-width envelopes.
- Then, we extract **heights** and apply LIS on it.

---

## 💻 Code (Python)

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort the envelopes by width ascending, and by height descending if widths are the same
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract the heights from the sorted envelopes
        heights = [envelope[1] for envelope in envelopes]
        
        # Step 3: Find the LIS on the heights using binary search
        # dp array will store the smallest possible tail value for increasing subsequences of different lengths
        dp = []
        
        for h in heights:
            # Use binary search to find the position to replace in dp array
            idx = bisect_left(dp, h)
            
            if idx == len(dp):
                dp.append(h)  # If h is greater than all elements in dp, append it
            else:
                dp[idx] = h  # Otherwise, replace the element at index idx with h
        
        # The length of dp is the length of the longest increasing subsequence
        return len(dp)

```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
   - Sorting takes O(n log n)
   - LIS using binary search takes O(n log n)
- **Space**: O(n)
   - For the dp array used in LIS.
