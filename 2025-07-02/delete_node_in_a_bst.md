# 🧲 Problem: Delete Node in a BST

- **Platform**: [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/description/)
- **Submission**: [https://leetcode.com/problems/delete-node-in-a-bst/submissions/1683952246/](https://leetcode.com/problems/delete-node-in-a-bst/submissions/1683952246/)
- **Date Solved**: 2025-07-02
- **Tags**: DSA, Binary Tree, Recusion, Tree
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

To delete a node in a BST, we first need to locate it using the BST property (left children are smaller, right children are larger). Once found, we handle three cases: if the node has no left child, replace it with its right child; if no right child, replace with the left child. The tricky case is when the node has both children. We find the in-order successor (the smallest node in the right subtree), copy its value to the current node, and then delete that successor node. This approach swaps values rather than restructuring pointers.

👣 Algorithm

1. If the root is null, return null.
2. If the key is greater than the root's value, recursively delete from the right subtree.
3. If the key is less than the root's value, recursively delete from the left subtree.
4. If the key matches the root's value:
   + If there is no left child, return the right child.
   + If there is no right child, return the left child.
   + Otherwise, find the in-order successor (leftmost node in the right subtree), copy its value to the current node, and recursively delete the successor.

5. Return the root.


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
