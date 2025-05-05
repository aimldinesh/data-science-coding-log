# 🧲 Problem: Best Time to Buy and Sell Stock II

- **Platform**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
- **Submission**: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1626042037/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1626042037/)
- **Date Solved**: 2025-05-05
- **Tags**: Array, Greedy, Dynamic Programming
- **Difficulty**: Medium

---

## ✅ Problem Statement
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

On each day, you may decide to:
- Buy and/or sell the stock
- You **can hold at most one share of the stock at any time**
- You can **buy and sell the stock multiple times**

Return the **maximum profit** you can achieve.

---

## 🧪 Example

```python
Input:
prices = [7,1,5,3,6,4]

Output: 7
Explanation:
Buy on day 2 (price = 1), sell on day 3 (price = 5),
buy on day 4 (price = 3), sell on day 5 (price = 6).
Total profit = (5 - 1) + (6 - 3) = 7.
```

---

## 🚀 My Approach
- This is a greedy problem.
-  We add profit whenever the price increases from one day to the next, because:
   - Buying on the lowest of two consecutive days and selling on the higher one always yields the same total profit as holding through a multi-day rise.

- Steps:
   - Loop through the array from the second day.
   - If today’s price is higher than yesterday’s, take the profit.
   - Sum up all such profits to get the max result.

---

## 💻 Code (Python)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize 'profit' to 0, which will store the total profit.
        profit = 0
        
        # Loop through the price list starting from the second day (index 1)
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's price,
            # we can make a profit by buying yesterday and selling today.
            if prices[i] > prices[i-1]:
                # Calculate the profit and add it to the total profit.
                profit += (prices[i] - prices[i-1])
        
        # Return the total profit after traversing all days.
        return profit

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
   - We iterate through the prices list once.
- **Space**: O(n)
   - We use only one variable to store the profit.
