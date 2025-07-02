# 🧲 Problem: Delete Node in a BST

- **Platform**: [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/description/)
- **Submission**: [https://leetcode.com/problems/delete-node-in-a-bst/submissions/1683952246/](https://leetcode.com/problems/delete-node-in-a-bst/submissions/1683952246/)
- **Date Solved**: 2025-07-02
- **Tags**: Binary Tree, Recusion, Tree
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given the root of a Binary Search Tree (BST) and an integer key, delete the node with value key and return the updated root of the tree.
### 📌 Example
```python
Input Tree:

    Tree:        key = 3
       5
      / \
     3   6
    /
   2

Output Tree :

       5
      / \
     2   6


```
---

## 🚀 Approach
💡 Intuition
- A node in a BST can be deleted in three possible scenarios:
   - Leaf Node (no children) → Just remove it.
   - One child (left or right) → Replace node with its child.
   - Two children → Replace the node with its in-order successor (smallest value in right subtree), and delete the successor node recursively.

👣 Approach
- Traverse the BST like normal using:
   - key < root.val → go left
   - key > root.val → go right
   - key == root.val → found the node to delete

- Deletion logic:
   - If the node has no left child → return root.right
   - If the node has no right child → return root.left
   - If the node has two children:
      - Find in-order successor (leftmost node in root.right)
      - Copy its value to root
      - Recursively delete the successor from the right subtree

- Return the updated root


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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: if the tree is empty, nothing to delete
        if not root:
            return root

        # If key is greater than root value, search in the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key is less than root value, search in the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Found the node to be deleted
        else:
            # Case 1: Node has no left child, replace node with right child
            if not root.left:
                return root.right

            # Case 2: Node has no right child, replace node with left child
            elif not root.right:
                return root.left

            # Case 3: Node has two children
            # Find the in-order successor (smallest in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left  # Go to the leftmost node in right subtree

            # Replace the value of current node with successor's value
            root.val = cur.val

            # Delete the in-order successor node from the right subtree
            root.right = self.deleteNode(root.right, root.val)

        # Return the updated root after deletion
        return root
   
```

---

## 💡 Time and Space Complexity
- **Time**: O(h)
    - Where h = height of the tree → O(log n) for balanced, O(n) for skewe
- **Space**: O(h)
    - For recursive call stack
