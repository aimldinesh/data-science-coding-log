# 🧲 Problem: Maximum Depth of Binary Tree

- **Platform**: [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)
- **Submission**: [https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1678351360/](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1678351360/)
- **Date Solved**: 2025-06-27
- **Tags**: Tree, Queue, BFS
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given the root of a binary tree, return its maximum depth.
- The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### 📌 Example
```python

Input:
    3
   / \
  9  20
     / \
    15  7

Output: 3
```
---

## 🚀 Approach
💡 Intuition
- Use Breadth-First Search (BFS) level by level.
- For every level processed, increase a level counter.
- Once all levels are processed (queue is empty), level will represent the maximum depth.

👣 Approach
- Edge Case: If root is None, return 0.
- Use a deque to implement a queue for level-order traversal (BFS).
- Initialize level = 0.
- While the queue is not empty:
     - For all nodes at the current level:
          - Pop them from the queue.
          - Add their left and right children to the queue if they exist.
     - After processing the level, increment level.

- Return level.


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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, depth is 0
        if not root:
            return 0
        
        level = 0  # Track depth level
        q = deque([root])  # Queue for BFS traversal starting from the root

        while q:
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()

                # Add left and right children (if exist) to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Increase level count after processing current level
            level += 1

        # Return the final depth of the tree
        return level

        
```

---
### 🔍 Step-by-step Execution with Example
```python
Input:
    1
   / \
  2   3
 / 
4

Level 0:
 - queue = [1] → level = 0

Level 1:
 - Pop 1 → Push 2 and 3
 - queue = [2, 3] → level = 1

Level 2:
 - Pop 2 → Push 4
 - Pop 3 → no children
 - queue = [4] → level = 2

Level 3:
 - Pop 4 → no children
 - queue = [] → level = 3

→ Final depth = 3
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each node is visited exactly once.
    - n is the number of nodes in the binary tree.
- **Space**: O(w)
    - w is the maximum width of the binary tree (i.e., the number of nodes at the widest level).
    - In the worst case (completely balanced binary tree), this becomes O(n/2) → O(n).

---
