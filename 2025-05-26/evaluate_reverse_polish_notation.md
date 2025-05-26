# 🧲 Problem: Evaluate Reverse Polish Notation

- **Platform**: [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
- **Submission**: [https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1644991902/](https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1644991902/)
- **Date Solved**: 2025-05-26
- **Tags**: Stack, Math, Array, String
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation.
- Evaluate the expression and return the result as an integer.
- Note:
    - Valid operators are +, -, *, and /.
    - Each operand may be an integer or another expression.
    - Division between two integers should truncate toward zero.

### 🔍 Examples
```python
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```
---

## 🚀 Approach : Stack
🧠 Intuition:
- In Reverse Polish Notation (postfix), we evaluate expressions using a stack:
    - Push numbers to the stack.
    - When an operator appears, pop two numbers, apply the operator, and push the result back.

🔧 Steps:
- Initialize an empty stack.
- Loop through each token:
    - If it’s a number → Push to stack.
    - If it’s an operator:
         - Pop two elements.
         - Apply operation (b op a where a is the last popped).
         - Push the result.
- Return the last element in the stack (final result).

---

## 💻 Code (Python)

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to store numbers and intermediate results.
        stack = []

        # Iterate through each token in the input list.
        for c in tokens:
            # If the token is '+', pop two elements, add them, and push the result back.
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            # If the token is '-', pop two elements and subtract the first popped from the second.
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            # If the token is '*', pop two elements, multiply them, and push the result back.
            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            # If the token is '/', pop two elements and divide the second popped by the first.
            # The result is converted to int to truncate toward zero.
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            # If the token is a number, convert it to int and push it onto the stack.
            else:
                stack.append(int(c))

        # After processing all tokens, the result will be the only element left in the stack.
        return stack[0]
```
---
```python
🔁 Example:

Input: ["2", "1", "+", "3", "*"]

Explanation:
- Push 2 → stack = [2]
- Push 1 → stack = [2, 1]
- "+" → Pop 1 and 2 → 2 + 1 = 3 → push 3 → stack = [3]
- Push 3 → stack = [3, 3]
- "*" → Pop 3 and 3 → 3 * 3 = 9 → push 9 → stack = [9]
- Output: 9
```
---
## 💡 Time and Space Complexity
- **Time**: O(n)
    - Explanation:
         - We iterate over each token once, performing constant time operations (push, pop, arithmetic).
         - Each operator or number takes O(1) time.
         - n = number of tokens in the input list.
    ✅ Total Time = O(n)
- **Space**: O(n)
    - Explanation:
         - We use a stack to store numbers during evaluation.
         - In the worst case (all tokens are numbers), the stack could hold n elements.
    ✅ Total Space = O(n)
