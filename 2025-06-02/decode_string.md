# 🧲 Problem: Decode String

- **Platform**: [LeetCode](https://leetcode.com/problems/decode-string/description/)
- **Submission**: [https://leetcode.com/problems/decode-string/submissions/1651672843/](https://leetcode.com/problems/decode-string/submissions/1651672843/)
- **Date Solved**: 2025-06-02
- **Tags**: Stack, String, Recursion
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an encoded string, return its decoded version.
- The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
- Note that k is a positive integer and can be more than one digit.

### 🌰 Example:
```python
Input: s = "3[a]2[bc]"

Output:"aaabcbc"

Explanation:
- "3[a]" becomes "aaa"
- "2[bc]" becomes "bcbc"
- Final output = "aaabcbc"

```

---

## 🚀 Approach
💡 Intuition:
- We use a stack to decode the string.
- Why? Because the encoding is nested, and stacks help in handling such LIFO (Last-In, First-Out) operations.
- Every time we encounter a ], we:
     - Pop characters till we get [, build the substring.
     - Then pop digits before [ to get the repetition count.
     - Multiply the substring and push it back to the stack.

- At the end, we join everything in the stack to get the decoded string.

🧠 Approach:
- Initialize an empty stack.
- Traverse the string character by character:
     - If character is not ], push it to stack.
     - If character is ], start decoding:
            - Pop from stack until [ is found → this is the substring.
            - Then pop digits before [ → this is the multiplier k.
            -Push k * substring back to stack.

- Finally, return "".join(stack).
---

## 💻 Code (Python)

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to store characters and repeated segments
        
        for i in range(len(s)):
            if s[i] != "]":
                # Push all characters except closing bracket
                stack.append(s[i])
            else:
                # Build substring inside brackets
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()  # Remove "["

                # Build the multiplier number k (can be >1 digit)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # Push repeated substring back to stack
                stack.append(int(k) * substr)

        return "".join(stack)  # Final decoded string

```
---

### Step-by-Step Execution of "3[a2[c]]"
```python
Input: s = "3[a2[c]]"

Initial Setup:
- Stack: []
- We will iterate over each character in s.

1. Char = '3'  
   Not ']', so push to stack  
   Stack → ['3']

2. Char = '['  
   Push to stack  
   Stack → ['3', '[']

3. Char = 'a'  
   Push to stack  
   Stack → ['3', '[', 'a']

4. Char = '2'  
   Push to stack  
   Stack → ['3', '[', 'a', '2']

5. Char = '['  
   Push to stack  
   Stack → ['3', '[', 'a', '2', '[']

6. Char = 'c'  
   Push to stack  
   Stack → ['3', '[', 'a', '2', '[', 'c']

7. Char = ']'  
   This triggers decoding:  
   - Pop 'c' → substr = `'c'`  
   - Pop `'['`  
   - Pop `'2'` → k = `'2'`  
   - Decode: `'c' * 2 = 'cc'`  
   - Push `'cc'` back →  
   Stack → ['3', '[', 'a', 'cc']

8. Char = ']'  
   Triggers another decoding:  
   - Pop `'cc'`, `'a'` → substr = `'acc'`  
   - Pop `'['`  
   - Pop `'3'` → k = `'3'`  
   - Decode: `'acc' * 3 = 'accaccacc'`  
   - Push result →  
   Stack → ['accaccacc']

✅ Final Output: "accaccacc"

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each character is pushed/popped from the stack at most once.
- **Space**: O(n)
    -  The stack stores up to O(n) characters in worst case.
