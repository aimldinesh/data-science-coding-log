# 🧲 Problem: Diameter of Binary Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/description/)
- **Submission**: [https://leetcode.com/problems/diameter-of-binary-tree/submissions/1679366698/](https://leetcode.com/problems/diameter-of-binary-tree/submissions/1679366698/)
- **Date Solved**: 2025-06-28
- **Tags**: Tree, DFS
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return the length of the diameter.
    - The diameter of a binary tree is the length of the longest path between any two nodes, which may or may not pass through the root.
    - Length = Number of edges, not nodes.

### 📌 Examples
```python
Input Tree:
      1
     / \
    2   3
   / \     
  4   5    

Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```
---

## 🚀 Approach
💡 Intuition
- To find the longest path (diameter), for every node:
    - The longest path through that node = left subtree height + right subtree height
    - Track the maximum such value as you do DFS traversal
    - Return the height of a node = 1 + max(left, right)

👣 Approach
- Use a helper DFS function to:
    - Recursively calculate left and right subtree heights.
    - At each node, compute: diameter = left + right.
    - Update a global variable (self.res) to keep track of the max diameter found.

- Start DFS from the root.
- Return self.res at the end.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the result variable to store the maximum diameter found
        self.res = 0
        
        # Depth-First Search (DFS) function to compute height and update diameter
        def dfs(curr):
            if not curr:  # Base case: If the node is None, return 0 (height of empty tree)
                return 0

            # Recursively find the height of left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update the maximum diameter found so far
            self.res = max(self.res, left + right)  # Diameter = left height + right height
            
            # Return the height of the current node (1 + max(left height, right height))
            return 1 + max(left, right)

        # Start DFS from the root
        dfs(root)
        
        # Return the maximum diameter found
        return self.res    

        
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each node is visited exactly once.
    - n = total number of nodes in the tree.
- **Space**: O(h)
    -  due to recursion stack, where h is the height of the tree.
    - In the worst case (skewed tree): O(n)
    - In the best/average case (balanced tree): O(log n)
