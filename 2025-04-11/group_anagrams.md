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
        # Initialize an empty dictionary to store sorted words as keys
        dic = {}

        # Iterate over each word in the input list
        for words in strs:
            # Sort the letters in the word to get the 'signature' of the anagram
            sorted_words = "".join(sorted(words))

            # If the sorted word (signature) is not in the dictionary, add it with the original word as a value
            if sorted_words not in dic:
                dic[sorted_words] = [words]
            else:
                # If the signature already exists, append the current word to the list of anagrams
                dic[sorted_words].append(words)

        # Return all values (grouped anagrams)
        return list(dic.values())
```

---

## 💡 Time and Space Complexity
- **Time**: O(n * klogk), Where n = number of strings, and k = max length of a string. Sorting each word takes O(k log k).
- **Space**: O(nk), For storing the grouped anagrams in the dictionary.
