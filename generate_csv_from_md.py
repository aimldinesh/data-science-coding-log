import csv
from collections import defaultdict
import re

# Read the progress.md file
with open("progress.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Dictionary to hold date -> count of problems
daily_counts = defaultdict(int)

# Regex pattern to match markdown table rows
row_pattern = r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|"  # Matches the date at the beginning of the row

# Count problems per date
for line in lines:
    match = re.match(row_pattern, line)
    if match:
        date = match.group(1)
        daily_counts[date] += 1

# Sort by date
sorted_data = sorted(daily_counts.items())

# Write to CSV
with open("daily_stats.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Problems_Solved"])
    for date, count in sorted_data:
        writer.writerow([date, count])

print("✅ CSV created: daily_stats.csv")
