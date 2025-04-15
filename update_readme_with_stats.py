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

# 4. Replace stats section
readme = replace_between_markers(readme, "<!-- STATS-START -->", "<!-- STATS-END -->", stats_content)

# 5. Replace progress section
readme = replace_between_markers(readme, "<!-- PROGRESS-START -->", "<!-- PROGRESS-END -->", progress_content)

# 6. Write updated README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme)

print("✅ GitHub README.md updated with latest stats and progress!")
