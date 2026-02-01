# 🧲 Problem: Lowest Common Ancestor of a Binary Search Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
- **Submission**: [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1685107135/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1685107135/)
- **Date Solved**: 2025-07-03
- **Tags**: Tree, Binary Search Tree, DFS, LCA
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given the root of a Binary Search Tree and two nodes p and q, find their Lowest Common Ancestor (LCA).
- The Lowest Common Ancestor is the lowest node in the tree that has both p and q as descendants (a node can be a descendant of itself).

### 📌 Example
```python
BST:
       6
      / \
     2   8
    / \ / \
   0  4 7 9
     / \
    3   5

Input:
p = 2, q = 8

Output: 6
Because 6 is the lowest node that has both 2 and 8 in its subtree.
```
---

## 🚀 Approach
💡 Intuition
- Use the BST properties:
   - Left child < parent < right child

- Start from the root:
   - If both p and q are less than current → move left
   - If both are greater → move right
   - If one is on each side (or equal to current) → current is LCA

👣 Approach
- Initialize a pointer cur = root
- Loop while cur is not None:
   - If p.val and q.val are both greater than cur.val → move right
   - If both are smaller → move left
   - Else → found the LCA (split point)

- Return cur
---

## 💻 Code (Python)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start from the root node of the BST
        cur = root

        # Traverse the tree until the LCA is found
        while cur:
            # If both p and q are greater than current node,
            # the LCA must be in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # If both p and q are less than current node,
            # the LCA must be in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # If the current node is between p and q (or equal to one),
            # then this is the Lowest Common Ancestor
            else:
                return cur
     
        
```

---

## 💡 Time and Space Complexity
- **Time**: O(h)
    - h is the height of the tree
    - (O(log n) for balanced BST, O(n) for skewed)
- **Space**: O(1)
    - Iterative (no recursion)
