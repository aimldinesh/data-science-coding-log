# 🧲 Problem: Asteroid Collision

- **Platform**: [LeetCode](https://leetcode.com/problems/asteroid-collision/description/)
- **Submission**: [https://leetcode.com/problems/asteroid-collision/submissions/1647033254/](https://leetcode.com/problems/asteroid-collision/submissions/1647033254/)
- **Date Solved**: 2025-05-28
- **Tags**: Array, Stack, Simulation
- **Difficulty**: Medium

---

## ✅ Problem Statement
- We are given an array of integers asteroids, representing asteroids in a row.
    - Each asteroid moves at the same speed.
    - A positive value means it is moving to the right.
    - A negative value means it is moving to the left.

- When two asteroids collide, the smaller one (by absolute value) explodes. If both are the same size, both explode.
- Two asteroids moving in the same direction will never collide.
- Return the state of the asteroids after all collisions.

### 🔍 Examples
```python
Input: asteroids = [5, 10, -5]
Output: [5, 10]
# -5 collides with 10 → 10 survives

Input: asteroids = [8, -8]
Output: []
# Both explode (equal magnitude)

Input: asteroids = [10, 2, -5]
Output: [10]
# 2 and -5 collide → -5 survives, then -5 collides with 10 → 10 survives

Input: asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
# No collisions, all are moving away from each other
```
---

## 🚀 Approach : Stack Simulation
🧠 Intuition:
- We use a stack to simulate asteroid collisions:
    - Push each asteroid onto the stack if it's safe.
    - If a left-moving asteroid meets a right-moving asteroid on the stack, simulate the collision:
         - The larger one (absolute value) survives.
         - If they are equal, both are destroyed.

🔧 Steps:
- Initialize an empty stack.
- Iterate through each asteroid:
     - While conditions match for a collision (stack[-1] > 0 and a < 0):
          - Compare their absolute values.
          - Pop the weaker one.
          - If they are equal, remove both.

- If an asteroid survives all collisions, push it to the stack.
- Return the final stack.
---

## 💻 Code (Python)

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack to keep track of asteroids that have not exploded
        stack = []

        # Iterate through each asteroid
        for a in asteroids:
            # Handle collision: when a moving left asteroid (negative) encounters a right-moving one (positive)
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]  # Calculate the net effect (collision result)

                if diff < 0:
                    # The left-moving asteroid is stronger; pop the top (right-moving) asteroid
                    stack.pop()
                    # Continue checking for more possible collisions
                elif diff > 0:
                    # The right-moving asteroid is stronger; mark the left-moving asteroid for destruction
                    a = 0  # It will not be pushed into the stack
                else:
                    # Both asteroids are equal in size and destroy each other
                    a = 0  # Mark for no push
                    stack.pop()  # Remove the right-moving asteroid
                    # No need to continue since both are destroyed

            # If current asteroid survives the collision, push it to the stack
            if a:
                stack.append(a)

        # Return the list of remaining asteroids
        return stack
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each asteroid is pushed to the stack at most once and popped at most once.
    - All operations inside the loop (comparisons, additions, etc.) are O(1).
    - ✅ Total Time: O(n), where n is the number of asteroids.

- **Space**: O(n)
    - In the worst case, none of the asteroids collide, and all are stored in the stack.
    - ✅ Total Space: O(n) for the stack storing surviving asteroids.
