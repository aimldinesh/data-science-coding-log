# 🧲 Problem: Baseball Game

- **Platform**: [LeetCode](https://leetcode.com/problems/baseball-game/)
- **Submission**: [https://leetcode.com/problems/baseball-game/submissions/](https://leetcode.com/problems/baseball-game/submissions/)
- **Date Solved**: 2025-05-23
- **Tags**: Stack, Simulation, list
- **Difficulty**: Easy

---

## ✅ Problem Statement
- You are keeping score for a baseball game with a list of operations that represent the scores of past rounds. The operations are given as a list of strings where each operation is one of the following: 
- An integer x — Record a new score of x.
    - "+" — Record a new score that is the sum of the previous two scores.
    - "D" — Record a new score that is double the previous score.
    - "C" — Invalidate and remove the previous score.
- Return the sum of all valid scores after processing all operations.
### 🔍 Examples
```python
Input: ["5", "-2", "4", "C", "D", "9", "+", "+"]
Output: 27

Explanation:
["5", "-2", "4", "C", "D", "9", "+", "+"]
Step-by-step:
- "5"  → [5]
- "-2" → [5, -2]
- "4"  → [5, -2, 4]
- "C"  → [5, -2]        (remove last score)
- "D"  → [5, -2, -4]    (double of -2)
- "9"  → [5, -2, -4, 9]
- "+"  → [5, -2, -4, 9, 5]   (9 + -4)
- "+"  → [5, -2, -4, 9, 5, 14] (5 + 9)

Final sum = **27**

```
---

## 🚀 Approach : Stack Simulation
🧠 Intuition:
- We use a stack to track all the valid scores. Each operation is handled based on its meaning.

🔧 Steps:
- Initialize an empty stack.
- Iterate over each operation in operations:
    - If "+", push the sum of the last two scores.
    - If "D", push double the last score.
    - If "C", remove the last score.
    - Else, convert the string to an integer and push it.
- Return the sum of all values in the stack.

---

## 💻 Code (Python)

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []  # Stack to keep track of valid scores

        for op in operations:
            if op == "+":
                # "+" means the current score is the sum of the last two valid scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # "D" means the current score is double the last valid score
                stack.append(2 * stack[-1])
            elif op == "C":
                # "C" means the last valid score is invalid and should be removed
                stack.pop()
            else:
                # Otherwise, it's an integer score (as a string), convert and add to stack
                stack.append(int(op))

        # Return the total sum of valid scores
        return sum(stack)
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - where n is the number of operations
- **Space**: O(n)
    - for the stack that stores valid scores
