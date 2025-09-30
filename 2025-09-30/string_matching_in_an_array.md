# 🧲 Problem: String Matching in an Array

- **Platform**: [LeetCode](https://leetcode.com/problems/string-matching-in-an-array/description/)
- **Submission**: [https://leetcode.com/problems/string-matching-in-an-array/description/](https://leetcode.com/problems/string-matching-in-an-array/description/)
- **Date Solved**: 2025-09-30
- **Tags**: DSA, Array, String, Sorting
- **Difficulty**: Easy

---

# ✅ Problem Statement  

You are given an array of **strings** `words`.  
Return all strings in `words` that are a **substring of another word** in the array.  

- A string `words[i]` is a substring of `words[j]` if `words[i]` appears consecutively in `words[j]`.  
- The result can be returned in **any order**.  

---

## 🔹 Example  

```python
Input: 
words = ["mass","as","hero","superhero"]

Output:
["as","hero"]

Explanation:

- "as" is a substring of "mass".
- "hero" is a substring of "superhero".
```
---

## 🔹 Approach 1 — Brute Force

- Initialize an empty list res to store results.
- Iterate over all pairs (i, j) in words where i != j.
- Check if words[i] is a substring of words[j] using in.
- If yes, add words[i] to res and break the inner loop to avoid duplicates.

---

## 💻 Code (Python)

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue  # Skip comparing the word with itself
                if words[i] in words[j]:
                    res.append(words[i])
                    break  # No need to check further once found
        
        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n² * m) → n = number of words, m = average word length
- **Space**: O(n) for result list

---

## Approach 2 — Using Sorting by Length

- Sort words by length (shorter strings first).
- Iterate over each word and compare it only with longer words that appear after it.
- Check if the current word is a substring of any longer word.
- If yes, add to res and break.

This reduces unnecessary comparisons compared to brute force.

---

## 💻 Code (Python)

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        # Sort words by length (ascending)
        words.sort(key=len)
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):  # Compare only with longer words
                if words[i] in words[j]:
                    res.append(words[i])
                    break  # Found a match, move to next word
        
        return res
```

---

## 💡 Time and Space Complexity
- **Time**: O(n² * m) worst case (still compares all substrings), but fewer checks due to sorting
- **Space**: O(n) for result list

