# 🧲 Problem: Find Users With Valid E-Mails

- **Platform**: [LeetCode](https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=top-sql-50)
- **Submission**: [https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/1781963024/?envType=study-plan-v2&envId=top-sql-50](https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/1781963024/?envType=study-plan-v2&envId=top-sql-50)
- **Date Solved**: 2025-09-25
- **Tags**: MySQL, Database, Regex, String
- **Difficulty**: Easy

---

## 📌 Problem Statement
We are given a table **Users**:

| Column Name | Type    |
|-------------|---------|
| user_id     | int     |
| name        | varchar |
| mail        | varchar |

- `user_id` is the **primary key**.  
- Each row represents a user with a username and email.  
- Some emails may be invalid.  

**Valid Email Rules:**
1. The **prefix name**:
   - Must **start with a letter** (a-z or A-Z).  
   - May contain letters, digits, underscore `_`, period `.`, and dash `-`.  

2. The **domain** must be exactly `@leetcode.com`.

**Task:**  
Return all users with valid emails.

---

## 📝 Example
**Input:**

**Users**
| user_id | name      | mail                    |
|---------|-----------|-------------------------|
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |

**Output:**
| user_id | name      | mail                    |
|---------|-----------|-------------------------|
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |

**Explanation:**
- `user_id = 1` ✅ valid.  
- `user_id = 2` ❌ no domain.  
- `user_id = 3` ✅ valid (prefix ends with `-`, still allowed).  
- `user_id = 4` ✅ valid.  
- `user_id = 5` ❌ contains `#`, not allowed.  
- `user_id = 6` ❌ wrong domain (`gmail.com`).  
- `user_id = 7` ❌ prefix starts with `.` (invalid).  

---

## 🧠 Approach  

1. Use a **regular expression** to validate emails.  
   - `^[A-Za-z]` → must start with a letter.  
   - `[A-Za-z0-9._-]*` → allowed characters for the prefix.  
   - `@leetcode\.com$` → domain must match exactly.  

2. By default, MySQL regex is **case-insensitive**.  
   - Example: `abc@leetcode.COM` would incorrectly pass.  
   - To enforce **case sensitivity**, use `COLLATE utf8_bin`.  

---

## ✅ SQL Query  

```sql
SELECT *
FROM Users
WHERE mail COLLATE utf8_bin REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';
```
---

## 🎯 Explanation

- COLLATE utf8_bin → ensures strict case-sensitive match.
- Regex breakdown:
  - ^ → start of string.
  - [A-Za-z] → first character must be a letter.
  - [A-Za-z0-9._-]* → rest of the prefix can include allowed characters.
  - @leetcode\.com$ → must end with @leetcode.com.