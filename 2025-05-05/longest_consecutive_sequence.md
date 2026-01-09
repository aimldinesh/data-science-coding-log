# 🧲 Problem: Longest Consecutive Sequence

- **Platform**: [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/description/)
- **Submission**: [https://leetcode.com/problems/longest-consecutive-sequence/submissions/1626033043/](https://leetcode.com/problems/longest-consecutive-sequence/submissions/1626033043/)
- **Date Solved**: 2025-05-05
- **Tags**: Array, Hash Table, Union Find
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an unsorted array of integers `nums`, return the **length of the longest consecutive elements sequence**.You must write an algorithm that runs in O(n) time.

---

### 🧪 Example

```python
Input:
nums = [100, 4, 200, 1, 3, 2]

Output:4
Explanation:The longest consecutive sequence is [1, 2, 3, 4], which has length 4.

```
---
## 🧠 Approach: Set + Brute Force Expansion

🧠 Intuition

The goal is to find the longest sequence of consecutive integers in the array.

To allow O(1) lookups, we store all numbers in a set.
Then for each number, we try to expand forward (num, num+1, num+2, ...) as long as the next number exists in the set.

For every starting number:

 +  Keep increasing the current value
 + Count how long the consecutive streak lasts
 + Update the maximum result

⚠️ Note: This approach works correctly but is not optimal, because it may repeatedly recompute the same sequences.

#### 🛠 Algorithm:

1. Convert the list nums into a set store for fast lookup.
2. Initialize res = 0 to track the longest streak.
3. For each number num in nums:

   + Initialize streak = 0 and curr = num
   + While curr exists in store:
     + Increment streak
     + Move to next number: curr += 1

   + Update res = max(res, streak)

4. Return res.


---
## 💻 Code (Python)

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0                     # Stores the longest consecutive sequence length
        store = set(nums)           # Convert list to set for O(1) lookup

        # Try to build consecutive sequence starting from each number
        for num in nums:
            streak = 0
            curr = num

            # Keep moving forward while consecutive numbers exist
            while curr in store:
                streak += 1
                curr += 1

            # Update result with maximum streak found so far
            res = max(res, streak)

        return res
````
---
#### step-by-step code execution with example

🔢 Input Example
````
nums = [100, 4, 200, 1, 3, 2]
````

🧠 Initial Setup

Convert list to set
```
store = {1, 2, 3, 4, 100, 200}
```
Initialize result
```
res = 0
```
🔁 Loop Execution (One Number at a Time)

▶️ Iteration 1: num = 100
```
streak = 0
curr = 100
```
while loop:
+ 100 in store → ✅
 streak = 1, curr = 101

+ 101 in store → ❌ → stop
```
res = max(0, 1) = 1
```
---
▶️ Iteration 2: num = 4
```
streak = 0
curr = 4
```
while loop:

+ 4 in store → ✅
  streak = 1, curr = 5

+ 5 in store → ❌ → stop
```
res = max(1, 1) = 1
```
---
▶️ Iteration 3: num = 200
```
streak = 0
curr = 200
```
while loop:

+ 200 in store → ✅
  streak = 1, curr = 201

+ 201 in store → ❌ → stop
```
res = max(1, 1) = 1
```
---
▶️ Iteration 4: num = 1
```
streak = 0
curr = 1
```
while loop:

+ 1 in store → ✅ → streak = 1, curr = 2

+ 2 in store → ✅ → streak = 2, curr = 3

+ 3 in store → ✅ → streak = 3, curr = 4

+ 4 in store → ✅ → streak = 4, curr = 5

+ 5 in store → ❌ → stop
```
res = max(1, 4) = 4
```
---
▶️ Iteration 5: num = 3
```
streak = 0
curr = 3
```
while loop:

+ 3 in store → ✅ → streak = 1, curr = 4

+ 4 in store → ✅ → streak = 2, curr = 5

+ 5 in store → ❌ → stop
```
res = max(4, 2) = 4
```
⚠️ Note: The sequence 3 → 4 is recomputed, which causes inefficiency.
---
▶️ Iteration 6: num = 2
```
streak = 0
curr = 2
```
while loop:

+ 2 in store → ✅ → streak = 1, curr = 3

+ 3 in store → ✅ → streak = 2, curr = 4

+ 4 in store → ✅ → streak = 3, curr = 5

+ 5 in store → ❌ → stop
```
res = max(4, 3) = 4
```
✅ Final Result
```
return res  # 4
```
The longest consecutive sequence is:
```
[1, 2, 3, 4]
```
----

## 🚀 Approach
- We use a set for O(1) lookups and a greedy strategy to only start a sequence when we find the beginning of one.
- Steps:
   1. Convert the array to a set for fast lookup.
   2. Iterate through the set:
      - Only try to start a sequence at numbers that don't have a predecessor (num - 1 not in set).
      - From the starting number, count how far the sequence continues (num + 1, num + 2, etc.).
   3. Keep track of the maximum sequence length found.

---

## 💻 Code (Python)

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Return 0 if the input list is empty
        
        num_set = set(nums)  # Convert the list to a set for O(1) lookups
        max_length = 0  # Store the longest sequence length
        
        for num in num_set:
            # Start a sequence only if 'num - 1' is not in the set (num is the start of a sequence)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count consecutive numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update max sequence length
                max_length = max(max_length, current_length)

        return max_length  # Return the longest consecutive sequence length

```
---

## 💡 Time and Space Complexity

- **Time**: O(n)
   - Each number is processed at most once.
- **Space**: O(n)
   - Set to store all numbers for fast access.
