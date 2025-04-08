# 🧮 Problem: Two Sum

- **Platform**: [Leetcode](https://leetcode.com/problems/two-sum/)
- **Submission**: [https://leetcode.com/submissions/detail/1600134420/](https://leetcode.com/submissions/detail/1600134420/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA

---

## ✅ Problem Statement
*Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.*

---

## 🚀 My Approach
- I used a **hashmap (dictionary)** to store visited numbers and their indices.
- For each number `x`, I check if `target - x` exists in the dictionary.

---

## 💻 Code (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map(one Pass)
        indices = {}  # Dictionary to store value -> index
        
        for i, n in enumerate(nums):
            diff = target - n  # Complement we are looking for
            if diff in indices:
                return [indices[diff], i]  # Return indices of both numbers
            indices[n] = i  # Store current number's index
        
        return []  # Return empty list if no solution is found

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(n)
