# 🧲 Problem: Time Based Key-Value Store

- **Platform**: [LeetCode](https://leetcode.com/problems/time-based-key-value-store/description/)
- **Submission**: [https://leetcode.com/problems/time-based-key-value-store/submissions/1662086389/](https://leetcode.com/problems/time-based-key-value-store/submissions/1662086389/)
- **Date Solved**: 2025-06-12
- **Tags**: Array, Binary Search
- **Difficulty**: Medium

---

## ✅ Problem Statement
Design a data structure that stores key-value pairs with a timestamp, and allows querying the most recent value for a key at or before a given timestamp.
### 🧾 Operations
- set(key: str, value: str, timestamp: int)
- Stores the key with the given value and timestamp.

- get(key: str, timestamp: int) -> str
- Returns a value such that set(key, value, timestamp_prev) was called previously with timestamp_prev <= timestamp.
- If there are multiple such values, return the one with the largest timestamp_prev.
- If none, return "".

### 🌰 Examples
```python
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output:
[None, None, "bar", "bar", None, "bar2", "bar2"]
```
---

## 🚀 Approach : Binary Search
💡 Intuition
- Store values and their timestamps for each key in a dictionary.
- Since timestamps are strictly increasing, we can binary search over them in get() to find the latest timestamp ≤ given timestamp.

🚀 Approach
- Use a dictionary keyStore:
     - Each key maps to a list of [value, timestamp] pairs.
- set() appends values in sorted timestamp order.
- get() uses binary search to find the rightmost timestamp ≤ target.

---

## 💻 Code (Python)

```python
class TimeMap:
    def __init__(self):
        self.keyStore = {}  # Maps key -> list of [value, timestamp] pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])  # Append value with timestamp

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])  # Get list for the key

        # Binary search for timestamp <= target
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Candidate result
                l = m + 1  # Search right for larger valid timestamp
            else:
                r = m - 1

        return res

```
---
### 🧮 Step-by-Step Example
```python
TimeMap.set("foo", "bar", 1)
# keyStore = {"foo": [["bar", 1]]}

TimeMap.get("foo", 1)
# Only one value with timestamp 1 -> return "bar"

TimeMap.get("foo", 3)
# 1 <= 3 => return "bar"

TimeMap.set("foo", "bar2", 4)
# keyStore = {"foo": [["bar", 1], ["bar2", 4]]}

TimeMap.get("foo", 4)
# Binary search -> return "bar2"

TimeMap.get("foo", 5)
# 4 <= 5 -> return "bar2"
```
---

## 💡 Time and Space Complexity
- **Time**: O(n log n)
- **Space**: O(n)
