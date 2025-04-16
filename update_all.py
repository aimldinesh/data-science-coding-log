# update_all.py

import subprocess
import os
import sys

def run_command(command):
    """ Run a command using subprocess and check for errors. """
    try:
        subprocess.run(command, check=True)
        print(f"✅ {command[0]} executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {e.cmd}")
        sys.exit(1)

def main(commit_message="🔁 Daily update"):
    # Step 1: Run the daily logger script to create a new problem entry (if any)
    run_command(["python", "daily_problem_logger.py"])

    # Step 2: Run the script to generate stats and update monthly counts
    run_command(["python", "generate_stats.py"])

    # Step 3: Update the README.md file with latest stats, progress, and badges
    run_command(["python", "update_readme_with_stats.py"])

    # Step 4: Git add, commit, and push the updates
    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", commit_message])
    run_command(["git", "push"])

    print("✅ All scripts executed and GitHub updated successfully!")

if __name__ == "__main__":
    # Optional: Pass a custom commit message as a command-line argument
    commit_message = sys.argv[1] if len(sys.argv) > 1 else "🔁 Daily update"
    main(commit_message)
