# Setting Up GitHub

This guide will walk you through setting up GitHub from scratch. By the end, you'll be ready to upload your first Python project!

## Part 1: Create a GitHub Account

### Step 1: Sign Up
1. Go to [github.com](https://github.com)
2. Click the **"Sign up"** button
3. Enter your email address (use one you check regularly)
4. Create a password (make it strong!)
5. Choose a username
   - This will be public and visible to everyone
   - Good examples: `john-codes`, `sarah-dev`, `alex-python`
   - Avoid: embarrassing names, since colleges/employers might see this

### Step 2: Verify Your Account
1. GitHub will send a verification code to your email
2. Check your email and enter the code
3. Complete the setup questions (you can skip the optional ones)

### Step 3: Choose Your Plan
- Select the **Free** plan (it's perfect for students!)
- Free plan gives you unlimited public and private repositories

---

## Part 2: Install Git on Your Computer

GitHub needs Git software on your computer to work. Here's how to install it:

### For Windows:

1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer
3. Use these recommended settings:
   - Default editor: Use Visual Studio Code (or your preferred editor)
   - PATH environment: "Git from the command line and also from 3rd-party software"
   - HTTPS transport backend: "Use the OpenSSL library"
   - Line ending conversions: "Checkout Windows-style, commit Unix-style"
   - Terminal emulator: "Use Windows' default console window"
   - For everything else: use the default options
4. Click "Install"

### For Mac:

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew first (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Git
brew install git
```

**Option 2: Download Installer**
1. Go to [git-scm.com/download/mac](https://git-scm.com/download/mac)
2. Download and run the installer
3. Follow the installation steps

### For Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install git
```

### Verify Installation

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
git --version
```

You should see something like: `git version 2.40.0`

If you see this, Git is installed correctly! 

---

## Part 3: Configure Git

Now tell Git who you are. Open your terminal and run these commands:

```bash
# Set your name (use your real name)
git config --global user.name "Your Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your.email@example.com"

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Make output colorful (easier to read)
git config --global color.ui auto
```

### Verify Your Configuration

```bash
git config --list
```

You should see your name and email in the output.

---

## Part 4: Connect Git to GitHub

You need to authenticate Git with your GitHub account. We'll use SSH keys (the secure way).

### Step 1: Check for Existing SSH Keys

```bash
ls -al ~/.ssh
```

If you see files named `id_rsa.pub` or `id_ed25519.pub`, you already have SSH keys. Skip to Step 3.

### Step 2: Generate a New SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

When prompted:
1. Press **Enter** to save in the default location
2. Enter a passphrase (optional but recommended - like a password for your key)
3. Re-enter the passphrase

### Step 3: Start the SSH Agent

**On Mac/Linux:**
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**On Windows (Git Bash):**
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

### Step 4: Copy Your SSH Public Key

**On Mac:**
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**On Windows (Git Bash):**
```bash
cat ~/.ssh/id_ed25519.pub | clip
```

**On Linux:**
```bash
cat ~/.ssh/id_ed25519.pub
# Then manually copy the output
```

### Step 5: Add SSH Key to GitHub

1. Go to [github.com](https://github.com) and log in
2. Click your profile picture (top right) ’ **Settings**
3. In the left sidebar, click **SSH and GPG keys**
4. Click **New SSH key**
5. Title: "My Laptop" (or whatever name helps you remember this computer)
6. Key type: **Authentication Key**
7. Paste your key into the "Key" field
8. Click **Add SSH key**

### Step 6: Test Your Connection

```bash
ssh -T git@github.com
```

You might see a warning about authenticity. Type `yes` and press Enter.

If successful, you'll see:
```
Hi YourUsername! You've successfully authenticated...
```

Congratulations! Your computer is now connected to GitHub! <‰

---

## Part 5: Create Your First Repository

Let's create a repository on GitHub and connect it to a project on your computer.

### Option A: Create Repository on GitHub First (Recommended for Beginners)

#### On GitHub:
1. Log in to [github.com](https://github.com)
2. Click the **+** icon (top right) ’ **New repository**
3. Fill in the details:
   - **Repository name**: `my-first-python-project` (no spaces, use hyphens)
   - **Description**: "My first Python project on GitHub" (optional)
   - **Public or Private**: Choose Public (or Private if you want only you to see it)
   - **Initialize this repository with**:
     -  Check "Add a README file"
     -  Add .gitignore: Choose **Python** from the dropdown
     - License: None (or choose MIT if you want)
4. Click **Create repository**

#### On Your Computer:
```bash
# Navigate to where you want to store your projects
cd ~/Documents  # or wherever you keep your projects

# Clone the repository
git clone git@github.com:YourUsername/my-first-python-project.git

# Go into the project folder
cd my-first-python-project

# Open in your code editor (if you use VS Code)
code .
```

### Option B: Upload an Existing Project

If you already have a Python project on your computer:

#### On GitHub:
1. Create a new repository (follow steps above)
2. **Don't** check "Initialize this repository with a README"
3. Click **Create repository**

#### On Your Computer:
```bash
# Navigate to your existing project folder
cd path/to/your/project

# Initialize Git in this folder
git init

# Add all your files
git add .

# Create your first commit
git commit -m "Initial commit - my first project"

# Connect to GitHub (replace YourUsername and repository-name)
git remote add origin git@github.com:YourUsername/repository-name.git

# Push your code to GitHub
git branch -M main
git push -u origin main
```

---

## Part 6: Understanding the Workflow

Now that everything is set up, here's your daily workflow:

### 1. Make Changes to Your Code
Edit your Python files as usual in your code editor.

### 2. Check What Changed
```bash
git status
```
This shows which files you modified.

### 3. Stage Your Changes
```bash
# Add specific file
git add filename.py

# Or add all changed files
git add .
```

### 4. Commit Your Changes
```bash
git commit -m "Describe what you changed"
```

**Good commit messages:**
- "Added login function"
- "Fixed bug in calculator"
- "Completed exercise 5"

**Bad commit messages:**
- "stuff"
- "changes"
- "asdfjkl"

### 5. Push to GitHub
```bash
git push
```

This uploads your changes to GitHub!

### 6. Pull Latest Changes
If you're working from multiple computers or with others:
```bash
git pull
```

This downloads any new changes from GitHub.

---

## Common Commands Cheat Sheet

```bash
# Check status of your files
git status

# Add files to staging
git add filename.py        # Add specific file
git add .                  # Add all files

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push

# Pull from GitHub
git pull

# View commit history
git log

# See what changed in files
git diff

# Create a new branch
git branch branch-name

# Switch to a branch
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch-name

# Clone a repository
git clone git@github.com:username/repo-name.git
```

---

## Tips for Success

### 1. **Commit Often**
- Make commits after completing small tasks
- Don't wait until the end of the day
- If you can describe what you did in one sentence, it's ready to commit

### 2. **Write Good Commit Messages**
- Start with a verb: "Add", "Fix", "Update", "Remove"
- Be specific: "Fix calculator division by zero error" not "Fix bug"
- Keep it under 50 characters if possible

### 3. **Don't Commit Everything**
- The `.gitignore` file tells Git what to ignore
- Don't commit: passwords, API keys, huge files, or temporary files
- Do commit: your code, documentation, configuration files

### 4. **Push Regularly**
- Push at least once a day when working on a project
- This backs up your work to the cloud
- Makes it easy to work from different computers

### 5. **Keep Your README Updated**
- The README.md file is the first thing people see
- Explain what your project does
- Include instructions on how to run it

---

## Troubleshooting

### "Permission denied (publickey)"
- Your SSH key isn't set up correctly
- Go back to Part 4 and make sure you added your SSH key to GitHub

### "fatal: not a git repository"
- You're not in a Git project folder
- Run `git init` to create a new repository, or `cd` into an existing one

### "Your branch is ahead of 'origin/main' by X commits"
- You have commits on your computer that aren't on GitHub yet
- Run `git push` to upload them

### "fatal: refusing to merge unrelated histories"
- Your local and remote repositories have different histories
- Try: `git pull origin main --allow-unrelated-histories`

### Accidentally Committed the Wrong Files
```bash
# Undo the last commit but keep the changes
git reset HEAD~1

# Remove file from staging (before commit)
git reset filename.py
```

---

## Next Steps

Now that you're set up, you can:

1. **Practice the workflow** - Create a simple Python file, commit it, and push it
2. **Explore GitHub** - Search for interesting Python projects
3. **Learn branching** - Create branches for new features
4. **Collaborate** - Work on a project with a friend
5. **Build your portfolio** - Upload your best projects to showcase your skills

---

## Additional Resources

- [GitHub Documentation](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

---

Congratulations! You're now ready to use GitHub like a professional developer! =€
