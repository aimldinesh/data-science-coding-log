# 🧲 Problem: Daily Temperatures

- **Platform**: [LeetCode](https://leetcode.com/problems/daily-temperatures/description/)
- **Submission**: [https://leetcode.com/problems/daily-temperatures/submissions/1647945958/](https://leetcode.com/problems/daily-temperatures/submissions/1647945958/)
- **Date Solved**: 2025-05-29
- **Tags**: Stack, Monotonic Stack, Array
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given a list of daily temperatures temperatures, return a list such that for each day, the output tells you how many days you would have to wait until a warmer temperature.
- If there is no future day for which this is possible, put 0 instead.

### 🔍 Examples
```python
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Explanation:
- Day 0: 73 → 74 (1 day)
- Day 1: 74 → 75 (1 day)
- Day 2: 75 → 76 (4 days)
- Day 3: 71 → 72 (2 days)
- Day 4: 69 → 72 (1 day)
- Day 5: 72 → 76 (1 day)
- Day 6: 76 → no warmer day → 0
- Day 7: 73 → no warmer day → 0
```
---

## 🚀 Approach 1 : Brute Force
🧠 Intuition:
- For each day, we look ahead in the array to find the next day with a higher temperature.
    - If found, we calculate how many days it takes and store it in the result.
    - If not found, we store 0.

🔧 Steps:
- Initialize an empty result list.
- Loop over each day i:
    - Check every day after i to find a warmer day.
    - If found, store the number of days waited.
    - If not found, store 0.
---

## 💻 Code (Python)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []  # Result list to store answer for each day

        for i in range(n):
            count = 1  # Days waited starts at 1
            j = i + 1  # Start checking from the next day
            while j < n:
                # Found a warmer temperature
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            # If j reached end of list, it means no warmer temp found
            count = 0 if j == n else count
            res.append(count)
        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(n²)
    - Nested loop for each element
- **Space**: O(n)
    - To store result

---

## 🚀 Approach 2 : Monotonic Stack
🧠 Intuition:
- We use a monotonic decreasing stack that stores pairs of (temperature, index).
- As we iterate:
     - If the current temperature is greater than the top of the stack, we found a warmer day for previous days.
     - We calculate the number of days waited and store the result.

🔧 Steps:
- Initialize a result list with 0 for all days.
- Use a stack to store [temperature, index].
- For each temperature:
     - While the stack is not empty and current temperature is greater than top:
         - Pop and compute the difference in indices (i.e., days waited).
- Push current temperature and index to the stack.
- Return the result.
---

## 💻 Code (Python)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with all 0s
        res = [0] * len(temperatures)
        # Stack to store pairs of (temperature, index)
        stack = []

        # Iterate through each temperature with its index
        for i, t in enumerate(temperatures):
            # While current temp is higher than the top of the stack
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                # Calculate the number of days between the current and previous warmer day
                res[stackInd] = (i - stackInd)
            # Push the current temperature and its index to the stack
            stack.append([t, i])

        # Return the result array
        return res
      
```
---
### Step by Step Execution
```python
- Given: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
- Goal: For each day, find out how many days you have to wait until a warmer temperature.
- Initial Setup:
  - res = [0, 0, 0, 0, 0, 0, 0, 0]
  - stack = []
-We'll iterate through temperatures using enumerate, which gives both index i and temperature t.
| Day (i) | Temp (t) | Action                                                   | Stack                        | Result                   |
| ------- | -------- | -------------------------------------------------------- | ---------------------------- | -------------------------|
| 0       | 73       | Push                                                     | [(73, 0)]                    | [0, 0, 0, 0, 0, 0, 0, 0] |
| 1       | 74       | 74 > 73 → pop, res[0]=1; push                            | [(74, 1)]                    | [1, 0, 0, 0, 0, 0, 0, 0] |
| 2       | 75       | 75 > 74 → pop, res[1]=1; push                            | [(75, 2)]                    | [1, 1, 0, 0, 0, 0, 0, 0] |
| 3       | 71       | Push                                                     | [(75, 2), (71, 3)]           | [1, 1, 0, 0, 0, 0, 0, 0] |
| 4       | 69       | Push                                                     | [(75, 2), (71, 3), (69, 4)]  | [1, 1, 0, 0, 0, 0, 0, 0] |
| 5       | 72       | 72 > 69 → pop, res[4]=1; 72 > 71 → pop, res[3]=2; push   | [(75, 2), (72, 5)]           | [1, 1, 0, 2, 1, 0, 0, 0] |
| 6       | 76       | 76 > 72 → pop, res[5]=1; 76 > 75 → pop, res[2]=4; push   | [(76, 6)]                    | [1, 1, 4, 2, 1, 1, 0, 0] |
| 7       | 73       | Push                                                     | [(76, 6), (73, 7)]           | [1, 1, 4, 2, 1, 1, 0, 0] |

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each index is pushed and popped at most once
- **Space**: O(n)
    - For the stack and result array
