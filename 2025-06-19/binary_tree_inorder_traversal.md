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

🧠 Intuition

Inorder traversal visits nodes in Left → Root → Right order. The iterative approach simulates the call stack manually — dive as far left as possible pushing nodes, then pop and visit, then explore the right subtree. For a BST this produces a sorted sequence.
```
        4
      /   \
     2     6
    / \   / \
   1   3 5   7

Inorder → [1, 2, 3, 4, 5, 6, 7] ✅ (sorted!)
```
📌 Approach

1. cur = root, stack = [], res = []
2. While cur or stack not empty:
   - Dive left — push all left nodes onto stack
   - Pop — visit node, add to res
   - Go right — set cur = cur.right

3. Return res
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
### 🔍 Step-by-Step Execution
```
Input Tree:
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```
Initial: cur=4, stack=[], res=[]

Dive left from 4:
```
cur=4 → push 4, move left
cur=2 → push 2, move left
cur=1 → push 1, move left
cur=None → stop diving

stack=[4, 2, 1]
```

Pop 1:
```
cur = stack.pop() = 1
res = [1]
cur = 1.right = None
```
Pop 2:
```
cur=None → skip dive
cur = stack.pop() = 2
res = [1, 2]
cur = 2.right = 3
```
Dive left from 3:
```
cur=3 → push 3, move left
cur=None → stop diving

stack=[4, 3]
```
Pop 3:
```
cur = stack.pop() = 3
res = [1, 2, 3]
cur = 3.right = None
```
Pop 4:
```
cur=None → skip dive
cur = stack.pop() = 4
res = [1, 2, 3, 4]
cur = 4.right = 6
```
Dive left from 6:
```
cur=6 → push 6, move left
cur=5 → push 5, move left
cur=None → stop diving

stack=[6, 5]
```
Pop 5:
```
cur = stack.pop() = 5
res = [1, 2, 3, 4, 5]
cur = 5.right = None
```
Pop 6:
```
cur=None → skip dive
cur = stack.pop() = 6
res = [1, 2, 3, 4, 5, 6]
cur = 6.right = 7
```
Dive left from 7:
```
cur=7 → push 7, move left
cur=None → stop

stack=[7]
```
Pop 7:
```
cur = stack.pop() = 7
res = [1, 2, 3, 4, 5, 6, 7]
cur = 7.right = None
```
Loop ends: cur=None, stack=[]

---
### 💡 Traversal Order Visualised
```
        4          ← visited 4th
      /   \
     2     6       ← visited 2nd, 6th
    / \   / \
   1   3 5   7     ← visited 1st, 3rd, 5th, 7th

L → Root → R at every subtree:
  subtree(2): 1 → 2 → 3
  subtree(6): 5 → 6 → 7
  full tree:  1 → 2 → 3 → 4 → 5 → 6 → 7
```
---
### 🔄 Three Traversals Compared
```python
# Inorder   L → Root → R  (sorted for BST)
res.append(cur.val)  ← after left dive, before right

# Preorder  Root → L → R
res.append(cur.val)  ← before pushing to stack

# Postorder L → R → Root
res.append(cur.val)  ← after both children processed
```
---
```
Traversal                  Order                BST Result            Use Case
Inorder                    L→Root→R             Sorted ✅V            alidate BST, kth smallest
Preorder                   Root→L→R             Root first             Copy tree, serialize
Postorder                  L→R→Root             Root last              Delete tree, evaluate expr
```
---
🔄 Recursive Alternative
```python
def inorderTraversal(self, root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)       # L
        res.append(node.val) # Root
        dfs(node.right)      # R
    dfs(root)
    return res
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Every node is visited exactly once.
- **Space**:
    - Worst case: O(n) — when the tree is completely unbalanced (like a linked list).
    - Best case: O(log n) — for a balanced binary tree (due to stack height).

---
## 🆚 Comparison
```
Approach                     Time                    Space                 Notes 
Iterative (stack)            O(n)                    O(h)                  Explicit stack, no recursion limit
Recursive                    O(n)                    O(h)                  Cleaner code, uses call stack
```
---
## ✅ Final Answer
```
return [1, 2, 3, 4, 5, 6, 7] ✅
```
---

### 💡 Interview tip: 

The while loop condition while cur or stack is the subtle key — cur handles the dive phase, stack handles the backtrack phase. Missing either condition breaks the traversal. Also worth mentioning: inorder on a BST = sorted array, which is why Validate BST and Kth Smallest in BST both use inorder traversal under the hood.
