# 🧲 Problem: Reverse Vowels of a String

- **Platform**: [LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)
- **Submission**: [https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1824127104/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1824127104/?envType=study-plan-v2&envId=leetcode-75)
- **Date Solved**: 2025-11-08
- **Tags**: DSA, Array, LeetCode75, Two Pointer
- **Difficulty**: Easy

---

## ✅ Problem Statement
Given a string `s`, reverse **only the vowels** of the string and return the resulting string.  
Vowels include: `a, e, i, o, u` (both lowercase and uppercase).

```python
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"
Output: "leotcede"

**Example 3:**  
Input: `"hello"`  
Output: `"holle"`

**Example 3:**  
Input: `"aA"`  
Output: `"Aa"`

```

---


# 🧠 Approach 1: Brute Force (Collect & Replace)

### 🔹 Idea:
1. Traverse the string and **collect all vowels** in a list.
2. Reverse the vowel list.
3. Traverse again and **replace vowels** with reversed vowels.

---

### 🧾 Code (Brute Force Approach)
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_list = []

        # Step 1: Collect vowels
        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)

        # Convert to list for modification
        s = list(s)

        # Step 2: Replace vowels using reversed order
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list.pop()  # last vowel

        return ''.join(s)

```

---

## 💡 Time and Space Complexity
- **Time**: O(n)
  - two full scans
- **Space**: O(n)
  - storing vowels list

---

## Approach 2: Efficient Two-Pointer Approach
Approach:
- Use two pointers, one at the start and one at the end:
  - Move left pointer until it finds a vowel
  - Move right pointer until it finds a vowel
  - Swap them
  - Move pointers inward and continue

This reverses vowels in-place (inside a list) efficiently.

---

## Code(Python)
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)   # Convert to list for modification
        
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer to vowel
            while left < right and s[left] not in vowels:
                left += 1
            
            # Move right pointer to vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap found vowels
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
        
        return ''.join(s)
```

---

### ▶️ Step-by-Step Execution with Example
```python
Input:
s = "hello"

Converted List:

['h', 'e', 'l', 'l', 'o']

Two pointers:
 left = 0 → 'h' (not vowel) → move to 1
 right = 4 → 'o' (vowel)

Find vowels:
 left stops at index 1 ('e')
 right stops at index 4 ('o')

Swap:
 ['h', 'o', 'l', 'l', 'e']

Move inward:
 left = 2, right = 3

Now:
'l' and 'l' are not vowels → pointers move past each other
Stop loop.

Output:
 "holle"

```

---

## ✅ Time & Space Complexity
- Time Complexity: O(n)
  - Each pointer moves across the string at most once.

- Space Complexity: O(n)
  - Converting string → list requires extra space.
  - ✅ If we didn’t convert the string (not possible in Python), space could be O(1).
