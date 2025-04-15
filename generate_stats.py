import os
import datetime
from collections import Counter

# 1. Setup
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday())
current_month = today.strftime("%Y-%m")
problem_count = 0
topics = []
platforms = []

# Count problems for current month
monthly_problem_count = 0
total_problem_count = 0

# 2. Loop through folders (assumed format: YYYY-MM-DD)
for folder in os.listdir():
    if os.path.isdir(folder):
        try:
            folder_date = datetime.datetime.strptime(folder, "%Y-%m-%d").date()
        except ValueError:
            continue  # skip non-date folders

        # Weekly count
        if folder_date >= start_of_week:
            for file in os.listdir(folder):
                if file.endswith(".md"):
                    problem_count += 1
                    file_path = os.path.join(folder, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().lower()
                        # Extract topic tags
                        if "sql" in content:
                            topics.append("SQL")
                        elif "pandas" in content or "dataframe" in content:
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

# 3. Count problems from progress.md for monthly & total stats
with open("progress.md", "r", encoding="utf-8") as progress_file:
    lines = progress_file.readlines()
    for line in lines:
        if line.startswith("| 20"):
            total_problem_count += 1
            if line.strip().split("|")[1].strip().startswith(current_month):
                monthly_problem_count += 1

# 4. Get stats
most_common_topic = Counter(topics).most_common(1)
most_common_platform = Counter(platforms).most_common(1)

# 5. Write to stats.md
with open("stats.md", "w", encoding="utf-8") as stats_file:
    stats_file.write("## 📊 Weekly Progress\n\n")
    stats_file.write(f"- Problems solved this week: {problem_count}\n")
    stats_file.write(f"- Most frequent topic: {most_common_topic[0][0] if most_common_topic else 'N/A'}\n")
    stats_file.write(f"- Platform(s): {', '.join(set(platforms)) if platforms else 'N/A'}\n")

# 6. Update monthly stats in progress.md
new_lines = []
inside_month_section = False
for line in lines:
    if line.strip().startswith("### 📅") and current_month in line:
        inside_month_section = True
        new_lines.append(line)
        continue

    if inside_month_section and line.strip().startswith("- ✅ Problems Solved This Month:"):
        line = f"- ✅ Problems Solved This Month: **{monthly_problem_count}**\n"
    elif inside_month_section and line.strip().startswith("- 🎯 Total Problems Solved:"):
        line = f"- 🎯 Total Problems Solved: **{total_problem_count}**\n"
        inside_month_section = False

    new_lines.append(line)

with open("progress.md", "w", encoding="utf-8") as progress_file:
    progress_file.writelines(new_lines)

print("✅ stats.md and monthly progress in progress.md updated successfully!")
