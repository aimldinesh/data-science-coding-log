# 🧮 Problem: Single Element in a Sorted Array

- **Platform**: [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/1609274051/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/1609274051/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA

---

## ✅ Problem Statement
- You're given a **sorted** array where every element appears exactly **twice**, except for one element which appears **only once**.Find that single element in `O(log n)` time and `O(1)` space.

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

## 💡 Time and Space Complexity
- **Time**: O(log n), Standard binary search time.
- **Space**: O(1), No extra space used.
