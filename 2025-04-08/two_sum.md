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
- Input: nums = [2, 7, 11, 15], target = 9  
- Output: [0, 1]
- Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
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

🧠 Approach (Optimized - One Pass Hash Map):
- Create an empty dictionary called indices to store the number and its index.
- Loop through the array nums using enumerate to get both index and number.
- For each number n, calculate the complement as target - n.
- Check if the complement is already in the dictionary:
      - If yes, return the indices of the complement and current number.
      - If no, store n with its index in the dictionary.

- If no such pair is found (though problem guarantees one), return an empty list.


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
### Step by step code execution
```python
Input: nums = [3, 2, 4], target = 6  
Output: [1, 2]

Step-by-step:
- i=0, n=3 → target-n=3 → not in dict → add 3:0
- i=1, n=2 → target-n=4 → not in dict → add 2:1
- i=2, n=4 → target-n=2 → found in dict → return [1, 2]

```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Only one pass through the list; each lookup in the hash map is O(1).
- **Space**: O(n)
    - Extra space used to store up to n elements in the dictionary.

