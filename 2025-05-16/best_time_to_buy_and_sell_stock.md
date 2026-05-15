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
🧠 Intuition

Track the cheapest buy day with l and scan every future day with r. If prices[r] > prices[l] → calculate profit. If prices[r] <= prices[l] → a cheaper buy day found, shift l to r. One pass captures the best buy-sell pair.
```
prices = [7, 1, 5, 3, 6, 4]

Day 1 (price=7) → buy here
Day 2 (price=1) → cheaper! new buy day
Day 5 (price=6) → sell here → profit = 6-1 = 5 ✅
```

📌 Approach : two-pointer (sliding window) technique:

1. l=0 (buy), r=1 (sell), maxProfit=0
2. While r < len(prices):
   + prices[l] < prices[r] → profitable → update maxProfit
   + prices[l] >= prices[r] → cheaper buy found → l = r
   + Always increment r
     
3. Return maxProfit
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
### 🔍 Step-by-Step Execution

Input: prices = [7, 1, 5, 3, 6, 4]
```
Indices:  0  1  2  3  4  5
Values:   7  1  5  3  6  4
             ↑        ↑
            buy       sell (max profit)
```

r=1: prices[l]=7, prices[r]=1
```
7 > 1 → price dropped, new buy day
l = 1
r = 2
```
r=2: prices[l]=1, prices[r]=5
```
1 < 5 → profit = 5-1 = 4
maxProfit = max(0, 4) = 4
r = 3
```
r=3: prices[l]=1, prices[r]=3
```
1 < 3 → profit = 3-1 = 2
maxProfit = max(4, 2) = 4
r = 4
```
r=4: prices[l]=1, prices[r]=6
```
1 < 6 → profit = 6-1 = 5
maxProfit = max(4, 5) = 5
r = 5
```
r=5: prices[l]=1, prices[r]=4
```
1 < 4 → profit = 4-1 = 3
maxProfit = max(5, 3) = 5
r = 6
```
Loop ends: r=6 == len(prices)

---
### 📊 Trace Table
```
r          prices[l]                 prices[r]     profit          maxProfit        action  
1          7                         1             —               0                l=1 (new buy)
2          1                         5             4               4                update max
3          1                         3             2               4                no update
4          1                         6             5               5                update max
5          1                         4             3               5                no update
```
---
### 🔍 Case 2 — Prices Always Falling

Input: prices = [7, 6, 4, 3, 1]
```
r         prices[l]                  prices[r]     action         maxProfit
1         7                          6             l=1            0
2         6                          4             l=2            0
3         4                          3             l=3            0 
4         3                          1             l=4            0
```
return maxProfit = 0 ✅  (never buy in falling market)
---
### 🔍 Case 3 — Best Buy is First Day

Input: prices = [1, 2, 3, 4, 5]
```
r        prices[l]                prices[r]       profit          maxProfit
1        1                        2               1               1
2        1                        3               2               2
3        1                        4               3               3
4        1                        5               4               4
```
return maxProfit = 4 ✅  (buy day 0, sell day 4)
---
### 💡 Two Pointer Visualised
````
prices = [7,  1,  5,  3,  6,  4]
          l
              l   r             → profit=4
              l       r         → profit=2
              l           r     → profit=5 ← max
              l               r → profit=3

l stays at index 1 (cheapest seen)
r keeps scanning forward
````
## ✅ Final Answer
```
return maxProfit = 5   (buy at price 1, sell at price 6) ✅
```


## 💡 Time and Space Complexity
- **Time**: O(n)
    - We traverse the prices array exactly once with the r pointer
- **Space**: O(1)
    - Only a fixed number of variables are used (l, r, maxProfit, profit) — no extra data structures

## 💡 Interview tip: 

If asked about multiple transactions (Buy and Sell Stock II), the approach flips — add every upward price difference (if prices[r] > prices[l]: profit += prices[r] - prices[l]) because you can buy and sell on every consecutive profitable day. Same O(n) time, completely different greedy logic.
