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

## 💡 Time and Space Complexity
- **Time**: O(L)
    - Where L is the length of the linked list. We traverse the list at most twice.
- **Space**: O(1)
    - No extra space is used aside from pointers.
