# 🧲 Problem: Reverse Linked List II

- **Platform**: [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/description/)
- **Submission**: [https://leetcode.com/problems/reverse-linked-list-ii/submissions/1672713153/](https://leetcode.com/problems/reverse-linked-list-ii/submissions/1672713153/)
- **Date Solved**: 2025-06-22
- **Tags**: Linked List
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given the head of a singly linked list and two integers left and right (1-indexed), reverse the nodes of the list from position left to position right, and return the modified list.
### 📌 Examples
```python
Input:
head = 1 → 2 → 3 → 4 → 5  
left = 2, right = 4

Output:
1 → 4 → 3 → 2 → 5
```
---

## 🚀 Approach
💡 Intuition
- To reverse a part of the list, we need to:
    - Reach the node just before the reversal segment (leftPrev)
    - Reverse nodes between positions left and right
    - Reconnect the reversed sublist with the remaining list
- We use a dummy node to handle edge cases like reversing from the head of the list.

👣 Approach
- Create a dummy node pointing to the head of the list.
- Move a pointer leftPrev to the node just before position left, and cur to the left-th node.
- Reverse the sublist of length right - left + 1 starting from cur.
- Reconnect:
    - leftPrev.next should point to the new head of the reversed sublist.
    - The original left-th node (now tail) should point to the node after position right.
- Return dummy.next.
---

## 💻 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node that points to head (helps handle edge cases)
        dummy = ListNode(0, head)

        # Step 1: Move `leftPrev` to the node before the `left`th node
        leftPrev, cur = dummy, head
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Step 2: Reverse nodes between left and right
        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next       # Temporarily store the next node
            cur.next = prev          # Reverse the link
            prev, cur = cur, tmpNext # Move pointers ahead

        # Step 3: Reconnect the reversed sublist with the original list
        leftPrev.next.next = cur     # Connect the tail of reversed sublist to the node after `right`
        leftPrev.next = prev         # Connect the node before `left` to the new head of reversed sublist

        # Return the new head (may have changed)
        return dummy.next
```

---
## 🧩 Step-by-step with example
```python
Input list:  1 → 2 → 3 → 4 → 5
left = 2, right = 4
```
We’ll visualize how pointers (leftPrev, cur, prev, tmpNext) move and how links change.

#### Step 0 — Setup dummy node
We create a dummy node pointing to the head.
```python
dummy → 1 → 2 → 3 → 4 → 5
```
Initialize:
```python
leftPrev = dummy
cur = head (node 1)
```
### Step 1 — Move leftPrev to the node before left

Move (left - 1) = 1 step:
```python
leftPrev = 1
cur = 2
```
Pointers:
```python
dummy → 1 → 2 → 3 → 4 → 5
          ↑     ↑
       leftPrev cur
```
### Step 2 — Reverse nodes between left and right (2 to 4)

We’ll reverse 3 nodes: 2, 3, 4

Iteration 1
```python
prev = None
cur = 2
tmpNext = 3
```
Reverse link:
```python
2.next = prev → None
```
Now:
```python
1 → 2    3 → 4 → 5
    ↑
   prev
cur → 3
```
Iteration 2
```python
prev = 2
cur = 3
tmpNext = 4
```
Reverse link:
```python
3.next = 2
```
Now:
```python
1 → 2 ← 3    4 → 5
         ↑
        prev
cur → 4
```
Iteration 3
```python
prev = 3
cur = 4
tmpNext = 5
```
Reverse link:
```python
4.next = 3
```
Now:
```python
1 → 2 ← 3 ← 4    5
             ↑
            prev
cur → 5
```
At this point:
 - prev = 4 → 3 → 2
 - cur = 

 ### Step 3 — Reconnect reversed sublist
 
 We had:
 ```python
leftPrev = 1
leftPrev.next = 2  (original left node)
```
Now connect:
```python
leftPrev.next.next = cur   # 2 → 5
leftPrev.next = prev       # 1 → 4
```
Connections become:
```python
dummy → 1 → 4 → 3 → 2 → 5
```
### Step 4 — Return final list

Return dummy.next, which is the real head of the new list:
```python
1 → 4 → 3 → 2 → 5
```

--- 

## 💡 Time and Space Complexity
- **Time**: O(n)
  -We traverse the list once.
- **Space**: O(1)
  - In-place reversal, no extra data structures used.
