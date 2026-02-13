# 🧲 Problem: Binary Tree Inorder Traversal

- **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
- **Submission**: [https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1669447673/](https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1669447673/)
- **Date Solved**: 2025-06-19
- **Tags**: Binary Tree, Recursion
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return its inorder traversal as a list of node values.

- Inorder traversal:
    - Left → Node → Right

### 📌 Examples:

```python
     1
      \
       2
      /
     3

- Inorder Traversal Output: [1, 3, 2]

```

---

## 🚀 Approach
💡 Intuition:
- In recursion, the call stack handles node processing order. In the iterative version, we simulate this using an explicit stack to manage traversal manually.

👣 Approach:
- Initialize:
    - res to store the final output
    - stack to simulate recursion
    - cur pointer to the root node

- While cur is not null or stack is not empty:
    - Go as far left as possible, pushing each node onto the stack.
    - Once you reach a null left, backtrack by popping from the stack.
    - Add the node’s value to res.
    - Move to the right child.

- Repeat until all nodes are processed.
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # List to store the result of inorder traversal
        res = []
        
        # Stack to simulate the recursion stack
        stack = []
        
        # Pointer to track the current node starting from the root
        cur = root
        
        # Traverse the tree
        while cur or stack:
            # Reach the leftmost node of the current subtree
            while cur:
                stack.append(cur)  # Push current node to stack
                cur = cur.left     # Move to left child
            
            # Current must be None at this point
            cur = stack.pop()      # Node with no left child
            res.append(cur.val)    # Visit the node (inorder step)
            
            cur = cur.right        # Visit the right subtree
        
        return res  # Return the final inorder traversal list

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Every node is visited exactly once.
- **Space**:
    - Worst case: O(n) — when the tree is completely unbalanced (like a linked list).
    - Best case: O(log n) — for a balanced binary tree (due to stack height).

---
