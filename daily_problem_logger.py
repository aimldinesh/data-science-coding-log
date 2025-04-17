import os
from datetime import datetime, timedelta
import subprocess
from collections import Counter, defaultdict
import re

# 1. Get today's date
today = datetime.today().strftime('%Y-%m-%d')

# 2. Inputs
date_input = input(f"🗕️ Enter date (default: {today}): ") or today
problem_name = input("🧠 Problem name (e.g., Two Sum): ").strip()
platform = input("🌐 Platform (e.g., LeetCode, GFG): ").strip()
difficulty = input("⚙️ Difficulty (Easy/Medium/Hard): ").strip()
tags = input("🏷️ Tags (comma separated, e.g., DSA, SQL, Pandas): ").strip()
problem_link = input("🔗 Problem link (optional): ").strip()
submission_link = input("✅ Your solution link (optional): ").strip()

# 3. File prep
folder_path = os.path.join(".", date_input)
os.makedirs(folder_path, exist_ok=True)

file_name = problem_name.strip().lower().replace(" ", "_") + ".md"
file_path = os.path.join(folder_path, file_name)

# 4. Markdown content
markdown = (
    f"# 🧲 Problem: {problem_name}\n\n"
    f"- **Platform**: [{platform}]({problem_link if problem_link else '#'})\n"
    f"- **Submission**: [{submission_link if submission_link else 'Not provided'}]({submission_link if submission_link else '#'})\n"
    f"- **Date Solved**: {date_input}\n"
    f"- **Tags**: {tags}\n"
    f"- **Difficulty**: {difficulty}\n\n"
    f"---\n\n"
    f"## ✅ Problem Statement\n"
    f"*(Write a brief summary or paste problem link)*\n\n"
    f"---\n\n"
    f"## 🚀 My Approach\n"
    f"*(Explain your logic in simple terms)*\n\n"
    f"---\n\n"
    f"## 💻 Code (Python)\n\n"
    f"```python\n"
    f"# Paste your solution here\n"
    f"```\n\n"
    f"---\n\n"
    f"## 💡 Time and Space Complexity\n"
    f"- **Time**: O(?)\n"
    f"- **Space**: O(?)\n"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"\n✅ Created: {file_path}")

# 5. Open file in VS Code
try:
    subprocess.run(["code", file_path])
except:
    print("⚠️ Could not open in VS Code.")

input("\n✍️ Fill out your markdown file in VS Code.\n✅ When you're done, press Enter here to commit and update stats...")

# 6. Update tracker table
tracker_path = "progress.md"
tracker_line = f"| {date_input} | [{problem_name}]({file_path.replace(' ', '%20')}) | {platform} | {difficulty} | {tags} |\n"

if not os.path.exists(tracker_path):
    with open(tracker_path, "w", encoding="utf-8") as f:
        f.write("| Date | Problem | Platform | Difficulty | Tags |\n")
        f.write("|------|---------|----------|------------|------|\n")

with open(tracker_path, "a", encoding="utf-8") as f:
    f.write(tracker_line)

# 7. Analyze past logs to update stats

def analyze_logs(directory="."):
    tag_counter = Counter()
    problems_per_day = defaultdict(int)
    solved_dates = set()

    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path) and re.match(r"\d{4}-\d{2}-\d{2}", folder):
            for file in os.listdir(folder_path):
                if file.endswith(".md"):
                    file_path = os.path.join(folder_path, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        date_match = re.search(r"\*\*Date Solved\*\*: (\d{4}-\d{2}-\d{2})", content)
                        tags_match = re.search(r"\*\*Tags\*\*: (.+)", content)
                        if date_match:
                            solved_date = date_match.group(1)
                            problems_per_day[solved_date] += 1
                            solved_dates.add(solved_date)
                        if tags_match:
                            tags = tags_match.group(1).split(",")
                            tag_counter.update(tag.strip() for tag in tags)

    today = datetime.today()
    week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    month_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")

    weekly_count = sum(v for k, v in problems_per_day.items() if k >= week_ago)
    monthly_count = sum(v for k, v in problems_per_day.items() if k >= month_ago)
    streak = 0
    current = today
    while current.strftime("%Y-%m-%d") in solved_dates:
        streak += 1
        current -= timedelta(days=1)

    most_common_tags = tag_counter.most_common(5)
    return weekly_count, monthly_count, most_common_tags, streak

# 8. Update stats.md
weekly, monthly, top_tags, streak = analyze_logs()
with open("stats.md", "w", encoding="utf-8") as f:
    f.write("# 📊 Coding Practice Stats\n\n")
    f.write(f"- ✅ Problems solved this week: **{weekly}**\n")
    f.write(f"- 🗖️ Problems solved this month: **{monthly}**\n")
    f.write(f"- 📌 Current daily streak: **{streak} days**\n")
    f.write(f"- 🏷️ Most frequent tags: ")
    if top_tags:
        f.write(", ".join([f"**{tag}** ({count})" for tag, count in top_tags]))
    else:
        f.write("None yet.")
    f.write("\n")

# 9. Update README.md with stats and full problem table
readme_path = "README.md"

if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    with open("stats.md", "r", encoding="utf-8") as f:
        stats_content = f.read()

    with open("progress.md", "r", encoding="utf-8") as f:
        progress_content = f.read()

    readme_content = re.sub(
        r"<!-- STATS_START -->(.*?)<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{stats_content}\n<!-- STATS_END -->",
        readme_content,
        flags=re.DOTALL
    )

    readme_content = re.sub(
        r"<!-- PROBLEM_TABLE_START -->(.*?)<!-- PROBLEM_TABLE_END -->",
        f"<!-- PROBLEM_TABLE_START -->\n{progress_content}\n<!-- PROBLEM_TABLE_END -->",
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

# 10. Git Commit + Push
try:
    subprocess.run(["git", "add", file_path, tracker_path, "stats.md", readme_path], check=True)
    commit_message = f"🧠 Add: {problem_name} [{date_input}]"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("\n🚀 Successfully committed and pushed to GitHub with updated stats and README!")
except subprocess.CalledProcessError:
    print("⚠️ Git push failed. Make sure you're in a repo and authenticated.")
