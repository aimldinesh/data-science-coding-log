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

---

## ⚙️ Approach 2: Character Count (Optimized)
- Instead of sorting, we can use the frequency count of each letter (a-z) as a key.
- This avoids the sorting overhead.

Example:

- "eat" → [1,0,0,0,1,0,...,1]
- "tea" → [1,0,0,0,1,0,...,1]
- → Same frequency tuple → same group.

---

### code 
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Initialize a 26-length list for character counts
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            # Use the tuple as a hashable key
            anagram_map[tuple(count)].append(word)
        
        return list(anagram_map.values())
```
---
## 💡 Time and Space Complexity
- **Time**: O(N·M)
- **Space**: O(N·M)

---

## 🧩 Comparison
| Approach     | Technique           | Time        | Space  | Notes                 |
| ------------ | ------------------- | ----------- | ------ | --------------------- |
| 1️⃣ Sorting  | Sort word letters   | O(N·M·logM) | O(N·M) | Easier to understand  |
| 2️⃣ Counting | Character frequency | O(N·M)      | O(N·M) | Faster for long words |

