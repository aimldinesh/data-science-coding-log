import os
import datetime

def format_problem_title(title):
    return title.lower().replace(' ', '_').replace('(', '').replace(')', '')

def log_problem(problem_title, platform, tags):
    # Prepare data
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    folder_name = f"{date_today}"
    os.makedirs(folder_name, exist_ok=True)

    # Format problem link and tags
    file_name = format_problem_title(problem_title) + ".md"
    problem_md_link = f"./{folder_name}/{file_name}"
    tags_str = ', '.join(tags)

    # Create individual problem markdown file
    problem_md_path = os.path.join(folder_name, file_name)
    if not os.path.exists(problem_md_path):
        with open(problem_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {problem_title}\n\n")
            f.write(f"- 📅 Date: {date_today}\n")
            f.write(f"- 🏷️ Platform: {platform}\n")
            f.write(f"- 🧠 Tags: {tags_str}\n")
            f.write("\n## 💡 Problem Description\n\n*(Add problem description here)*\n")
            f.write("\n## 🚀 Solution\n\n*(Add your solution here)*\n")

    # Format table entry
    new_entry = f"| {date_today} | [{problem_title}]({problem_md_link}) | {platform} | {tags_str} |\n"

    # Update progress.md
    progress_path = 'progress.md'
    if not os.path.exists(progress_path):
        with open(progress_path, 'w', encoding='utf-8') as f:
            f.write("# 📊 Daily Coding Progress Log\n\n")
            f.write("### 📅 April 2025 (2025-04)\n")
            f.write("- ✅ Problems Solved This Month: **0**\n")
            f.write("- 🎯 Total Problems Solved: **0**\n\n")
            f.write("This file tracks my daily problem-solving activity and overall progress. Each entry logs the problems solved, platform used, and topics practiced.\n\n")
            f.write("---\n\n")
            f.write("| Date       | Problem Name | Platform  | Tags |\n")
            f.write("|------------|--------------|-----------|------|\n")
            f.write(new_entry)
            return

    with open(progress_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Insert before '---' line above Summary
    insert_index = None
    for i in range(len(lines)):
        if lines[i].strip() == '---' and i + 1 < len(lines) and '📈 Summary' in lines[i + 1]:
            insert_index = i
            break

    if insert_index is not None:
        lines.insert(insert_index, new_entry)
        with open(progress_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"✅ Logged: {problem_title}")
    else:
        print("⚠️ Couldn't find the right place to insert in progress.md. Please check the format.")

if __name__ == "__main__":
    # Example usage
    problem_title = "Single Element in a Sorted Array"
    platform = "LeetCode"
    tags = ["Binary Search", "Array", "DSA"]
    log_problem(problem_title, platform, tags)
