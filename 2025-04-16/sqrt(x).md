# 🧮 Problem: Sqrt(x)

- **Platform**: [LeetCode](https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/sqrtx/submissions/1608375841/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Implement a function that computes the square root of a non-negative integer `x`, and returns the integer part of the square root.


---
## Examples
```python
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```
---

## 🚀 Approach : Binary Search
🧠 Intuition

Square root is monotonically increasing — so binary search works perfectly. Search for the largest integer mid where mid² ≤ x. Since we want the floor of the square root, when there's no exact answer, right ends up pointing to the best integer answer.
```python
x = 8  →  √8 = 2.82...  →  floor = 2

Try mid=1 → 1²=1  < 8  → go right
Try mid=2 → 2²=4  < 8  → go right
Try mid=3 → 3²=9  > 8  → go left
→ right = 2 ✅
```
---

📌 Approach

1. Handle base case — x < 2 returns x directly
2. Binary search between left=0 and right=x
3. At each mid:
   - mid² == x → exact answer, return mid
   - mid² < x  → too small → left = mid + 1
   - mid² > x  → too big  → right = mid - 1

4. Loop exits when left > right → return right

---

## 💻 Code (Python)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle base cases for small inputs
        if x < 2:  # For x = 0 or 1, the square root is x itself
            return x

        # Initialize the search range
        left, right = 0, x

        while left <= right:
            # Find the middle of the current range
            mid = (left + right) // 2
            square = mid * mid  # Calculate the square of mid

            if square == x:  # If mid squared equals x, we've found the exact square root
                return mid
            elif square < x:  # If mid squared is less than x, move to the right half
                left = mid + 1
            else:  # If mid squared is greater than x, move to the left half
                right = mid - 1

        # When the loop exits, right points to the largest integer such that right^2 <= x
        return right

```

---
## 🔍 Step-by-Step Execution
```
Input: x = 8
Actual √8 = 2.828...  →  expected output = 2
```
Iteration 1
```
left=0, right=8
mid = (0+8)//2 = 4
square = 4×4 = 16

16 > 8 → too big ❌
right = mid-1 = 3
```
Iteration 2
```
left=0, right=3
mid = (0+3)//2 = 1
square = 1×1 = 1

1 < 8 → too small ❌
left = mid+1 = 2
```
Iteration 3
```
left=2, right=3
mid = (2+3)//2 = 2
square = 2×2 = 4

4 < 8 → too small ❌
left = mid+1 = 3
```
Iteration 4
```
left=3, right=3
mid = (3+3)//2 = 3
square = 3×3 = 9

9 > 8 → too big ❌
right = mid-1 = 2
```
Loop ends: left=3 > right=2
```
return right = 2 ✅
```
---
📊 Trace Table
```
Iter   left   right    mid   mid²         mid² vs x       Action           
1       0      8       4     16            16 > 8 ❌      right=3 
2       0      3       1     1             1 < 8 ❌       left=2
3       2      3       2     4             4 < 8 ❌       left=3
4       3      3       3     9             9 > 8 ❌       right=2
```
---

💡 Why Return right Not left?
```
When loop exits:  left = 3,  right = 2

right = 2  →  2² = 4  ≤  8  ✅  largest valid answer
left  = 3  →  3² = 9  >  8  ❌  overshoots

right always lands on the largest integer whose square ≤ x
left  always lands one step too far (overshoots)
```
---

### 🔍 Exact Square Root Case
```
Input: x = 9

Iter           left          right        mid        mid²        Action
1               0            9            4           16         right=3 
2               0            3            1           1          left=2
3               2            3            2           4          left=3
4               3            3            3           9          return 3 ✅
```
```
mid²== x → return mid immediately, no need to wait for loop exit
```
✅ Final Answer
```
x=8  →  return right = 2   (floor of √8 = 2.82) ✅
x=9  →  return mid   = 3   (exact √9 = 3)       ✅
```
---

## 💡 Time and Space Complexity
- **Time**: O(log x), due to the binary search.
- **Space**: O(1), Only pointers and square variable used
