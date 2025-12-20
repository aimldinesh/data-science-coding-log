# 🧲 Problem: Remove Element

- **Platform**: [LeetCode](https://leetcode.com/problems/remove-element/description/)
- **Submission**: [https://leetcode.com/problems/remove-element/submissions/1613144650/](https://leetcode.com/problems/remove-element/submissions/1613144650/)
- **Date Solved**: 2025-04-21
- **Tags**: Array, Two Pointer, DSA
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**. The function should return the new length of the array after removal.

- Do **not** allocate extra space — modify `nums` in-place with `O(1)` extra memory.


---
## Eaxmples
```
Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
---

## 🚀 Approach: Brute Force (Using Extra Array)
🔹 Intuition

The simplest way to remove all occurrences of a given value val from the array is to:

+ Create a new temporary list
+ Copy only those elements that are not equal to val
+ Overwrite the original array with these filtered elements

This approach is straightforward and easy to understand, though it uses extra space.

🧩 Algorithm

1. Initialize an empty list temp.
2. Traverse the array nums:
   + If the current element is equal to val, skip it.
   + Otherwise, append it to temp.
     
3. Copy elements from temp back into nums (in-place update).
4. Return the length of temp (number of elements not equal to val).
---

## 💻 Code (Python)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Step 1: Create a temporary list to store elements != val
        temp = []

        # Step 2: Traverse original array
        for num in nums:
            # Skip elements equal to val
            if num == val:
                continue
            # Keep valid elements
            temp.append(num)

        # Step 3: Copy filtered elements back to nums
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Step 4: Return new length of the array
        return len(temp)

```

---
### ▶️ Step-by-Step Execution (Example)
```python
Input:
nums = [3, 2, 2, 3], val = 3
```
▶️ Step-by-Step Execution (Example)
```python
Input:
nums = [3, 2, 2, 3], val = 3
```
Step 1: Filtering
```python
temp = []
num = 3 → skip
num = 2 → temp = [2]
num = 2 → temp = [2, 2]
num = 3 → skip
```
Step 2: Copy back to nums
```python
nums = [2, 2, _, _]
```
Output
```
Return: 2
nums becomes [2, 2, _, _]
```
---

## 💡 Time and Space Complexity
- **Time**: O(n), one pass to filter, another to copy back.
- **Space**: O(n), due to the use of extra temporary list.

---
## 🚀 Approach: Two-Pointer (Optimal, In-Place)
🔹 Intuition

We want to remove all occurrences of val in-place and return the number of remaining elements.

Instead of using extra space, we:

+ Maintain a pointer k that marks the position where the next valid (non-val) element should go.
+ Traverse the array with another pointer i.
+ Every time we see a value that is not equal to val, we place it at index k and move k forward.

This ensures:

+ All non-val elements are shifted to the front.
+ The order of elements is preserved.
+ The operation is done in O(1) extra space.

🛠 Algorithm

1. Initialize k = 0.
2. Traverse the array using index i from 0 to n-1.
3. If nums[i] != val:
   + Assign nums[k] = nums[i].
   + Increment k.
     
4. After traversal, k represents the number of elements not equal to val.
5. Return k.

---

## 💻 Code (Python)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k points to the index where the next non-val element should be placed
        k = 0
        
        # Traverse the array
        for i in range(len(nums)):
            # If current element is not equal to val
            if nums[i] != val:
                # Place it at index k
                nums[k] = nums[i]
                # Move k forward
                k += 1

        # k is the new length of the array after removing val
        return k


```

---
### ▶️ Step-by-Step Execution (Example)
```python
Input:
nums = [3, 2, 2, 3], val = 3
```
| i | nums[i] | Action    | nums (partial) | k |
| - | ------- | --------- | -------------- | - |
| 0 | 3       | skip      | [3,2,2,3]      | 0 |
| 1 | 2       | nums[0]=2 | [2,2,2,3]      | 1 |
| 2 | 2       | nums[1]=2 | [2,2,2,3]      | 2 |
| 3 | 3       | skip      | [2,2,2,3]      | 2 |

Output:
```
Return: 2
nums = [2, 2, _, _]
```
---

## 💡 Time and Space Complexity
- **Time**: O(n), single pass through the array.
- **Space**: O(1), in-place operation with no extra space used.

---
## 📌 Why This Is Optimal

+ ✔ In-place
+ ✔ Preserves order
+ ✔ Linear time
+ ✔ Constant space
