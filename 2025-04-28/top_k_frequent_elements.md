# 🧲 Problem: Top K Frequent Elements

- **Platform**: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
- **Submission**: [https://leetcode.com/problems/top-k-frequent-elements/submissions/1620179770/](https://leetcode.com/problems/top-k-frequent-elements/submissions/1620179770/)
- **Date Solved**: 2025-04-28
- **Tags**: Hash Table, Bucket Sort, Heap (Priority Queue)
- **Difficulty**: Medium

---

## ✅ Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.  
You may return the answer in **any order**.

**Example 1**:
- Input: `nums = [1,1,1,2,2,3]`, `k = 2`
- Output: `[1,2]`

**Example 2**:
- Input: `nums = [1]`, `k = 1`
- Output: `[1]`

---

## 🚀 Approach
 - Use a **hashmap** (`count`) to store the frequency of each element.
- Use a **bucket sort** idea:
  - Create a list of empty lists `freq`, where `freq[i]` holds numbers that appear exactly `i` times.
- Traverse `count` and populate `freq`.
- Then traverse `freq` from the **highest frequency to the lowest**:
  - Keep adding elements to the result until we have collected `k` elements.

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

---

## 📝 Approach — Sorting by Frequency

1. **Count Frequencies**
   - Traverse the `nums` list.
   - Use a dictionary (`freq`) to store each unique number as a key and its frequency as the value.
   - Example:  
     ```
     nums = [1, 1, 1, 2, 2, 3]
     freq = {1: 3, 2: 2, 3: 1}
     ```

2. **Sort by Frequency**
   - Convert the dictionary into a list of `(number, frequency)` tuples using `.items()`.
   - Sort this list by frequency **in descending order**:
     ```python
     sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
     ```

3. **Pick Top K Elements**
   - Take the first `k` elements from the sorted list:  
     ```python
     sorted_items[:k]
     ```
   - Extract only the numbers (keys) from these tuples using list comprehension:
     ```python
     top_k_keys = [key for key, value in sorted_items[:k]]
     ```

4. **Return Result**
   - Return the list of `k` most frequent elements.

---

## 💻 Code (Python)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the frequency of each element
        freq = {}
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1
        
        # Sort the dictionary items based on the frequency in descending order
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Extract the top k keys
        top_k_keys = [key for key, value in sorted_items[:k]]
        return top_k_keys
```
---
## 🧠 Example Walkthrough
```python
Input:
nums = [1,1,2,2,2,3], k = 2

Step 1 → Frequency Dictionary:
freq = {1: 2, 2: 3, 3: 1}

Step 2 → Sorted by frequency:
sorted_items = [(2,3), (1,2), (3,1)]

Step 3 → Take top k=2:
top_k_keys = [2, 1]

✅ Output: [2, 1]
```
---

### ⏳ Complexity Analysis
- **Time Complexity**:  
  - Counting frequencies → **O(n)**  
  - Sorting by frequency → **O(m log m)** where `m` = number of unique elements.  
  - **Total**: **O(n + m log m)**
- **Space Complexity**: **O(m)** for storing frequency counts.

