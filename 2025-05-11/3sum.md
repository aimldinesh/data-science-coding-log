# 🧲 Problem: 3Sum

- **Platform**: [LeetCode](https://leetcode.com/problems/3sum/description/)
- **Submission**: [https://leetcode.com/problems/3sum/submissions/1488602791/](https://leetcode.com/problems/3sum/submissions/1488602791/)
- **Date Solved**: 2025-05-11
- **Tags**: Array, Two Pointer, Sorting
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] such that:
   - i != j, j != k, and i != k
   - nums[i] + nums[j] + nums[k] == 0
- The solution set must not contain duplicate triplets.

---

## 🧠 Intuition
- We need to find three numbers that sum up to 0.
- To make it efficient, we can:
    - Sort the array.
    - Fix one element, and then use the two-pointer technique to find the other two elements.
- Skipping duplicate values ensures that we only return unique triplets.

---

## 🚀 Approach
Step 1: Sort the Array
   - Sorting helps us use two pointers and avoid duplicates efficiently.
Step 2: Iterate with a Fixed Element
   - Use a loop to fix the first element of the triplet.
   - For each fixed element, use two pointers (left and right) to find pairs that sum to -nums[i].
Step 3: Skip Duplicates
   - Skip duplicate values for the fixed element and for left/right pointers to ensure uniqueness.


---

## 💻 Code (Python)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()  # Sort the array to apply the two-pointer approach
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Define the two pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Triplet found
                    result.append([nums[i], nums[left], nums[right]])

                    # Move pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after processing
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # Need a larger sum, move the left pointer
                    left += 1
                else:
                    # Need a smaller sum, move the right pointer
                    right -= 1

        return result
```

---

## 💡 Time and Space Complexity
- **Time**: O(n ^2)
   - Sorting takes O(n log n).
   - The nested loop (with two pointers) takes O(n²) in the worst case.
- **Space**: O(1)
   - Sorting is done in-place, no additional data structures used.
