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
![Problems Solved](https://img.shields.io/badge/Problems_Solved-{problems_solved}-brightgreen)
![Platform](https://img.shields.io/badge/Platform-{platforms_used.replace(" ", "_")}-orange)
![Focus Topic](https://img.shields.io/badge/Focus-{most_frequent_topic.replace(" ", "_")}-blue)
![Last Updated](https://img.shields.io/badge/Last_Updated-{date_today}-informational)
"""

    # New content for README
    new_content = f"""
{badges}

## 📊 Weekly Stats for {date_today}

- ✅ Problems solved this week: **{problems_solved}**
- 📚 Most frequent topic: **{most_frequent_topic}**
- 🌐 Platforms used: {platforms_used}

## 📈 Weekly Progress

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

    # Prepend new content
    updated_readme = new_content + "\n" + old_content

    with open(readme_file, 'w', encoding='utf-8') as file:  # Ensure UTF-8 encoding
        file.write(updated_readme)

    print(f"✅ README updated successfully for {date_today} with badges and progress.")

if __name__ == "__main__":
    update_readme_with_stats()
