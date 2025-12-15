# 🧲 Problem: Random Pick with Weight

- **Platform**: [LeetCode](https://leetcode.com/problems/random-pick-with-weight/description/?envType=study-plan-v2&envId=binary-search)
- **Submission**: [https://leetcode.com/problems/random-pick-with-weight/submissions/1484563131/?envType=study-plan-v2&envId=binary-search](https://leetcode.com/problems/random-pick-with-weight/submissions/1484563131/?envType=study-plan-v2&envId=binary-search)
- **Date Solved**: 2025-04-17
- **Tags**: Binary Search, Array, DSA
- **Difficulty**: Medium

---

## ✅ Problem Statement
- You are given an integer array `w` where `w[i]` represents the weight of the `i`-th index. You need to randomly pick an index based on the weights such that the probability of picking an index `i` is proportional to `w[i]`.

---
## Examples
```python
Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

```
---

## 🚀 My Approach : Prefix Sum and Binary Search
The idea is to use a **prefix sum array** to store cumulative weights, and then use **binary search** to efficiently select an index based on the weighted probability.

### 🔸 Steps:

1. **Prefix Sum Calculation:**
   - Calculate the prefix sum of the weights. This array will store cumulative sums, making it easier to map a randomly generated number to a weight.

2. **Random Target:**
   - Generate a random target number between `0` and the total weight (`sum(w)`).

3. **Binary Search:**
   - Use binary search on the prefix sum array to find the index where the cumulative weight is greater than or equal to the random target. This index is then returned as the result.


---

## 💻 Code (Python)

```python
class Solution:

    def __init__(self, w: List[int]):
        # Initialize an empty list for the prefix sum and a variable to hold the total weight.
        self.prefix_sum = []
        total = 0
        
        # Calculate the prefix sum array and the total weight.
        for weight in w:
            total += weight
            self.prefix_sum.append(total)  # Append the cumulative sum up to the current weight
        
        # Store the total weight for later use in pickIndex method.
        self.total = total

    def pickIndex(self) -> int:
        # Generate a random target between 0 and the total weight.
        target = random.uniform(0, self.total)
        
        # Initialize binary search bounds.
        left, right = 0, len(self.prefix_sum) - 1  # Fix here: right should be len(self.prefix_sum) - 1

        # Perform binary search to find the correct index.
        while left < right:
            # Find the middle index.
            mid = (left + right) // 2
            
            # If the cumulative weight at mid is less than the target, move the left pointer.
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                # Otherwise, move the right pointer.
                right = mid

        # Return the index where the cumulative weight is greater than or equal to the target.
        return left
```

---

## 💡 Time and Space Complexity
- **Time**:
   - Constructor (__init__): O(n) where n is the length of the weights array w (because we calculate the prefix sum).
   - pickIndex: O(log n) due to binary search on the prefix sum array.
- **Space**:
   - O(n) due to the storage of the prefix sum array.
