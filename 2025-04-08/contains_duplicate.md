# 🧮 Problem: Contains Duplicate

- **Platform**: [LeetCode](https://leetcode.com/problems/contains-duplicate/)
- **Submission**: [https://leetcode.com/problems/contains-duplicate/submissions/1586471444/](https://leetcode.com/problems/contains-duplicate/submissions/1586471444/)
- **Date Solved**: 2025-04-08
- **Tags**: DSA, Array, HashSet, Sorting, Duplicate

---

## ✅ Problem Statement
- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### 🌰 Example:
```python
Input: nums = [1,2,3,1]
Output: True

Input: nums = [1,2,3,4]
Output: False

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
```
---

## 🚀 Approach 1: Brute Force
💡 Intuition:
- We want to check if there are any duplicates in the list.
- A brute-force way is to compare every pair of elements and check if any are the same.

🧠 Approach:
- Use two nested loops:
     - Outer loop goes from 0 to n-1.
     - Inner loop checks all elements after the current element.
- If any pair nums[i] == nums[j], return True.
- If no duplicates are found after all checks, return False.

---

## 💻 Code (Python)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Loop through each element in the list
        for i in range(len(nums)):
            # Compare the current element with all elements that come after it
            for j in range(i + 1, len(nums)):
                # If a duplicate is found, return True
                if nums[i] == nums[j]:
                    return True
        # If no duplicates are found after checking all pairs, return False
        return False

```

---

## 💡 Time and Space Complexity
- **Time**: O(n^2)
    - Nested loops compare every pair in the list.
- **Space**: O(1)
    - No extra space is used apart from a few variables.
---

## 🚀 Approach 2: Set (Efficient Time)
💡 Intuition:
- We need to find whether any number appears more than once in the array.
- If we can keep track of all the numbers we've seen so far using a set, then:
     - If a number already exists in the set, it's a duplicate.
     - If not, we add it to the set.

🧠 Approach :
- Initialize an empty set seen.
- Iterate through each number in nums.
- If the number is already in seen, return True (duplicate found).
- Otherwise, add the number to the set.
- If the loop finishes, return False (no duplicates found).

---

## 💻 Code (Python)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Initialize an empty set to store unique elements
        
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        
        return False  # No duplicates found
```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - We iterate through the list once and perform constant-time set operations (in and add) for each element.
- **Space**: O(n)
    - In the worst case (no duplicates), we store all n elements in the seen set.

---

## 🚀 Approach 3: Sorting (Efficient Space)
💡 Intuition:
If we sort the array, any duplicates will be next to each other.
So we just need to compare adjacent elements.

🧠 Approach :
- Sort the array nums.
- Iterate from index 1 to len(nums) - 1.
- If nums[i] == nums[i-1], return True (duplicate found).
- If no duplicates are found in the loop, return False.

## 💻 Code (Python)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the array
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Check adjacent elements
                return True
        return False  # No duplicates found

```

---

## 💡 Time and Space Complexity
- **Time**: O(nlogn)
- **Space**: O(1) or O(n) (depends on sorting implementation)

---
