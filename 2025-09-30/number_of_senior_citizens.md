# 🧲 Problem: Number of Senior Citizens

- **Platform**: [LeetCode](https://leetcode.com/problems/number-of-senior-citizens/description/)
- **Submission**: [https://leetcode.com/problems/number-of-senior-citizens/submissions/1786936839/](https://leetcode.com/problems/number-of-senior-citizens/submissions/1786936839/)
- **Date Solved**: 2025-09-30
- **Tags**: DSA, String
- **Difficulty**: Easy

---


## ✅ Problem Statement
You are given a list of strings `details`, where each string contains encoded information about a passenger.  
Each string has the following fixed format:

- First 10 characters → phone number  
- 11th character → gender (`M` or `F`)  
- 12th and 13th characters → **age** (two digits)  
- Remaining characters → seat number  

A person is considered a **senior citizen** if their `age > 60`.  

Return the number of senior citizens.

---

## 🔹 Example

**Example 1:** 
```python 
Input:  
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

Step-by-step:

"7868190130M7522" → age = 75 → senior ✅
"5303914400F9211" → age = 92 → senior ✅

"9273338290F4010" → age = 40 → not senior ❌

Output: 2
```
**Example 2:**
```python
Input:
details = ["1313579440F2036","2921522980M5644"]

"1313579440F2036" → age = 20 → not senior ❌

"2921522980M5644" → age = 56 → not senior ❌

Output: 0
```
---

## 🚀 Approach

- Initialize a counter res = 0.
- For each string in details, extract substring d[11:13] → this represents the passenger's age.
- Convert it to integer and check if age > 60.
- If true, increment counter.
- Return the final counter.

---

## 💻 Code (Python)

```python
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            # Extract age from index 11 and 12
            age = int(d[11:13])
            if age > 60:
                res += 1
        return res

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
    - iterate once over details.
- **Space**: O(1)
    - uses only a counter.
