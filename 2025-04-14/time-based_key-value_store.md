# 🧮 Problem: Time-Based Key-Value Store

- **Platform**: [LeetCode](https://leetcode.com/problems/time-based-key-value-store/)
- **Submission**: [https://leetcode.com/problems/time-based-key-value-store/submissions/1479146255/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/time-based-key-value-store/submissions/1479146255/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-14
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Design a `TimeMap` class that supports the following two operations:

1. `set(key: str, value: str, timestamp: int)`: Stores the key with the given value and timestamp.
2. `get(key: str, timestamp: int)`: Returns a value such that `set` was called previously with `timestamp_prev <= timestamp`, and returns the value associated with the largest such `timestamp_prev`. If there is no such value, return `""`.


---
## Examples
```python
Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

```
---

## 🚀 My Approach
- Use a dictionary `keyStore` to map each key to a list of `[value, timestamp]` pairs.
- When inserting with `set()`, append to the list — the timestamps are guaranteed to be strictly increasing.
- Use **binary search** in `get()` to find the most recent value with `timestamp ≤ given timestamp`.

---

## 💻 Code (Python)

```python
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # Dictionary to store key-value pairs along with timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given timestamp.
        """
        if key not in self.keyStore:
            self.keyStore[key] = []  # Create a new list for the key if not present
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously,
        with timestamp_prev <= timestamp.
        If there are multiple such values, it returns the value
        associated with the largest timestamp_prev. If there are
        no values, it returns an empty string.
        """
        res, values = "", self.keyStore.get(key, [])  # Initialize result and get list of values for the key
        l, r = 0, len(values) - 1  # Initialize left and right pointers for binary search

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Update result if the timestamp is valid
                l = m + 1
            else:
                r = m - 1

        return res  # Return the final result

        

```

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
  - set() → O(1), appending to a list
  - get() → O(log n), binary search in the list of values for a key
- **Space**: O(n)
  - Where n is the number of set operations performed
