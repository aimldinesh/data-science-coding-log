# 🧲 Problem: Merge Two Sorted Lists

- **Platform**: [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/description/)
- **Submission**: [https://leetcode.com/problems/merge-two-sorted-lists/submissions/1667194835/](https://leetcode.com/problems/merge-two-sorted-lists/submissions/1667194835/)
- **Date Solved**: 2025-06-17
- **Tags**: Linked List, Sorting, Two Pointer, Merge
- **Difficulty**: Easy

---

## ✅ Problem Statement
- You are given two sorted linked lists list1 and list2. Your task is to merge them into one sorted linked list and return its head.
### 📌 Examples:
```python
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
```

---

## 🚀 Approach
🔍 Intuition:
- Since both lists are already sorted, you can use two pointers (list1 and list2) to compare elements one by one and build a new sorted list. This way, no sorting is needed afterward.

🧠 Approach:
- Create a dummy node to act as the head of the new merged list.
- Use a tail pointer starting at the dummy node to build the merged list.
- Loop while both list1 and list2 are not empty:
     - Compare list1.val and list2.val
     - Append the smaller node to tail.next
     - Advance the list whose node was chosen
     - Move tail forward

- After the loop, one of the lists may still have remaining nodes.
     - Attach the non-empty list to tail.next

- Return dummy.next (which points to the actual start of the merged list).
---

## 💻 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode()
        tail = dummy  # Tail will always point to the last node in the merged list

        # Traverse both lists until either becomes empty
        while list1 and list2:
            # Compare current nodes of both lists
            if list1.val < list2.val:
                tail.next = list1      # Append list1 node to merged list
                list1 = list1.next     # Move to next node in list1
            else:
                tail.next = list2      # Append list2 node to merged list
                list2 = list2.next     # Move to next node in list2

            tail = tail.next           # Move the tail pointer forward

        # If any nodes remain in either list, append them directly
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the merged list (skipping the dummy node)
        return dummy.next
```
---
### 🔢 Step by Step Code Execution With Example
```python
Input:
list1 = 1 -> 2 -> 4  
list2 = 1 -> 3 -> 5

| Step | `list1.val` | `list2.val` | `tail` added | New `list1` | New `list2` | `Merged List`         |
| ---- | ----------- | ----------- | ------------ | ----------- | ----------- | --------------------  |
| 1    | 1           | 1           | `list2` (1)  | 1 → 2 → 4   | 3 → 5       | 1                     |
| 2    | 1           | 3           | `list1` (1)  | 2 → 4       | 3 → 5       | 1 → 1                 |
| 3    | 2           | 3           | `list1` (2)  | 4           | 3 → 5       | 1 → 1 → 2             |
| 4    | 4           | 3           | `list2` (3)  | 4           | 5           | 1 → 1 → 2 → 3         |
| 5    | 4           | 5           | `list1` (4)  | None        | 5           | 1 → 1 → 2 → 3 → 4     |

- At this point, list1 is None, but list2 is 5. So we attach remaining list2.
| Final| -           | -           | list2 (5)    | None        | None        | 1 → 1 → 2 → 3 → 4 → 5 |

- ✅ Final Output

dummy.next → 1 → 1 → 2 → 3 → 4 → 5
```
---

## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are the lengths of the two lists
- **Space**: O(1)
    - No extra memory used, merging done in-place
