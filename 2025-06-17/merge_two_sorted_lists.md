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
🧠 Intuition
Use a dummy node as a fake head so you never need special logic for the first node. Keep a tail pointer at the end of the merged list. At each step, compare the current nodes of both lists — attach the smaller one to tail and advance that list's pointer. When one list runs out, attach the remaining list directly.
```python
list1: 1 → 3 → 5
list2: 2 → 4 → 6

Compare heads, pick smaller, advance:
1 < 2 → take 1
2 < 3 → take 2
3 < 4 → take 3
4 < 5 → take 4
5 < 6 → take 5
list1 empty → attach rest of list2 (6)

Result: 1 → 2 → 3 → 4 → 5 → 6
```
---

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

Input:
```python
list1: 1 → 3 → 5 → None
list2: 2 → 4 → 6 → None
```
Initial:
```python
dummy → None
tail  = dummy
```
Step 1: list1.val=1, list2.val=2
```python
1 < 2 → tail.next = node(1)
list1 = node(3)
tail  = node(1)

dummy → 1
             ↑tail
```
Step 2: list1.val=3, list2.val=2
```python
3 > 2 → tail.next = node(2)
list2 = node(4)
tail  = node(2)

dummy → 1 → 2
                  ↑tail
```
Step 3: list1.val=3, list2.val=4
```python
3 < 4 → tail.next = node(3)
list1 = node(5)
tail  = node(3)

dummy → 1 → 2 → 3
                      ↑tail
```
Step 4: list1.val=5, list2.val=4
```python
5 > 4 → tail.next = node(4)
list2 = node(6)
tail  = node(4)

dummy → 1 → 2 → 3 → 4
                           ↑tail
```
Step 5: list1.val=5, list2.val=6
```python
5 < 6 → tail.next = node(5)
list1 = None
tail  = node(5)

dummy → 1 → 2 → 3 → 4 → 5
                                ↑tail
```
Loop ends: list1=None
Attach remainder:
```python
list1 = None → skip
list2 = node(6) → tail.next = node(6)

dummy → 1 → 2 → 3 → 4 → 5 → 6
```
---
### 💡 Why Dummy Node?
```python
# Without dummy — need special case for first node:
head = None
if list1.val < list2.val:
    head = list1
    list1 = list1.next
else:
    head = list2
    list2 = list2.next
tail = head
# messy and error-prone ❌

# With dummy — uniform logic from start:
dummy = ListNode()
tail = dummy
# tail.next = whoever wins — no special case ✅
# return dummy.next at end
```
---
### 🔍 Edge Cases
```python
# One list empty
list1=None, list2=[1,2,3]
→ while loop skipped entirely
→ tail.next = list2
→ return [1,2,3] ✅

# Both empty
list1=None, list2=None
→ while skipped, both if/elif skipped
→ return dummy.next = None ✅

# Lists of different lengths
list1=[1,3], list2=[2,4,5,6]
→ while handles 1,2,3,4
→ list1 exhausted → attach list2 remainder [5,6] ✅

# Duplicate values
list1=[1,2], list2=[1,3]
→ 1==1 → else branch takes list2's 1
→ 1<2  → takes list1's 1
→ 2<3  → takes list1's 2
→ attach list2's 3
→ [1,1,2,3] ✅
```
---
### 💡 Pointer Flow Visualised
```python
dummy → [?]
  ↑tail

After step 1:         After step 2:         After step 3:
dummy → 1             dummy → 1 → 2         dummy → 1 → 2 → 3
        ↑tail                     ↑tail                       ↑tail

list1: 3→5            list1: 3→5            list1: 5
list2: 2→4→6          list2: 4→6            list2: 4→6
```
---


## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - where n and m are the lengths of the two lists
- **Space**: O(1)
    - No extra memory used, merging done in-place

---
## 🔄 Recursive Alternative
```python
def mergeTwoLists(self, list1, list2):
    if not list1: return list2
    if not list2: return list1

    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
```
---
### 🆚 Comparison
```python
Approach             Time               Space            Notes
Iterative           O(n+m)O             (1)             ✅ In-place, no call stack
Recursive           O(n+m)              O(n+m)           Clean but uses call stack
```
---

## ✅ Final Answer
```python
return dummy.next = 1 → 2 → 3 → 4 → 5 → 6 ✅
```
---

### 💡 Interview tip: 

The dummy node pattern is one of the most reusable linked list tricks — it also appears in Merge K Sorted Lists, Remove Nth Node, and Partition List. Always mention it by name: "I'll use a dummy head to avoid special-casing the first node" — interviewers recognise it immediately as a sign of linked list fluency.

