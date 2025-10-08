# 🧮 Problem: Group Anagrams

- **Platform**: [LeetCode](https://leetcode.com/problems/group-anagrams/description/)
- **Submission**: [https://leetcode.com/problems/group-anagrams/submissions/1603567085/](https://leetcode.com/problems/group-anagrams/submissions/1603567085/)
- **Date Solved**: 2025-04-11
- **Tags**: DSA

---

## ✅ Problem Statement
- Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.Two strings are anagrams of each other if the letters of one string can be rearranged to form the other.


---

## 🚀 My Approach
- I used a **dictionary** to group words by their **sorted character signature**.
- For each word:
  - I sorted the characters of the word (e.g., "eat" → "aet").
  - I used the sorted word as a key in the dictionary.
  - Words with the same sorted characters were grouped together.
- Finally, I returned all the dictionary values as the result.

---

## 💻 Code (Python)

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty dictionary to group anagrams
        # Key → sorted version of the word (signature)
        # Value → list of all words matching that signature
        dic = {}

        # Iterate through each word in the input list
        for word in strs:
            # Sort the letters in the word to form a signature
            # Example: "eat" → "aet", "tea" → "aet"
            sorted_word = "".join(sorted(word))

            # If the signature doesn't exist, create a new entry
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                # If signature exists, append current word to the list
                dic[sorted_word].append(word)

        # Return the grouped anagrams as a list of lists
        return list(dic.values())

```
---
### 🧠 Step-by-Step Example
```python
Input: ["eat","tea","tan","ate","nat","bat"]

Process:
| Word  | Sorted | Dictionary State                                 |
| ----- | ------ | ------------------------------------------------ |
| "eat" | "aet"  | { "aet": ["eat"] }                               |
| "tea" | "aet"  | { "aet": ["eat", "tea"] }                        |
| "tan" | "ant"  | { "aet": [...], "ant": ["tan"] }                 |
| "ate" | "aet"  | { "aet": ["eat", "tea", "ate"], "ant": ["tan"] } |
| "nat" | "ant"  | { "aet": [...], "ant": ["tan","nat"] }           |
| "bat" | "abt"  | { "aet": [...], "ant": [...], "abt": ["bat"] }   |

```

---

## 💡 Time and Space Complexity
- **Time**: O(n * klogk), Where n = number of strings, and k = max length of a string. Sorting each word takes O(k log k).
- **Space**: O(nk), For storing the grouped anagrams in the dictionary.
