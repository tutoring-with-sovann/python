# GitHub Quick Reference Guide

A quick reference for all essential GitHub and Git commands and concepts.

---

## Table of Contents
1. [Essential Commands](#essential-commands)
2. [Git Configuration](#git-configuration)
3. [Common Workflows](#common-workflows)
4. [Troubleshooting](#troubleshooting)
5. [GitHub Features](#github-features)
6. [Best Practices Checklist](#best-practices-checklist)

---

## Essential Commands

### Setup and Configuration

```bash
# Configure your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View all configurations
git config --list

# Set default branch name
git config --global init.defaultBranch main

# Enable colored output
git config --global color.ui auto
```

### Creating Repositories

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone <url>

# Clone with a specific folder name
git clone <url> <folder-name>

# Clone only the latest commit (faster)
git clone --depth 1 <url>
```

### Basic Workflow

```bash
# Check status of files
git status

# Add file to staging area
git add <filename>

# Add all changed files
git add .

# Add all files of a specific type
git add *.py

# Commit staged changes
git commit -m "Your message"

# Add and commit in one step
git commit -am "Your message"  # Only works for tracked files

# Push to remote
git push

# Pull from remote
git pull

# Fetch changes without merging
git fetch
```

### Viewing Information

```bash
# View commit history
git log

# Compact log view
git log --oneline

# Log with graph
git log --graph --oneline --all

# Show last N commits
git log -n 5

# View changes in files
git diff

# View changes in staged files
git diff --staged

# View commit details
git show <commit-hash>

# View file at specific commit
git show <commit-hash>:<file-path>
```

### Branches

```bash
# List all local branches
git branch

# List all branches (including remote)
git branch -a

# Create new branch
git branch <branch-name>

# Switch to branch
git checkout <branch-name>

# Create and switch to new branch
git checkout -b <branch-name>

# Switch to main branch
git checkout main

# Merge branch into current branch
git merge <branch-name>

# Delete local branch
git branch -d <branch-name>

# Force delete branch
git branch -D <branch-name>

# Delete remote branch
git push origin --delete <branch-name>

# Rename current branch
git branch -m <new-name>
```

### Undoing Changes

```bash
# Discard changes to a file
git checkout -- <filename>

# Unstage a file (keep changes)
git reset HEAD <filename>

# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Undo specific commit (create new commit)
git revert <commit-hash>

# Modify last commit message
git commit --amend -m "New message"

# Add forgotten files to last commit
git add <forgotten-file>
git commit --amend --no-edit

# Discard all local changes
git reset --hard HEAD

# Remove untracked files
git clean -fd
```

### Remote Repositories

```bash
# View remote repositories
git remote -v

# Add remote repository
git remote add origin <url>

# Change remote URL
git remote set-url origin <new-url>

# Remove remote
git remote remove <remote-name>

# Push to specific remote and branch
git push origin main

# Set upstream for current branch
git push -u origin <branch-name>

# Push all branches
git push --all

# Push tags
git push --tags
```

### Stashing (Temporary Storage)

```bash
# Stash current changes
git stash

# Stash with message
git stash save "Work in progress"

# List all stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Delete most recent stash
git stash drop

# Delete all stashes
git stash clear
```

### Tags (Version Markers)

```bash
# Create tag for current commit
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# Tag specific commit
git tag v1.0.0 <commit-hash>

# List all tags
git tag

# Push tag to remote
git push origin v1.0.0

# Push all tags
git push --tags

# Delete tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
```

---

## Git Configuration

### Useful Configurations

```bash
# Set default editor (VS Code)
git config --global core.editor "code --wait"

# Set default editor (nano)
git config --global core.editor "nano"

# Auto-correct typos
git config --global help.autocorrect 1

# Show full paths in diffs
git config --global diff.noprefix true

# Cache credentials (save password)
git config --global credential.helper cache

# Cache for 1 hour
git config --global credential.helper 'cache --timeout=3600'

# Permanently store credentials (use carefully!)
git config --global credential.helper store

# Always pull with rebase
git config --global pull.rebase true

# Default to push current branch only
git config --global push.default current
```

### Aliases (Shortcuts)

```bash
# Create shortcuts for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'

# Now you can use:
git st         # instead of git status
git co main    # instead of git checkout main
git visual     # beautiful commit graph
```

---

## Common Workflows

### Starting a New Project

```bash
# Method 1: Start locally
mkdir my-project
cd my-project
git init
# Create files...
git add .
git commit -m "Initial commit"
# Create repo on GitHub, then:
git remote add origin git@github.com:username/my-project.git
git push -u origin main

# Method 2: Start on GitHub
# Create repo on GitHub first, then:
git clone git@github.com:username/my-project.git
cd my-project
# Start coding...
```

### Daily Development Workflow

```bash
# Morning: get latest code
git pull

# Create feature branch
git checkout -b new-feature

# Work on your code...
# ...make changes...

# Check what you changed
git status
git diff

# Stage and commit
git add .
git commit -m "Add new feature"

# Push your branch
git push -u origin new-feature

# When feature is done, merge to main
git checkout main
git pull
git merge new-feature
git push

# Delete feature branch
git branch -d new-feature
git push origin --delete new-feature
```

### Collaboration Workflow

```bash
# Get repository
git clone git@github.com:team/project.git
cd project

# Always pull before starting work
git pull

# Create feature branch
git checkout -b fix-bug

# Make changes and commit
git add .
git commit -m "Fix login bug"

# Push branch
git push -u origin fix-bug

# Create Pull Request on GitHub
# After PR is approved and merged:

# Switch back to main and update
git checkout main
git pull

# Delete your feature branch
git branch -d fix-bug
```

### Sync Fork with Original

```bash
# Add original repo as upstream (once)
git remote add upstream git@github.com:original/repo.git

# Fetch changes from original
git fetch upstream

# Merge into your main
git checkout main
git merge upstream/main

# Push to your fork
git push
```

---

## Troubleshooting

### Common Problems and Solutions

#### "Permission denied (publickey)"

**Problem:** SSH key not set up or not recognized

**Solution:**
```bash
# Check if SSH key exists
ls -al ~/.ssh

# Generate new SSH key if needed
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key
ssh-add ~/.ssh/id_ed25519

# Copy public key and add to GitHub
cat ~/.ssh/id_ed25519.pub
# Copy the output and add at: GitHub → Settings → SSH Keys
```

#### Merge Conflicts

**Problem:** Git can't automatically merge changes

**Solution:**
```bash
# When you see conflict error after merge or pull:
git status  # See which files have conflicts

# Open conflicted file, look for:
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> branch-name

# Edit file to resolve conflict
# Remove markers (<<<, ===, >>>)
# Keep the code you want

# Stage resolved file
git add <filename>

# Complete the merge
git commit -m "Resolve merge conflict"
```

#### Accidentally Committed to Wrong Branch

**Solution:**
```bash
# If you haven't pushed yet:
# Save the commit hash
git log -1

# Undo commit (keep changes)
git reset HEAD~1

# Switch to correct branch
git checkout correct-branch

# Commit again
git add .
git commit -m "Your message"
```

#### Want to Change Last Commit

**Solution:**
```bash
# Change commit message
git commit --amend -m "New message"

# Add forgotten file to last commit
git add forgotten-file.py
git commit --amend --no-edit

# Warning: Only do this if you haven't pushed yet!
```

#### Accidentally Deleted a File

**Solution:**
```bash
# If not committed yet
git checkout -- <filename>

# If already committed
git log --all --full-history -- <filename>
git checkout <commit-hash> -- <filename>
```

#### Push Rejected

**Problem:** "Updates were rejected because the remote contains work..."

**Solution:**
```bash
# Pull first
git pull

# If there are conflicts, resolve them
# Then push
git push
```

#### Detached HEAD State

**Problem:** "You are in 'detached HEAD' state"

**Solution:**
```bash
# Create a branch from current state
git checkout -b temp-branch

# Or go back to main
git checkout main
```

---

## GitHub Features

### Pull Requests

**Creating a PR:**
1. Push your branch to GitHub
2. Go to repository on GitHub
3. Click "Pull requests" → "New pull request"
4. Select your branch
5. Add title and description
6. Click "Create pull request"

**PR Best Practices:**
- Write clear title and description
- Reference related issues (#123)
- Request specific reviewers
- Add labels if available
- Keep PRs small and focused

### Issues

**Creating an Issue:**
1. Go to repository → "Issues"
2. Click "New issue"
3. Add title and description
4. Add labels (bug, enhancement, etc.)
5. Assign to someone if needed
6. Submit issue

**Closing Issues:**
```bash
# In commit message:
git commit -m "Fix login bug. Closes #42"

# The issue will auto-close when merged
```

### GitHub Pages

**Enable for your project:**
1. Go to repository → Settings
2. Scroll to "GitHub Pages"
3. Select branch (usually main)
4. Select folder (usually /docs or root)
5. Save

Your site will be at: `https://username.github.io/repository-name/`

### Releases

**Creating a Release:**
1. Go to repository → "Releases"
2. Click "Create a new release"
3. Choose or create a tag (e.g., v1.0.0)
4. Add release title
5. Describe what's new
6. Attach files if needed
7. Publish release

**From command line:**
```bash
# Create and push tag
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0

# Then create release on GitHub
```

---

## Best Practices Checklist

### Before Committing

- [ ] Code runs without errors
- [ ] Removed debug print statements
- [ ] Updated comments if needed
- [ ] Checked what files changed: `git status`
- [ ] Reviewed actual changes: `git diff`
- [ ] Not committing sensitive data (passwords, API keys)

### Commit Messages

- [ ] Starts with a verb (Add, Fix, Update, Remove)
- [ ] Under 50 characters for title
- [ ] Describes WHY, not just WHAT
- [ ] Written in present tense
- [ ] Specific and clear

**Good Examples:**
```
Add user authentication
Fix crash on empty input
Update README with installation steps
Remove deprecated function
```

**Bad Examples:**
```
changes
fixed stuff
update
asdfasdf
```

### Repository Organization

```
my-project/
├── README.md           # Project overview
├── requirements.txt    # Python dependencies
├── .gitignore         # Files to ignore
├── LICENSE            # License (optional)
├── src/               # Source code
│   └── main.py
├── tests/             # Test files
│   └── test_main.py
├── docs/              # Documentation
│   └── usage.md
└── data/              # Data files (small only)
    └── sample.csv
```

### .gitignore Template

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv
pip-log.txt
pip-delete-this-directory.txt

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Environment
.env
.env.local
*.env

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Logs
*.log

# Databases
*.db
*.sqlite
*.sqlite3
```

### README Template

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
git clone https://github.com/username/project.git
cd project
pip install -r requirements.txt
```

## Usage

```python
python main.py
```

Or:

```bash
python main.py --option value
```

## Examples

```python
# Example code
from project import function
result = function("example")
```

## Requirements

- Python 3.8+
- [List any other requirements]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Author

Your Name - [Your GitHub](https://github.com/username)

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- References
```

---

## Keyboard Shortcuts (GitHub Website)

| Shortcut | Action |
|----------|--------|
| `?` | Show keyboard shortcuts |
| `s` or `/` | Focus search bar |
| `g` then `n` | Go to notifications |
| `g` then `c` | Go to code tab |
| `g` then `i` | Go to issues |
| `g` then `p` | Go to pull requests |
| `t` | Activate file finder |
| `l` | Jump to line |
| `w` | Switch branch or tag |
| `y` | Get permalink |
| `i` | Show/hide comments |

---

## Quick Decision Tree

### "Which command should I use?"

```
Want to save your work?
├─ Not committed yet?
│  ├─ Stage: git add .
│  └─ Commit: git commit -m "message"
└─ Already committed?
   └─ Upload: git push

Want to get code?
├─ First time?
│  └─ Clone: git clone <url>
└─ Already have it?
   └─ Update: git pull

Made a mistake?
├─ Not committed?
│  └─ Undo: git checkout -- <file>
├─ Already committed?
│  └─ Undo: git reset HEAD~1
└─ Already pushed?
   └─ Revert: git revert <hash>

Want to try something new?
├─ Create branch: git checkout -b <name>
├─ Make changes and commit
└─ Merge: git merge <name>
```

---

## Summary

### The 10 Most Important Commands

```bash
1.  git status          # Check what's happening
2.  git add .           # Stage all changes
3.  git commit -m       # Save changes
4.  git push            # Upload to GitHub
5.  git pull            # Download from GitHub
6.  git clone           # Get a repository
7.  git checkout -b     # Create new branch
8.  git merge           # Combine branches
9.  git log             # View history
10. git diff            # See changes
```

**Remember:** When in doubt, run `git status`!

---

## Additional Resources

- **Official Git Documentation:** [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Guides:** [guides.github.com](https://guides.github.com)
- **Interactive Learning:** [learngitbranching.js.org](https://learngitbranching.js.org)
- **Git Cheat Sheet:** [education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)
- **Markdown Guide:** [markdownguide.org](https://www.markdownguide.org)

---

**Pro Tip:** Bookmark this page and refer to it whenever you need a quick reminder! 📚
