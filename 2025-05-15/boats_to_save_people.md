# 🧲 Problem: Boats to Save People

- **Platform**: [LeetCode](https://leetcode.com/problems/boats-to-save-people/description/)
- **Submission**: [https://leetcode.com/problems/boats-to-save-people/submissions/1634666063/](https://leetcode.com/problems/boats-to-save-people/submissions/1634666063/)
- **Date Solved**: 2025-05-15
- **Tags**: Two Pointers, Greedy, Sorting
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given an array people where people[i] is the weight of the i-th person, and an integer limit which is the maximum weight a boat can carry.Each boat carries at most two people at the same time, provided the sum of their weights is at most limit.
- Return the minimum number of boats required to carry every person.
### 🧾 Examples
```python
Example 1:
Input:people = [1, 2], limit = 3
Output: 1
Explanation: Both people can share one boat.

Example 2:
Input:people = [3, 2, 2, 1], limit = 3
Output: 3
Explanation:
   - One boat: 1 + 2
   - One boat: 2
   - One boat: 3

Example 3:
Input:people = [3, 5, 3, 4], limit = 5
Output: 4
```
---
## 🧠 Intuition
- Pair the heaviest person with the lightest one who can still fit.
- If the lightest can't pair with the heaviest, the heaviest goes alone.
- Greedy approach: always attempt the best pairing to reduce total boats.
## 🚀 Approach : Two Pointers + Greedy
🔸 Steps:
- Sort the people array.
- Use two pointers:
    - l for the lightest person (start)
    - r for the heaviest person (end)
   
- If the lightest + heaviest ≤ limit → use one boat for both.
- If not, the heaviest goes alone.
- Repeat until all people are placed.

---

## 💻 Code (Python)

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people by their weight in non-decreasing order
        people.sort()
        
        res = 0  # This will store the count of boats used
        l, r = 0, len(people) - 1  # Two pointers: l for lightest person, r for heaviest

        # Continue until all people are considered
        while l <= r:
            remain = limit - people[r]  # Try to place the heaviest person on a boat
            r -= 1  # This person is now assigned to a boat
            res += 1  # We've used one more boat

            # Check if the lightest person can also fit in the same boat
            if l <= r and remain >= people[l]:
                l += 1  # If yes, move the left pointer to the next lightest person

        return res  # Return the total number of boats used

```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
    - Due to sorting the people array.
- **Space**: O(1)
    - Only pointers and counters are used.
