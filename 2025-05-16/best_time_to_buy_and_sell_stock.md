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
### 🧠 Intuition

We want to buy low and sell high, but the buy must happen before the sell.
A brute-force approach would check every pair of days — but that's O(n²). The key insight is: if we're at a day with a lower price than our current buy day, there's no reason to keep the old buy day. We can never do better by buying at a higher price. So we greedily shift our buy pointer to the cheaper day and keep scanning forward.
This means we only ever need one pass through the array.

### 📌 Approach
We use a two-pointer (sliding window) technique:

1. Start l = 0 (buy) and r = 1 (sell)
2. While r is within bounds:
   - If prices[r] > prices[l] → we have a profitable transaction, compute and update maxProfit
   - If prices[r] <= prices[l] → prices[r] is a cheaper buy day, move l = r
   - Always increment r
3. Return maxProfit

The window expands when we find profit, and resets when we find a cheaper price to buy at.
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
    - We traverse the prices array exactly once with the r pointer
- **Space**: O(1)
    - Only a fixed number of variables are used (l, r, maxProfit, profit) — no extra data structures
