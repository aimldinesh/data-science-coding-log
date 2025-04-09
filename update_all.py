# update_all.py
import subprocess
import os

# Step 1: Run the daily problem logger
subprocess.run(["python", "daily_problem_logger.py"])

# Step 2: Run stats updater
subprocess.run(["python", "generate_stats.py"])

# Step 3: Update README.md with stats
subprocess.run(["python", "update_readme_with_stats.py"])

# Step 4: Git add, commit, and push
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "🔁 Daily update"])
subprocess.run(["git", "push"])
