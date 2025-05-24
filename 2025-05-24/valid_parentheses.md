# 🧲 Problem: Valid Parentheses

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-parentheses/description/)
- **Submission**: [https://leetcode.com/problems/valid-parentheses/submissions/1643011527/](https://leetcode.com/problems/valid-parentheses/submissions/1643011527/)
- **Date Solved**: 2025-05-24
- **Tags**: Stack, String
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- A string is valid if:
     - Open brackets are closed by the same type of brackets.
     - Open brackets are closed in the correct order.
     - Every closing bracket has a corresponding open bracket of the same type.

### 🔍 Examples
```python
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: "({[]})"
Output: True
Explanation:
( → push → ['(']
{ → push → ['(', '{']
[ → push → ['(', '{', '[']
] → matches [ → pop → ['(', '{']
} → matches { → pop → ['(']
) → matches ( → pop → []

Final stack is empty ⇒ ✅ Valid
```
---

## 🚀 Approach : Stack Matching
🧠 Intuition:
- Use a stack to keep track of the last unmatched opening bracket.
- Whenever a closing bracket is encountered, check if it matches the most recent opening bracket on top of the stack.

🔧 Steps:
- Create a dictionary CloseToOpen mapping closing to opening brackets.
- Initialize an empty stack.
- Iterate through each character in s:
     - If it's a closing bracket, check if the stack is not empty and its top matches the corresponding opening bracket.
           - If it matches, pop it.
           - If not, return False.
     - If it's an opening bracket, push it onto the stack.
- At the end, return True only if the stack is empty (all brackets matched).
---

## 💻 Code (Python)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack to keep track of opening brackets
        CloseToOpen = {")": "(", "}": "{", "]": "["}  # Mapping of closing to opening brackets

        for c in s:
            # If the current character is a closing bracket
            if c in CloseToOpen:
                # Check if the top of the stack has the matching opening bracket
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()  # Pop the matched opening bracket
                else:
                    return False  # Either stack is empty or brackets don’t match
            else:
                # It's an opening bracket, push it to the stack
                stack.append(c)

        # If stack is empty, all brackets are matched correctly
        return True if not stack else False
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each character is processed once.
- **Space**: O(n)
    - Stack could grow up to length n in the worst case (e.g., all opening brackets).
