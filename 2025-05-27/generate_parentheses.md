# 🧲 Problem: Generate Parentheses

- **Platform**: [LeetCode](https://leetcode.com/problems/generate-parentheses/description/)
- **Submission**: [https://leetcode.com/problems/generate-parentheses/submissions/1646054484/](https://leetcode.com/problems/generate-parentheses/submissions/1646054484/)
- **Date Solved**: 2025-05-27
- **Tags**: Backtracking, String, Recursion
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### 🔍 Examples
```python
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```
---

## 🚀 Approach : Backtracking
🧠 Intuition:
- This is a classic backtracking problem. We generate the parentheses step-by-step, and only add ( or ) if it's valid to do so:
   - Only add ( if we haven't used all n open brackets yet.
   - Only add ) if it won’t exceed the number of ( used.

🔧 Steps:
- Use a stack to track the current string (combination being built).
- Use a recursive function to backtrack:
   - Add ( if open count < n.
   - Add ) if close count < open count.
   - If both counts reach n, add current combination to result.
- Pop from the stack after each recursive call (backtracking).
---

## 💻 Code (Python)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Stack to build the current combination of parentheses
        stack = []
        # Result list to store all valid combinations
        res = []

        # Backtracking function to generate all combinations
        def backtrack(openN, closedN):
            # Base case: if the number of open and closed parentheses both reach n
            # we have formed a valid combination
            if openN == closedN == n:
                res.append("".join(stack))  # Add the combination to the result
                return

            # If we can still add an open parenthesis
            if openN < n:
                stack.append("(")  # Add '(' to the stack
                backtrack(openN + 1, closedN)  # Recurse with one more open parenthesis
                stack.pop()  # Backtrack: remove the last parenthesis added

            # If we can add a closing parenthesis (must not exceed the number of open)
            if closedN < openN:
                stack.append(")")  # Add ')' to the stack
                backtrack(openN, closedN + 1)  # Recurse with one more closed parenthesis
                stack.pop()  # Backtrack: remove the last parenthesis added

        # Initial call to backtracking function with 0 open and closed parentheses
        backtrack(0, 0)
        
        # Return the list of all valid parentheses combinations
        return res
```

---

## 🧠 Time and Space Complexity

### ⏱ Time Complexity: `O(4ⁿ / √n)`

- The number of valid combinations of parentheses is given by the **n-th Catalan number**:
  
  \[
  C_n = \frac{1}{n + 1} \binom{2n}{n} \approx \frac{4^n}{n^{3/2}}
  \]

- This means that in the worst case, the backtracking algorithm explores approximately `O(4ⁿ / √n)` valid combinations.

✅ **Total Time Complexity:** `O(4ⁿ / √n)`

---

### 🧮 Space Complexity:

- **Stack Space (Recursive Depth):**  
  - At most `2n` characters are stored on the stack at a time → `O(n)`

- **Result Storage (`res`):**  
  - Up to `Catalan(n)` valid combinations are generated → `O(4ⁿ / √n)`
  - Each combination is a string of length `2n` → `O(n)` per combination

✅ **Total Space Complexity:** `O((4ⁿ / √n) × n)`
---