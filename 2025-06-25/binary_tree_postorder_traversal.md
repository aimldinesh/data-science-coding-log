# 🧲 Problem: Binary Tree Postorder Traversal

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
- **Submission**: [https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1676065788/](https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1676065788/)
- **Date Solved**: 2025-06-25
- **Tags**: Tree, Iterative, Recursive
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return the postorder traversal of its nodes' values.

- Postorder Traversal Order:
  
    - Left → Right → Node

## 📌 Example
```python
Input:
    1
     \
      2
     /
    3

output:
[3, 2, 1]
```

---

## 🚀 Approach
💡 Intuition
- In postorder traversal, we visit:
   - Left child
   - Then right child
   - Then the node itself

To simulate recursion iteratively, we use:
   - A stack to control the traversal flow
   - A visit flag to know whether a node is being visited for the first time (so we can push children) or the second time (so we can process it)


👣 Approach
- Initialize stack = [root] and visit = [False]
- While stack is not empty:
     - Pop a node and its visit flag
     - If node is None, skip
     - If visited flag is True, append its value to the result
     - If visited flag is False:
          - Push the node back with visited=True (to process it after its children)
          - Push its right child with visited=False
          - Push its left child with visited=False

- Return the res list containing the postorder traversal.

---

## 💻 Code (Python)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Stack to store nodes to be processed
        stack = [root]
        # Stack to track whether the node has been visited before
        visit = [False]
        # Result list to store postorder traversal
        res = []

        while stack:
            # Pop the current node and its visited flag
            cur, v = stack.pop(), visit.pop()

            if cur:
                if v:
                    # If the node was already visited, add its value to the result
                    res.append(cur.val)
                else:
                    # Postorder: Left → Right → Node
                    # Push the current node again, marked as visited
                    stack.append(cur)
                    visit.append(True)

                    # Push right child (to be visited later)
                    stack.append(cur.right)
                    visit.append(False)

                    # Push left child (to be visited before right)
                    stack.append(cur.left)
                    visit.append(False)

        return res

```
---
### 🔍 Step-by-step Execution with example
```python
Input:
    1
     \
      2
     /
    3

✅ Goal:
Postorder = [3, 2, 1]
(Left → Right → Node)

🧰 Variables:
stack: holds nodes to process
visit: parallel list indicating whether a node has been visited before
res: result list

| Step | Action                                                            | `stack` (top right)           | `visit`                                   | `res`       |
| ---- | ----------------------------------------------------------------- | ----------------------------- | ----------------------------------------- | ----------- |
| 0    | Init                                                              | `[1]`                         | `[False]`                                 | `[]`        |
| 1    | Pop 1 (not visited) → Push back `1 (T)`, push `2 (F)`, `None (F)` | `[1, 2, None]`                | `[True, False, False]`                    | `[]`        |
| 2    | Pop `None`                                                        | `[1, 2]`                      | `[True, False]`                           | `[]`        |
| 3    | Pop 2 (not visited) → Push back `2 (T)`, `None (F)`, `3 (F)`      | `[1, 2, None, 3]`             | `[True, True, False, False]`              | `[]`        |
| 4    | Pop 3 (not visited) → Push back `3 (T)`, `None (F)`, `None (F)`   | `[1, 2, None, 3, None, None]` | `[True, True, False, True, False, False]` | `[]`        |
| 5    | Pop `None`                                                        | `[1, 2, None, 3, None]`       | `[True, True, False, True, False]`        | `[]`        |
| 6    | Pop `None`                                                        | `[1, 2, None, 3]`             | `[True, True, False, True]`               | `[]`        |
| 7    | Pop 3 (visited) → append 3                                        | `[1, 2, None]`                | `[True, True, False]`                     | `[3]`       |
| 8    | Pop `None`                                                        | `[1, 2]`                      | `[True, True]`                            | `[3]`       |
| 9    | Pop 2 (visited) → append 2                                        | `[1]`                         | `[True]`                                  | `[3, 2]`    |
| 10   | Pop 1 (visited) → append 1                                        | `[]`                          | `[]`                                      | `[3, 2, 1]` |

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - each node is visited once
- **Space**: O(n)
    - stack may store up to all nodes in worst case (skewed tree)

---
