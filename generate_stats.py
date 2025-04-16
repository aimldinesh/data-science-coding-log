import os
import re
import datetime
from collections import Counter
import argparse

def detect_topic(content):
    if re.search(r"\b(sql)\b", content):
        return "SQL"
    elif re.search(r"\b(pandas|dataframe)\b", content):
        return "Pandas"
    else:
        return "DSA"

def detect_platform(content):
    if "leetcode" in content:
        return "LeetCode"
    elif "gfg" in content or "geeksforgeeks" in content:
        return "GFG"
    elif "strata" in content:
        return "StrataScratch"
    else:
        return "Other"

def main(dry_run=False):
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    current_month = today.strftime("%Y-%m")
    month_header = f"### 📅 {today.strftime('%B %Y')} ({current_month})"

    problem_count = 0
    topics = []
    platforms = []

    monthly_problem_count = 0
    total_problem_count = 0

    # Count problems for this week
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
                            topics.append(detect_topic(content))
                            platforms.append(detect_platform(content))

    # Count monthly/total from progress.md
    with open("progress.md", "r", encoding="utf-8") as progress_file:
        lines = progress_file.readlines()

    for line in lines:
        if line.startswith("| 20"):
            total_problem_count += 1
            if line.strip().split("|")[1].strip().startswith(current_month):
                monthly_problem_count += 1

    # Most common stats
    most_common_topic = Counter(topics).most_common(1)
    most_common_platforms = Counter(platforms).most_common(3)
    platform_summary = ", ".join(f"{name} ({count})" for name, count in most_common_platforms)

    # Write stats.md
    stats_content = [
        "## 📊 Weekly Progress\n\n",
        f"- ✅ Problems solved this week: **{problem_count}**\n",
        f"- 📚 Most frequent topic: **{most_common_topic[0][0]}**\n" if most_common_topic else "- 📚 Most frequent topic: N/A\n",
        f"- 🌐 Platforms used: {platform_summary if platforms else 'N/A'}\n"
    ]

    if not dry_run:
        with open("stats.md", "w", encoding="utf-8") as stats_file:
            stats_file.writelines(stats_content)

    # Update or insert month section in progress.md
    new_lines = []
    found_month_section = False
    inside_month_section = False

    for line in lines:
        if month_header in line:
            found_month_section = True
            inside_month_section = True
            new_lines.append(line)
            continue

        if inside_month_section:
            if line.strip().startswith("- ✅ Problems Solved This Month:"):
                line = f"- ✅ Problems Solved This Month: **{monthly_problem_count}**\n"
            elif line.strip().startswith("- 🎯 Total Problems Solved:"):
                line = f"- 🎯 Total Problems Solved: **{total_problem_count}**\n"
                inside_month_section = False

        new_lines.append(line)

    if not found_month_section:
        month_section = [
            f"\n{month_header}\n",
            f"- ✅ Problems Solved This Month: **{monthly_problem_count}**\n",
            f"- 🎯 Total Problems Solved: **{total_problem_count}**\n"
        ]
        new_lines.insert(2, "".join(month_section))  # Insert near the top (after title)

    if not dry_run:
        with open("progress.md", "w", encoding="utf-8") as progress_file:
            progress_file.writelines(new_lines)

    print("✅ stats.md and progress.md updated successfully!" if not dry_run else "🔍 Dry run completed. No files were modified.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate coding stats.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing to files")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
