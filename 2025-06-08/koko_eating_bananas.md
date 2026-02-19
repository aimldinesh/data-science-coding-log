# 🧲 Problem: Koko Eating Bananas

- **Platform**: [LeetCode](https://leetcode.com/problems/koko-eating-bananas/description/)
- **Submission**: [https://leetcode.com/problems/koko-eating-bananas/submissions/1657673318/](https://leetcode.com/problems/koko-eating-bananas/submissions/1657673318/)
- **Date Solved**: 2025-06-08
- **Tags**: Binary Search, Greedy, Array
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Koko loves to eat bananas. There are n piles of bananas, the i-th pile has piles[i] bananas. The guards allow her to eat at most h hours.
- Each hour, she chooses a pile and eats up to k bananas from that pile. If the pile has less than k bananas, she eats all of them and won't return to it.
- Return the minimum integer k such that she can eat all the bananas within h hours.

### 🌰 Examples
```python
Input: piles = [3, 6, 7, 11], h = 8
Output: 4

Explanation:
At speed 4, Koko can eat all bananas in 8 hours:
[3/4=1hr], [6/4=2hr], [7/4=2hr], [11/4=3hr] → total = 8hr
```
---

## 🚀 Approach : Binary Search
💡 Intuition
- The higher the eating speed k, the faster Koko finishes.
- We want the minimum speed such that total time ≤ h.
- So we apply binary search on the value of k.

🚀 Approach
- Search Range:
     - left = 1 (minimum speed)
     - right = max(piles) (worst case: eat largest pile in 1 hour)

- Binary Search:
     - For a mid-speed k, calculate the total hours needed to finish all piles.
     - Use math.ceil(p / k) to get the hours for each pile.
     - If total hours ≤ h, try to minimize speed (search left).
     - If total hours > h, increase speed (search right).

---

## 💻 Code (Python)

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search range: minimum speed = 1, maximum = max pile size
        left, right = 1, max(piles)
        res = right  # Initialize result with the highest possible speed

        # Binary Search to find minimum valid eating speed
        while left <= right:
            k = (left + right) // 2  # Try middle speed

            hour = 0
            for p in piles:
                # How many hours to eat pile p at speed k (round up)
                hour += math.ceil(p / k)

            if hour <= h:
                # If she can eat all in 'h' hours or less, try slower speed
                res = min(res, k)
                right = k - 1
            else:
                # Too slow, increase speed
                left = k + 1

        return res

```

---

## 💡 Time and Space Complexity
- **Time**:O(n * log(max(piles)))
    - Binary search log range × O(n) to compute total time for each speed
- **Space**: O(1)
    - No extra space used
