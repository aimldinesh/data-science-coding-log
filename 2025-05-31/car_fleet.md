# 🧲 Problem: Car Fleet

- **Platform**: [LeetCode](https://leetcode.com/problems/car-fleet/description/)
- **Submission**: [https://leetcode.com/problems/car-fleet/submissions/1649790737/](https://leetcode.com/problems/car-fleet/submissions/1649790737/)
- **Date Solved**: 2025-05-31
- **Tags**: Stack, Sorting, Greedy
- **Difficulty**: Medium

---
## ✅ Problem Statement
- You are given:
   - An integer target, representing the destination position.
   - Two lists:
         - position[i] is the starting position of the i-th car.
         - speed[i] is the speed of the i-th car.

- Each car drives towards the target in the same lane.
- A car can never pass another car ahead of it. But if it catches up to a slower car, it forms a car fleet, and they move together at the slower car’s speed.
- You must return the number of car fleets that will arrive at the destination.

### ✅ Example
```python
Input:

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

Output: 3

Explanation:
We sort the cars by their position from nearest to farthest from the target (i.e., right to left):
| Position | Speed | Time to reach target                                 |
| -------- | ----- | ---------------------------------------------------- |
| 10       | 2     | (12 - 10)/2 = 1.0                                    |
| 8        | 4     | (12 - 8)/4 = 1.0     → **same time → merge with 10** |
| 5        | 1     | (12 - 5)/1 = 7.0                                     |
| 3        | 3     | (12 - 3)/3 = 3.0     → **caught by 5 → merge**       |
| 0        | 1     | (12 - 0)/1 = 12.0                                    |

Final fleets:
   - Fleet 1: Cars at 10 & 8
   - Fleet 2: Cars at 5 & 3
   - Fleet 3: Car at 0

✅ Total Fleets = 3

```
---

## 🚀 Approach
💡 Intuition
- If a faster car is behind a slower one, it will catch up and join the slower car, forming a fleet. So we track the time each car needs to reach the target, and check whether a car in front takes more or equal time than the one behind — if yes, they merge.

🧠 Approach
- Pair up each car's (position, speed).
- Sort them in reverse order of position.
- For each car, calculate the time to reach the destination.
- Use a stack to track fleet times:
     - If a car reaches earlier or at the same time as the one ahead, it merges.
     - If it takes more time, it forms a new fleet.
---

## 💻 Code (Python)

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into (position, speed) pairs
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort pairs by position in descending order (rightmost car first)
        pair.sort(reverse=True)
        
        # Stack to track the time each fleet takes to reach the target
        stack = []

        for p, s in pair:
            # Time to reach the destination
            time_to_reach = (target - p) / s
            stack.append(time_to_reach)

            # If current car reaches target earlier or at the same time as the one in front,
            # it merges into the same fleet (pop it from stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Length of the stack = number of fleets
        return len(stack)
  
```
---
### 🧠 Step-by-Step Example
```python
Input:
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

Sorted by position (descending):
[(10,2), (8,4), (5,1), (3,3), (0,1)]

Time to reach target:
(12-10)/2 = 1.0  
(12-8)/4 = 1.0  
(12-5)/1 = 7.0  
(12-3)/3 = 3.0  
(12-0)/1 = 12.0

Fleet stack building:
stack = [1.0]        # car at 10
stack = [1.0]        # car at 8 merges with previous
stack = [1.0, 7.0]   # car at 5 becomes a new fleet
stack = [1.0, 7.0]   # car at 3 merges into fleet of 5
stack = [1.0, 7.0, 12.0]  # car at 0 is slowest, forms own fleet

✅ Output: 3 fleets

```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
    - Sorting the cars by position takes O(n log n)
    - A single pass through the list to compute time and form fleets: O(n)
- **Space**: O(n)
    - Stack to store time values for at most n cars
