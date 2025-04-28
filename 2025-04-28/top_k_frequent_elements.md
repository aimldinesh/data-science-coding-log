# 🧲 Problem: Top K Frequent Elements

- **Platform**: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
- **Submission**: [https://leetcode.com/problems/top-k-frequent-elements/submissions/1620179770/](https://leetcode.com/problems/top-k-frequent-elements/submissions/1620179770/)
- **Date Solved**: 2025-04-28
- **Tags**: Hash Table, Bucket Sort, Heap (Priority Queue)
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
  - Input: nums = [1,1,1,2,2,3], k = 2
  - Output: [1,2]
Example 2:
  - Input: nums = [1], k = 1
  - Output: [1]

---

## 🚀 Approach
 - Use a hashmap (count) to store the frequency of each element.
 - Use a bucket sort idea:
    - Create a list of empty lists freq, where freq[i] holds numbers that appear exactly i times.

 - Traverse count and populate freq.
 - Then traverse freq from the highest possible frequency down to the lowest:
    - Add elements to the result until we have collected k elements.


---

## 💻 Code (Python)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # Dictionary to store the frequency of each element
        freq = [[] for _ in range(len(nums) + 1)]  # Bucket array: index represents frequency

        # Step 1: Count the frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Place numbers into the bucket according to their frequency
        for n, c in count.items():
            freq[c].append(n)

        res = []  # List to store the top k frequent elements

        # Step 3: Traverse the bucket from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)  # Add the number to result
                if len(res) == k:
                    return res  # Return as soon as we have k elements

```

---

## 💡 Time and Space Complexity
- **Time**: O(n), where n = length of nums
   - Counting frequencies takes O(n)
   - Bucket filling and final traversal also take O(n)
- **Space**: O(n)
   - Space used by count and freq arrays.
