# 🧲 Problem: Contains Duplicate II

- **Platform**: [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/description/)
- **Submission**: [https://leetcode.com/problems/contains-duplicate-ii/submissions/1635554373/](https://leetcode.com/problems/contains-duplicate-ii/submissions/1635554373/)
- **Date Solved**: 2025-05-16
- **Tags**: Array, Hash Table, Sliding Window
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that:
   - nums[i] == nums[j]
   - and abs(i - j) <= k
### 🔍 Examples
```python
Example 1
Input:nums = [1, 2, 3, 1], k = 3
Output: True
Explanation: nums[0] == nums[3] and abs(0 - 3) = 3 <= 3

Example 2
Input:nums = [1, 0, 1, 1], k = 1
Output: True
Explanation: nums[2] == nums[3] and abs(2 - 3) = 1

Example 3
Input:nums = [1, 2, 3, 1, 2, 3], k = 2
Output: False
```
---

## 🚀 Approach 1 : Brute Force
🔸 Steps:
- Loop over each element as the first pointer L.
- For each L, check the next k elements (R) to see if any match nums[L].
- If any match is found, return True.
- If no matches found after checking all, return False.
---

## 💻 Code (Python)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Outer loop over every element (index L)
        for L in range(len(nums)):
            # Inner loop checks next k elements (within index difference ≤ k)
            for R in range(L + 1, min(len(nums), L + k + 1)):
                # If we find any two equal elements within distance k
                if nums[L] == nums[R]:
                    return True  # Found a duplicate within k distance
        return False  # No such pair found

```

---

## 💡 Time and Space Complexity
- **Time**: O(n × k)
    - For each of the n elements, we check up to k elements ahead.
- **Space**: O(1)
    - No extra space used.

---

## 🚀 Approach 2 : Sliding Window + HashSet (Optimized)
🔸 Steps:
- Use a sliding window of size at most k.
- For each number, check if it’s already in the window set:
   - If yes → return True.
   - If no → add it to the set.
- Remove the oldest element if window size exceeds k.

---

## 💻 Code (Python)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Set to hold elements in the current window
        L = 0  # Left pointer of the sliding window

        for R in range(len(nums)):  # R is the right pointer
            # Maintain window size <= k
            if R - L > k:
                window.remove(nums[L])  # Remove the element at the left end
                L += 1

            # If current number is already in the window, we found a duplicate
            if nums[R] in window:
                return True

            # Add the current number to the window
            window.add(nums[R])

        return False  # No duplicates found within distance k

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - The loop runs once for each element: n times.
   - Each add, remove, and in check on a set is O(1) on average.
   - So all operations inside the loop are constant time.
- **Space**: O(k)
   - The set window only holds at most k + 1 elements.
   - So in the worst case, the space used by the set is O(k).
