# 🧲 Problem: Binary Tree Preorder Traversal

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- **Submission**: [https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1674867044/](https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1674867044/)
- **Date Solved**: 2025-06-24
- **Tags**: Tree, Iterative, Recursion
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return the preorder traversal of its nodes’ values.
- Preorder Traversal Order:
     - Node → Left → Right

### 📌 Example
```python
Input:
    1
     \
      2
     /
    3

Output:
[1, 2, 3]

```
---

## 🚀 Approach
💡 Intuition
- In preorder traversal, we visit the root node first, then recursively visit the left subtree, followed by the right subtree.
- The iterative approach simulates the recursive stack using an explicit stack.
- Instead of recursion, we manually:
    - Process the current node
    - Push the right child (to visit later)
    - Move left (deeper into the tree)

👣 Approach
- Use a stack to manage right children for later backtracking.
- Start from the root as cur.
- While either cur is not None or stack is not empty:
     - Visit current node: res.append(cur.val)
     - Push cur.right onto the stack
     - Move to cur.left
- If cur becomes None, pop from the stack (i.e., go to previously saved right child).
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the current pointer and a stack to help traverse the tree
        cur, stack = root, []
        res = []  # Result list to store the preorder traversal

        # Loop until all nodes are visited (stack is empty and cur is None)
        while cur or stack:
            if cur:
                # Visit the current node (Preorder: Node → Left → Right)
                res.append(cur.val)

                # Store the right child to visit it later
                stack.append(cur.right)

                # Move to the left child next
                cur = cur.left
            else:
                # If current is None, pop a node from the stack to backtrack
                cur = stack.pop()

        return res
         
```
---
### Step by step Execution with example
```
Input:
    1
     \
      2
     /
    3

Output:
[1, 2, 3]
---------------------------------------------
Steps:

Initial:
  cur = 1
  stack = []
  res = []

Iteration 1:
  Visit 1 → res = [1]
  Push 2 → stack = [2]
  Move to left (None)

Iteration 2:
  cur = None → pop 2 → cur = 2
  Visit 2 → res = [1, 2]
  Push None (2.right) → stack = [None]
  Move to 2.left → cur = 3

Iteration 3:
  Visit 3 → res = [1, 2, 3]
  Push None → stack = [None, None]
  Move left → cur = None

Remaining:
 Stack has None entries → pop → cur = None → loop ends

Final result: [1, 2, 3]


```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each node is visited exactly once.
- **Space**: O(h), Where h is the height of the tree (stack stores right nodes).
    - Worst case (skewed tree): O(n)
    - Best case (balanced tree): O(log n)

---
