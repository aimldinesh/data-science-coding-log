# 🧲 Problem: Sum of Square Numbers

- **Platform**: [LeetCode](https://leetcode.com/problems/sum-of-square-numbers/description/)
- **Submission**: [https://leetcode.com/problems/sum-of-square-numbers/submissions/1785320932/](https://leetcode.com/problems/sum-of-square-numbers/submissions/1785320932/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given a non-negative integer `c`, determine if there exist two integers `a` and `b` such that:  

\[
a^2 + b^2 = c
\]

---

## 🔹 Examples

**Example 1:**  
Input: `c = 5`  
Output: `true`  
Explanation: 1² + 2² = 5  

**Example 2:**  
Input: `c = 3`  
Output: `false`  
Explanation: No integers `a` and `b` exist such that a² + b² = 3.  

---
---
🧠 Approach 1: Brute Force (O(√c²) = O(c))

🔹 Intuition
    - We can try every possible value of a and b, and check if any pair satisfies a² + b² = c.

## Code(Python)
```python
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Try all possible values for a
        for a in range(int(math.sqrt(c)) + 1):
            for b in range(int(math.sqrt(c)) + 1):
                if a * a + b * b == c:
                    return True
        return False

````
---

## Step by Step code execution with example
Example: c = 5

| a | b | a² + b² | Matches?        |
| - | - | ------- | --------------- |
| 0 | 0 | 0       | ❌               |
| 0 | 1 | 1       | ❌               |
| 0 | 2 | 4       | ❌               |
| 1 | 0 | 1       | ❌               |
| 1 | 1 | 2       | ❌               |
| 1 | 2 | 5       | ✅ → return True |

- ✅ Output: True (since 1² + 2² = 5)

---
Time Complexity
 + Outer loop: √c iterations
 + Inner loop: √c iterations
 + Total: O(c)
 + Very slow for large c (e.g., c = 10⁹)

Space Complexity: O(1)

---

## 🔹 Approach2 : Two-Pointer (Efficient O(√c))

We use the **two-pointer technique**:

1. Initialize `left = 0` and `right = int(sqrt(c))`.  
   - Because `a` and `b` cannot be larger than `sqrt(c)`.  
2. Compute `total = left² + right²`.  
   - If `total == c` → return `True`.  
   - If `total > c` → decrease `right` (to reduce sum).  
   - If `total < c` → increase `left` (to increase sum).  
3. Repeat until `left > right`.  
4. If no match found → return `False`.

---

## 🔹 Code (Python)

```python
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Two-pointer approach
        left, right = 0, int(sqrt(c))

        while left <= right:
            total = left * left + right * right

            if total > c:
                # Too large, decrease right
                right -= 1
            elif total < c:
                # Too small, increase left
                left += 1
            else:
                # Found: left^2 + right^2 == c
                return True

        # No such pair found
        return False
```
---
## Step by step code execution with example
Example: c = 5

We want to check if there exist integers a, b such that
a² + b² = 5

Initialization:
```python
left = 0
right = int(sqrt(5)) = 2
```
Iteration 1:
```python
left = 0, right = 2
total = 0² + 2² = 0 + 4 = 4
```
Compare:
  + total (4) < c (5)
  + ➡️ Increase left → left = 1

Iteration 2:
```python
left = 1, right = 2
total = 1² + 2² = 1 + 4 = 5
```
Compare:
 + total (5) == c (5)
 + ✅ Condition satisfied → return True

✅ Output: True
Because 5 = 1² + 2²

---
Example 2: c = 3
```python
left = 0, right = 1
```
| left | right | total               | Action             |
| ---- | ----- | ------------------- | ------------------ |
| 0    | 1     | 1                   | total < c → left++ |
| 1    | 1     | 2                   | total < c → left++ |
| 2    | 1     | left > right → stop |                    |

- No match found → return False
- ✅ Output: False (no two squares sum to 3)

---

## 💡 Time and Space Complexity
- **Time**: 
    - O(√c) (each pointer moves at most √c times)
    - Complexity = O(√c).
- **Space**: O(1)
    - Only constant extra space is used.

---
