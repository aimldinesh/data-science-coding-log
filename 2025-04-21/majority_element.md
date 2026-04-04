# 🧲 Problem: Majority Element

- **Platform**: [LeetCode](https://leetcode.com/problems/majority-element/description/)
- **Submission**: [https://leetcode.com/problems/majority-element/submissions/1613222218/](https://leetcode.com/problems/majority-element/submissions/1613222218/)
- **Date Solved**: 2025-04-21
- **Tags**: Array, HashMap, Sorting, Boyer-Moore
- **Difficulty**: Easy

---

## ✅ Problem Statement
- Given an array `nums` of size `n`, return the **majority element**.The majority element is the element that appears more than ⌊n / 2⌋ times. It is guaranteed that the majority element always exists in the array.


---
## Examples
```python
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```
---

## 🚀 Approach 1 : Brute Force
### 💡 Intuition:
- For each element in the array, count how many times it appears. If its count exceeds `n // 2`, it is the majority element.

---

## 💻 Code (Python)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute Force
        n = len(nums)
        
        for i in range(n):
            count = 0
            # Count occurrences of nums[i]
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            # If count of current element > n // 2, it's the majority
            if count > n // 2:
                return nums[i]

```

---

## 💡 Time and Space Complexity
- **Time**: O(n^2)
- **Space**: O(1)

---

## 🚀 Approach 2 : Hash Map (Dictionary)
🧠 Intuition
+ Use a HashMap to count every element's frequency in one pass. While counting, track the running maximum — so by the time the loop ends, res already holds the majority element. No second pass needed.

📌 Approach

1. Initialize count = {}, res = 0, maxCount = 0
2. For each number n in nums:
   + Increment count[n]
   + If count[n] > maxCount → update res = n and maxCount = count[n]
   + 
3. Return res

---

## 💻 Code (Python)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash Map to store the count of each number
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            # Increase the count of the current number n
            count[n] = 1 + count.get(n, 0)

            # If this number's count is greater than the maxCount seen so far
            if count[n] > maxCount:
                res = n  # Update result to current number
                maxCount = count[n]  # Update maxCount

        # Return the number with the highest count (majority element)
        return res
  
```

---

### 🔍 Step-by-Step Execution

Input: nums = [2, 2, 1, 1, 2] → threshold = 5 // 2 = 2

n=2
```
count = {2: 1}
count[2]=1 > maxCount=0 ✅
res=2, maxCount=1
```
n=2
```
count = {2: 2}
count[2]=2 > maxCount=1 ✅
res=2, maxCount=2
```
n=1
```
count = {2:2, 1:1}
count[1]=1 > maxCount=2 ❌
res=2, maxCount=2
```
n=1
```
count = {2:2, 1:2}
count[1]=2 > maxCount=2 ❌
res=2, maxCount=2
```
n=2
```
count = {2:3, 1:2}
count[2]=3 > maxCount=2 ✅
res=2, maxCount=3
```
📊 Trace Table
```
n          count         count[n] > maxCount?            res        maxCount 
2          {2:1}         ✅ 1 > 0                        2           1 
2          {2:2}         ✅ 2 > 1                        2           2 
1          {2:2, 1:1}    ❌ 1 > 2                        2           2 
1          {2:2, 1:2}    ❌ 2 > 2                        2           2 
2          {2:3, 1:2}    ✅ 3 > 2                        2           3
```
✅ Final Answer
```
return res = 2
```
### 💡 Key Detail — count.get(n, 0)

count[n] = 1 + count.get(n, 0)
#                        ↑
#               returns 0 if key doesn't exist
#               avoids KeyError on first occurrence

---


## 💡 Time and Space Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## 🚀 Approach 3 : Sorting
### 💡 Intuition:
- If the array is sorted, the majority element (which appears more than ⌊n/2⌋ times) will always occupy the middle position.

---

## 💻 Code (Python)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```

---

## 💡 Time and Space Complexity
- **Time**: O(n log n), due to sorting
- **Space**: O(1), if in-place sorting is allowed (otherwise O(n) depending on sorting method)

---

## 🚀 Approach 4 : Efficient: Boyer-Moore Voting Algorithm
### 💡 Intuition:
- If there is a majority element (appears more than ⌊n/2⌋ times), we can track a **res** and a **count**. If we see the res, we increment count. Otherwise, we decrement. When the count hits zero, we choose a new res. In the end, the majority element will remain.

---

## 💻 Code (Python)

```python
lass Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Efficient Approach: Boyer-Moore Voting Algorithm
        
        res, count = 0, 0  # Initialize res and count
        
        for n in nums:
            if count == 0:
                # If count is 0, we choose the current element as the new res
                res = n
            # If current element equals res, increment count
            # Otherwise, decrement count
            count += (1 if n == res else -1)

        # The res will be the majority element
        return res     
```

---

## 💡 Time and Space Complexity
- **Time**: O(n), one pass through the array
- **Space**: O(1), constant space used regardless of input size
