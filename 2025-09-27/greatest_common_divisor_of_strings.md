# 🧲 Problem: Greatest Common Divisor of Strings

- **Platform**: [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)
- **Submission**: [https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/](https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/)
- **Date Solved**: 2025-09-27
- **Tags**: DSA, Math, String, Leet75
- **Difficulty**: Easy

---

## 📌 Problem Statement
For two given strings `str1` and `str2`, return the **greatest common divisor (GCD) string**.

A string `x` is a divisor of string `y` if and only if:
- `y = x + x + ... + x` (concatenated some number of times).

The GCD string is the **largest string** that can divide both `str1` and `str2`.

---
## ✅ Example:
```text
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
```
---

## 💡 Approach 1: Brute-force (try prefix lengths from large → small)
- Core idea

- If x is a common divisor string of str1 and str2, then:
  - len(x) must divide len(str1) and len(str2).
  - Repeating x the required number of times reconstructs each original string.

- So: try possible prefix lengths l = min(len1,len2), ..., 1. For each l:
  - Check len1 % l == 0 and len2 % l == 0. If not, skip.
  - Let prefix = str1[:l].
  - Check prefix * (len1//l) == str1 and prefix * (len2//l) == str2.
    - If yes → prefix is a common divisor; since we tried lengths from largest to smallest, return it.

---

## 🐍 Python Code

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # Helper function to check if prefix of length l divides both strings
        def isDivisor(l):
            # Length must divide both strings evenly
            if len1 % l != 0 or len2 % l != 0:
                return False

            # Number of times prefix repeats in each string
            f1, f2 = len1 // l, len2 // l

            # Check if repeating prefix reconstructs both strings
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Try all possible prefix lengths from largest to smallest
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]  # Found the largest valid divisor

        # No common divisor found
        return ""

```
---
## 🧮 Step by step execution with example
```text
Example A — positive

str1 = "ABCABC", str2 = "ABC"

len1 = 6, len2 = 3, min = 3.

Try l = 3:

  6 % 3 == 0 and 3 % 3 == 0 → OK.
  prefix = str1[:3] = "ABC".
  prefix * (6//3) = "ABC" * 2 = "ABCABC" == str1 ✔
  prefix * (3//3) = "ABC" * 1 = "ABC" == str2 ✔

Both true → return "ABC". Done.

----------------

Example B — positive (another)

str1 = "ABABAB", str2 = "ABAB"

  len1 = 6, len2 = 4, min = 4.
  Try l = 4: 6%4 != 0 → skip.
  Try l = 3: 4%3 != 0 → skip.
  Try l = 2: 6%2 == 0 and 4%2 == 0.

      prefix = "AB".
      "AB" * (6//2) = "AB" * 3 = "ABABAB" == str1 ✔
      "AB" * (4//2) = "AB" * 2 = "ABAB" == str2 ✔

   Return "AB".
---------------------
Example C — negative

str1 = "LEET", str2 = "CODE"

  len1 = 4, len2 = 4.
  Try l = 4: prefix = "LEET". "LEET"*1 == "LEET" (true), "LEET"*1 == "CODE" (false).
  Try l = 3,2,1: none will satisfy both reconstructions.
  Return "".
```
---

## 💡 Time and Space Complexity
- **Time**:
    - Checking divisibility requires repeating prefix strings → O(n + m) per check.
    - At most min(n, m) checks.
    - Worst case: O((n + m) * min(n, m)).
- **Space**: O(n + m)
    - For temporary string constructions during prefix checks.

---

## 💡 Approach2 : Optimized Approach (Using Math GCD)
Key observations / proof sketch

- If a string x divides both str1 and str2, then:
  - str1 = x^a and str2 = x^b for some integers a, b.
  - Then str1 + str2 = x^{a+b} = str2 + str1.
So a necessary condition for any non-empty gcd-string is:
str1 + str2 == str2 + str1.

- If that holds, the largest such x must have length g = gcd(len1, len2); specifically the answer is str1[:g] (or str2[:g]) — because the greatest common divisor of the lengths gives the maximum possible repeating block length that can divide both lengths.

Algorithm (concise)

- If str1 + str2 != str2 + str1, return "". (No common repeating block can make both concatenations equal.)
- Let g = gcd(len(str1), len(str2)).
- Return str1[:g].

Why gcd(len1, len2)?
- If str1 = x^a and str2 = x^b, then len1 = a*len(x), len2 = b*len(x) → len(x) divides both lengths → len(x) divides gcd(len1,len2). The largest candidate length is gcd(len1,len2). If str1 + str2 == str2 + str1, the prefix of length g will repeat to form both, hence it's the answer.
---

## 🐍 Python Code

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if both strings share the same repeated pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Find GCD of lengths
        g = gcd(len(str1), len(str2))

        # Step 3: Return prefix of length g
        return str1[:g]
```
---
## Step by step execution with example
```python
Example A again (efficient)

str1 = "ABCABC", str2 = "ABC"

Check concatenation:

    str1 + str2 = "ABCABCABC", str2 + str1 = "ABCABCABC" → equal.

    g = gcd(6,3) = 3.

    Return str1[:3] = "ABC".

------

Example B again

str1 = "ABABAB", str2 = "ABAB"

   str1 + str2 = "ABABABABAB", str2 + str1 = "ABABABABAB" → equal.

   g = gcd(6,4) = 2.

   Return str1[:2] = "AB".

---
Example C (negative)

str1 = "LEET", str2 = "CODE"

       str1 + str2 = "LEETCODE", str2 + str1 = "CODELEET" → not equal → return "".
---

Complexity (efficient method):

- Checking concatenation equality str1 + str2 == str2 + str1 takes O(len1 + len2).
- Computing gcd is O(log(min(len1,len2))) (very small).
- Slicing str1[:g] is O(g).
Overall O(len1 + len2) time, O(1) extra space.
```
---

## 💡 Time and Space Complexity
- **Time**: O(n + m)
    - Concatenation check str1 + str2 == str2 + str1 takes O(n + m).
    - GCD calculation is O(log(min(n, m))), negligible.

- **Space**: O(1)
    - Only storing variables, no extra structures.
