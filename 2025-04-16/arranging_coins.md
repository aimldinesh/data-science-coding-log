# 🧮 Problem: Arranging Coins

- **Platform**: [LeetCode](https://leetcode.com/problems/arranging-coins/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/arranging-coins/submissions/1482651655/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/arranging-coins/submissions/1482651655/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Given `n` coins, you need to arrange them in a staircase shape such that each row has one more coin than the previous row. You need to determine the maximum number of complete rows that can be formed with the `n` coins.

---
## Examples
```python
Example1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
```

---


## 🚀 My Approach
We use **binary search** to find the maximum number of complete rows that can be formed:

1. **Initialize the search range:** We start with `left = 0` and `right = n` as the possible number of rows.
2. **Binary Search:** 
   - Calculate the middle value `mid` between `left` and `right`.
   - The total number of coins required for `mid` rows can be computed using the formula: 
     \[
     \text{coins} = \frac{\text{mid}}{2} \times (\text{mid} + 1)
     \]
   - If the total coins exceed `n`, we reduce the search range by setting `right = mid - 1`.
   - If the coins fit within `n`, we update the result and increase the search range by setting `left = mid + 1`.

3. **Final Result:** After the binary search, the variable `res` will hold the maximum number of complete rows.

---

## 💻 Code (Python)

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize the search range for the number of rows
        left, right = 0, n
        res = 0  # Variable to store the maximum number of complete rows

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle value
            # Total coins required for 'mid' rows using the formula: (mid/2) * (mid + 1)
            coins = (mid / 2) * (mid + 1)

            # If the total coins exceed 'n', reduce the search space
            if coins > n:
                right = mid - 1
            else:
                # If coins fit within 'n', update result and increase the search space
                left = mid + 1
                res = max(res, mid)

        # Return the maximum number of complete rows
        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), The binary search runs in O(log n) because the search range is halved in each iteration.
- **Space**: O(1),  Only a few variables are used for computation, so the space complexity is constant.
