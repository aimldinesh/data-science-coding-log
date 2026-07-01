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
Example 1:

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


Example 2:

Tree:                Key:3
       5
      / \
     3   6
    / \   \
   2   4   7

Output Tree:

       5
      / \
     4   6
    /     \
   2       7


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
📌 Three Deletion Cases

```
Case 1: No left child  →  return root.right
Case 2: No right child →  return root.left
Case 3: Two children   →  find inorder successor
                          copy its val to root
                          delete successor from right subtree
```
---

### 🔍 Step-by-Step Execution

Input Tree, key = 3:
```
        5
      /   \
     3     6
    / \
   2   4
```
Call 1: deleteNode(5, 3)

```python
key=3 < root.val=5
→ root.left = deleteNode(3, 3)

```
Call 2: deleteNode(3, 3)
```python
key=3 == root.val=3 → found!

Case 3: has both children (left=2, right=4)
  Find inorder successor:
    cur = root.right = 4
    4.left = None → stop
    successor = 4

  root.val = 4   ← copy successor value

        5
      /   \
     4     6      ← node val replaced
    / \
   2   4          ← 4 still exists in right subtree

  root.right = deleteNode(4, 4)  ← delete old successor
```
Call 3: deleteNode(4, 4) (right subtree of node 4)
```python
key=4 == root.val=4 → found!
Case 1: no left child → return root.right = None
```
Back in Call 2:
```python
root.right = None

        5
      /   \
     4     6
    /
   2
return node(4)
```
Back in Call 1:
```python
root.left = node(4)

Final tree:
        5
      /   \
     4     6
    /
   2
return node(5) ✅
```
---
### 💡 All Three Cases Visualised
```python
CASE 1 — No left child:
    [5]              [7]
      \      →
      [7]
  return root.right

CASE 2 — No right child:
    [5]          [3]
    /      →
  [3]
  return root.left

CASE 3 — Two children:
      [5]              [6]
      / \    →         / \
    [3] [7]          [3] [7]
        /
       [6] ← successor
  copy 6→5, delete 6 from right subtree
```
---
### 💡 Why Inorder Successor?
```python
BST property: left < root < right

After deletion, replacement must satisfy:
  > all nodes in left subtree  ← inorder successor is > everything in left ✅
  < all nodes in right subtree ← inorder successor is SMALLEST in right    ✅

Inorder successor = leftmost node of right subtree
  = smallest value greater than root
  = perfect replacement ✅

Could also use inorder PREDECESSOR (largest in left subtree):
  cur = root.left
  while cur.right: cur = cur.right
  (either works, successor is more common)
````
---
### 🔍 All Deletion Scenarios
```python
# Delete leaf node (no children) → case 1 or 2
     [3]                 (None)
  no children   →   parent.child = None

# Delete node with one child
     [3]               [3]
       \       →         \
       [5]               [7]
         \
         [7]

# Delete root with two children
        [5]            [6]
       /   \    →     /   \
     [3]   [7]      [3]   [7]
           /
          [6]
```
---
### 🔄 Recursive Call Flow
```python
deleteNode(root=5, key=3)
  └─ deleteNode(root=3, key=3)   ← found here
       successor = 4
       root.val  = 4
       └─ deleteNode(root=4, key=4)  ← delete successor
            no left → return None
       root.right = None
       return node(4)
  root.left = node(4)
  return node(5)
```
---
### ✅ Final Tree
```python
Before:          After deleting 3:
    5                  5
   / \                / \
  3   6      →       4   6
 / \                /
2   4              2
```

---

## 💡 Time and Space Complexity
- **Time**: O(h)
    - Where h = height of the tree → O(log n) for balanced, O(n) for skewe
- **Space**: O(h)
    - For recursive call stack

---

💡 Interview tip: 

The three cases must be stated clearly before coding — interviewers specifically check that you handle all of them. The most common mistake is forgetting to delete the successor from the right subtree after copying its value — leaving a duplicate node. Always say "copy the value then recursively delete the original successor".
