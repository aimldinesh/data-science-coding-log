import os
import re
import subprocess
from datetime import datetime, timedelta
from collections import Counter, defaultdict


def get_input(prompt: str, default: str = "") -> str:
    return input(prompt).strip() or default


def create_markdown(problem_name: str, platform: str, tags: str, date_input: str, problem_link: str, submission_link: str) -> str:
    return (
        f"# 🧮 Problem: {problem_name}\n\n"
        f"- **Platform**: [{platform}]({problem_link or '#'})\n"
        f"- **Submission**: [{submission_link or 'Not provided'}]({submission_link or '#'})\n"
        f"- **Date Solved**: {date_input}\n"
        f"- **Tags**: {tags}\n\n"
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


def update_progress_tracker(tracker_path: str, date_input: str, problem_name: str, file_path: str, platform: str, tags: str):
    if not os.path.exists(tracker_path):
        with open(tracker_path, "w", encoding="utf-8") as f:
            f.write("| Date | Problem | Platform | Tags |\n")
            f.write("|------|---------|----------|------|\n")

    # Generate correct relative path and encode spaces
    relative_path = os.path.relpath(file_path, os.path.dirname(tracker_path)).replace("\\", "/")
    relative_path = relative_path.replace(" ", "%20")

    line = f"| {date_input} | [{problem_name}]({relative_path}) | {platform} | {tags} |\n"

    # Avoid duplicate entries
    with open(tracker_path, "r+", encoding="utf-8") as f:
        content = f.read()
        if problem_name not in content:
            f.write(line)


def analyze_logs(directory: str = "."):
    tag_counter = Counter()
    problems_per_day = defaultdict(int)

    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path) and re.match(r"\d{4}-\d{2}-\d{2}", folder):
            for file in os.listdir(folder_path):
                if file.endswith(".md"):
                    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                        content = f.read()
                        date_match = re.search(r"\*\*Date Solved\*\*: (\d{4}-\d{2}-\d{2})", content)
                        tags_match = re.search(r"\*\*Tags\*\*: (.+)", content)
                        if date_match:
                            solved_date = date_match.group(1)
                            problems_per_day[solved_date] += 1
                        if tags_match:
                            tag_counter.update(tag.strip() for tag in tags_match.group(1).split(","))

    today = datetime.today()
    week_ago = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    month_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")

    weekly_count = sum(count for date, count in problems_per_day.items() if date >= week_ago)
    monthly_count = sum(count for date, count in problems_per_day.items() if date >= month_ago)
    most_common_tags = tag_counter.most_common(5)

    return weekly_count, monthly_count, most_common_tags


def update_stats_md(weekly_count: int, monthly_count: int, most_common_tags: list):
    with open("stats.md", "w", encoding="utf-8") as f:
        f.write("# 📊 Coding Practice Stats\n\n")
        f.write(f"- ✅ Problems solved this week: **{weekly_count}**\n")
        f.write(f"- 📆 Problems solved this month: **{monthly_count}**\n")
        f.write(f"- 🏷️ Most frequent tags: ")
        f.write(", ".join([f"**{tag}** ({count})" for tag, count in most_common_tags]) if most_common_tags else "None yet.")
        f.write("\n")


def git_commit_push(files: list, message: str):
    try:
        subprocess.run(["git", "add"] + files, check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("\n🚀 Successfully committed and pushed to GitHub with updated stats!")
    except subprocess.CalledProcessError:
        print("⚠️ Git push failed. Make sure you're in a Git repo and authenticated.")


def main():
    today = datetime.today().strftime('%Y-%m-%d')

    # Inputs
    date_input = get_input(f"📅 Enter date (default: {today}): ", today)
    problem_name = get_input("🧠 Problem name (e.g., Two Sum): ")
    platform = get_input("🌐 Platform (e.g., LeetCode, GFG): ")
    tags = get_input("🏷️ Tags (comma separated, e.g., DSA, SQL, Pandas): ")
    problem_link = get_input("🔗 Problem link (optional): ")
    submission_link = get_input("✅ Your solution link (optional): ")

    # File handling
    folder_path = os.path.join(".", date_input)
    os.makedirs(folder_path, exist_ok=True)

    file_name = problem_name.lower().replace(" ", "_") + ".md"
    file_path = os.path.normpath(os.path.join(folder_path, file_name))

    # Write markdown
    markdown_content = create_markdown(problem_name, platform, tags, date_input, problem_link, submission_link)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"\n✅ Created: {file_path}")

    # Open in VS Code
    try:
        subprocess.run(["code", file_path])
    except Exception:
        print("⚠️ Could not open in VS Code.")

    input("\n✍️ Fill out your markdown file in VS Code.\n✅ When you're done, press Enter here to commit and update stats...")

    # Update tracker
    tracker_path = os.path.join(".", "progress.md")
    update_progress_tracker(tracker_path, date_input, problem_name, file_path, platform, tags)

    # Analyze logs and update stats
    weekly_count, monthly_count, most_common_tags = analyze_logs()
    update_stats_md(weekly_count, monthly_count, most_common_tags)

    # Git commit and push
    commit_msg = f"🧠 Add: {problem_name} [{date_input}]"
    git_commit_push([file_path, tracker_path, "stats.md"], commit_msg)


if __name__ == "__main__":
    main()
