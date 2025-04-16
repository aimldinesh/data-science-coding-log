import os
import datetime

def update_readme_with_stats(stats_file='stats.md', progress_file='progress.md', readme_file='README.md'):
    # Read stats from stats.md
    if not os.path.exists(stats_file):
        print(f"Error: {stats_file} does not exist.")
        return

    with open(stats_file, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        stats_content = file.read()

    # Extract values
    problems_solved = None
    most_frequent_topic = None
    platforms_used = None

    for line in stats_content.split('\n'):
        if 'Problems solved this week:' in line:
            problems_solved = line.split(':')[1].strip().split(' ')[0]
        elif 'Most frequent topic:' in line:
            most_frequent_topic = line.split(':')[1].strip()
        elif 'Platforms used:' in line:
            platforms_used = line.split(':')[1].strip()

    if not all([problems_solved, most_frequent_topic, platforms_used]):
        print("Error: Could not extract all necessary data from stats.md.")
        return

    # Read progress.md
    if not os.path.exists(progress_file):
        print(f"Error: {progress_file} does not exist.")
        return

    with open(progress_file, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        progress_content = file.read()

    # Today's date
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')

    # Build badge section
    badges = f"""
![LeetCode](https://img.shields.io/badge/LeetCode-{problems_solved}-brightgreen)
![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-{problems_solved}-brightgreen)
![HackerRank](https://img.shields.io/badge/HackerRank-{problems_solved}-brightgreen)
![DSA](https://img.shields.io/badge/DSA-{problems_solved}-brightgreen)
![Data Science](https://img.shields.io/badge/Data_Science-{problems_solved}-brightgreen)
![Artificial Intelligence](https://img.shields.io/badge/AI-{problems_solved}-brightgreen)
"""

    # New content for README
    new_content = f"""
{badges}

## 📊 Weekly Stats for {date_today}

- ✅ Problems solved this week: **{problems_solved}**
- 📚 Most frequent topic: **{most_frequent_topic}**
- 🌐 Platforms used: {platforms_used}


{progress_content}
"""

    # Read or create README.md
    if not os.path.exists(readme_file):
        with open(readme_file, 'w', encoding='utf-8') as file:  # Ensure UTF-8 encoding
            file.write("# My Coding Journey\n\n")
            file.write(new_content)
        print(f"Created and updated {readme_file} for {date_today}.")
        return

    with open(readme_file, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        old_content = file.read()

    # Check if today's content is already present
    if new_content in old_content:
        print("No update needed: Today's stats and progress already exist in the README.")
        return

    # Prepend new content if it's not already in the README
    updated_readme = new_content + "\n" + old_content

    with open(readme_file, 'w', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        file.write(updated_readme)

    print(f"✅ README updated successfully for {date_today} with badges and progress.")

if __name__ == "__main__":
    update_readme_with_stats()
