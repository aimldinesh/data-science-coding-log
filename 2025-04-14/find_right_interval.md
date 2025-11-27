# 🧮 Problem: Find Right Interval

- **Platform**: [LeetCode](https://leetcode.com/problems/find-right-interval/)
- **Submission**: [https://leetcode.com/problems/find-right-interval/submissions/1477590154/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-right-interval/submissions/1477590154/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-14
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- You are given a list of intervals, where each interval is represented as a pair of integers `[start, end]`. For each interval `i`, find the index of the **interval with the smallest start time** that is **greater than or equal to** `interval[i][1]`. If no such interval exists, return `-1` for that interval.

---
## Examples
```python
Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
````
---

## 🚀 My Approach
- Pair each interval with its original index.
- Sort the intervals based on their **start times**.
- For each interval in the original list:
  - Use **binary search** to find the interval with the smallest start time ≥ the current interval’s end time.
  - Return the **original index** of the found interval, or `-1` if no such interval exists.


---

## 💻 Code (Python)

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Step 1: Store intervals with their original indices
        indexed_intervals = [(interval[0], interval[1], index) for index, interval in enumerate(intervals)]
        
        # Step 2: Sort by start time
        indexed_intervals.sort(key=lambda x: x[0])
        
        result = []

        # Step 3: Binary search helper
        def binary_search(target_end):
            low, high = 0, len(indexed_intervals) - 1
            while low <= high:
                mid = (low + high) // 2
                if indexed_intervals[mid][0] >= target_end:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        # Step 4: For each original interval, find the right interval
        for interval in intervals:
            start, end = interval
            idx = binary_search(end)

            if idx < len(indexed_intervals):
                result.append(indexed_intervals[idx][2])  # Original index
            else:
                result.append(-1)  # No right interval found

        return result
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n), Sorting takes O(n log n), Each of the n binary searches takes O(log n)
- **Space**: O(n), Extra space for storing the indexed intervals and result list
