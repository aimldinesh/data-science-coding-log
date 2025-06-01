# 🧲 Problem: Simplify Path

- **Platform**: [LeetCode](https://leetcode.com/problems/simplify-path/description/)
- **Submission**: [https://leetcode.com/problems/simplify-path/submissions/1650723801/](https://leetcode.com/problems/simplify-path/submissions/1650723801/)
- **Date Solved**: 2025-06-01
- **Tags**: Stack, String, Simulation, Path Simplification
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given a string path, which is an absolute Unix-style file path, simplify it. Return the simplified canonical path.
- Canonical Path Rules:
     - Starts with a single /.
     - No trailing / at the end unless it’s root (/).
     - . means current directory → ignore.
     - .. means go back to the previous directory.
     - Multiple slashes // are treated as a single slash /.

### 🌰 Example:
```python
Input: 

path = "/a/./b/../../c/"

Output: "/c"

Explanation:
- /a → go into a
- /./ → stay in a
- /b/ → go into b
- /../ → back to a
- /../ → back to /
- /c/ → go into c
So final path = "/c"
```
---

## 🚀 Approach
💡 Intuition:
- We can simulate navigating the path using a stack:
     - If we see a directory name, we push it.
     - If we see .., we pop from the stack (go back).
     - If we see . or an empty string (due to multiple /), we ignore it.

🧠 Approach:
- Initialize an empty stack and a string cur to build each path segment.
- Add a trailing / to make sure the last folder is processed.
- Traverse each character:
     - If character is /, process the current cur segment:
          - If cur == ".." → go back (pop from stack)
          - If cur != "" and cur != "." → push to stack
          - Reset cur
     - Else, keep building the segment name
- Finally, join all elements in the stack with '/'.
---

## 💻 Code (Python)

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Stack to keep valid directory names
        cur = ""    # To build the current part between '/'

        # Add a trailing '/' to ensure the last part is processed
        for c in path + "/":
            if c == "/":
                # Process current segment
                if cur == "..":
                    if stack: 
                        stack.pop()  # Go back to parent directory
                elif cur != "" and cur != ".":
                    stack.append(cur)  # Add valid directory name
                cur = ""  # Reset for next segment
            else:
                cur += c  # Build directory name

        return "/" + "/".join(stack)  # Construct the simplified path
                  
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Traverse each character once → O(n)
- **Space**: O(n)
    -  Stack holds at most n components in worst case
