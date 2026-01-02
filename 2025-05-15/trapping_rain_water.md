# 🧲 Problem: Trapping Rain Water

- **Platform**: [LeetCode](https://leetcode.com/problems/trapping-rain-water/description/)
- **Submission**: [https://leetcode.com/problems/trapping-rain-water/submissions/1634709940/](https://leetcode.com/problems/trapping-rain-water/submissions/1634709940/)
- **Date Solved**: 2025-05-15
- **Tags**: Array, Two Pointers, Dynamic Programming, Stack
- **Difficulty**: Hard

---

## ✅ Problem Statement
- Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---
### 🧾 Examples
```python
Example 1:
Input:height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation:
Water trapped at positions:
    index 2 → 1 unit
    index 4 → 1 unit
    index 5 → 2 units
    index 6 → 1 unit
    index 10 → 1 unit

Example 2:
Input:height = [4,2,0,3,2,5]

Output: 9
```
---
## 🧠 Intuition
- The amount of water trapped at any index depends on the minimum of the max height to its left and right, minus its own height.
- By using two pointers from both ends and tracking leftMax and rightMax, we can compute the trapped water in one pass.
## 🚀 Approach : Two Pointers (Optimal)
🔸 Steps:
- Use two pointers l and r starting from both ends.
- Track leftMax and rightMax.
- Always move the pointer at the side with the lower max, since that determines the water level at that side.
- At each step, calculate trapped water as min(leftMax, rightMax) - height[i].

---

## 💻 Code (Python)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0  # If the height array is empty, no water can be trapped

        l, r = 0, len(height) - 1  # Two pointers: left and right ends
        leftMax, rightMax = height[l], height[r]  # Max heights seen so far from both ends
        res = 0  # Total water trapped

        while l < r:
            if leftMax < rightMax:
                # Move left pointer
                l += 1
                leftMax = max(leftMax, height[l])  # Update leftMax if needed
                res += leftMax - height[l]  # Water trapped at index l = leftMax - current height
            else:
                # Move right pointer
                r -= 1
                rightMax = max(rightMax, height[r])  # Update rightMax if needed
                res += rightMax - height[r]  # Water trapped at index r = rightMax - current height

        return res  # Return total water trapped

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Single pass using two pointers.
- **Space**: O(1)
    - Constant extra space used.
