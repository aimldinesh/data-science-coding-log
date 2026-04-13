# 🧮 Problem: Single Element in a Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/1609274051/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/1609274051/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- You're given a **sorted** array where every element appears exactly **twice**, except for one element which appears **only once**.Find that single element in `O(log n)` time and `O(1)` space.

---
## Examples
```python
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```
---

## 🚀 My Approach: Binary Search
We use Binary Search to efficiently locate the unique element:
### 🔸 Observations:
- The array is sorted.
- Pairs of identical elements are adjacent (like [1,1,2,2,3,3,...]).
- Before the single element, the first instance of a pair is at an **even** index, and the second at an **odd** index.
- After the single element, this pattern **breaks**.

### 🔸 Steps:
1. Initialize two pointers: `left = 0`, `right = len(nums) - 1`
2. Run a binary search while `left < right`:
   - Compute `mid = (left + right) // 2`
   - Check if `mid` is even or odd.
   - If `mid` is even:
     - If `nums[mid] == nums[mid + 1]`: the unique element is on the **right**
     - Else: it’s on the **left**
   - If `mid` is odd:
     - If `nums[mid] == nums[mid - 1]`: move to the **right**
     - Else: move to the **left**
3. When `left == right`, return `nums[left]`


---

## 💻 Code (Python)

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # Ensure mid is even to make comparisons easier
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left]
```

---
### 🔍 Step-by-Step Execution

Input: nums = [1, 1, 2, 3, 3, 4, 4, 5, 5] → n=9
```
Indices:  0  1  2  3  4  5  6  7  8
Values:   1  1  2  3  3  4  4  5  5
                ↑ single element
```

Iteration 1
```
left=0, right=8
mid = (0+8)//2 = 4  → even ✅
nums[4]=3 == nums[5]=4? ❌
→ right = mid = 4
```
Iteration 2
```
left=0, right=4
mid = (0+4)//2 = 2  → even ✅
nums[2]=2 == nums[3]=3? ❌
→ right = mid = 2
```
Iteration 3
```
left=0, right=2
mid = (0+2)//2 = 1  → odd ❌
nums[1]=1 == nums[0]=1? ✅
→ left = mid + 1 = 2
```
Loop ends: left=2 == right=2
```
return nums[2] = 2 ✅
```
💡 Why Force Even Mid?
```
Before single:   pairs at (even, odd)  →  nums[even] == nums[even+1]
After single:    pairs at (odd, even)  →  nums[odd]  == nums[odd-1]

So always check from the EVEN index of each pair:
  mid even → compare with mid+1
  mid odd  → compare with mid-1  (shift back to even)
```
```
[1, 1, 2, 3, 3, 4, 4, 5, 5]
  ↑___↑  ↑  ↑___↑  ↑___↑  ↑___↑
 pair  single  pair    pair    pair
 (0,1)  [2]   (3,4)  (5,6)  (7,8)
```
✅ Final Answer
```
return nums[2] = 2
```
---

## 💡 Time and Space Complexity
- **Time**: O(log n), Binary search halves the search space each iteration
- **Space**: O(1), Only pointers used, no extra data structures
---

💡 Interview tip: 
+ The key insight examiners look for is why you force mid to even. Saying "pairs break their even-odd alignment after the single element, so I normalise mid to always inspect from the even side of a pair" is what earns full marks.
