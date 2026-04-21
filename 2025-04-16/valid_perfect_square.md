# 🧮 Problem: Valid Perfect Square

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-perfect-square/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/valid-perfect-square/submissions/1608349630/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/valid-perfect-square/submissions/1608349630/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Math, Binary Search, DSA

---

## ✅ Problem Statement
- Given a positive integer `num`, write a function that returns `True` if `num` is a perfect square else `False`.

---
## Examples
```python
Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

```
---


## 🚀 Approach : Binary Search
🧠 Intuition
A perfect square is an integer whose square root is also an integer — 1, 4, 9, 16, 25.... Since squares grow monotonically, binary search the range 1 to num looking for an exact mid² == num. If found → True, if the loop exhausts without finding it → False.
```
num=16 → is there an integer mid where mid²=16? → mid=4 ✅ True
num=14 → is there an integer mid where mid²=14? → no   ❌ False
```
📌 Approach

1. Base case — num < 2 returns True (0 and 1 are perfect squares)
2. Binary search between left=1 and right=num
3. At each mid:
   - mid² == num → perfect square → return True
   - mid² < num  → too small → left = mid + 1
   - mid² > num  → too big  → right = mid - 1

4. Loop exits → no perfect square found → return False
---

## 💻 Code (Python)

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:  # Handle small numbers
            return True

        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:  # Perfect square found
                return True
            elif square < num:  # Search in the right half
                left = mid + 1
            else:  # Search in the left half
                right = mid - 1

        return False  # No perfect square found

```

---
## 🔍 Step-by-Step Execution — Case 1

Input: num = 16 (perfect square)
```
Expected: True  (4 × 4 = 16)
Iteration 1
left=1, right=16
mid = (1+16)//2 = 8
square = 8×8 = 64

64 > 16 → too big ❌
right = mid-1 = 7
```
Iteration 2
```
left=1, right=7
mid = (1+7)//2 = 4
square = 4×4 = 16

16 == 16 → ✅ Perfect square found!
return True
```
---
### 📊 Trace Table — num = 16
```
Iter       left      right        mid       mid²         mid² vs num      Action  
1           1         16          8         64            64 > 16 ❌      right=7
2           1         7           4         16            16 == 16 ✅     return True
```
---
🔍 Step-by-Step Execution — Case 2

Input: num = 14 (not a perfect square)
```
Expected: False  (√14 = 3.74...)
```
Iteration 1
```
left=1, right=14
mid = (1+14)//2 = 7
square = 7×7 = 49

49 > 14 → too big ❌
right = mid-1 = 6
```
Iteration 2
```
left=1, right=6
mid = (1+6)//2 = 3
square = 3×3 = 9

9 < 14 → too small ❌
left = mid+1 = 4
```
Iteration 3
```
left=4, right=6
mid = (4+6)//2 = 5
square = 5×5 = 25

25 > 14 → too big ❌
right = mid-1 = 4
```
Iteration 4
```
left=4, right=4
mid = (4+4)//2 = 4
square = 4×4 = 16

16 > 14 → too big ❌
right = mid-1 = 3
Loop ends: left=4 > right=3
return False ✅
```
---
### 📊 Trace Table — num = 14
```
Iter          left     right       mid      mid²         mid² vs num        Action
1             1        14          7        49            49 > 14 ❌        right=6
2             1        6           3        9              9 < 14 ❌        left=4
3             4        6           5        25            25 > 14 ❌        right=4
4             4        4           4        16            16 > 14 ❌        right=3
```
---
## 💡 isPerfectSquare vs mySqrt — Key Difference
```
python# mySqrt → finds floor of √x, always returns a value
# returns right when no exact root exists

mySqrt(14)          →  3        (floor of 3.74)
mySqrt(16)          →  4        (exact)

# isPerfectSquare → only cares about exact match
# returns False when no exact root exists

isPerfectSquare(14) →  False    (3.74 is not integer)
isPerfectSquare(16) →  True     (4 is integer)

# In fact isPerfectSquare can be written using mySqrt:
def isPerfectSquare(num):
    r = mySqrt(num)
    return r * r == num
```
✅ Final Answers
```
num=16  →  return True   (4² = 16  exact match) ✅
num=14  →  return False  (no integer squares to 14) ✅
```
---

## 💡 Time and Space Complexity
- **Time**: O(log n), due to binary search.
- **Space**: O(1), no extra space used, Only pointers and square variable used

---
## 💡 Tip: 
There's also an O(1) math solution using int(num**0.5) ** 2 == num — but floating point precision can fail on large numbers. Binary search is the safe, interview-preferred approach as it avoids float precision issues entirely.

