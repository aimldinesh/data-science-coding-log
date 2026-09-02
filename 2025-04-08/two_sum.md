# 🧮 Problem: Two Sum

- **Platform**: [Leetcode](https://leetcode.com/problems/two-sum/)
- **Submission**: [https://leetcode.com/submissions/detail/1600134420/](https://leetcode.com/submissions/detail/1600134420/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA

---

## ✅ Problem Statement
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.

### 🌰 Example:
```python
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
---

## 🚀  Approach : Brute Force
💡 Intuition:
- We are looking for two numbers in the array whose sum equals the target.
- The simplest way is to check every possible pair in the array.

🧠 Approach :
- Loop through the array with index i.
- For each i, loop through elements after it (index j = i + 1).
- If nums[i] + nums[j] == target, return [i, j].

---

## 💻 Code (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through the list with index i
        for i in range(len(nums)):
            # For each i, iterate through the remaining list with index j
            for j in range(i + 1, len(nums)):
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # If yes, return their indices
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []

```

---

## 💡 Time and Space Complexity
- **Time**: O(n²)
    - Nested loops mean every pair is checked once — inefficient for large list
- **Space**: O(1)
    - No extra space used beyond a few variables — purely in-place computation.

---
## 🚀  Approach 2 : Optimized - One Pass Hash Map
💡 Intuition:
- We want to find two numbers in the list that add up to a given target.
- A brute force way would be to check all pairs, but that takes O(n²) time.

- Instead, we can solve it in O(n) time using a hash map:
     - As we go through the array, we store each number and its index in a dictionary.
     - For every number, we check if the complement (i.e. target - current_number) is already in the dictionary.
     - If it is, we’ve found our answer.
- This works because the dictionary helps us instantly look up if we've already seen the number needed to complete the pair.
```
nums = [2, 7, 11, 15],  target = 9

At n=2:  need 7  → not in map yet → store {2:0}
At n=7:  need 2  → 2 IS in map ✅ → return [0, 1]
```

🧠 Approach :

1. Initialize empty indices = {}
2. For each (i, n):
   + Compute diff = target - n
   + If diff in indices → return [indices[diff], i]
   + Else → store indices[n] = i

4. Return [] if no pair found


---

## 💻 Code (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map (One Pass)
        indices = {}  # Dictionary to store number -> its index

        # Loop through the array with index and value
        for i, n in enumerate(nums):
            # Calculate the complement needed to reach the target
            diff = target - n

            # If complement already exists in the map, we found the pair
            if diff in indices:
                return [indices[diff], i]  # Return indices of the two numbers

            # Otherwise, store the current number and its index
            indices[n] = i

        # If no valid pair is found, return an empty list
        return []


```
---
### 🔍 Step-by-Step Execution 

Input: nums = [2, 7, 11, 15], target = 9
```
Indices:  0   1   2   3
Values:   2   7  11  15
          ↑   ↑
       pair found here
```

i=0, n=2
```
diff = 9 - 2 = 7
7 in {}? ❌
store indices = {2: 0}
```
i=1, n=7
```
diff = 9 - 7 = 2
2 in {2:0}? ✅
return [indices[2], 1] = [0, 1]
```
---
### 📊 Trace Table
```
i          n            diff            diff in map?         indices       action
0          2            7               ❌                   {2:0}        store 2
1          7            2               ✅                   {2:0}        return [0,1]
```
---
### 🔍 Case 2 — Answer at End

Input: nums = [3, 2, 4], target = 6
i=0, n=3
```
diff = 6-3 = 3
3 in {}? ❌
indices = {3:0}
```
i=1, n=2
```
diff = 6-2 = 4
4 in {3:0}? ❌
indices = {3:0, 2:1}
```
i=2, n=4
```
diff = 6-4 = 2
2 in {3:0, 2:1}? ✅
return [indices[2], 2] = [1, 2]
```
---
### 📊 Trace Table
```
i     n      diff            diff in map?           indices            action
0     3      3               ❌                     {3:0}              store 3
1     2      4               ❌                     {3:0, 2:1}         store 2 
2     4      2               ✅                     {3:0, 2:1}         return [1,2]
```
---
### 🔍 Case 3 — Same Number Twice

Input: nums = [3, 3], target = 6
i=0, n=3
```
diff = 6-3 = 3
3 in {}? ❌
indices = {3:0}
```
i=1, n=3
```
diff = 6-3 = 3
3 in {3:0}? ✅
return [indices[3], 1] = [0, 1] ✅
```
```
Works correctly because we check BEFORE storing — so indices[3] still points to index 0, not overwritten by index 1.
```
---
### 💡 Why Check Before Store?
```
for i, n in enumerate(nums):
    diff = target - n
    if diff in indices:      # ← check first
        return [indices[diff], i]
    indices[n] = i           # ← store after

# If we stored first:
# nums=[3,3], target=6
# i=0: store {3:0}
# i=1: n=3, diff=3
#       store {3:1}  ← overwrites!
#       3 in {3:1}? ✅ but returns [1,1] ❌ same index used twice
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Only one pass through the list; each lookup in the hash map is O(1).
- **Space**: O(n)
    - Extra space used to store up to n elements in the dictionary.

---
### 🆚 Brute Force vs HashMap
```
Approach        Time                Space            Notes
Brute Force     O(n²)               O(1)             Two nested loops
HashMap         O(n)                O(n)             ✅ One pass, optimal
```

---

## 🚀  Approach 3 : Hash Map (Two-Pass)
Intuition

The goal is to find two distinct indices whose values add up to the target.
Using a hash map (dictionary), we can store each number’s index and then check if the complement exists.

This version is a two-pass hash map approach:

Pass 1:

Build a dictionary indices where:
```python
value → index
```
Pass 2:

For each number nums[i]:
  - Compute diff = target - nums[i]
  - Check if diff exists in the dictionary AND its index is not the same as i

If yes → we found the pair.

🛠 Algorithm

1. Create an empty dictionary indices.
2. First pass through the array:
   - Store each number’s index in the dictionary.

3. Second pass through the array:
   - Compute the difference: diff = target - nums[i]
   - If diff is in the dictionary and it’s a different index, return the pair.

4. If no valid pair found, return an empty list.

---

## 💻 Code (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # maps value → index

        # First pass: store each number with its index
        for i, n in enumerate(nums):
            indices[n] = i

        # Second pass: find complement
        for i, n in enumerate(nums):
            diff = target - n  # value needed to reach target

            # Check if complement exists and is not the same index
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []  # no solution found (though problem guarantees one)


```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Two passes through the list → O(n) + O(n)
- **Space**: O(n)
    - Dictionary stores up to n key-value pairs.

