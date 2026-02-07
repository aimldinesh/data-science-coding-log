# 🧲 Problem: Invert Binary Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/invert-binary-tree/description/)
- **Submission**: [https://leetcode.com/problems/invert-binary-tree/submissions/1677231073/](https://leetcode.com/problems/invert-binary-tree/submissions/1677231073/)
- **Date Solved**: 2025-06-26
- **Tags**: Tree, Iterative, Recursive, DFS, BFS
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, invert the tree, and return its root.
- Inversion means swapping the left and right subtrees at every node.

### 📌 Example
```python
Input:

     4
    / \
   2   7
  / \ / \
 1  3 6  9

Output (Inverted):
     4
    / \
   7   2
  / \ / \
 9  6 3  1

```
---

## 🚀 Approach 1 : Recursive
💡 Intuition
- You can solve this by recursively swapping the left and right children of every node.
- Each recursive call:
     - Swaps the children
     - Inverts the left and right subtrees
       

👣 Approach
- Base case: If the node is None, return None.
- Swap the left and right children.
- Recursively invert the left subtree (root.left)
- Recursively invert the right subtree (root.right)
- Return the root

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is None, return None
        if not root:
            return None

        # Swap the left and right subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root after inverting its children
        return root
```
---
### 🔍 Step-by-step Execution with example
```python
     1
    / \
   2   3

Step 1:
- At node 1 → swap 2 and 3
- Tree becomes:
   1
  / \
 3   2

Step 2:
- Recur on node 3 → it's a leaf → no change

Step 3:
- Recur on node 2 → it's a leaf → no change

Done!
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Every node is visited once.
- **Space**: O(h)-Due to recursion stack.
    - O(log n) for balanced tree
    - O(n) for skewed tree
---
## 🚀 Approach 2 : Iterative
💡 Intuition
- Instead of using recursion, you can simulate DFS with a stack.
- For each node:
    - Swap its left and right child.
    - Push its children into the stack to process them next.

👣 Approach
- Edge Case: If the root is None, return None.
- Initialize a stack with the root node.
- While the stack is not empty:
    - Pop a node.
    - Swap its left and right children.
    - Push left and right into the stack if they exist.

- Return the root once all nodes are processed.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Use a stack to implement iterative DFS
        stack = [root]

        while stack:
            # Pop the top node
            node = stack.pop()

            # Swap its left and right children
            node.left, node.right = node.right, node.left

            # Push left and right children to the stack (if they exist)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Return the root of the inverted tree
        return root
```
---
### 🔍 Step-by-step Execution example
```python
Input Tree:
    1
   / \
  2   3

Stack: [1]

Step 1:
- Pop 1
- Swap → 3 becomes left, 2 becomes right
- Push 3 and 2
  - (stack = [3, 2])

Step 2:
- Pop 2 → leaf → no children to push

Step 3:
- Pop 3 → leaf → no children to push

Final Tree:
    1
   / \
  3   2

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - All n nodes are visited once.
- **Space**: O(h), Stack size depends on tree height.
    - O(log n) for balanced
    - O(n) for skewed

---
