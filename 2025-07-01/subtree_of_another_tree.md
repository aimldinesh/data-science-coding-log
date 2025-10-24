# 🧲 Problem: Subtree of Another Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/description/)
- **Submission**: [https://leetcode.com/problems/subtree-of-another-tree/submissions/](https://leetcode.com/problems/subtree-of-another-tree/submissions/)
- **Date Solved**: 2025-07-01
- **Tags**: Tree, Recursion, DFS
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given two binary trees root and subRoot, return True if subRoot is a subtree of root.

- A subtree of a tree T is a tree consisting of a node in T and all of that node’s descendants.
- Both the structure and node values must match exactly.
### 📌 Example
```python
Input:

Tree root:            Tree subRoot:
     3                      4
    / \                    / \
   4   5                  1   2
  / \
 1   2

Output: True

Because the subtree rooted at the left child of 3 matches subRoot.
```
---

## 🚀 Approach
🔍 Intuition
- We are given two binary trees:
   - A main tree root
   - A second tree subRoot

- We need to determine if subRoot is an exact subtree of root.
- This means that there should be a node in root where the structure and values of its subtree exactly match the entire structure and values of subRoot.

- Think of it like scanning the main tree at every node, and checking:"Does the subtree starting at this node look exactly like subRoot?"

## 🧠 Approach

### 🔹 Base Cases:
- If `subRoot` is `None`, it’s always a subtree — an empty tree is considered a subtree of any tree.
- If `root` is `None` but `subRoot` is not, return `False` — we've reached the end of `root` without finding `subRoot`.


### 🔹 Recursive Check:
- For each node in the main tree (`root`), use a helper function `sameTree()` to check if the subtree rooted at that node is **identical** to `subRoot`.


### 🔹 `sameTree` Function Logic:
This function checks whether two trees are **exactly identical** in both structure and node values.

It returns `True` if:
- Both nodes are `None` (i.e., both subtrees are empty at that position), **or**
- Both nodes exist, their values match, and their left and right children match recursively.


### 🔹 Explore Entire Main Tree:
- If the current node does **not** match `subRoot`, recursively check the **left** and **right** subtrees of `root`.


---

## 💻 Code (Python)

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it's always a subtree of any tree
        if not subRoot:
            return True
        # If root is None but subRoot isn't, it can't be a subtree
        if not root:
            return False

        # Check if the current root matches the subRoot using sameTree
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, check recursively in the left and right subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are None, they match
        if not root and not subRoot:
            return True

        # If both nodes exist and values match, recursively check left and right
        if root and subRoot and root.val == subRoot.val:
            return (
                self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right)
            )

        # If nodes don’t match or structure is different, return False
        return False

        
```

---

## 💡 Time and Space Complexity
- **Time**: O(m * n)
    - Let n be the number of nodes in root, m in subRoot
    - For each node in root, you may call sameTree, which takes O(m) time
- **Space**: O(h), due to recursion stack
    - h is height of the tree (O(log n) for balanced, O(n) for skewed)
