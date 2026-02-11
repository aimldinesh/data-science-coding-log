# 🧲 Problem: Linked List Cycle

- **Platform**: [LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)
- **Submission**: [https://leetcode.com/problems/linked-list-cycle/submissions/1668331936/](https://leetcode.com/problems/linked-list-cycle/submissions/1668331936/)
- **Date Solved**: 2025-06-18
- **Tags**: Linked list, Tortoise , Set
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Detect if a singly linked list has a cycle in it.

### 📌 Examples:

```python
- Case 1 (Cycle exists):
Input:  3 → 2 → 0 → -4 ↘
             ↑_________↗
Output: True

- Case 2 (No cycle):
Input: 1 → 2 → None
Output: False
```
---

## 🚀 Approach 1 : Floyd’s Cycle Detection Algorithm 
🧠 Intuition:
- If a cycle exists in the list, then a faster-moving pointer will eventually meet the slower one by "lapping" it — similar to two runners on a circular track.
- This idea is implemented using Floyd’s Cycle Detection Algorithm (also known as the Tortoise and Hare Algorithm).

👣 Approach:
- Initialize two pointers:
     - slow (moves one step at a time)
     - fast (moves two steps at a time)

- Traverse the list:
     - If fast or fast.next becomes None, there’s no cycle.
     - If slow and fast ever meet, a cycle exists.

- Return True if a cycle is found; otherwise, False.
---

## 💻 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the linked list.
        slow, fast = head, head

        # Continue traversing the linked list as long as fast and fast.next are not None.
        while fast and fast.next:
            # Move slow pointer by one step (next node).
            slow = slow.next
            # Move fast pointer by two steps (next next node).
            fast = fast.next.next
            
            # If the slow and fast pointers meet, there is a cycle in the linked list.
            if slow == fast:
                return True
        
        # If the loop completes without the slow and fast pointers meeting, there is no cycle.
        return False
        
```
---
### 🔍 Step-by-Step Execution:
```python
- Let’s consider a list:
- head = 1 → 2 → 3 → 4 → 2 (cycle back to node with value 2)

1. slow = 1, fast = 1

2. Iteration 1:
   - slow → 2
   - fast → 3

3. Iteration 2:
   - slow → 3
   - fast → 2 (after 4 → 2 due to cycle)

4. Iteration 3:
   - slow → 4
   - fast → 4
   - Now, slow == fast, so cycle detected

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each node is visited at most twice.
- **Space**: O(1)
    - Uses only two pointers.

---

## 🚀 Approach 2 : HashSet
💡 Intuition:
- As we traverse the list, we can store each node's reference in a set.
- If we ever visit the same node again, it confirms there's a cycle.
- Think of it like visiting rooms in a house — if you find yourself back in the same room, you're looping.

👣 Approach:
- Create an empty set called hashSet.
- Start from the head of the linked list.
- For each node:
    - If it already exists in the set → cycle detected, return True.
    - Otherwise, add it to the set and move to the next node.
- If traversal reaches the end (None), return False.


---

## 💻 Code (Python)

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()     # A set to store visited nodes
        cur = head          # Start traversing from the head

        while cur:
            if cur in hashSet:
                # If we’ve seen this node before, a cycle exists
                return True

            # Add the current node to the set and move to the next node
            hashSet.add(cur)
            cur = cur.next

        # If we reach the end of the list, there’s no cycle
        return False
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each node is visited once until a cycle is found or list ends.
- **Space**: O(n)
    - In the worst case (no cycle), all nodes are stored in the set.

---
