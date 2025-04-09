import os
import datetime
from collections import Counter

# 1. Setup
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday())
problem_count = 0
topics = []
platforms = []

# 2. Loop through folders (assumed format: YYYY-MM-DD)
for folder in os.listdir():
    if os.path.isdir(folder):
        try:
            folder_date = datetime.datetime.strptime(folder, "%Y-%m-%d").date()
        except ValueError:
            continue  # skip non-date folders

        if folder_date >= start_of_week:
            for file in os.listdir(folder):
                if file.endswith(".md"):
                    problem_count += 1
                    file_path = os.path.join(folder, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().lower()
                        # Extract topic tags from section titles or keywords
                        if "sql" in content:
                            topics.append("SQL")
                        elif "pandas" in content:
                            topics.append("Pandas")
                        elif "dataframe" in content:
                            topics.append("Pandas")
                        else:
                            topics.append("DSA")

                        # Extract platform
                        if "leetcode" in content:
                            platforms.append("LeetCode")
                        elif "gfg" in content or "geeksforgeeks" in content:
                            platforms.append("GFG")
                        elif "strata" in content:
                            platforms.append("StrataScratch")

# 3. Get stats
most_common_topic = Counter(topics).most_common(1)
most_common_platform = Counter(platforms).most_common(1)

# 4. Write to stats.md
with open("stats.md", "w", encoding="utf-8") as stats_file:
    stats_file.write("## 📊 Weekly Progress\n\n")
    stats_file.write(f"- Problems solved this week: {problem_count}\n")
    stats_file.write(f"- Most frequent topic: {most_common_topic[0][0] if most_common_topic else 'N/A'}\n")
    stats_file.write(f"- Platform(s): {', '.join(set(platforms)) if platforms else 'N/A'}\n")

print("✅ stats.md updated successfully!")
