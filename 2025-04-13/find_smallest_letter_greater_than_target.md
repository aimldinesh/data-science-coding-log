# 🧮 Problem: Find Smallest Letter Greater Than Target

- **Platform**: [LeetCode](https://leetcode.com/problems/next-greatest-letter/)
- **Submission**: [https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1605322776/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1605322776/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: DSA, Binary Search, Array

---

## ✅ Problem Statement
- Given a list of **sorted** characters `letters` and a **target** character `target`, return the **smallest** character in the list that is **greater than** the target. Note that the letters wrap around in a circular fashion (i.e., if the target is greater than or equal to the largest letter, the next greatest letter is the smallest letter).


---

## 🚀 My Approach
- **Binary Search**: Since the list is sorted, we can use binary search to efficiently find the next greatest letter.
- The `left` pointer moves towards the right if the middle letter is less than or equal to the target.
- The `right` pointer moves to the left if the middle letter is greater than the target.
- After the search loop, `left` will point to the smallest letter greater than the target.
- If `left` exceeds the array length, we return the first letter (circular).
---

## 💻 Code (Python)

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # Initialize two pointers for binary search
        left, right = 0, len(letters) - 1

        # Perform binary search to find the desired letter
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # If the middle letter is less than or equal to the target,
            # move the left pointer to search in the right half
            if letters[mid] <= target:
                left = mid + 1
            else:
                # Otherwise, move the right pointer to search in the left half
                right = mid - 1

        # After the loop, `left` points to the smallest letter greater than the target.
        # If `left` exceeds the array length, return the first letter (circular array).
        return letters[left] if left < len(letters) else letters[0]

```

---

## 💡 Time and Space Complexity
- **Time**: O(logn),  where n is the length of letters. Binary search reduces the problem size by half at each step.
- **Space**: O(1), as no additional space is used except for the pointers.
