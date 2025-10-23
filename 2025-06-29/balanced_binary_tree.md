# 🧲 Problem: Balanced Binary Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/balanced-binary-tree/description/)
- **Submission**: [https://leetcode.com/problems/balanced-binary-tree/submissions/1680375312/](https://leetcode.com/problems/balanced-binary-tree/submissions/1680375312/)
- **Date Solved**: 2025-06-29
- **Tags**: Tree, DFS
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return True if it is height-balanced, and False otherwise.
    - A binary tree is height-balanced if for every node, the height difference between its left and right subtrees is no more than 1.
### 📌 Example
```python
Input Tree:
        1
       / \
      2   3
     / \
    4   5

Output:True (balanced)
```
---

## 🚀 Approach
💡 Intuition
- Instead of recalculating the height at each node repeatedly, we combine the balance check and height calculation in a single DFS traversal.
- We return:
   - [True, height] if subtree is balanced
   - [False, height] if not

- If at any node:
   - Left or right subtree is unbalanced
   - OR the height difference exceeds 1
   - → Then the current subtree is not balanced

👣 Approach
- Define a helper function dfs(root) that returns a pair:[is_balanced, height]
- For each node:
   - Recur for left and right child
   - Check if both subtrees are balanced and their height difference ≤ 1
   - Return combined balance and height

- In main function, return dfs(root)[0]

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform DFS and check balance of each subtree
        def dfs(root):
            # An empty tree is balanced and has height 0
            if not root:
                return [True, 0]  # [is_balanced, height]

            # Recursively check left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A tree is balanced if:
            # 1. Both left and right subtrees are balanced
            # 2. The difference in height between them is no more than 1
            balanced = (
                left[0] and right[0] and  # Both subtrees are balanced
                abs(left[1] - right[1]) <= 1  # Height difference is acceptable
            )

            # Return whether the current subtree is balanced,
            # and its height (1 + max of left and right heights)
            return [balanced, 1 + max(left[1], right[1])]

        # The first element of the returned pair tells if the tree is balanced
        return dfs(root)[0]
                       
```
---
### 🔍 Step-by-step Execution with example
```python
Input Tree:
        1
       / \
      2   3
     / \
    4   5

TreeNode Structure:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

Goal:
Check if this tree is height-balanced, i.e., for every node, the left and right subtree heights differ by no more than 1.

Step-by-step dfs() Execution:
1. Start at root = 1
Calls dfs(root)
→ goes into dfs(root.left) = dfs(2)

2. At node 2
→ goes into dfs(root.left) = dfs(4)

3. At node 4
- Left and right children are None
- So both return [True, 0]
- Now check:
   - balanced = True and True and abs(0 - 0) <= 1 → True
   - Height = 1 + max(0, 0) = 1

- Return [True, 1] up to node 2

4. Back to node 2 → now go into dfs(5)

5. At node 5
  - Same as node 4
  - Return [True, 1]

6. Back at node 2
  - Left = [True, 1], Right = [True, 1]
  - balanced = True and True and abs(1 - 1) <= 1 → True
  - Height = 1 + max(1, 1) = 2
  - Return [True, 2] to root

7. Back to root → now go into dfs(3)

8. At node 3
  - Left and right = None → [True, 0]
  - balanced = True and True and abs(0 - 0) <= 1 → True
  - Height = 1 + max(0, 0) = 1
  - Return [True, 1] to root

9. Final at root node 1
  - Left = [True, 2], Right = [True, 1]
  - balanced = True and True and abs(2 - 1) <= 1 → True
  - Height = 1 + max(2, 1) = 3
  - Return [True, 3]

Final Output: return dfs(root)[0] → True

Conclusion: The tree is balanced.

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Visit every node once
- **Space**: O(h)
    - Recursion stack space (h = height of tree)

---
