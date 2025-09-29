# 🧲 Problem: Count of Matches in Tournament

- **Platform**: [LeetCode](https://leetcode.com/problems/count-of-matches-in-tournament/description/)
- **Submission**: [https://leetcode.com/problems/count-of-matches-in-tournament/submissions/1786200562/](https://leetcode.com/problems/count-of-matches-in-tournament/submissions/1786200562/)
- **Date Solved**: 2025-09-29
- **Tags**: DSA, Math
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are given an integer `n`, the number of teams in a tournament.  
Teams are paired up in each round:  
- If the number of teams is **even**, every team plays and `n/2` matches are held.  
- If the number of teams is **odd**, one team advances automatically, and `(n-1)/2` matches are held.  

Return the **total number of matches played** until there is exactly one winner.

---

## 🔹 Examples

**Example 1:**  
Input: `n = 7`  
Output: `6`  
Explanation:  
- Round 1: 3 matches + 1 team advances → 4 teams remain  
- Round 2: 2 matches → 2 teams remain  
- Round 3: 1 match → 1 winner  
Total = 6 matches  

**Example 2:**  
Input: `n = 14`  
Output: `13`

---

## 🔹 Approach:

We simulate the rounds:
1. While more than 1 team remains:  
   - Add `n // 2` matches to result.  
   - Update `n = ceil(n/2)` for the next round.  
2. Continue until only 1 team remains.  

**Mathematical Insight:**  
The total matches will always be `n - 1`.  
Why?  
- Each match eliminates exactly 1 team.  
- To reduce `n` teams to 1 winner, we must eliminate `n - 1` teams.  

So the simulation works, but we can simplify to a **one-liner**.

---

## 🔹 Code (Simulation)

```python
import math

class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2              # matches in this round
            n = math.ceil(n / 2)       # teams advancing to next round
        return res
```
---

## 🔹 Optimized Code (Mathematical Shortcut)
```python
class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Always n - 1 matches in total
        return n - 1

```
---

🔹 Time & Space Complexity

- Simulation:
   - Time Complexity: O(log n) (halving teams each round).
   - Space Complexity: O(1)

- Optimized formula:
   - Time Complexity: O(1)
   - Space Complexity: O(1)
