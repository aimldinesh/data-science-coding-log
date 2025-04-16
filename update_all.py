# update_all.py

import subprocess
import os

# Optional: Set working directory if running from a different location
# os.chdir("/path/to/your/project")

# Step 1: Run the daily logger script to create a new problem entry (if any)
subprocess.run(["python", "daily_problem_logger.py"])

# Step 2: Run the script to generate stats and update monthly counts
subprocess.run(["python", "generate_stats.py"])

# Step 3: Update the README.md file with latest stats, progress, and badges
subprocess.run(["python", "update_readme_with_stats.py"])

# Step 4: Git add, commit, and push the updates
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "🔁 Daily update"])
subprocess.run(["git", "push"])

print("✅ All scripts executed and GitHub updated successfully!")
