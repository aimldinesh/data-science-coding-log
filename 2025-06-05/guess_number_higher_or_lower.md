# 🧲 Problem: Guess Number Higher or Lower

- **Platform**: [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/description/)
- **Submission**: [https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1654742912/](https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1654742912/)
- **Date Solved**: 2025-06-05
- **Tags**: Binary Search, Linear Search
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given an integer n, where you need to guess a number from 1 to n.
There is a pre-defined API int guess(int num):

- It returns:

   - -1 if the number I picked is lower than your guess.
   - 1 if the number I picked is higher than your guess.
   - 0 if your guess is correct.

### Example:
```python
Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

```
---

## 🚀 Approach : Binary Search
💡 Intuition:
- The feedback from the guess() function helps us decide whether to search left or right — just like in binary search.
- We can use binary search to efficiently zero in on the correct number in log(n) time.

🧠 Approach :
- Set the initial boundaries: left = 1, right = n.
- While left <= right:
     - Calculate mid = (left + right) // 2.
     - Call guess(mid):
          - If result is 0, return mid — the correct number is found.
          - If result is -1, the correct number is lower → update right = mid - 1.
          - If result is 1, the correct number is higher → update left = mid + 1.
---

## 💻 Code (Python)

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize search boundaries
        left, right = 1, n

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle number
            res = guess(mid)           # Call the guess API with mid

            if res == 0:
                return mid             # If guess is correct, return mid
            elif res < 0:
                # If the target number is lower than mid, move left
                right = mid - 1
            else:
                # If the target number is higher than mid, move right
                left = mid + 1
```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
    - Efficient binary search reduces the number of guesses logarithmically.
- **Space**: O(1)
    - Uses constant space regardless of input size.

---

## 🚀 Approach : Linear Search


## 💻 Code (Python)

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        # Iterate through numbers from 1 to n
        for num in range(1, n + 1):
            # Call the guess API
            # guess(num) returns:
            # -1 if the number is higher
            #  1 if the number is lower
            #  0 if it's the correct number
            if guess(num) == 0:
                return num  # Found the correct number

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - n the worst case, the loop runs n times if the number is at the end.
- **Space**: O(1)
    - No extra space is used apart from variables.
