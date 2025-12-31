# 🧲 Problem: Subarray Sum Equals K

- **Platform**: [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- **Submission**: [https://leetcode.com/problems/subarray-sum-equals-k/submissions/1625197142/](https://leetcode.com/problems/subarray-sum-equals-k/submissions/1625197142/)
- **Date Solved**: 2025-05-04
- **Tags**: Array, Hash Table, Prefix Sum
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an array of integers `nums` and an integer `k`, return the **total number of subarrays whose sum equals to `k`**.
---
## 🧪 Example

```python
Input:
nums = [1, 2, 3], k = 3

Output: 2
Explanation:
  - Subarrays: [1, 2], [3]
```
---

## 🚀 Approach : 

🧠 Intuition

A brute-force approach would check all possible subarrays, but that takes O(n²) time.

To optimize, we use the Prefix Sum technique:

💡 Key Idea:

If:
```
current_sum - previous_sum = k
```

Then:
```
previous_sum = current_sum - k
```

This means:

+ If we have seen current_sum - k before,
+ Then a subarray ending at the current index sums to k.

We use a hash map to store how many times each prefix sum has appeared.

🧩 Algorithm

1. Initialize:

 + res = 0 → count of valid subarrays
 + curSum = 0 → running cumulative sum
 + prefixSum = {0: 1} → handles subarrays starting from index 0

2. Traverse through the array:

 + Add current number to curSum
 + Compute diff = curSum - k
 + If diff exists in prefixSum, add its frequency to res
 + Update prefixSum[curSum]

3. Return res

---


## 💻 Code (Python)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # Stores count of valid subarrays
        curSum = 0  # Stores the cumulative sum
        prefixSum = {0: 1}  # HashMap to store prefix sum frequencies

        for n in nums:
            curSum += n  # Add current number to cumulative sum
            diff = curSum - k  # Find difference needed to form subarray sum = k
            
            # If this difference has been seen before, add its frequency to result
            res += prefixSum.get(diff, 0)
            
            # Update the prefix sum frequency
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res  # Return total count of valid subarrays

```

---

## 🧩 Step-by-Step Code Execution

Given:
```
nums = [1, 2, 3]
k = 3
```

Output:
```
2
```
Explanation:

Subarrays with sum = 3 are:

+ [1, 2]

+ [3]
---

Initial Setup
```
res = 0                 # count of valid subarrays
curSum = 0              # running prefix sum
prefixSum = {0: 1}      # prefix sum frequency map
```
🔹 Iteration 1
```
n = 1
curSum = 0 + 1 = 1
diff = curSum - k = 1 - 3 = -2
```

+ -2 not in prefixSum → no subarray found

+ Update prefixSum:
```
prefixSum = {0: 1, 1: 1}
```
🔹 Iteration 2

```
n = 2
curSum = 1 + 2 = 3
diff = 3 - 3 = 0
```

+ 0 exists in prefixSum → count = 1
+ Add to result:
```
res = 1
```

+ Update prefixSum:
```
prefixSum = {0: 1, 1: 1, 3: 1}
```
✅ Found subarray: [1, 2]

🔹 Iteration 3
```
n = 3
curSum = 3 + 3 = 6
diff = 6 - 3 = 3
```

+ 3 exists in prefixSum → count = 1
+ Add to result:
```
res = 2
```

+ Update prefixSum:
```
prefixSum = {0: 1, 1: 1, 3: 1, 6: 1}
```

✅ Found subarray: [3]

✅ Final Output
```
return res  # 2
```
---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - Single pass through the array.
- **Space**: O(n)
   - Space for storing prefix sums in a hashmap.
