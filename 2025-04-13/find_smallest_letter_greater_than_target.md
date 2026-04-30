# 🧮 Problem: Find Smallest Letter Greater Than Target

- **Platform**: [LeetCode](https://leetcode.com/problems/next-greatest-letter/)
- **Submission**: [https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1605322776/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1605322776/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-13
- **Tags**: DSA, Binary Search, Array

---

## ✅ Problem Statement
- Given a list of **sorted** characters `letters` and a **target** character `target`, return the **smallest** character in the list that is **greater than** the target. Note that the letters wrap around in a circular fashion (i.e., if the target is greater than or equal to the largest letter, the next greatest letter is the smallest letter).


---
## Examples
```python
Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"

Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

```
---

## 🚀 Approach : Binary Search
🧠 Intuition
The letters list is sorted — so binary search for the smallest letter strictly greater than target. If no such letter exists (target ≥ all letters), wrap around and return letters[0]. This is essentially finding the leftmost insertion point of target+1.
```
letters = ['c', 'f', 'j'],  target = 'd'

'd' fits between 'c' and 'f'
→ smallest letter > 'd' is 'f' ✅

target = 'j'  (equal to last element)
→ no letter > 'j' exists → wrap → return 'c' ✅
```
📌 Approach

1. Binary search with left=0, right=n-1
2. At each mid:
   + letters[mid] <= target → need something bigger → left = mid + 1
   + letters[mid] > target  → possible answer, but search left for smaller → right = mid - 1


3. After loop, left is the answer index
   + If left < len(letters) → return letters[left]
   + Else → wrap around → return letters[0]
     
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
## ▶️ Step-by-Step Execution with Example
```python
Example:

letters = ["c","f","j"]
target = "c"

Initial:
left = 0, right = 2

Step1:
mid = 1 → letters[1] = 'f'
'f' > 'c' → move right = mid - 1 = 0

Step2:
mid = 0 → letters[0] = 'c'
'c' <= 'c' → move left = mid + 1 = 1

Loop ends because left > right.

✔ Final left = 1
✔ Return letters[1] → 'f'

```
---

```python
Example (wrap-around case):
letters = ["x","x","y","y"]
target = "y"

Process:
 All elements 'x','x','y','y' are <= target ('y')
 Binary search pushes left = len(letters)
 left = 4 → out of range
 Return letters[0] → 'x'

✔ Correct due to wrap-around rule.

```
---

## 💡 Time and Space Complexity
- **Time**: O(logn),  where n is the length of letters. Binary search reduces the problem size by half at each step.
- **Space**: O(1), as no additional space is used except for the pointers.
