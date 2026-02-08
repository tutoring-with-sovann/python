# Python Recap

This recap will help you to remember what we have learnt from previous lesson. Python is a versatile, beginner-friendly language used for web, data science, automation, and AI. Its clean syntax makes it great for learning programming fundamentals.

## Variables and data types

### String
Text data enclosed in quotes (`""` or `''`). Can be combined with `+` or repeated with `*`. Support f-strings for embedding variables: `f"Hello {name}"`.

### Number
Two main types: integers (whole numbers) and floats (decimals). Support all math operations: `+`, `-`, `*`, `/`, `//` (floor), `%` (modulo), `**` (power).

### Boolean
Represents truth values: `True` or `False`. Used in conditions and comparisons. Results from comparison operators like `==`, `>`, `<`.

### List
Ordered collection that can hold multiple values. Created with square brackets: `items = [1, 2, 3]`. Mutable - can add, remove, or modify elements.

### Dictionary
Key-value pairs like a real dictionary. Created with curly braces: `person = {"name": "Alex", "age": 15}`. Access values by key: `person["name"]`.

### Tuple
Like a list but immutable (cannot be changed after creation). Created with parentheses: `(1, 2, 3)`. Useful for fixed collections of data.

### Object
Everything in Python is an object. Has attributes (data) and methods (functions). Example: `"hello".upper()` returns `"HELLO"`.

## Operators

### Arithematic
Math operations: `+`, `-`, `*`, `/`, `//` (floor division), `%` (remainder), `**` (power). Used with numbers for calculations.

### Assignment
Assign values to variables: `=`, `+=`, `-=`, `*=`, `/=`. Example: `x += 5` means `x = x + 5`.

### Comparison
Compare values and return `True` or `False`: `==` (equal), `!=` (not equal), `>` (greater), `<` (less), `>=`, `<=`.

### Logical
Combine conditions: `and`, `or`, `not`. `True and False` → `False`. `True or False` → `True`.

## Loops
Repeat code blocks multiple times. Essential for processing collections, automating repetitive tasks, and iterating through data.

### For Loop

#### for
Iterate over sequences like lists or strings. Use `for item in list:` or `for i in range(5):`.

#### while
Repeat while a condition is true: `while count < 5:`. Be careful - can run forever if condition never becomes false!

## Control Statement

### If-Else
Run code based on conditions: `if`, `elif`, `else`. Only one block executes based on the first true condition.

### Switch-Case
Python uses `match`-`case` (Python 3.10+) or `if`-`elif` chains. `match value:` checks against multiple `case` patterns.

### Loops (Control)
`break` exits the loop early. `continue` skips to the next iteration. Used within `for` or `while` loops.

## Function
Reusable blocks of code that perform specific tasks. Help organize code, avoid repetition, and make programs easier to maintain and debug.

### Default Value
Parameters can have default values: `def greet(name="Guest"):`. Called with or without arguments.

### Lambda
Small anonymous function: `lambda x: x * 2`. Useful for short, simple functions as arguments.

### Multi Return
Functions can return multiple values: `return a, b`. Returns as a tuple, can unpack: `x, y = get_coords()`.

### Recursion
Function calls itself to solve problems. Must have a base case to stop. Example: factorial, fibonacci.

### Error handling
Catch and handle errors gracefully: `try`-`except` blocks. Prevents program crashes when things go wrong.

## OOP(Class)

Classes are blueprints for creating objects. Objects have **attributes** (data) and **methods** (functions). Use `__init__` to initialize new objects. Inheritance lets classes share code.

# Git Recap
Version control system for tracking code changes. Enables collaboration, experimentation through branches, and the ability to undo mistakes.

## Normal workflow between
`git add` → stage changes, `git commit` → save locally, `git push` → send to GitHub. Three stages: working directory → staging → repository.

## Snapshot(commit) Mental Model
Each commit is a **snapshot** of your entire project. Not just changes - the complete state. Commits form a timeline you can travel through. Parent commits link backwards, creating a history tree. You can revisit any snapshot anytime using `git checkout`.

## Local and Remote Mental Model
**Local** = your computer (your work, commits, branches). **Remote** = GitHub (shared copy). Must `push` to send local → remote, `pull` to get remote → local. Changes don't sync automatically - you control when to share or receive updates.
