# 🧲 Problem: Add Two Numbers

- **Platform**: [LeetCode](https://leetcode.com/problems/add-two-numbers/solutions/)
- **Submission**: [https://leetcode.com/problems/add-two-numbers/submissions/](https://leetcode.com/problems/add-two-numbers/submissions/)
- **Date Solved**: 2025-06-21
- **Tags**: Linked List, Iteration, Two Pointer
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given two non-empty linked lists representing two non-negative integers.
- The digits are stored in reverse order, and each node contains a single digit.
- Add the two numbers and return the result as a linked list (also in reverse order).

### 📌 Examples
```
Input:
l1 = 2 → 4 → 3   (represents 342)
l2 = 5 → 6 → 4   (represents 465)

Output:
7 → 0 → 8        (represents 807)
```
---

## 🚀 Approach
💡 Intuition
- This is like doing column-wise addition (like grade school):
    - Add digits from l1 and l2 at the same positions.
    - Keep track of a carry.
    - If sum ≥ 10, carry to next digit.
    - Build the resulting number as a new linked list.

👣 Approach
- Use a dummy node to start the result list.
- Use cur to point to the current node in the result list.
- Initialize carry = 0.
- Traverse both l1 and l2:
    - Add their values plus carry.
    - Store sum % 10 in the current node.
    - Update carry = sum // 10.

- After loop ends, if any carry remains, add it as a final node.
- Return dummy.next.

---

## 💻 Code (Python)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge case handling and to return the head easily
        dummy = ListNode()
        cur = dummy  # Pointer to build the result list

        carry = 0  # Initialize carry to 0

        # Traverse both lists until all digits and carry are processed
        while l1 or l2 or carry:
            # Extract current values or use 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate sum and update carry
            val = v1 + v2 + carry
            carry = val // 10  # Integer division to find carry
            val = val % 10     # Remainder is the current digit

            # Add the computed digit as a new node in the result list
            cur.next = ListNode(val)
            cur = cur.next  # Move the pointer forward

            # Move input list pointers forward if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the head of the resulting linked list (excluding dummy node)
        return dummy.next
```

---

### 🔍 Step-by-Step Execution
```python
Let:

l1 = 2 → 4 → 3 (represents 342)
l2 = 5 → 6 → 4 (represents 465)

Step 1:

v1 = 2, v2 = 5, carry = 0
sum = 7 → new node: 7

Step 2:

v1 = 4, v2 = 6, carry = 0
sum = 10 → new node: 0, carry = 1

Step 3:

v1 = 3, v2 = 4, carry = 1
sum = 8 → new node: 8

Final List: 7 → 0 → 8 (represents 807)

```

## 💡 Time and Space Complexity
- **Time**: O(max(m, n))
    - Where m and n are the lengths of the two linked list
- **Space**: O(max(m, n))
    - Because we create a new list to store the result
