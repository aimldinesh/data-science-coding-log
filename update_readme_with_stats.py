import re

# 1. Read stats from stats.md
with open("stats.md", "r", encoding="utf-8") as stats_file:
    stats_content = stats_file.read()

# 2. Read progress from progress.md
with open("progress.md", "r", encoding="utf-8") as progress_file:
    progress_content = progress_file.read()

# 3. Read current README.md
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

# 4. Replace the stats section between markers
start_marker = "<!-- STATS-START -->"
end_marker = "<!-- STATS-END -->"

if start_marker in readme and end_marker in readme:
    updated_readme = re.sub(
        f"{start_marker}.*?{end_marker}",
        f"{start_marker}\n{stats_content.strip()}\n{end_marker}",
        readme,
        flags=re.DOTALL
    )
else:
    # If markers don't exist, add them at the end
    updated_readme = readme.strip() + f"\n\n{start_marker}\n{stats_content.strip()}\n{end_marker}"

# 5. Replace the progress section between markers
progress_start_marker = "<!-- PROGRESS-START -->"
progress_end_marker = "<!-- PROGRESS-END -->"

if progress_start_marker in updated_readme and progress_end_marker in updated_readme:
    updated_readme = re.sub(
        f"{progress_start_marker}.*?{progress_end_marker}",
        f"{progress_start_marker}\n{progress_content.strip()}\n{progress_end_marker}",
        updated_readme,
        flags=re.DOTALL
    )
else:
    # If markers don't exist, add them at the end
    updated_readme = updated_readme.strip() + f"\n\n{progress_start_marker}\n{progress_content.strip()}\n{progress_end_marker}"

# 6. Write the updated README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(updated_readme)

print("✅ GitHub README.md updated with latest stats and progress!")
