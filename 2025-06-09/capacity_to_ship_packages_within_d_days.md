# 🧲 Problem: Capacity To Ship Packages Within D Days

- **Platform**: [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)
- **Submission**: [https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/1658583861/](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/1658583861/)
- **Date Solved**: 2025-06-09
- **Tags**: Binary Search, Greedy, Array
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given a list of weights of packages and an integer days.
- You need to ship all packages within days days. Packages must be shipped in order (i.e., you cannot split or rearrange them), and the ship has a maximum weight capacity per day.
- Return the minimum ship capacity to ship all the packages within the given number of days.
### 🌰 Example
```python

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5  
Output: 15

Explanation:  
A capacity of 15 can ship the weights in 5 days:  
- Day 1: 1 + 2 + 3 + 4 + 5 = 15  
- Day 2: 6 + 7 = 13  
- Day 3: 8  
- Day 4: 9  
- Day 5: 10  

```
---

## 🚀 Approach : Binary Search
💡 Intuition
- The minimum possible capacity is the heaviest package (because we must be able to ship each item).
- The maximum possible capacity is the sum of all weights (if shipped all in one day).
- Use binary search to find the smallest valid capacity such that we can ship within the given days.

🚀 Approach
- Search Range:
    - left = max(weights)
    - right = sum(weights)

- Binary Search:
    - Use a helper function isFeasibleCapacity(cap) that checks if a given capacity can ship the packages within the allowed days.

- Greedy Simulation in the helper:
    - Keep loading packages to current ship.
    - If adding a package exceeds the capacity → start a new ship/day.

- Adjust binary search range:
    - If current capacity is feasible, try smaller (right = mid - 1)
    - If not feasible, try larger (left = mid + 1)
---

## 💻 Code (Python)

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum possible capacity is the heaviest package
        # Maximum possible capacity is the total weight of all packages
        left, right = max(weights), sum(weights)
        res = right  # Start with the maximum as initial result

        # Helper function to check if a given capacity can ship within 'days'
        def isFeasibleCapacity(capacity):
            ships, currentLoad = 1, 0
            for weight in weights:
                # If adding current weight exceeds capacity, need a new ship
                if currentLoad + weight > capacity:
                    ships += 1
                    currentLoad = 0
                currentLoad += weight
            return ships <= days

        # Binary search for the smallest feasible capacity
        while left <= right:
            mid = (left + right) // 2
            if isFeasibleCapacity(mid):
                res = min(res, mid)  # Try smaller capacity
                right = mid - 1
            else:
                left = mid + 1  # Increase capacity

        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n · log(sum(weights) - max(weights)))
    - n = number of weights (packages).
    -  Binary search range is from max(weights) to sum(weights) → range of size ≈ sum(weights).
    - In each binary search step:
         - The helper function isFeasibleCapacity() loops over all n weights → O(n).
    - So total complexity:
         - O(n⋅log(sum(weights)−max(weights)))
- **Space**: O(1)
    - We use only a few variables (left, right, res, etc.).
    - No extra space is used that grows with input size.
