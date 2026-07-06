# 🧲 Problem: Remove Nth Node From End of List

- **Platform**: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
- **Submission**: [https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1670603831/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1670603831/)
- **Date Solved**: 2025-06-20
- **Tags**: Linked List, Two Pointer
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given the head of a linked list and an integer n.
- Remove the n-th node from the end of the list and return the head of the modified list.

### 📌 Examples
```
Input:

List: 1 → 2 → 3 → 4 → 5, n = 2

Output:
List: 1 → 2 → 3 → 5 (the 4 is removed, which is the 2nd from the end)

```
---

## 🚀 Approach
💡 Intuition
- If we know the length of the list, we can calculate the index from the start as:length - n, and delete that node.
- But to do it in one pass, we can use the two-pointer technique:
     - Move the right pointer n steps ahead.
     - Then move both left and right together until right reaches the end.
     - Now left is just before the node we need to delete.
```python
Remove 2nd from end in [1, 2, 3, 4, 5]

right moves n=2 steps ahead:
left=dummy, right=3

then both move together until right=None:
left=3, right=None

left.next = left.next.next → skip 4
Result: [1, 2, 3, 5] ✅
```

👣 Approach
- Create a dummy node pointing to head. This helps handle edge cases (like deleting the first node).
- Initialize two pointers: left = dummy and right = head.
- Move right n steps ahead.
- Move both left and right together until right reaches the end.
- Now left.next is the node to remove.
- Set left.next = left.next.next to delete it.
- Return dummy.next as the new head.
---

## 💻 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head (helps handle edge cases like removing the head)
        dummy = ListNode(0, head)
        
        # Initialize two pointers: 'left' starts at dummy, 'right' starts at head
        left = dummy
        right = head

        # Move 'right' n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers one step at a time until 'right' reaches the end
        # After the loop, 'left' will be just before the node we want to remove
        while right:
            left = left.next
            right = right.next

        # Skip the target node
        left.next = left.next.next

        # Return the updated list (could be a new head if original head was removed)
        return dummy.next

```

---
### 🔍 Step-by-Step Execution with Example
```python
Input:
head = 1 → 2 → 3 → 4 → 5, n = 2

Initialization:
dummy → 0 → 1 → 2 → 3 → 4 → 5
```
```python
dummy → 1 → 2 → 3 → 4 → 5 → None
  ↑left
        ↑right
```
---

Phase 1 — Move right n=2 steps
n=2: right = right.next = 2
```
dummy → 1 → 2 → 3 → 4 → 5 → None
  ↑left     ↑right
```
n=1: right = right.next = 3
```python
dummy → 1 → 2 → 3 → 4 → 5 → None
  ↑left          ↑right
```
n=0: stop
---

Phase 2 — Move both until right=None
Step 1:
```python
left  = left.next  = 1
right = right.next = 4

dummy → 1 → 2 → 3 → 4 → 5 → None
        ↑left       ↑right
```
Step 2:
```python
left  = left.next  = 2
right = right.next = 5

dummy → 1 → 2 → 3 → 4 → 5 → None
            ↑left       ↑right
```
Step 3:
```python
left  = left.next  = 3
right = right.next = None

dummy → 1 → 2 → 3 → 4 → 5 → None
                ↑left        ↑right
```
right=None → stop

---

Phase 3 — Delete target
```python
left = node(3)
left.next = node(4)   ← this is the node to delete
left.next = left.next.next = node(5)

dummy → 1 → 2 → 3 → 5 → None
                  ↑left  ↑(skipped 4)
```
---

### 🔍 Edge Cases

Remove head (n = length of list)
```python
Input: [1, 2, 3],  n=3

Phase 1: right moves 3 steps → right=None
Phase 2: right already None → skip entirely
left = dummy

left.next = left.next.next = node(2)
dummy → 2 → 3

return dummy.next = [2, 3] ✅
```
Single node list
```python
Input: [1],  n=1

dummy → 1 → None
left=dummy, right=1

Phase 1: right = right.next = None
Phase 2: right=None → skip

left.next = left.next.next = None
dummy → None

return dummy.next = None ✅
```
Two nodes, remove last
```python
Input: [1, 2],  n=1

Phase 1: right = 2
Phase 2: left=1, right=None → stop
left.next = left.next.next = None

return [1] ✅
```
---



## 💡 Time and Space Complexity
- **Time**: O(L)
    - Where L is the length of the linked list. We traverse the list at most twice.
- **Space**: O(1)
    - No extra space is used aside from pointers.
