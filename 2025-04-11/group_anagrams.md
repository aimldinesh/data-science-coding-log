# 🧮 Problem: Group Anagrams

- **Platform**: [LeetCode](https://leetcode.com/problems/group-anagrams/description/)
- **Submission**: [https://leetcode.com/problems/group-anagrams/submissions/1603567085/](https://leetcode.com/problems/group-anagrams/submissions/1603567085/)
- **Date Solved**: 2025-04-11
- **Tags**: DSA

---

## ✅ Problem Statement
- Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.Two strings are anagrams of each other if the letters of one string can be rearranged to form the other.


---
## Examples
```python
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
 - There is no string in strs that can be rearranged to form "bat".
 - The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
 - The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

 ```
---

## 🚀 Approach : Sort-As-Key (Anagram Signature Method)
Intuition

Two words are anagrams if and only if they contain the exact same characters in any order.
A simple and reliable way to check this is:

- ✔ Sort the characters
- ✔ Use the sorted string as a unique signature

Examples:

- "eat" → "aet"
- "tea" → "aet"
- "ate" → "aet"

So all these words share the same sorted key, meaning they belong to the same anagram group.

We maintain a dictionary:
```python
key = sorted(word)
value = list of all words having this key
```
At the end, we return all grouped lists.

🛠 Algorithm

1. Create an empty dictionary dic.
2. Loop through each word in strs:
3. Sort the word to get its "signature"
   - If signature not in dic, create a new list
   - Else append the word to the existing list

5. Return dic.values() as the final list of anagram groups.

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

## ⚙️ Approach 2: Character Count Signature (Optimal O(n·k))
Intuition

Instead of sorting each word (which costs O(k log k)), we can uniquely identify an anagram by counting how many times each character appears.

Since we have only 26 lowercase English letters, each word can be represented by a 26-length frequency array, such as:

- "eat" → [1,0,0,0,1,0,...]

- "tea" → [1,0,0,0,1,0,...]

- "tan" → [1,0,0,0,...,1,...]

Two words are anagrams if and only if their frequency arrays are identical.

We convert this list into a tuple (because lists are not hashable) and use it as a dictionary key.

This avoids sorting entirely and improves performance.

🛠 Algorithm

1. Create a defaultdict(list) to store grouped anagrams.
2. For each word in strs:
   - Initialize a 26-length array of zeros.
   - For each character, increment its frequency position.
   - Convert the frequency list into a tuple (hashable).
   - Append the word to anagram_map[tuple].

3. Return the grouped values.
---

### code 
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # maps frequency tuple → list of anagrams
        
        for word in strs:
            # Step 1: Frequency array for this word
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
                
            # Step 2: Convert list to tuple (so it becomes hashable)
            key = tuple(count)
            
            # Step 3: Group words with the same signature
            anagram_map[key].append(word)
        
        # Step 4: Return grouped anagrams
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

