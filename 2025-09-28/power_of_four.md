# 🧲 Problem: Power of Four

- **Platform**: [LeetCode](https://leetcode.com/problems/power-of-four/description/)
- **Submission**: [https://leetcode.com/problems/power-of-four/submissions/1784972731/](https://leetcode.com/problems/power-of-four/submissions/1784972731/)
- **Date Solved**: 2025-09-28
- **Tags**: DSA, Math
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given an integer `n`.  
Return **true** if `n` is a power of four, otherwise return **false**.  


Formally, `n` is a power of four if there exists an integer `x` such that:  

\[
n = 4^x
\]

---

## 🔹 Examples

**Example 1:**  
Input: `n = 16`  
Output: `true`  

(Explanation: \( 4^2 = 16 \))  

**Example 2:**  
Input: `n = 5`  
Output: `false`  

**Example 3:**  
Input: `n = 1`  
Output: `true`  
(Explanation: \( 4^0 = 1 \))  

---

## 🔹 Approaches

### 1️⃣ Recursive Approach

1. **Base Case**  
   - If `n == 1`, return `True`.  

2. **Invalid Case**  
   - If `n <= 0` or `n % 4 != 0`, return `False`.  

3. **Recursive Step**  
   - Divide `n` by 4 and check recursively.  

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Base case
        if n == 1:
            return True
        # Invalid case
        if n <= 0 or n % 4 != 0:
            return False
        # Recursive step
        return self.isPowerOfFour(n // 4)
```
---

### Step by step Execution with example

Example 1: n = 16

Step 1:
 + n = 16
 + n > 0 ✅
 + n % 4 == 0 ✅
 → recursive call with n = 16 // 4 = 4

Step 2:
 + n = 4
 + n % 4 == 0 ✅
 → recursive call with n = 4 // 4 = 1

Step 3:
 + n = 1
 + Base case → return True

All recursive calls return True ✅
Final Output → True
---
Example 2: n = 8

Step 1:
 + n = 8
 + n % 4 == 0 ✅
 → recursive call with n = 8 // 4 = 2

Step 2:
 + n = 2
 + n % 4 != 0 ❌ → return False
- Final Output → False
---
Example 3: n = -4
- n <= 0 ❌ → return False immediately

---

## 💡 Time and Space Complexity
- **Time**: O(log4​^n)
- **Space**: O(log4^n)

---

### Aproach:Iterative Approach
- Check negativity
  - If n < 0, return False.

- Loop division by 4
  - While n > 1, check if divisible by 4.
  - If not divisible, return False.
  - Otherwise, divide by 4.

- Final check
  - Return True if n reaches 1.

---

## code
```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4

        return n == 1
```
---

### Step by step execution with example
Example 1: n = 16
| Step | n  | n % 4 | Action                |
| ---- | -- | ----- | --------------------- |
| 1    | 16 | 0     | Divide → n = 4        |
| 2    | 4  | 0     | Divide → n = 1        |
| 3    | 1  | —     | End loop → `n == 1` ✅ |

- ✅ Output → True (16 = 4²)
 
---

Example 2: n = 8

| Step | n | n % 4 | Action                         |
| ---- | - | ----- | ------------------------------ |
| 1    | 8 | 0     | Divide → n = 2                 |
| 2    | 2 | 2     | Not divisible → return False ❌ |

- ❌ Output → False (8 is not a power of 4)

---

## 💡 Time and Space Complexity
- **Time**: O(log4​^n)
- **Space**: O(1)

---

3️⃣ Math / Logarithm Approach

- Check positivity
  - If n <= 0, return False.

- Logarithm Check
  - Take logarithm of n base 4.
  - If the result is an integer, n is a power of 4.

---

## Code:
```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) % 1 == 0
```
---
### step by step execution with example

Input: n = 64
 - log₄(64) = log(64) / log(4) = 3
 - 3 % 1 == 0 ✅
 - Return True

Input: n = 12
 - log₄(12) ≈ 1.792
 - 1.792 % 1 ≠ 0 ❌
 - Return False

--- 

## 💡 Time and Space Complexity
- **Time**: O(1)
- **Space**: O(1)
