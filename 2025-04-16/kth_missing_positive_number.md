# 🧮 Problem: Kth Missing Positive Number

- **Platform**: [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/kth-missing-positive-number/submissions/1483432687/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/kth-missing-positive-number/submissions/1483432687/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Given an integer array `arr` of sorted distinct positive integers and an integer `k`, you need to find the `k`-th missing positive integer.


---
## Examples
```python
Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```
---

## 🚀 Approach : Binary Search Approach (Optimal)
#### Intuition:

We need the k-th missing positive number from a sorted array arr of positive integers.
A direct scan works, but binary search makes it O(log n).

Key observation:

For any index i in arr:
```python
missing_count = arr[i] - (i + 1)
```
This tells us how many positive numbers are missing before arr[i].

Example:
arr = [2,3,4,7,11]

At index 3 (value = 7):
```python
missing = 7 - (3 + 1) = 3
```
So missing numbers before 7 are: 1, 5, 6.

Goal:

Find the first index where missing >= k.
This means the k-th missing number lies before or at this index.

🛠 Algorithm

1. Set left = 0, right = n-1.
2. While left <= right:
   - Compute mid.
   - Compute missing numbers up to mid.

3. If missing < k, move right (increase left pointer).

4. Else move left (decrease right pointer).

5. After the loop:
   - The position is at index right
   - The k-th missing = right + k + 1

Why? Because:
   - At index right, missing numbers < k
   - We need exactly k, so we shift forward.
---

## 💻 Code (Python)

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        # Binary search to find the correct position
        while left <= right:
            mid = (left + right) // 2
            # Calculate the number of missing elements until the current index
            missing = arr[mid] - mid - 1

            if missing < k:
                left = mid + 1  # Move right to find more missing numbers
            else:
                right = mid - 1  # Move left to find fewer missing numbers

        # The kth missing number is right + k + 1
        return right + k + 1

```

---
### Setp by Step Code execution with Example
🔍 Initial Values
    - arr = [2, 3, 4, 7, 11]
    - k = 5
    - left = 0
    - right = len(arr) - 1 = 4

- We now enter the while left <= right loop.

▶️ Iteration 1
```python
mid = (left + right) // 2 = (0 + 4) // 2 = 2
arr[mid] = arr[2] = 4
missing = arr[mid] - mid - 1 = 4 - 2 - 1 = 1
```
So:
  - Missing numbers up to 4 are: [1]
  - missing = 1

Now compare:
```python
if missing < k:   # 1 < 5 → True
    left = mid + 1 = 2 + 1 = 3
```
So:

  - left = 3
  - right = 4

We move left rightward because we still need more missing numbers (we only have 1 so far, but need 5).

▶️ Iteration 2

Now:
  - left = 3
  - right = 4
```python
mid = (left + right) // 2 = (3 + 4) // 2 = 3
arr[mid] = arr[3] = 7
missing = arr[mid] - mid - 1 = 7 - 3 - 1 = 3
```
So:

  - Missing numbers up to 7 are: [1, 5, 6]
  - missing = 3

Compare:
```python
if missing < k:   # 3 < 5 → True
    left = mid + 1 = 3 + 1 = 4
```
Update:

   - left = 4
   - right = 4

Still not enough: we have 3 missing, need 5.

▶️ Iteration 3

Now:
  - left = 4
  - right = 4
```python
mid = (left + right) // 2 = (4 + 4) // 2 = 4
arr[mid] = arr[4] = 11
missing = arr[mid] - mid - 1 = 11 - 4 - 1 = 6
```
So:

  - Missing numbers up to 11 are: [1, 5, 6, 8, 9, 10]
  - missing = 6

Compare:
```python
if missing < k:   # 6 < 5 → False
else:
    right = mid - 1 = 4 - 1 = 3
```
Update:

   - left = 4
   - right = 3

Now left > right, so the loop stops.

🧩 What do left and right mean now?

At the end:

  - right = 3 → at index 3, value 7, missing = 3
  - At index 4, value 11, missing = 6

We are looking for the point where missing values cross k = 5.

  - At index 3 (value 7): 3 missing
  - At index 4 (value 11): 6 missing

So the 5th missing lies between 7 and 11.

The loop ends with:

   - right at the last index where missing < k
   - left at the first index where missing ≥ k

Here:

   - right = 3 (missing = 3 < 5)
   - left = 4 (missing = 6 ≥ 5)

🧮 Final Formula: right + k + 1

Return
```python
return right + k + 1
```

Plug in Values
```python
right = 3
k = 5

answer = 3 + 5 + 1 = 9
```
✅ Output: 9

---

## 💡 Time and Space Complexity
- **Time**: O(log n)
   - The binary search halves the search space in each iteration, making the time complexity logarithmic with respect to the size of the input array.
- **Space**: O(1)
   - The solution uses only a constant amount of extra space, as the solution operates in-place.
