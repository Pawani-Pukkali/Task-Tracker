Mac Bash Script & Git Workflow Guide
1. Setting Up Your Mac Environment
a. Install Homebrew:
Homebrew acts as a package manager for macOS. Install it using:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

b. Configure Environment Path:
Ensure the installed binaries are in your environment path:

echo $PATH
export PATH="$PATH:/opt/homebrew/bin"

Reload the shell configuration:

source ~/.zshrc

c. Check and Install Essential Tools:
Verify Git and Python installation:

which git
which python

If not installed:

brew install git
brew install python

d. Install Docker & VS Code:
Download from their official websites and VS Code.

e. Set Global Git Configuration:

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

2. Directory Management
Create required directories:

mkdir -p ~/projects/devops

The -p flag ensures parent directories are created as needed.

3. Git Commit Flow for DevOps Engineers
Understanding Git’s code flow enhances collaboration:

Git Workflow:
Working Directory → (git add) → Staging Area → (git commit) → Local Repository → (git push) → Remote Repository (GitHub/GitLab)

a. Working Directory:
Where you modify files.

git status          # Check modified/untracked files
git diff            # View changes

b. Staging Area:
Prepare files for commit.

git add file.py     # Stage a file
git diff --cached   # View staged changes

c. Local Repository:
Store changes locally.

git commit -m "Add login feature"
git log             # View commit history

d. Remote Repository:
Share commits with the team.

git push origin main

4. Advanced Git Usage
a. Testing Staged vs Working Directory:
To test staged code:

git checkout -- file.py  # Match staged version
python file.py           # Run staged version

b. Stop Tracking Files/Folders:
To untrack a folder (e.g., temp/):

echo "temp/" >> .gitignore
git rm -r --cached temp/
git commit -m "Untrack temp folder"

c. Ignore Specific Files Permanently:
Sample .gitignore:

temp/
build/
*.log

5. Removing Git Tracking Completely:
To stop Git tracking in a folder:

rm -rf .git
