# GitHub Hands-On Exercises

These exercises will help you practice using GitHub with Python projects. Start with Exercise 1 and work your way through!

---

## Exercise 1: Your First Repository
**Difficulty:** Beginner
**Time:** 15 minutes

### Objectives
- Create your first GitHub repository
- Make your first commit
- Push code to GitHub

### Instructions

1. **Create a repository on GitHub:**
   - Go to GitHub and create a new repository named `hello-github`
   - Add a README file
   - Choose "Public"
   - Add Python .gitignore

2. **Clone it to your computer:**
   ```bash
   git clone git@github.com:your-username/hello-github.git
   cd hello-github
   ```

3. **Create a Python file:**
   Create `hello.py` with this code:
   ```python
   print("Hello, GitHub!")
   print("My name is [Your Name]")
   print("This is my first repository!")
   ```

4. **Commit and push:**
   ```bash
   git add hello.py
   git commit -m "Add hello.py with greeting message"
   git push
   ```

5. **Verify:**
   - Go to your repository on GitHub
   - You should see your `hello.py` file!

### Success Criteria
- ✅ Repository exists on GitHub
- ✅ hello.py is visible on GitHub
- ✅ Commit message is clear and descriptive

---

## Exercise 2: The Commit Practice
**Difficulty:** Beginner
**Time:** 20 minutes

### Objectives
- Practice making multiple commits
- Learn to write good commit messages
- Understand staging and committing

### Instructions

1. **Create a new repository** named `calculator-project`

2. **Create calculator.py** with just this:
   ```python
   # Simple Calculator

   def add(a, b):
       return a + b
   ```

3. **Make your first commit:**
   ```bash
   git add calculator.py
   git commit -m "Add addition function"
   git push
   ```

4. **Add subtraction:**
   ```python
   def subtract(a, b):
       return a - b
   ```
   **Commit:** "Add subtraction function"

5. **Add multiplication:**
   ```python
   def multiply(a, b):
       return a * b
   ```
   **Commit:** "Add multiplication function"

6. **Add division:**
   ```python
   def divide(a, b):
       if b == 0:
           return "Error: Cannot divide by zero"
       return a / b
   ```
   **Commit:** "Add division function with zero check"

7. **Add a main section:**
   ```python
   if __name__ == "__main__":
       print("Calculator ready!")
       print("5 + 3 =", add(5, 3))
       print("5 - 3 =", subtract(5, 3))
       print("5 * 3 =", multiply(5, 3))
       print("5 / 3 =", divide(5, 3))
   ```
   **Commit:** "Add main section with example calculations"

8. **Check your commit history:**
   ```bash
   git log --oneline
   ```

### Success Criteria
- ✅ You made at least 5 separate commits
- ✅ Each commit message is clear and descriptive
- ✅ All code is on GitHub
- ✅ `git log` shows your commit history

---

## Exercise 3: The .gitignore Challenge
**Difficulty:** Beginner
**Time:** 15 minutes

### Objectives
- Learn to use .gitignore
- Understand what files should and shouldn't be committed

### Instructions

1. **Create a new repository** named `gitignore-practice`

2. **Create these files:**
   ```bash
   touch main.py
   touch config.py
   touch secrets.txt
   touch notes.txt
   mkdir __pycache__
   touch __pycache__/main.cpython-39.pyc
   ```

3. **Add some content to main.py:**
   ```python
   print("This should be committed")
   ```

4. **Add content to secrets.txt:**
   ```
   API_KEY=super_secret_key_12345
   PASSWORD=my_password
   ```

5. **Check status:**
   ```bash
   git status
   ```
   You'll see ALL files listed.

6. **Create .gitignore:**
   ```
   # Secret files
   secrets.txt

   # Personal notes
   notes.txt

   # Python
   __pycache__/
   *.pyc
   ```

7. **Check status again:**
   ```bash
   git status
   ```
   Now secrets.txt, notes.txt, and __pycache__/ should NOT appear!

8. **Commit only the right files:**
   ```bash
   git add .
   git commit -m "Add main.py and .gitignore"
   git push
   ```

9. **Verify on GitHub:**
   - main.py should be there
   - .gitignore should be there
   - secrets.txt should NOT be there
   - __pycache__ should NOT be there

### Success Criteria
- ✅ .gitignore file exists
- ✅ Sensitive files are NOT on GitHub
- ✅ Only appropriate files were committed

---

## Exercise 4: Branch and Merge
**Difficulty:** Intermediate
**Time:** 25 minutes

### Objectives
- Create and use branches
- Merge branches
- Understand branch workflow

### Instructions

1. **Create repository** named `story-writer`

2. **Create story.txt on main branch:**
   ```
   Once upon a time, there was a programmer named Alex.
   ```

3. **Commit and push:**
   ```bash
   git add story.txt
   git commit -m "Start the story"
   git push
   ```

4. **Create a branch for a happy ending:**
   ```bash
   git checkout -b happy-ending
   ```

5. **Edit story.txt** (on happy-ending branch):
   ```
   Once upon a time, there was a programmer named Alex.
   Alex learned GitHub and became a successful developer.
   They lived happily ever after, coding amazing projects!
   ```

6. **Commit on the branch:**
   ```bash
   git add story.txt
   git commit -m "Add happy ending"
   git push -u origin happy-ending
   ```

7. **Switch back to main:**
   ```bash
   git checkout main
   ```
   Open story.txt - the ending is gone! It's still just one line.

8. **Create another branch for an adventure ending:**
   ```bash
   git checkout -b adventure-ending
   ```

9. **Edit story.txt** (on adventure-ending branch):
   ```
   Once upon a time, there was a programmer named Alex.
   Alex decided to travel the world, coding from different countries.
   Their adventure had just begun!
   ```

10. **Commit:**
    ```bash
    git add story.txt
    git commit -m "Add adventure ending"
    git push -u origin adventure-ending
    ```

11. **Merge happy-ending into main:**
    ```bash
    git checkout main
    git merge happy-ending
    git push
    ```

12. **View all branches:**
    ```bash
    git branch -a
    ```

### Success Criteria
- ✅ Created at least 2 branches
- ✅ Successfully merged a branch
- ✅ Main branch has the complete story
- ✅ Can switch between branches

### Challenge
Try creating a third branch with a different ending, then merge it!

---

## Exercise 5: Fixing Mistakes
**Difficulty:** Intermediate
**Time:** 20 minutes

### Objectives
- Learn to undo changes
- Practice fixing commits
- Handle common mistakes

### Instructions

1. **Create repository** named `mistake-practice`

2. **Create a Python file** with a "bug":
   ```python
   def greet(name):
       print("Hello, " + nam)  # Oops! Wrong variable

   greet("World")
   ```

3. **Commit it:**
   ```bash
   git add greet.py
   git commit -m "Add greeting function"
   ```

4. **Realize the mistake! Fix it:**
   ```python
   def greet(name):
       print("Hello, " + name)  # Fixed!

   greet("World")
   ```

5. **Commit the fix:**
   ```bash
   git add greet.py
   git commit -m "Fix typo in variable name"
   git push
   ```

6. **Now practice undoing** (create a new mistake):
   ```python
   def greet(name):
       print("COMPLETELY WRONG CODE")
   ```

7. **Undo the changes BEFORE committing:**
   ```bash
   git checkout -- greet.py
   ```
   The file is back to the last committed version!

8. **Make a commit with wrong message:**
   ```bash
   # Add a new function
   def farewell(name):
       print(f"Goodbye, {name}")

   git add greet.py
   git commit -m "asdf"  # Bad commit message!
   ```

9. **Fix the commit message:**
   ```bash
   git commit --amend -m "Add farewell function"
   ```

10. **Push everything:**
    ```bash
    git push
    ```

### Success Criteria
- ✅ Successfully undid changes with checkout
- ✅ Amended a commit message
- ✅ Final commit messages are clear
- ✅ All code is correct on GitHub

---

## Exercise 6: Collaboration Simulation
**Difficulty:** Intermediate
**Time:** 30 minutes

### Objectives
- Practice collaborative workflow
- Use Pull Requests
- Simulate working with a team

### Instructions

For this exercise, you'll simulate being two different developers!

1. **Create repository** named `team-project`

2. **Add a Python file** (as Developer 1):
   ```python
   # Team Project
   # Add your name when you contribute!

   contributors = [
       "Developer 1"
   ]

   print("Team members:", contributors)
   ```

3. **Commit and push:**
   ```bash
   git add team.py
   git commit -m "Initialize team project"
   git push
   ```

4. **Create a feature branch** (as Developer 2):
   ```bash
   git checkout -b add-greeting-feature
   ```

5. **Add a feature:**
   ```python
   # Team Project
   # Add your name when you contribute!

   contributors = [
       "Developer 1",
       "Developer 2"
   ]

   def greet_team():
       print("Hello team!")
       print("Team members:", contributors)

   greet_team()
   ```

6. **Commit and push the branch:**
   ```bash
   git add team.py
   git commit -m "Add greeting feature and Developer 2 name"
   git push -u origin add-greeting-feature
   ```

7. **Create a Pull Request on GitHub:**
   - Go to your repository
   - Click "Pull requests" → "New pull request"
   - Select `add-greeting-feature` branch
   - Write description: "Added greeting feature and my name to contributors"
   - Create the PR

8. **Review your own PR:**
   - Look at the "Files changed" tab
   - See what was added/removed
   - Add a comment: "Looks good to me!"

9. **Merge the PR:**
   - Click "Merge pull request"
   - Confirm the merge
   - Delete the branch

10. **Pull the changes on main:**
    ```bash
    git checkout main
    git pull
    ```

### Success Criteria
- ✅ Created and pushed a feature branch
- ✅ Created a Pull Request
- ✅ Merged the PR
- ✅ Main branch has all changes

---

## Exercise 7: Real Project - Todo List
**Difficulty:** Advanced
**Time:** 45 minutes

### Objectives
- Build a real Python project
- Practice full GitHub workflow
- Create good documentation

### Instructions

Build a command-line todo list application!

1. **Create repository** named `python-todo-list`

2. **Create branches for features:**
   ```bash
   # For adding tasks
   git checkout -b feature/add-task

   # For viewing tasks
   git checkout -b feature/view-tasks

   # For completing tasks
   git checkout -b feature/complete-task
   ```

3. **Implement on feature/add-task branch:**
   ```python
   # todo.py

   tasks = []

   def add_task(task):
       tasks.append({"task": task, "completed": False})
       print(f"Added: {task}")
   ```

   Commit: "Add function to add tasks"

4. **Merge to main:**
   ```bash
   git checkout main
   git merge feature/add-task
   git push
   ```

5. **Implement on feature/view-tasks branch:**
   ```bash
   git checkout feature/view-tasks
   ```

   ```python
   def view_tasks():
       if not tasks:
           print("No tasks yet!")
           return

       print("\nYour Tasks:")
       for i, task in enumerate(tasks, 1):
           status = "✓" if task["completed"] else " "
           print(f"{i}. [{status}] {task['task']}")
   ```

   Commit: "Add function to view tasks"
   Merge to main

6. **Implement on feature/complete-task branch:**
   ```bash
   git checkout feature/complete-task
   ```

   ```python
   def complete_task(task_number):
       if 0 < task_number <= len(tasks):
           tasks[task_number - 1]["completed"] = True
           print(f"Completed: {tasks[task_number - 1]['task']}")
       else:
           print("Invalid task number")
   ```

   Commit: "Add function to complete tasks"
   Merge to main

7. **Add main program:**
   ```python
   if __name__ == "__main__":
       while True:
           print("\n--- Todo List ---")
           print("1. Add task")
           print("2. View tasks")
           print("3. Complete task")
           print("4. Quit")

           choice = input("Choose: ")

           if choice == "1":
               task = input("Enter task: ")
               add_task(task)
           elif choice == "2":
               view_tasks()
           elif choice == "3":
               view_tasks()
               num = int(input("Task number to complete: "))
               complete_task(num)
           elif choice == "4":
               print("Goodbye!")
               break
   ```

   Commit: "Add main menu and user interaction"

8. **Create a great README.md:**
   ```markdown
   # Python Todo List

   A simple command-line todo list application.

   ## Features
   - Add tasks
   - View all tasks
   - Mark tasks as complete

   ## How to Use
   1. Run `python todo.py`
   2. Choose an option from the menu
   3. Follow the prompts

   ## Example
   ```
   --- Todo List ---
   1. Add task
   2. View tasks
   3. Complete task
   4. Quit
   Choose: 1
   Enter task: Learn GitHub
   Added: Learn GitHub
   ```

   ## Author
   Your Name
   ```

   Commit: "Add comprehensive README"

9. **Create requirements.txt** (even if empty):
   ```bash
   touch requirements.txt
   git add requirements.txt
   git commit -m "Add requirements.txt"
   ```

10. **Final push:**
    ```bash
    git push
    ```

### Success Criteria
- ✅ Used multiple branches
- ✅ Made meaningful commits
- ✅ Program works correctly
- ✅ Good README documentation
- ✅ Clean commit history

### Challenge Extensions
- Add task persistence (save to file)
- Add due dates
- Add task priorities
- Add task categories

---

## Exercise 8: GitHub Detective
**Difficulty:** Beginner
**Time:** 20 minutes

### Objectives
- Explore other people's repositories
- Learn from existing code
- Practice cloning and reading code

### Instructions

1. **Explore Python projects on GitHub:**
   - Go to github.com
   - Search for "python beginner projects"
   - Find a project that interests you

2. **Clone a repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

3. **Investigate:**
   - Read the README
   - Look at the code structure
   - Check the commit history: `git log --oneline`
   - See who contributed: `git log --format='%an' | sort | uniq`

4. **Answer these questions:**
   - What does this project do?
   - How many commits does it have?
   - When was the last commit?
   - How is the code organized?
   - What can you learn from it?

5. **Write a summary** in a file called `project-review.md`

### Success Criteria
- ✅ Cloned an open-source project
- ✅ Explored the commit history
- ✅ Understood the project structure
- ✅ Wrote a review

---

## Exercise 9: Portfolio Project
**Difficulty:** Advanced
**Time:** 60+ minutes

### Objectives
- Create a portfolio-worthy project
- Practice everything you've learned
- Showcase your skills

### Instructions

Create ANY Python project you want! Ideas:
- Number guessing game
- Password generator
- Simple text adventure
- Dice roller
- Unit converter
- Rock-paper-scissors
- Mad libs generator

**Requirements:**
1. ✅ Use branches for features
2. ✅ Make regular commits (at least 10)
3. ✅ Write a professional README with:
   - Project description
   - How to run it
   - Screenshots or examples
   - Your name
4. ✅ Use .gitignore properly
5. ✅ Write clean, commented code
6. ✅ Add at least one "release" on GitHub

**Bonus Points:**
- Add multiple features
- Include error handling
- Write tests
- Add a LICENSE file
- Make it actually useful!

### Success Criteria
- ✅ Project works without errors
- ✅ Professional documentation
- ✅ Good commit history
- ✅ Something you're proud to show!

---

## Exercise 10: GitHub Profile README
**Difficulty:** Intermediate
**Time:** 30 minutes

### Objectives
- Create a special GitHub profile README
- Showcase your projects
- Build your developer brand

### Instructions

1. **Create a special repository:**
   - Name it exactly your GitHub username
   - Make it public
   - Initialize with README

2. **Edit the README.md:**
   ```markdown
   # Hi, I'm [Your Name]! 👋

   ## About Me
   - 🎓 High school student learning Python
   - 💻 Interested in [your interests]
   - 🌱 Currently learning: GitHub, Python, [other topics]
   - 📫 How to reach me: [email or social media]

   ## My Projects
   - [Project 1](link) - Brief description
   - [Project 2](link) - Brief description
   - [Project 3](link) - Brief description

   ## Skills
   - Python
   - Git & GitHub
   - [Other skills]

   ## GitHub Stats
   ![Your GitHub stats](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true)

   ## Fun Fact
   [Something interesting about you!]
   ```

3. **Customize it:**
   - Add emojis
   - Link to your projects
   - Make it unique to you
   - Add badges or images

4. **Commit and push:**
   ```bash
   git add README.md
   git commit -m "Create profile README"
   git push
   ```

5. **View it:**
   - Go to your GitHub profile
   - Your README should appear at the top!

### Success Criteria
- ✅ Special repository created
- ✅ Professional-looking profile
- ✅ Links to projects
- ✅ Shows personality

---

## Completion Checklist

Mark off exercises as you complete them:

- [ ] Exercise 1: Your First Repository
- [ ] Exercise 2: The Commit Practice
- [ ] Exercise 3: The .gitignore Challenge
- [ ] Exercise 4: Branch and Merge
- [ ] Exercise 5: Fixing Mistakes
- [ ] Exercise 6: Collaboration Simulation
- [ ] Exercise 7: Real Project - Todo List
- [ ] Exercise 8: GitHub Detective
- [ ] Exercise 9: Portfolio Project
- [ ] Exercise 10: GitHub Profile README

## What's Next?

After completing these exercises, you should:
- Feel comfortable with basic Git commands
- Understand the GitHub workflow
- Have several projects in your portfolio
- Be ready to collaborate with others

**Keep learning:**
- Contribute to open-source projects
- Take on more complex projects
- Learn about GitHub Actions
- Explore GitHub Pages for hosting websites

**Remember:** The best way to learn is by doing. Keep coding, keep committing, and keep pushing! 🚀
