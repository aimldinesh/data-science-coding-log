# 🧮 Problem: Successful Pairs of Spells and Potions

- **Platform**: [LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/successful-pairs-of-spells-and-potions/submissions/1484515870/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/submissions/1484515870/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-16
- **Tags**: Array, Binary Search, DSA

---

## ✅ Problem Statement
- You're given two arrays `spells` and `potions`, representing the strength of spells and potions respectively.You're also given an integer `success`, and your task is to count for each spell how many potions form **successful pairs**.

- A pair is successful if:  
  - `spell[i] * potion[j] >= success`

---

## 🚀 My Approach
We solve this efficiently using **Binary Search**:

### 1. Sort the Potions Array:
Since we need to find how many potions satisfy `spell * potion >= success`, sorting helps apply binary search.

### 2. Iterate Through Each Spell:
For every spell, calculate how many potions satisfy:

---

## 💻 Code (Python)

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array in ascending order
        potions.sort()

        # Initialize a result list to store the number of successful pairs for each spell
        res = []

        # Iterate over each spell in the spells list
        for s in spells:
            # Perform binary search to find the smallest potion that forms a successful pair
            left, right = 0, len(potions) - 1
            idx = len(potions)  # Default index if no successful pair is found

            while left <= right:
                # Calculate the middle index
                m = (left + right) // 2

                # Check if the product of the spell and potion meets the success threshold
                if s * potions[m] >= success:
                    idx = m       # Valid potion found
                    right = m - 1 # Try to find earlier valid potion
                else:
                    left = m + 1

            # The number of successful pairs is from index `idx` to the end
            res.append(len(potions) - idx)

        return res
```

---

## 💡 Time and Space Complexity
- **Time**:
   - Sorting potions: O(m log m)
   - For each spell: Binary Search on potions: O(log m)
   - Total: O(m log m + n log m) where n = len(spells) and m = len(potions)
- **Space**:
   - O(1) extra space (if we ignore the result list)
   - Sorting can be done in-place or use O(m) space depending on implementation

