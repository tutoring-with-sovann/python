# Math Quiz Game using For Loop
# User answers 5 addition questions or quits early

score = 0  # Integer variable for score
max_questions = 5  # Integer variable for question limit

for question_num in range(1, max_questions + 1):  # Loop for 5 questions
    # Generate simple addition question
    num1 = question_num * 2  # Integer for first number
    num2 = question_num * 3  # Integer for second number
    correct_answer = num1 + num2  # Operator for correct answer
    
    # String input from user
    user_input = input(f"Question {question_num}: What is {num1} + {num2}? (Enter answer or 'q' to quit): ")
    
    if user_input.lower() == 'q':  # Check if user wants to quit
        print("You chose to quit!")
        break  # Exit loop immediately
    elif not user_input.isdigit():  # Check if input is not a number
        print("Please enter a number or 'q'.")
        continue  # Skip to next question
    else:
        user_answer = int(user_input)  # Convert string to integer
    
    if user_answer == correct_answer:  # Correct answer
        score += 1  # Operator to increment score
        print(f"Correct! Score: {score}/{max_questions}")
    elif user_answer != correct_answer:  # Wrong answer
        print(f"Wrong! The answer was {correct_answer}. Try again.")
        pass  # Placeholder for future feedback enhancements
    
else:  # Runs if loop completes all questions without break
    print(f"Quiz complete! You answered all {max_questions} questions.")

print(f"Quiz ended. Final score: {score}/{max_questions}")