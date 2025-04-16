import os
import datetime

def create_markdown_for_problem(problem_name, date, platform, tags):
    # Create directory for the day if it doesn't exist
    date_str = date.strftime('%Y-%m-%d')
    directory = f"{date_str}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Markdown file for each problem solved
    problem_file = os.path.join(directory, f"{problem_name.lower().replace(' ', '_')}.md")
    
    # Content of the problem's markdown file
    content = f"# {problem_name}\n\n" \
              f"Problem solved on: {date_str}\n\n" \
              f"Platform: {platform}\n\n" \
              f"Tags: {', '.join(tags)}\n\n" \
              f"Link to the problem: [LeetCode Link](https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}))"
    
    # Writing the content into the markdown file
    with open(problem_file, 'w') as file:
        file.write(content)
    
    return problem_file


def log_problem_to_progress(problem_name, date, platform, tags):
    date_str = date.strftime('%Y-%m-%d')
    progress_file = 'progress.md'
    
    # Check if progress file exists; if not, create it
    if not os.path.exists(progress_file):
        with open(progress_file, 'w') as file:
            file.write("# 📊 Daily Coding Progress Log\n\n")
            file.write("### 📅 April 2025 (2025-04)\n")
            file.write("- ✅ Problems Solved This Month: **0**\n")
            file.write("- 🎯 Total Problems Solved: **0**\n")
            file.write("This file tracks my daily problem-solving activity and overall progress. Each entry logs the problems solved, platform used, and topics practiced.\n")
            file.write("\n---\n")
            file.write("| Date       | Problem Name  | Platform  | Tags |\n")
            file.write("|------------|---------------|-----------|------|\n")
    
    # Open progress file to append data
    with open(progress_file, 'a') as file:
        file.write(f"| {date_str} | [{problem_name}](./{date_str}/{problem_name.lower().replace(' ', '_')}.md) | {platform} | {', '.join(tags)} |\n")


def main():
    # Example problem names and date
    problem_name = "Two Sum"  # Change this dynamically as per your input
    platform = "LeetCode"  # Platform (e.g., LeetCode)
    tags = ["Array", "Hash Map", "DSA"]  # Tags related to the problem
    date_today = datetime.datetime.today()  # Get today's date
    
    # Create a markdown file for the problem
    create_markdown_for_problem(problem_name, date_today, platform, tags)
    
    # Log the problem in progress.md file
    log_problem_to_progress(problem_name, date_today, platform, tags)
    
    print(f"Logged problem '{problem_name}' for {date_today.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
