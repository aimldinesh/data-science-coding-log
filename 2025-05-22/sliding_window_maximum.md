# 🧲 Problem: Sliding Window Maximum

- **Platform**: [LeetCode](https://leetcode.com/problems/sliding-window-maximum/description/)
- **Submission**: [https://leetcode.com/problems/sliding-window-maximum/submissions/1641261983/](https://leetcode.com/problems/sliding-window-maximum/submissions/1641261983/)
- **Date Solved**: 2025-05-22
- **Tags**: Array, Heap, Sliding Window, Monotonic Queue, Deque
- **Difficulty**: Hard

---

## ✅ Problem Statement
You are given an integer array `nums`, and an integer `k`.

Return the **maximum value in each sliding window of size `k`** as it moves from left to right across the array.

---

### 🔍 Examples

```python
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [3,3,5,5,6,7]

Explanation:
Window positions:
[1 3 -1] -3  5  3  6  7 → max = 3  
 1 [3 -1 -3] 5  3  6  7 → max = 3  
 1  3 [-1 -3 5] 3  6  7 → max = 5  
 1  3 -1 [-3 5 3] 6  7 → max = 5  
 1  3 -1 -3 [5 3 6] 7 → max = 6  
 1  3 -1 -3  5 [3 6 7] → max = 7  

```

---

## 🚀 Approach : Monotonic Queue (Deque)
🧠 Intuition:
- We use a deque to keep track of indices of useful elements in decreasing order (i.e., the front always has the index of the current window's maximum).

🔸 Steps:
- Initialize a deque q and an output list output.
- Use two pointers l and r to represent the sliding window.
- For each r:
    - Remove elements from back of q while nums[q[-1]] < nums[r] (they can't be max anymore).
    - Add r to q.
    - If q[0] (front) is outside the window (< l), pop it from front.
    - If window size is at least k, append nums[q[0]] (current max) to result and increment l.


---

## 💻 Code (Python)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []          # Stores the result: max elements of each window
        q = deque()          # Will store indices of elements in decreasing order
        l = r = 0            # Left and right pointers of the window

        while r < len(nums):
            # Remove all elements smaller than the current from the back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index to deque
            q.append(r)

            # Remove elements from the front if they are outside the window
            if l > q[0]:
                q.popleft()

            # When we have a valid window (size k), record the max (which is at front of deque)
            if (r - l + 1) >= k:
                output.append(nums[q[0]])  # q[0] is index of max element
                l += 1  # Shrink window from the left

            # Always move right pointer
            r += 1

        return output

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Each element is added and removed from deque at most once.
- **Space**: O(k)
    - Deque stores at most k indices at a time.
