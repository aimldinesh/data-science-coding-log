# 🧮 Problem: Snapshot Array

- **Platform**: [LeetCode](https://leetcode.com/problems/snapshot-array/)
- **Submission**: [https://leetcode.com/problems/snapshot-array/submissions/1479156798/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/snapshot-array/submissions/1479156798/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-14
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- Implement a `SnapshotArray` class with the following operations:

  - `set(index, val)`: Sets the element at the given index to `val`.
  - `snap()`: Takes a snapshot and returns the `snap_id`.
  - `get(index, snap_id)`: Returns the value at the index at the time of the given `snap_id`.


---

## Examples
```python
Example 1:
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```
---

## 🚀 My Approach
1. **Data Structure**:
   - Maintain an array of lists. Each list stores `(snap_id, value)` pairs for each index.
   - This allows us to store only updates, not full snapshots.

2. **Setting a value**:
   - When `set(index, val)` is called, we append the current `snap_id` and value to the list at that index.

3. **Taking a snapshot**:
   - Simply increment the global `snap_id` counter and return the previous value. No need to copy the whole array.

4. **Getting a value**:
   - To find the correct value for a given `snap_id`, we perform **binary search** on the list of versions for that index to find the **most recent snapshot** less than or equal to the given `snap_id`.


---

## 💻 Code (Python)

```python
class SnapshotArray:

    def __init__(self, length: int):
        # Initialize the array to hold a list of (snap_id, value) tuples for each index
        self.array = [[(0, 0)] for _ in range(length)]  # Initialize with (snap_id=0, value=0) for each element
        self.snap_id = 0  # Start with snap_id 0
        
    def set(self, index: int, val: int) -> None:
        # Append the (snap_id, value) tuple to the list at the given index
        self.array[index].append((self.snap_id, val))
        
    def snap(self) -> int:
        # Increment the snap_id and return the new snap_id
        self.snap_id += 1
        return self.snap_id - 1  # Return the snap_id before incrementing

    def get(self, index: int, snap_id: int) -> int:
        # Perform binary search to find the most recent value at or before the snap_id
        history = self.array[index]
        left, right = 0, len(history) - 1

        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1  # Adjust the range based on snap_id comparison

        # Return the value corresponding to the closest snap_id <= the requested snap_id
        return history[right][1]


```

---

## 💡 Time and Space Complexity
- **Time**:
  - set() → O(1)
  - snap() → O(1)
  - get() → O(log k), where k is the number of versions at that index
- **Space**: O(n + m)
  - Where n = number of indices,
  - m = total number of set calls (each call appends a new version)
