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

🧠 Intuition
Every closing bracket must match the most recently opened unmatched bracket — classic Last In First Out → use a stack. Push opening brackets, and when a closing bracket arrives, check if the top of the stack is its matching pair. If at any point it doesn't match, or stack is empty when expecting a match → invalid.
```python
s = "({[]})"

Push (  → stack=[(]
Push {  → stack=[(, {]
Push [  → stack=[(, {, []
] arrives → matches [ on top → pop → stack=[(, {]
} arrives → matches { on top → pop → stack=[(]
) arrives → matches ( on top → pop → stack=[]
Empty stack → True ✅
```
📌 Approach

1. stack=[], CloseToOpen = {")":"(", "}":"{", "]":"["}
2. For each character c:
   - If closing bracket → check stack[-1] == CloseToOpen[c]
     - Match → stack.pop()
     - No match or empty → return False

   - If opening bracket → stack.append(c)

3. Return True if stack empty, else False
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
