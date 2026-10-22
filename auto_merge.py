import os
import subprocess
import time

def run_command(command):
    """Executes a system command and returns the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error executing: {command}\n{result.stderr}")
    return result.returncode == 0

def main():
    # Configure git dummy identity for the runner
    run_command('git config --global user.name "Merged Bot"')
    run_command('git config --global user.email "merged-bot@example.com"')
    
    # Target loops per run (GitHub Actions jobs have a 6-hour limit, 50-100 is safe and fast)
    total_merges = 50 
    
    print(f"🚀 Starting the automation of {total_merges} merges...")

    for i in range(1, total_merges + 1):
        timestamp = time.time()
        branch_name = f"feature/merge-increment-{timestamp}"
        
        # 1. Create and checkout to a new branch
        if not run_command(f"git checkout -b {branch_name}"):
            continue
            
        # 2. Make a unique modification
        with open("merge_log.txt", "a") as f:
            f.write(f"Merge counter automated update at timestamp: {timestamp}\n")
            
        # 3. Stage and commit the change in the feature branch
        run_command("git add merge_log.txt")
        if not run_command(f'git commit -m "feat: adding logs for merge pulse {timestamp}"'):
            # If nothing changed, revert to main and clean up
            run_command("git checkout main")
            run_command(f"git branch -D {branch_name}")
            continue
            
        # 4. Switch back to the main branch
        run_command("git checkout main")
        
        # 5. Merge the feature branch into main (forcing a merge commit)
        print(f"⚡ Merging {branch_name} into main [{i}/{total_merges}]...")
        run_command(f'git merge {branch_name} --no-ff -m "Merge branch \'{branch_name}\' into main [Automated]"')
        
        # 6. Delete the temporary local branch to keep it clean
        run_command(f"git branch -D {branch_name}")
        
    print("🎯 Batch completed! Preparing to push changes to GitHub...")

if __name__ == "__main__":
    main()
