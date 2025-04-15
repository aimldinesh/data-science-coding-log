# update_readme_with_stats.py

# 1. Read stats from stats.md
with open("stats.md", "r", encoding="utf-8") as stats_file:
    stats_content = stats_file.read().strip()

# 2. Read progress from progress.md
with open("progress.md", "r", encoding="utf-8") as progress_file:
    progress_content = progress_file.read().strip()

# 3. Read README.md
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Helper function to safely replace content between markers
def replace_between_markers(text, start_marker, end_marker, new_content):
    if start_marker in text and end_marker in text:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker)
        return text[:start] + "\n" + new_content + "\n" + text[end:]
    else:
        return text.strip() + f"\n\n{start_marker}\n{new_content}\n{end_marker}"

# Function to create an emoji progress bar
def create_progress_bar(current, total, bar_length=15):
    filled = int((current / total) * bar_length)
    bar = "█" * filled + "-" * (bar_length - filled)
    percentage = int((current / total) * 100)
    return f"[{bar}] {percentage}%"

# Extract current month problem count and generate progress bar
monthly_stats_raw = "".join(progress_content.splitlines()).strip()

import re
match = re.search(r"Problems Solved This Month: \*\*(\d+)\*\*", monthly_stats_raw)
current_count = int(match.group(1)) if match else 0
goal = 30  # Customize this goal
progress_bar = create_progress_bar(current_count, goal)

# Add progress bar to the monthly stats
monthly_stats = f"{monthly_stats_raw}\n- 📈 Progress: {progress_bar}"

# Replace stats section in the README
readme = replace_between_markers(readme, "<!-- STATS-START -->", "<!-- STATS-END -->", stats_content)

# Replace progress section in the README
readme = replace_between_markers(readme, "<!-- PROGRESS-START -->", "<!-- PROGRESS-END -->", progress_content)

# Check if monthly stats section exists already and update it, or add if not
if "<!-- MONTHLY-START -->" in readme and "<!-- MONTHLY-END -->" in readme:
    # If the monthly section exists, replace it
    readme = replace_between_markers(readme, "<!-- MONTHLY-START -->", "<!-- MONTHLY-END -->", monthly_stats)
else:
    # If it doesn't exist, add it at the end of the README
    readme = readme.strip() + f"\n\n<!-- MONTHLY-START -->\n{monthly_stats}\n<!-- MONTHLY-END -->"

# Optional: Add color badges at the top of README
badges = """
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat&logo=leetcode&logoColor=black)
![Daily](https://img.shields.io/badge/Daily%20Coding-Yes-brightgreen)
"""

# Insert badges at the top of the README (after the title, for example)
readme = badges + readme

# 4. Write updated README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme)

print("✅ GitHub README.md updated with latest stats, progress, and badges!")
