# 🧲 Problem: Container With Most Water

- **Platform**: [LeetCode](https://leetcode.com/problems/container-with-most-water/description/)
- **Submission**: [https://leetcode.com/problems/container-with-most-water/submissions/1633741140/](https://leetcode.com/problems/container-with-most-water/submissions/1633741140/)
- **Date Solved**: 2025-05-14
- **Tags**: Two Pointers, Array, Greedy
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).Find two lines that, together with the x-axis, form a container that can store the most water.
```python
Example:
Input:
height = [1,8,6,2,5,4,8,3,7]
Output:49

Explanation:
The lines at index 1 and 8 can hold the most water.
min(8, 7) * (8 - 1) = 7 * 7 = 49
```
---
## 🚀 Approach 1 : Brute Force (O(n²))

🧠 Intuition

Try every possible pair of lines (i, j) and compute the water they can hold. Area = width × height where width = j - i and height = the shorter of the two lines (water spills over the shorter one). Track the maximum across all pairs.
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Try all pairs:
(0,1) → min(1,8) × 1 = 1
(1,7) → min(8,3) × 6 = 18
(1,8) → min(8,7) × 7 = 49 ✅ max
```

📌 Approach

1. Outer loop i from 0 to n-1
2. Inner loop j from i+1 to n-1
3. area = (j - i) * min(height[i], height[j])
4. Update max_area
5. Return max_area

---

## 💻 Code (Python)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the area for every pair of lines
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area


```

---

## 💡 Time and Space Complexity
- **Time**:  O(n²)
- **Space**: O(1)
   - No extra space is used.

## 🚀 Approach 2 : Two Pointers (Optimized O(n))

🧠 Intuition
Start with the widest possible container (pointers at both ends). Width can only shrink as pointers move inward — so the only hope of finding a bigger area is finding a taller line. Always move the shorter line inward — keeping it guarantees area stays same or shrinks, moving it gives a chance to find something taller.
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          ↑                          ↑
        left                       right
        
Width is maximum here — move inward only if height can compensate
```

📌 Approach

1. left=0, right=n-1, res=0
2. While left < right:
   + Compute area = (right - left) × min(height[left], height[right])
   + Update res
   + Move shorter pointer inward

3. Return res



---

## 💻 Code (Python)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the start and end of the array
        left, right = 0, len(height) - 1
        # Variable to store the maximum area
        res = 0

        # Loop until the pointers meet
        while left < right:
            # Calculate the area between the two lines
            area = (right - left) * min(height[left], height[right])
            # Update the maximum area found so far
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left

        # Return the maximum area
        return res

```

---
### 🔍 Step-by-Step Execution

Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```
Indices:  0  1  2  3  4  5  6  7  8
Values:   1  8  6  2  5  4  8  3  7
```

Step 1: left=0, right=8
```
area = (8-0) × min(1,7) = 8×1 = 8
res = max(0,8) = 8
height[0]=1 < height[8]=7 → left++
left=1
```
Step 2: left=1, right=8
```
area = (8-1) × min(8,7) = 7×7 = 49
res = max(8,49) = 49
height[1]=8 > height[8]=7 → right--
right=7
```
Step 3: left=1, right=7
```
area = (7-1) × min(8,3) = 6×3 = 18
res = max(49,18) = 49
height[1]=8 > height[7]=3 → right--
right=6
```
Step 4: left=1, right=6
```
area = (6-1) × min(8,8) = 5×8 = 40
res = max(49,40) = 49
height[1]=8 == height[6]=8 → right--
right=5
```
Step 5: left=1, right=5
```
area = (5-1) × min(8,4) = 4×4 = 16
res = max(49,16) = 49
height[1]=8 > height[5]=4 → right--
right=4
```
Step 6: left=1, right=4
```
area = (4-1) × min(8,5) = 3×5 = 15
res = max(49,15) = 49
height[1]=8 > height[4]=5 → right--
right=3
```
Step 7: left=1, right=3
```
area = (3-1) × min(8,2) = 2×2 = 4
res = max(49,4) = 49
height[1]=8 > height[3]=2 → right--
right=2
```
Step 8: left=1, right=2
```
area = (2-1) × min(8,6) = 1×6 = 6
res = max(49,6) = 49
height[1]=8 > height[2]=6 → right--
right=1
```
Loop ends: left=1 == right=1

---
### 💡 Why Moving Shorter Line is Always Correct
```
Current state: left=L, right=R, height[L] < height[R]

Area = (R-L) × height[L]   ← capped by LEFT (shorter)

If we move RIGHT inward instead:
  New width  = (R-1-L)      → strictly smaller
  New height ≤ height[L]    → still capped by left (shorter)
  → New area < current area  → pointless ❌

If we move LEFT inward:
  New width  = (R-L-1)      → smaller
  New height = min(height[L+1], height[R])
             could be > height[L] ✅  → area might improve

∴ Always move the shorter pointer inward
```
---
### 💡 Pointer Movement Visualised
```
[1,  8,  6,  2,  5,  4,  8,  3,  7]
 L→                                R    area=8,  move L (shorter)
     L                             R    area=49, move R (shorter)
     L                         R        area=18, move R
     L                     R            area=40, move R
     L                 R                area=16, move R
     L             R                    area=15, move R
     L         R                        area=4,  move R
     L     R                            area=6,  move R
     L  R                               left==right → stop

```
---
## ✅ Final Answer
```
return res = 49   (between index 1 and 8, heights 8 and 7) ✅
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Each element is visited at most once by the two pointers.
- **Space**: O(1)
   - No extra space is used.

---
### 💡 Interview tip: 

If asked "how do you know you're not missing the optimal pair?" — the answer is: "When we move the shorter pointer, we've already considered every pair that included it at its current position. Any pair with the taller pointer and a closer index will have smaller width AND same or smaller height — so none of them can beat what we've already seen."
