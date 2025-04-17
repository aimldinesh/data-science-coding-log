import os
from datetime import datetime, timedelta
import subprocess
from collections import Counter, defaultdict
import re

# 1. Get today's date
today = datetime.today().strftime('%Y-%m-%d')

# 2. Inputs
date_input = input(f"📅 Enter date (default: {today}): ") or today
problem_name = input("🧠 Problem name (e.g., Two Sum): ").strip()
platform = input("🌐 Platform (e.g., LeetCode, GFG): ").strip()
tags = input("🏷️ Tags (comma separated, e.g., DSA, SQL, Pandas): ").strip()
difficulty = input("💡 Difficulty (easy, medium, hard): ").strip()
problem_link = input("🔗 Problem link (optional): ").strip()
submission_link = input("✅ Your solution link (optional): ").strip()
review_link = input("🔍 Code review link (optional): ").strip()

# 3. Time Tracking
start_time = input("⏳ Start time (HH:MM, optional): ").strip()
end_time = input("⏳ End time (HH:MM, optional): ").strip()

# 4. File prep
folder_path = os.path.join(".", date_input)
os.makedirs(folder_path, exist_ok=True)

file_name = problem_name.strip().lower().replace(" ", "_") + ".md"
file_path = os.path.join(folder_path, file_name)

# 5. Markdown content
markdown = (
    f"# 🧮 Problem: {problem_name}\n\n"
    f"- **Platform**: [{platform}]({problem_link if problem_link else '#'})\n"
    f"- **Submission**: [{submission_link if submission_link else 'Not provided'}]({submission_link if submission_link else '#'})\n"
    f"- **Date Solved**: {date_input}\n"
    f"- **Tags**: {tags}\n"
    f"- **Difficulty**: {difficulty}\n"
    f"- **Code Review**: [{review_link if review_link else 'Not provided'}]({review_link if review_link else '#'})\n"
    f"- **Time Taken**: {start_time} - {end_time}\n\n"
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

# 6. Open file in VS Code
try:
    subprocess.run(["code", file_path])
except:
    print("⚠️ Could not open in VS Code.")

input("\n✍️ Fill out your markdown file in VS Code.\n✅ When you're done, press Enter here to commit and update stats...")

# 7. Update tracker table
tracker_path = "progress.md"
tracker_line = f"| {date_input} | [{problem_name}]({file_path.replace(' ', '%20')}) | {platform} | {tags} | {difficulty} |\n"

if not os.path.exists(tracker_path):
    with open(tracker_path, "w", encoding="utf-8") as f:
        f.write("| Date | Problem | Platform | Tags | Difficulty |\n")
        f.write("|------|---------|----------|------|------------|\n")

with open(tracker_path, "a", encoding="utf-8") as f:
    f.write(tracker_line)

# 8. Analyze past logs to update stats
def analyze_logs(directory="."):
    tag_counter = Counter()
    problems_per_day = defaultdict(int)
    difficulty_counter = Counter()

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
                        difficulty_match = re.search(r"\*\*Difficulty\*\*: (.+)", content)
                        if date_match:
                            solved_date = date_match.group(1)
                            problems_per_day[solved_date] += 1
                        if tags_match:
                            tags = tags_match.group(1).split(",")
                            tag_counter.update(tag.strip() for tag in tags)
                        if difficulty_match:
                            difficulty = difficulty_match.group(1)
                            difficulty_counter[difficulty] += 1

    today = datetime.today()
    week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    month_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")

    weekly_count = sum(v for k, v in problems_per_day.items() if k >= week_ago)
    monthly_count = sum(v for k, v in problems_per_day.items() if k >= month_ago)

    most_common_tags = tag_counter.most_common(5)
    most_common_difficulties = difficulty_counter.most_common(3)

    return weekly_count, monthly_count, most_common_tags, most_common_difficulties

# 9. Update stats.md
weekly_count, monthly_count, most_common_tags, most_common_difficulties = analyze_logs()
with open("stats.md", "w", encoding="utf-8") as f:
    f.write("# 📊 Coding Practice Stats\n\n")
    f.write(f"- ✅ Problems solved this week: **{weekly_count}**\n")
    f.write(f"- 📆 Problems solved this month: **{monthly_count}**\n")
    f.write(f"- 🏷️ Most frequent tags: ")
    if most_common_tags:
        f.write(", ".join([f"**{tag}** ({count})" for tag, count in most_common_tags]))
    else:
        f.write("None yet.")
    f.write("\n")
    f.write(f"- 🧠 Most frequent difficulty levels: ")
    if most_common_difficulties:
        f.write(", ".join([f"**{level}** ({count})" for level, count in most_common_difficulties]))
    else:
        f.write("None yet.")
    f.write("\n")

# 10. Update README.md between <!-- STATS_START --> and <!-- STATS_END -->
readme_path = "README.md"
stats_path = "stats.md"

if os.path.exists(readme_path) and os.path.exists(stats_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    with open(stats_path, "r", encoding="utf-8") as f:
        stats_content = f.read()

    updated_readme = re.sub(
        r"<!-- STATS_START -->(.*?)<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{stats_content}\n<!-- STATS_END -->",
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_readme)

# 11. Git Commit + Push
try:
    subprocess.run(["git", "add", file_path, tracker_path, "stats.md", readme_path], check=True)
    commit_message = f"🧠 Add: {problem_name} [{date_input}]"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("\n🚀 Successfully committed and pushed to GitHub with updated stats and README!")
except subprocess.CalledProcessError:
    print("⚠️ Git push failed. Make sure you're in a repo and authenticated.")
