# This small application is a "To-Do List Checker" where users check tasks off a list by entering their names. 
# It uses a while loop with break, continue, and else, requires user input.
# The program combines data types (strings, integers), operators, and if-else for task validation.

# To-Do List Checker using While Loop
# User checks off tasks until all are done or they quit

tasks = ["Homework", "Clean room", "Call friend"]  # String list for tasks
task_index = 0  # Integer variable for task index
completed = 0  # Integer variable for completed tasks

while task_index < len(tasks):  # Loop until all tasks checked
    # String input from user
    user_input = input(f"Task {task_index + 1}: '{tasks[task_index]}' done? (y/n or 'q' to quit): ")
    
    if user_input.lower() == 'q':  # User wants to quit
        print("You quit checking tasks!")
        break  # Exit loop immediately
    elif user_input.lower() not in ['y', 'n']:  # Invalid input
        print("Please enter 'y', 'n', or 'q'.")
        continue  # Skip to next iteration
    elif user_input.lower() == 'n':  # Task not done
        print(f"'{tasks[task_index]}' not done yet.")
        pass  # Placeholder for future task reminders
    else:  # user_input == 'y'
        completed += 1  # Operator to increment completed count
        print(f"'{tasks[task_index]}' marked as done!")
    
    task_index += 1  # Move to next task

else:  # Runs if loop completes without break
    print(f"All {len(tasks)} tasks checked! Completed: {completed}/{len(tasks)}.")

print(f"Final status: {completed}/{len(tasks)} tasks completed.")