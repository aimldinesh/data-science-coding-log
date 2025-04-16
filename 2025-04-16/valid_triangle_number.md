# 🧮 Problem: Valid Triangle Number

- **Platform**: [LeetCode](https://leetcode.com/problems/valid-triangle-number/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/valid-triangle-number/submissions/1484489984/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/valid-triangle-number/submissions/1484489984/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

---

## 🚀 My Approach
We solve this problem using the **Two-Pointer Technique** after sorting the array.

1. **Sort the Array:**
We sort the array to simplify checking the triangle inequality condition.

2. **Fix the Largest Side:**
We fix one side of the triangle (say `nums[i]`) starting from the end of the array. For each such `i`, we try to find two other numbers `nums[left]` and `nums[right]` such that:

```python
nums[left] + nums[right] > nums[i]

This ensures the triangle inequality holds.

3. Two-Pointer Search:
- Initialize two pointers: left = 0, right = i - 1

- If nums[left] + nums[right] > nums[i], then all elements between left and right form valid triangles with nums[i]. So, we add right - left to our count and move the right pointer left.Otherwise, we move the left pointer to the right to find a larger side.

4. Repeat Until All Elements Checked:
- We iterate this way for all elements from n-1 to 2 as the largest side and count all valid triangles.


---

## 💻 Code (Python)

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Get the length of the input array
        n = len(nums)

        # Sort the array to simplify the triangle inequality checks
        nums.sort()

        # Initialize a counter to store the number of valid triangles
        count = 0

        # Iterate from the last element to the third element (nums[i] as the largest side)
        for i in range(n - 1, 1, -1):
            left = 0  # Initialize left pointer at the beginning of the array
            right = i - 1  # Initialize right pointer just before nums[i]

            # Use the two-pointer technique to find valid pairs
            while left < right:
                # Check if the sum of nums[left] and nums[right] satisfies the triangle condition
                if nums[left] + nums[right] > nums[i]:
                    # If valid, all pairs between left and right are valid
                    count += (right - left)
                    right -= 1  # Move the right pointer to the left
                else:
                    left += 1  # Otherwise, move the left pointer to the right

        # Return the total count of valid triangles
        return count
              

```

---

## 💡 Time and Space Complexity
- **Time**: Sorting takes O(n log n) and the two-pointer loop takes O(n^2) in worst case.So total: O(n^2)
- **Space**:Only a few pointers and a counter are used, so O(1)
