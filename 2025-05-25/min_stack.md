# 🧲 Problem: Min Stack

- **Platform**: [LeetCode](https://leetcode.com/problems/min-stack/description/)
- **Submission**: [https://leetcode.com/problems/min-stack/submissions/1644085498/](https://leetcode.com/problems/min-stack/submissions/1644085498/)
- **Date Solved**: 2025-05-25
- **Tags**: Stack, Design, Data Structure
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Design a stack that supports:
   - push(val): Pushes an element onto the stack.
   - pop(): Removes the element on the top of the stack.
   - top(): Gets the top element.
   - getMin(): Retrieves the minimum element in the stack.

- Implement the above operations in O(1) time.
### 🔍 Example
```python
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],         [-2],  [0],   [-3],   [],      [],   [],    []]

Output:
[None, None, None, None, -3, None, 0, -2]
```
---

## 🚀 Approach : Two Stacks (Main Stack + Min Stack)
🧠 Intuition:
- We maintain two stacks:
    - One stack stack to store all elements.
    - One stack minStack to keep track of the minimum value at each level of the main stack.
- This way, the top of minStack always contains the current minimum value.

🔧 Steps:
- push(val):
    - Push the value to stack.
    - Push min(val, minStack[-1]) to minStack to track the new minimum.

- pop():
    - Pop from both stack and minStack.

- top():
    - Return the top of stack.

- getMin():
    - Return the top of minStack.

---

## Key Insight: Track Minimum at Every Level

At each position in the stack, remember "what's the minimum from here down?"
```python
Push: 5 → 3 → 7 → 2

Main Stack    Min Stack
    2             2     ← min of entire stack
    7             3     ← min if top 2 elements removed
    3             3     ← min if top 3 elements removed
    5             5     ← min if only this element exists
```
minStack[-1] always gives the current minimum instantly!

---

## 💻 Code (Python)

```python
class MinStack:

    def __init__(self):
        # Initialize two stacks:
        # 1. 'stack' stores all values normally.
        # 2. 'minStack' keeps track of the minimum at each level.
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push the value to the main stack.
        self.stack.append(val)
        # Push the new minimum to the minStack.
        # If minStack is empty, val is the minimum.
        # Otherwise, compare with the current min and push the smaller one.
        minVal = val if not self.minStack else min(val, self.minStack[-1])
        self.minStack.append(minVal)

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync.
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top of minStack, which holds the current minimum value.
        return self.minStack[-1]
```

---
## Step-by-Step Walkthrough
```python
Operations: push(5), push(3), push(7), push(2), pop(), getMin()
```
push(5)
```python
val=5, minStack empty → minVal = 5

stack    = [5]
minStack = [5]
            ↑ 5 is the only element, so min=5
```
push(3)
```python
val=3, min(3, 5) = 3 → minVal = 3

stack    = [5, 3]
minStack = [5, 3]
               ↑ new min is 3
```
push(7)
```python
val=7, min(7, 3) = 3 → minVal = 3

stack    = [5, 3, 7]
minStack = [5, 3, 3]
               ↑ min stays 3, even though 7 was pushed
```
push(2)
```python
val=2, min(2, 3) = 2 → minVal = 2

stack    = [5, 3, 7, 2]
minStack = [5, 3, 3, 2]
                     ↑ new min is 2
```

pop()
```python
Remove top from BOTH stacks (keep in sync!)

stack    = [5, 3, 7]
minStack = [5, 3, 3]
                  ↑ min restored to 3 automatically!
```
getMin()
```python
return minStack[-1] = 3 ✅

Why Pop From Both Stacks?
```python
If we only popped main stack:

stack    = [5, 3, 7]     ← 2 removed
minStack = [5, 3, 3, 2]  ← 2 still here (WRONG!)
                      ↑ getMin() would return 2 (stale!)

Popping both keeps them perfectly in sync:
Each index i represents the same "state" of the stack
```
Visual: What Each minStack Entry Means
```python
stack    = [5,  3,  7,  2]
minStack = [5,  3,  3,  2]
            ↑   ↑   ↑   ↑
            |   |   |   └─ min of [5,3,7,2] = 2
            |   |   └───── min of [5,3,7]   = 3
            |   └───────── min of [5,3]     = 3
            └───────────── min of [5]       = 5
```
---

## 💡 Time and Space Complexity
- **Time**:
    - push(val):O(1)
        - Constant time to append to both stack and minStack.
    - pop():O(1)
        - Constant time to pop from both stacks.
    - top():O(1)
        - Just accessing the last element of the list.
    - getMin():O(1)
        - Just accessing the last element of the minStack.
    - All operations run in constant time.

- **Space**: O(n)
    - We maintain two stacks:
        - stack: stores all values ⇒ O(n)
        - minStack: stores the minimum value at each position ⇒ O(n)
    - So, if there are n elements pushed onto the stack, then total Space = O(n)
