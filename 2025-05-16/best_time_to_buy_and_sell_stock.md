# 🧲 Problem: Best Time to Buy and Sell Stock

- **Platform**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
- **Submission**: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1521751739/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1521751739/)
- **Date Solved**: 2025-05-16
- **Tags**: Array, Dynamic Programming, Greedy, Two Pointers
- **Difficulty**: Easy

---

## ✅ Problem Statement
- You are given an array prices where prices[i] is the price of a given stock on the i-th day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### 🔍 Example
```python
Example 1:

Input:prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:

Input:prices = [7, 6, 4, 3, 1]
Output: 0
Explanation:
No profit can be made since prices keep going down.
```
---

## 🚀 Approach 1 : Brute Force Approach
🔸 Idea
- Try every possible pair of buy/sell days and compute profit. Keep track of the maximum.

---

## 💻 Code (Python)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force approach: Try every pair (buy, sell)
        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = max(profit, sell - buy)
        return profit

```

---

## 💡 Time and Space Complexity
- **Time**: O(n²)
    - Every pair is checked → nested loops.
- **Space**: O(1)
    - No extra data structures used.

---

## 🚀 Approach 2 : Two Pointers (Single Pass)
🔸 Idea
- Use two pointers (l = buy day, r = sell day).
- Track the minimum price so far to maximize the profit.
- Move r forward and update the profit when a higher selling price is found.

---

## 💻 Code (Python)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers:
        # l points to the day to buy, r points to the day to sell
        l, r = 0, 1 
        
        # Initialize the maximum profit to 0
        maxProfit = 0
        
        # Iterate through the price list starting from the second day (r)
        while r < len(prices):
            # If the current price on day r is greater than the price on day l
            # it means selling on day r would yield a profit
            if prices[l] < prices[r]:
                # Calculate the profit
                profit = prices[r] - prices[l]
                # Update maxProfit
                maxProfit = max(maxProfit, profit)
            else:
                # If price drops, move buy day to r
                l = r
            # Move r to next day
            r += 1
        
        # Return the maximum profit
        return maxProfit

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - Only one pass through the list.
- **Space**: O(1)
    - No extra space used.
