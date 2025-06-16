# 🧲 Problem: Reverse Linked List

- **Platform**: [LeetCode](https://leetcode.com/problems/reverse-linked-list/description/)
- **Submission**: [https://leetcode.com/problems/reverse-linked-list/submissions/1666024597/](https://leetcode.com/problems/reverse-linked-list/submissions/1666024597/)
- **Date Solved**: 2025-06-16
- **Tags**: Linked List, Two Pointer, Iteration, Recursion
- **Difficulty**: Easy

---

## ✅ Problem Statement
- You are given the head of a singly linked list. Reverse the list and return the new head.
### 📌 Examples
```python
Input: 1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None
```
---

## 🚀 Approach : Iterative Metho
💡 Intuition
- We need to reverse the direction of each node's .next pointer.
- To do this:
     - We'll iterate through the list.
     - At each node, we’ll make it point to the previous node instead of the next.
     - Keep track of the current and previous nodes.

🧠 Approach
- Initialize:
     - curr = head (current node we are processing)
     - prev = None (previous node, initially nothing)

- While curr is not None:
     - Save the next node: next_node = curr.next
     - Reverse the link: curr.next = prev
     - Move pointers ahead: prev = curr, curr = next_node

- When loop ends, prev will be the new head.
- Return prev.
---

## 💻 Code (Python)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head       # Start from the head of the list
        prev = None       # Initially, previous is None (new tail of the list)

        while curr is not None:
            next_node = curr.next      # 1. Save the next node before breaking the link
            curr.next = prev           # 2. Reverse the current node's pointer
            prev = curr                # 3. Move prev forward (prev now becomes curr)
            curr = next_node           # 4. Move curr forward (go to next node in original list)

        return prev  # At the end, prev will point to the new head of the reversed list

```
---
### 🧮 Step-by-Step Execution
- We track 3 pointers: curr, prev, next_node
✅ Initial State:
```python
curr = Node(1)
prev = None
```
🔁 Iteration 1:
- next_node = curr.next → next_node = Node(2)
- curr.next = prev → 1.next = None
- prev = curr → prev = Node(1)
- curr = next_node → curr = Node(2)

🔄 List becomes:
```python
1 → None
```

🔁 Iteration 2:
- next_node = curr.next → next_node = Node(3)
- curr.next = prev → 2.next = Node(1)
- prev = curr → prev = Node(2)
- curr = next_node → curr = Node(3)

🔄 List becomes:
```python
2 → 1 → None

```
🔁 Iteration 3:
- next_node = curr.next → next_node = None
- curr.next = prev → 3.next = Node(2)
- prev = curr → prev = Node(3)
- curr = next_node → curr = None

🔄 Final List:
```python
3 → 2 → 1 → None
```
🏁 Loop ends (because curr == None)
- We return prev → which is now the new head of the reversed list.

✅ Final Output:
```python
head → 3 → 2 → 1 → None
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(1)
