# 🧮 Problem: Guess Number Higher or Lower

- **Platform**: [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1607542988/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1607542988/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-15
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
The number you are guessing is between `1` and `n`. You need to guess the number using a binary search algorithm. The `guess()` API is available, and it works as follows:

- `guess(x)` returns:
  - `-1` if `x` is higher than the number,
  - `1` if `x` is lower than the number,
  - `0` if `x` is the number.

Your task is to guess the number.

---

## 🚀 My Approach
We will use a binary search approach to find the correct number. The algorithm follows these steps:

1. **Initialize Search Range**: Start with the left boundary at `1` and the right boundary at `n`.
2. **Binary Search**:
   - Calculate the middle point `m` of the current search range.
   - Call `guess(m)` to check if `m` is the number.
     - If `guess(m) == 1`, the target number is greater than `m`, so adjust the left boundary: `left = m + 1`.
     - If `guess(m) == -1`, the target number is smaller than `m`, so adjust the right boundary: `right = m - 1`.
     - If `guess(m) == 0`, then `m` is the target number and we return `m`.

---

## 💻 Code (Python)

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the search range
        left, right = 1, n

        # Perform a binary search to find the guessed number
        while True:
            # Find the middle point of the current range
            m = (left + right) // 2

            # Get the result of guessing 'm'
            res = guess(m)

            # If the guess is too low, move the left boundary up
            if res > 0:
                left = m + 1

            # If the guess is too high, move the right boundary down
            elif res < 0:
                right = m - 1

            # If the guess is correct, return the guessed number
            else:
                return m
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n), The algorithm divides the search space by half each time, leading to a logarithmic time complexity.
- **Space**: O(1), The solution uses a constant amount of space regardless of the input size.
