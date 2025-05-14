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
🧾 Example
Input:
height = [1,8,6,2,5,4,8,3,7]
Output:49
Explanation:
The lines at index 1 and 8 can hold the most water.
min(8, 7) * (8 - 1) = 7 * 7 = 49
```
---
## 🧠 Intuition
- A brute-force method would be to try every pair of lines, but that takes O(n²) time.
- Using the two-pointer approach, we can move inward from both ends and keep track of the maximum area.
- The key insight is that the shorter line limits the height, so we move the shorter line inward to potentially find a better container.

---
## 🚀 Approach 1 : Brute Force (O(n²))
🔸 Steps:
      - Use two nested loops to try every pair (i, j).
      - For each pair, calculate the area.
      - Track the maximum.
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
🔸 Steps:
      - Initialize two pointers — one at the start (left) and one at the end (right).
      - Calculate the area between them.
      - Update the maximum area.
      - Move the pointer pointing to the shorter line inward to possibly find a taller line.

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
