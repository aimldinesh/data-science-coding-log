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
## 🔍 Step-by-Step Execution
Input Tree:
```
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```
Initial: stack = [4]

Iteration 1 — pop 4
```
node = 4
swap: left=7, right=2

        4
      /   \
     7     2        ← swapped
    / \   / \
   6   9 1   3

push left=7  → stack=[7]
push right=2 → stack=[7, 2]
```
Iteration 2 — pop 2
```
node = 2
swap: left=3, right=1

        4
      /   \
     7     2
    / \   / \
   6   9 3   1     ← swapped

push left=3  → stack=[7, 3]
push right=1 → stack=[7, 3, 1]
```
Iteration 3 — pop 1
```
node = 1
1 is a leaf → swap None,None (no effect)
no children to push
stack=[7, 3]
```
Iteration 4 — pop 3
```
node = 3
3 is a leaf → swap None,None (no effect)
no children to push
stack=[7]
```
Iteration 5 — pop 7
```
node = 7
swap: left=9, right=6

        4
      /   \
     7     2
    / \   / \
   9   6 3   1     ← swapped

push left=9  → stack=[9]
push right=6 → stack=[9, 6]
```
Iteration 6 — pop 6
```
node = 6
6 is a leaf → no effect
stack=[9]
```
Iteration 7 — pop 9
```
node = 9
9 is a leaf → no effect
stack=[]
```
Loop ends: stack empty

---

### 💡 Stack Order Visualised
```
stack grows →

Start:     [4]
After 4:   [7, 2]       ← 2 on top, processed next
After 2:   [7, 3, 1]    ← 1 on top
After 1:   [7, 3]
After 3:   [7]
After 7:   [9, 6]
After 6:   [9]
After 9:   []
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - All n nodes are visited once.
- **Space**: O(h), Stack size depends on tree height.
    - O(log n) for balanced
    - O(n) for skewed

---

### 💡 Interview tip: 

For a balanced tree space is O(log n), for a skewed tree (linked list shape) space is O(n). Always clarify this when stating space complexity for tree problems — it shows depth of understanding.
