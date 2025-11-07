# 🧲 Problem: Can Place Flowers

- **Platform**: [LeetCode](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)
- **Submission**: [https://leetcode.com/problems/can-place-flowers/submissions/1823284871/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/can-place-flowers/submissions/1823284871/?envType=study-plan-v2&envId=leetcode-75)
- **Date Solved**: 2025-11-07
- **Tags**: DSA, Array, LeetCode75
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given a flowerbed representing plots:
- `1` → already has a flower  
- `0` → empty  

A new flower cannot be planted in **adjacent** plots.
  + flowerbed: List[int]
  + n: int (number of flowers you want to plant)

- Return **True** if you can plant all `n` flowers without violating rules.  
- Return **False** otherwise.

```python
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Explanation: You can plant at index 2.

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

```


---

## 🚀 ✅ Approach 1: Padding Technique
### 🔹 Idea

- To avoid dealing with boundary cases (i = 0 and i = last),
- we add a 0 at the start and end of the flowerbed:
```python
flowerbed = [1,0,0,0,1]
padded     = [0,1,0,0,0,1,0]
```
Now, for any position i, we simply check:
```python
f[i-1] == 0 AND f[i] == 0 AND f[i+1] == 0
```
- If yes → we plant a flower there (f[i] = 1) and reduce n.

### 🔹 Why it works?
- Padding ensures every position always has valid left/right neighbors.
  - → No need for boundary checks.
  - → Logic becomes simple and uniform.

---

## 💻 Code (Python)

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add padding to avoid boundary checks
        f = [0] + flowerbed + [0]

        # Check each plot from index 1 to len(f)-2
        for i in range(1, len(f) - 1):
            # If left, current, and right are empty
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1      # Plant flower
                n -= 1         # Decrease required count

        # Return True if all required flowers were planted
        return n <= 0

```

---

## ✅ Step-by-Step Dry Run
```python
Input:
flowerbed = [1,0,0,0,1]
n = 1

After Padding:
f = [0, 1, 0, 0, 0, 1, 0]
```
Iteration:
| i | f[i-1] | f[i] | f[i+1] | Can Plant? | Action                  |
| - | ------ | ---- | ------ | ---------- | ----------------------- |
| 1 | 0      | 1    | 0      | ❌          | Skip                    |
| 2 | 1      | 0    | 0      | ❌          | Skip                    |
| 3 | 0      | 0    | 0      | ✅          | Plant → f[3] = 1, n = 0 |
| 4 | 1      | 0    | 1      | ❌          | Skip                    |
| 5 | 0      | 1    | 0      | ❌          | Skip                    |

- ✅ n == 0 → Return True

## 💡 Time and Space Complexity
- **Time**: O(n)
  - We traverse the padded array once.
  - Padding adds constant overhead.
- **Space**: O(n)
  - We create a new array [0] + flowerbed + [0].

---

## ✅ Approach 2: Greedy Skip Method (Optimal O(1) Space)
### 🔹 Idea

We iterate through the flowerbed and skip positions smartly:

- If flowerbed[i] == 1
  - → We must skip the next plot (i += 2) because planting is not allowed adjacent.

- If flowerbed[i] == 0:
  - If i == last index OR flowerbed[i+1] == 0
    - → We can plant at i
    - → Set flowerbed[i] = 1, decrement n, and skip next index (i += 2)

  - Else
    - → Next is 1, so we skip (i += 3)

This method ensures:
  - No extra space
  - Fewer checks
  - Faster traversal

---

✅ Code (Greedy Skip)
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        size = len(flowerbed)

        while i < size:
            # Case 1: Already has a flower
            if flowerbed[i] == 1:
                i += 2  # skip next plot
                continue

            # Case 2: Empty plot
            next_empty = (i == size - 1) or (flowerbed[i + 1] == 0)

            if next_empty:
                flowerbed[i] = 1   # plant flower
                n -= 1
                i += 2             # skip next plot
            else:
                i += 3  # next is 1, skip 2 plots

            if n <= 0:
                return True

        return n <= 0
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
  - Single pass.
  - Skips unnecessary indices, but worst-case still linear.
- **Space**: O(1)
  - Uses only a few variables (i, size).
  - Modifies flowerbed in-place.

---

## ✅ Approach 3: Brute Force Neighbor Check (Simple to Understand)
### 🔹 Idea

For each position i:
  - If it's 0, check:
    - Left neighbor is 0 or out of bounds
    - Right neighbor is 0 or out of bounds
  - If both conditions are true → plant a flower.

This method is simple but includes boundary checks.

## ✅ Code (Brute Force)
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return n <= 0
```
---
## ✅ Step-by-Step Dry Run
```python
flowerbed = [1,0,0,0,1], n = 1
```
| i | flowerbed | left ok?  | right ok? | action        |
| - | --------- | --------- | --------- | ------------- |
| 0 | 1 0 0 0 1 | —         | —         | cannot plant  |
| 1 | 1 0 0 0 1 | left=1→no | —         | cannot plant  |
| 2 | 1 0 0 0 1 | left=0    | right=0   | ✅ plant → n=0 |
| 3 | —         | —         | —         | exit early    |
| 4 | —         | —         | —         | —             |

- ✅ Output: True

---

## 💡 Time and Space Complexity
- **Time**: O(n)
  - Single full scan of the flowerbed.

- **Space**: O(1)
  - Constant extra space.
  - Only uses local variables (left_empty, right_empty).

---

✅ Summary Table (All Approaches)
| Approach                       | Description                             | Time     | Space    | Best Use Case                |
| ------------------------------ | --------------------------------------- | -------- | -------- | ---------------------------- |
| **Padding Technique**          | Add 0’s on both ends for easy checking  | **O(n)** | **O(n)** | When readability is priority |
| **Greedy Skip (Optimal)**      | Skip neighbors smartly to reduce checks | **O(n)** | **O(1)** | Best & most efficient        |
| **Brute Force Neighbor Check** | Check each index and its neighbors      | **O(n)** | **O(1)** | Simple logic, no extra space |

