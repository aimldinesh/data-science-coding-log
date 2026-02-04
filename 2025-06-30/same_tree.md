# 🧲 Problem: Same Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/same-tree/description/)
- **Submission**: [https://leetcode.com/problems/same-tree/submissions/1681476181/](https://leetcode.com/problems/same-tree/submissions/1681476181/)
- **Date Solved**: 2025-06-30
- **Tags**: Tree, BFS, DFS, Interative, Recursive
- **Difficulty**: Easy

---

## ✅ Problem Statement
Given the roots of two binary trees p and q, return True if they are structurally identical and node values are the same at every position.
### 📌 Example
```python
Input:

Tree p:           Tree q:
    1                 1
   / \               / \
  2   3             2   3

Output: True

Input: 

Tree p:           Tree q:
    1                 1
   /                   \
  2                     2

Output: False
```
---

## 🚀 Approach
💡 Intuition
- We want to compare both trees node-by-node:
   - If both nodes are None, return True
   - If both are not None and values match:
- Recursively check left and right subtrees
   - Else return False

👣 Approach
- Base case:
   - If p and q are both None → return True
- If both nodes exist and values match:
   - Recurse on left children: isSameTree(p.left, q.left)
   - Recurse on right children: isSameTree(p.right, q.right)
- If values differ or one node is None, return False
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, we've reached the end of both trees at the same position
        if not p and not q:
            return True

        # If both nodes are present and have the same value, 
        # recursively check their left and right children
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left) and  # Check left subtrees
                self.isSameTree(p.right, q.right)    # Check right subtrees
            )
        
        # If one is None and the other isn't, or values don't match, trees aren't the same
        else:
            return False
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    -  Each node is visited once
- **Space**: O(h)
    - Recursion stack (h = height of tree)

---
