# 🧲 Problem: Online Stock Span

- **Platform**: [LeetCode](https://leetcode.com/problems/online-stock-span/description/)
- **Submission**: [https://leetcode.com/problems/online-stock-span/submissions/1648925217/](https://leetcode.com/problems/online-stock-span/submissions/1648925217/)
- **Date Solved**: 2025-05-30
- **Tags**: Stack, Monotonic Stack, Design
- **Difficulty**: Medium

---

## ✅ Problem Statement
- Design an algorithm that collects daily stock prices and returns the span of that stock's price for the current day.
- The span of the stock's price today is defined as the number of consecutive days (including today) the price was less than or equal to today's price.
- Implement the StockSpanner class:
     - StockSpanner(): Initializes the object.
     - int next(int price): Returns the span of the stock's price for the current day.

### 🔍 Example
```python
Input: 
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output: 
[None, 1, 1, 1, 2, 1, 4, 6]

```
---

## 🚀 Approach 1 : Brute Force (Array)
- The problem requires computing the stock span — the number of consecutive days before today (including today) where the stock price was less than or equal to today's price.
- This brute-force approach stores all previous prices in a list. For each new price:
     - We append it to the list.
     - We then scan backward through previous prices until we find a price greater than the current one.
     - The difference in indices gives us the stock span for that day.

---

## 💻 Code (Python)

```python
class StockSpanner:

    def __init__(self):
        # Stores all previous prices
        self.arr = []

    def next(self, price: int) -> int:
        # Add the current price to the list
        self.arr.append(price)

        # Start from the previous index
        i = len(self.arr) - 2

        # Move backward as long as prices are <= current price
        while i >= 0 and self.arr[i] <= price:
            i -= 1

        # Span = current index - index of last higher price
        return len(self.arr) - i - 1

```
---
### 🔁 Step-by-Step Example
```python

Input: [100, 80, 60, 70, 60, 75, 85]

| Price | Span Computation                                                                                    | Span |
| ----- | --------------------------------------------------------------------------------------------------- | ---- |
| 100   | No previous prices → span = 1                                                                       | 1    |
| 80    | 80 < 100 → span = 1                                                                                 | 1    |
| 60    | 60 < 80 → span = 1                                                                                  | 1    |
| 70    | 70 > 60 → go back → 70 < 80 → span = 2                                                              | 2    |
| 60    | 60 < 70 → span = 1                                                                                  | 1    |
| 75    | 75 > 60 → go back → 75 > 70 → go back → 75 < 80 → span = 4                                          | 4    |
| 85    | 85 > 75 → go back → 85 > 60 → go back → 85 > 70 → go back → 85 > 60 → go back → 85 < 100 → span = 6 | 6    |

Output : [1, 1, 1, 2, 1, 4, 6]

```

---

## ⏱ Time and Space Complexity

### Time Complexity:
- Worst Case per call: O(n) — when current price is greater than all previous prices.
- Total worst-case time for n calls: **O(n²)**

### Space Complexity:
- O(n) to store `n` prices in the array.

⚠️ This solution is inefficient for large inputs compared to the stack-based optimized solution which runs in O(n) overall.

---

## 🚀 Approach  2 : Using a Monotonic Stack
💡 Intuition
- Instead of checking the stock prices for all previous days manually (which is inefficient), we want to skip over many days at once if their prices are less than or equal to the current day’s price.
- To do this, we store previous prices along with their spans. When we see a new price, we collapse all previous prices that are less than or equal to it and combine their spans. This helps us efficiently compute the span in amortized constant time.

Steps
- We use a stack of pairs where each element is (price, span):
     - Initialize a stack in the constructor.
     - For every call to next(price):
           - Start span = 1 (at least today counts).
           - While the stack is not empty and the top price is <= price, pop from stack and add its span to the current span.
           - Push (price, span) to the stack.
           - Return span.

- This ensures all older prices that are less than or equal are collapsed and don't need to be checked again in future calls.
---

## 💻 Code (Python)

```python
lass StockSpanner:

    def __init__(self):
        # Stack to store tuples of (price, span)
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1  # Minimum span is always 1 (current day)
        
        # While current price is greater than or equal to the top of the stack
        # Pop and accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        
        # Push current price and its span onto the stack
        self.stack.append((price, span))
        
        # Return the computed span
        return span
```
---
### 🔁 Step-by-Step with Example
```python
Intput:[100, 80, 60, 70, 60, 75, 85]

| Price | Stack Before                           | Span Computed | Stack After                           |
| ----- | -------------------------------------- | ------------- | --------------------------------------|
| 100   | []                                     | 1             | [(100, 1)]                            |
| 80    | [(100, 1)]                             | 1             | [(100, 1), (80, 1)]                   |
| 60    | [(100, 1), (80, 1)]                    | 1             | [(100, 1), (80, 1), (60, 1)]          |
| 70    | [(100, 1), (80, 1), (60, 1)]           | 2             | [(100, 1), (80, 1), (70, 2)]          |
| 60    | [(100, 1), (80, 1), (70, 2)]           | 1             | [(100, 1), (80, 1), (70, 2), (60, 1)] |
| 75    | [(100, 1), (80, 1), (70, 2), (60, 1)]  | 4             | [(100, 1), (80, 1), (75, 4)]          |
| 85    | [(100, 1), (80, 1), (75, 4)]           | 6             | [(100, 1), (85, 6)]                   |

Output : [1, 1, 1, 2, 1, 4, 6]
```
---

## ⏱ Time and Space Complexity

- **Time Complexity**: O(n)
  - Each element is pushed and popped from the stack at most once.
  - So, over `n` calls to `next()`, total time = O(n), making each call O(1) on average.

- **Space Complexity**: O(n)
  - Stack stores a pair (price, span) for each day.
  - In the worst case (strictly decreasing prices), all `n` elements are stored.
