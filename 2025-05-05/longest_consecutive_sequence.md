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
