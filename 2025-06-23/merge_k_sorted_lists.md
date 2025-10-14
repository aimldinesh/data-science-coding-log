# 🧲 Problem: Merge k Sorted Lists

- **Platform**: [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/description/)
- **Submission**: [https://leetcode.com/problems/merge-k-sorted-lists/submissions/1576765940/](https://leetcode.com/problems/merge-k-sorted-lists/submissions/1576765940/)
- **Date Solved**: 2025-06-23
- **Tags**: Linked List, Merge Sort, Heap
- **Difficulty**: Hard

---

## ✅ Problem Statement
- You are given a list of k sorted linked lists.
- Merge them into a single sorted linked list and return its head.

### 📌 Examples
```python
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
```
---

## 🚀 Approach
💡 Intuition
- Merging two sorted linked lists is a classic problem.
- To merge k lists efficiently, apply pairwise merging repeatedly.
- This is similar to the merge step in merge sort, giving better performance than naive merging one by one.

👣 Approach
- Edge Case: If the input lists is empty, return None.
- While there’s more than one list:
    - Merge lists in pairs (i.e., 0 & 1, 2 & 3, etc.)
    - Store the merged results in a temporary list.
    - Update lists to the new merged list collection.

- Return the only list left in lists.

#### Helper Function – mergeList(l1, l2):
- Classic two-pointer merge:
    - Create a dummy node.
    - Append the smaller node of l1 and l2 to the result.
    - When one list is exhausted, attach the rest of the other list.
---

## 💻 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Return None if the input list of linked lists is empty
        if not lists or len(lists) == 0:
            return None

        # Continuously merge pairs of lists until we only have one list left
        while len(lists) > 1:
            mergedLists = []  # Temporary list to store merged results

            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair
                # Second list in the pair (may be None if lists length is odd)
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the two lists and append the result to mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            
            # Update lists to contain only the merged lists
            lists = mergedLists
        
        # The final merged list is the only element left in lists
        return lists[0]

    def mergeList(self, l1, l2):
        # Create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy  # Tail of the merged list for appending nodes

        # Merge nodes from l1 and l2 based on their values
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append any remaining nodes from either l1 or l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the merged list starting from the node after the dummy
        return dummy.next
```

---

## 💡 Time and Space Complexity
- **Time**: O(N log k)
    - N: total number of nodes across all lists
    - k: number of input lists
    - Why log k? Each round reduces the number of lists by half (merge sort style)
- **Space**: O(1)
    - Merging is done in-place (excluding recursive stack or heap usage if used)

---
