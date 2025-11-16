# GitHub Workflow for Python Projects

This guide shows you how to use GitHub in your daily Python programming workflow.

## Table of Contents
1. [Starting a New Python Project](#starting-a-new-python-project)
2. [Daily Workflow](#daily-workflow)
3. [Working with Branches](#working-with-branches)
4. [Collaborating with Others](#collaborating-with-others)
5. [Best Practices](#best-practices)

---

## Starting a New Python Project

### Step-by-Step Setup

#### 1. Create Repository on GitHub

```bash
# Option 1: Use GitHub website
# Go to github.com → New Repository → Fill in details → Create

# Option 2: Use GitHub CLI (if installed)
gh repo create my-python-project --public --clone
cd my-python-project
```

#### 2. Set Up Your Project Structure

```bash
# Create essential files
touch README.md
touch main.py
touch requirements.txt
touch .gitignore

# Create a proper Python .gitignore
cat > .gitignore << EOL
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

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Environment variables
.env
EOL
```

#### 3. Create a Good README

```markdown
# Project Name

## Description
A brief description of what this project does.

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the program: `python main.py`

## Requirements
- Python 3.8 or higher

## Author
Your Name
```

#### 4. Make Your First Commit

```bash
git add .
git commit -m "Initial commit: project setup"
git push -u origin main
```

---

## Daily Workflow

This is what you'll do every day when working on your project:

### Morning: Start Your Work Session

```bash
# 1. Navigate to your project
cd path/to/your/project

# 2. Make sure you have the latest code
git pull

# 3. Check the status
git status
```

### During the Day: Work and Save Progress

```bash
# After making changes to your code...

# 1. See what you changed
git status           # See which files changed
git diff             # See exactly what changed in the files

# 2. Add your changes to staging
git add main.py      # Add specific file
# OR
git add .            # Add all changed files

# 3. Commit with a descriptive message
git commit -m "Add player scoring system"

# 4. Push to GitHub (backup your work)
git push
```

### Example Session

Let's say you're building a calculator:

```bash
# You add addition function
# Edit calculator.py...

git add calculator.py
git commit -m "Add addition function"
git push

# You add subtraction function
# Edit calculator.py...

git add calculator.py
git commit -m "Add subtraction function"
git push

# You fix a bug in addition
# Edit calculator.py...

git add calculator.py
git commit -m "Fix bug: addition now handles negative numbers"
git push
```

### End of Day: Final Backup

```bash
# Make sure everything is committed and pushed
git status           # Should show "nothing to commit, working tree clean"
git push            # Push any remaining commits
```

---

## Working with Branches

Branches let you try new features without breaking your main code.

### Why Use Branches?

- **Main branch**: Your working, stable code
- **Feature branch**: Try new features safely
- If the feature works → merge it into main
- If the feature doesn't work → delete the branch, main is still safe

### Creating and Using Branches

#### Create a New Feature Branch

```bash
# Create and switch to new branch
git checkout -b add-multiplication

# Now you're on the 'add-multiplication' branch
# The main branch is safe and unchanged
```

#### Work on Your Feature

```bash
# Make changes to your files...
# Edit calculator.py to add multiplication

git add calculator.py
git commit -m "Add multiplication function"
git push -u origin add-multiplication
```

#### Switch Between Branches

```bash
# Go back to main
git checkout main

# Go to your feature branch
git checkout add-multiplication

# See all branches
git branch
```

#### Merge Your Feature into Main

When your feature is complete and tested:

```bash
# 1. Switch to main branch
git checkout main

# 2. Merge your feature branch
git merge add-multiplication

# 3. Push the updated main branch
git push

# 4. Delete the feature branch (optional)
git branch -d add-multiplication
git push origin --delete add-multiplication
```

### Visual Example

```
main:      A --- B --- C --- G (merged!)
                \           /
feature:         D --- E --- F
```

- A, B, C: Commits on main
- Created feature branch at C
- D, E, F: Commits on feature branch
- G: Merge feature back into main

---

## Collaborating with Others

### Forking vs Cloning

**Clone**: Make a copy of a repository you have access to
```bash
git clone git@github.com:username/project.git
```

**Fork**: Make your own copy of someone else's project on GitHub
1. Go to their repository on GitHub
2. Click "Fork" button (top right)
3. Clone your forked version
```bash
git clone git@github.com:your-username/project.git
```

### Working on a Team Project

#### Setup (Do Once)

```bash
# Clone your team's repository
git clone git@github.com:team-name/project.git
cd project
```

#### Daily Team Workflow

```bash
# 1. Always pull before starting work
git pull

# 2. Create a branch for your task
git checkout -b fix-login-bug

# 3. Do your work and commit
git add .
git commit -m "Fix login validation bug"

# 4. Push your branch
git push -u origin fix-login-bug

# 5. Create Pull Request on GitHub
# Go to GitHub → Your repository → Pull Requests → New Pull Request
```

### Pull Requests (PRs)

A Pull Request is asking to merge your code into the main branch.

**Creating a PR:**
1. Push your branch to GitHub
2. Go to the repository on GitHub
3. Click "Pull requests" → "New pull request"
4. Select your branch
5. Write a description of your changes
6. Click "Create pull request"

**Reviewing a PR:**
- Look at the code changes
- Test the code if possible
- Leave comments or suggestions
- Approve or request changes

**Merging a PR:**
- Once approved, click "Merge pull request"
- Delete the branch after merging

---

## Best Practices

### 1. Commit Messages

**Good Examples:**
```bash
git commit -m "Add user login functionality"
git commit -m "Fix crash when dividing by zero"
git commit -m "Update README with installation instructions"
git commit -m "Remove unused import statements"
```

**Bad Examples:**
```bash
git commit -m "changes"
git commit -m "stuff"
git commit -m "idk"
git commit -m "asdfasdf"
```

**Format:**
```
Type: Short description (50 chars or less)

Optional longer explanation if needed.
```

**Types:**
- `Add`: New feature or file
- `Fix`: Bug fix
- `Update`: Improve existing feature
- `Remove`: Delete code or file
- `Refactor`: Restructure code without changing functionality
- `Docs`: Documentation changes

### 2. When to Commit

**✅ Good Times to Commit:**
- After completing a function
- After fixing a bug
- After adding a feature
- At the end of a work session
- Before trying something risky

**❌ Don't Commit:**
- Code that doesn't run
- Half-finished features (unless on a feature branch)
- Code with syntax errors

**Rule of Thumb:** If you can describe what you did in one sentence, commit it!

### 3. What to Commit

**✅ Do Commit:**
- Source code (.py files)
- README and documentation (.md files)
- Configuration files
- Requirements files (requirements.txt)
- Small data files for testing

**❌ Don't Commit:**
- API keys or passwords
- Large data files (>100MB)
- Generated files (__pycache__, .pyc)
- Virtual environments (venv/, env/)
- IDE settings (.vscode/, .idea/)
- Personal notes with sensitive information

Use `.gitignore` to automatically ignore these files!

### 4. Keep Your Repository Organized

```
my-python-project/
│
├── README.md              # Project description and instructions
├── requirements.txt       # Python dependencies
├── .gitignore            # Files to ignore
│
├── main.py               # Main program file
├── utils.py              # Utility functions
│
├── data/                 # Data files (if small)
│   └── sample.csv
│
├── tests/                # Test files
│   └── test_main.py
│
└── docs/                 # Additional documentation
    └── usage.md
```

### 5. Branch Naming

**Good branch names:**
```bash
feature/add-user-profile
fix/login-bug
update/readme
refactor/database-code
```

**Pattern:** `type/short-description`

### 6. Syncing with Remote

```bash
# Always pull before starting new work
git pull

# Push frequently (at least once per day)
git push

# Check if you're behind
git fetch
git status
```

---

## Common Scenarios

### Scenario 1: You Made a Mistake in Your Last Commit

**Forgot to add a file:**
```bash
# Add the forgotten file
git add forgotten_file.py

# Amend the last commit
git commit --amend --no-edit
```

**Wrong commit message:**
```bash
git commit --amend -m "Correct message"
```

### Scenario 2: You Want to Undo Changes

**Undo changes to a file (not yet committed):**
```bash
git checkout -- filename.py
```

**Undo the last commit (keep changes):**
```bash
git reset HEAD~1
```

**Undo the last commit (discard changes):**
```bash
git reset --hard HEAD~1
```

### Scenario 3: Merge Conflicts

When two people change the same part of a file:

```bash
# Try to merge or pull
git pull
# CONFLICT!

# Open the conflicted file, you'll see:
<<<<<<< HEAD
your code
=======
their code
>>>>>>> branch-name

# Choose which code to keep, remove the markers
# Then:
git add filename.py
git commit -m "Resolve merge conflict"
git push
```

### Scenario 4: You're Working from Multiple Computers

**On Computer 1:**
```bash
# Do work
git add .
git commit -m "Complete homework part 1"
git push
```

**On Computer 2:**
```bash
# Get the latest code
git pull

# Continue working
git add .
git commit -m "Complete homework part 2"
git push
```

**Back on Computer 1:**
```bash
# Get the work from Computer 2
git pull

# Continue working...
```

---

## Quick Reference Commands

```bash
# Setup
git init                          # Initialize new repository
git clone <url>                   # Clone repository

# Daily workflow
git status                        # Check status
git add <file>                    # Stage file
git add .                         # Stage all files
git commit -m "message"           # Commit changes
git push                          # Push to GitHub
git pull                          # Pull from GitHub

# Branches
git branch                        # List branches
git branch <name>                 # Create branch
git checkout <name>               # Switch branch
git checkout -b <name>            # Create and switch
git merge <branch>                # Merge branch
git branch -d <name>              # Delete branch

# Information
git log                           # View commit history
git log --oneline                 # Compact history
git diff                          # See changes
git remote -v                     # See remotes

# Undo
git checkout -- <file>            # Discard changes to file
git reset HEAD <file>             # Unstage file
git reset HEAD~1                  # Undo last commit (keep changes)
git reset --hard HEAD~1           # Undo last commit (discard changes)
```

---

## Practice Exercise

Try this to practice the workflow:

1. **Create a new repository** called "python-practice"
2. **Create a simple Python file** (hello.py) that prints "Hello, GitHub!"
3. **Commit and push** the file
4. **Create a branch** called "add-name-feature"
5. **Modify the file** to ask for the user's name and greet them
6. **Commit and push** the branch
7. **Merge** the branch into main
8. **Delete** the feature branch

Try to do this without looking at the instructions!

---

## Tips for Success

1. **Commit early and often** - Small commits are better than big ones
2. **Write clear commit messages** - Your future self will thank you
3. **Always pull before you start** - Avoid conflicts
4. **Push at least once a day** - Keep your backup current
5. **Use branches for experiments** - Keep main stable
6. **Review your changes** - Use `git diff` before committing
7. **Don't commit secrets** - Use .gitignore and environment variables

Happy coding! 🚀
