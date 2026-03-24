# 🧲 Problem: Baseball Game

- **Platform**: [LeetCode](https://leetcode.com/problems/baseball-game/)
- **Submission**: [https://leetcode.com/submissions/detail/1622630589/](https://leetcode.com/submissions/detail/1622630589/)
- **Date Solved**: 2025-05-01
- **Tags**: Stack, Array, Simulation
- **Difficulty**: Easy

---

## ✅ Problem Statement
You are keeping score for a baseball game with strange rules.

Each operation is a string representing the action:

- Integer (e.g., `"5"`): Record this number as a new score.
- `"+"`: Record a new score that is the sum of the previous two scores.
- `"D"`: Record a new score that is double the previous score.
- `"C"`: Invalidate and remove the previous score.

Return the **sum of all valid scores**.

## 🧪 Example

**Input**: `["5","2","C","D","+"]`  
**Output**: `30`  

**Explanation**:
- "5" → record 5 → `[5]`
- "2" → record 2 → `[5, 2]`
- "C" → remove 2 → `[5]`
- "D" → record 10 (double of 5) → `[5, 10]`
- "+" → record 15 (5 + 10) → `[5, 10, 15]`
- Total sum = 5 + 10 + 15 = `30`


---

## 🚀 Approach
- Use a **stack** to keep track of valid scores.
- Iterate through the list of operations:
  - `"C"` → Remove the last score using `pop()`.
  - `"D"` → Push `2 * last_score`.
  - `"+"` → Push `sum of last two scores`.
  - Otherwise, convert to integer and push to stack.
- Return the sum of the stack at the end.

---

## 💻 Code (Python)

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                # Remove the last valid score
                stack.pop()
            elif op == "D":
                # Double the last score
                stack.append(2 * stack[-1])
            elif op == "+":
                # Sum of the last two scores
                stack.append(stack[-1] + stack[-2])
            else:
                # Convert the number string to integer and add to stack
                stack.append(int(op))

        # Sum all valid scores
        return sum(stack)
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   -  Each operation is processed once.
- **Space**: O(n)
   - Stack stores up to n elements in the worst case.
