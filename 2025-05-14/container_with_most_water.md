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

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Each element is visited at most once by the two pointers.
- **Space**: O(1)
   - No extra space is used.
