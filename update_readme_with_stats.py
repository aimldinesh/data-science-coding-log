import re
import argparse

BADGES = """
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat&logo=leetcode&logoColor=black)
![Daily](https://img.shields.io/badge/Daily%20Coding-Yes-brightgreen)
"""

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def replace_between_markers(text, start_marker, end_marker, new_content):
    if start_marker in text and end_marker in text:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker)
        return text[:start] + "\n" + new_content + "\n" + text[end:]
    else:
        # If markers are not found, just add the new content at the end
        return text.strip() + f"\n\n{start_marker}\n{new_content}\n{end_marker}"

def create_progress_bar(current, total, bar_length=15):
    filled = int((current / total) * bar_length)
    bar = "█" * filled + "-" * (bar_length - filled)
    percentage = int((current / total) * 100)
    return f"[{bar}] {percentage}%"

def extract_monthly_progress(progress_md, goal):
    flat_text = "".join(progress_md.splitlines())
    match = re.search(r"Problems Solved This Month: \*\*(\d+)\*\*", flat_text)
    current = int(match.group(1)) if match else 0
    bar = create_progress_bar(current, goal)
    return f"{progress_md}\n- 📈 Progress: {bar}"

def insert_badges(readme):
    if BADGES.strip() not in readme:
        return BADGES + "\n" + readme
    return readme

def main(goal):
    stats_content = read_file("stats.md")
    progress_content = read_file("progress.md")
    readme = read_file("README.md")

    # Monthly section with emoji bar
    monthly_stats = extract_monthly_progress(progress_content, goal)

    # Replace sections between markers, ensuring not to add duplicates
    readme = replace_between_markers(readme, "<!-- STATS-START -->", "<!-- STATS-END -->", stats_content)
    readme = replace_between_markers(readme, "<!-- PROGRESS-START -->", "<!-- PROGRESS-END -->", progress_content)
    readme = replace_between_markers(readme, "<!-- MONTHLY-START -->", "<!-- MONTHLY-END -->", monthly_stats)

    # Add badges if missing
    readme = insert_badges(readme)

    # Save updated README
    write_file("README.md", readme)
    print("✅ GitHub README.md updated with latest stats, progress, and badges!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update README with progress stats.")
    parser.add_argument("--goal", type=int, default=30, help="Monthly goal for problems solved.")
    args = parser.parse_args()
    main(goal=args.goal)
