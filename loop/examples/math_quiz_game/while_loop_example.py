# Math Quiz Game using While Loop
# User answers addition questions until they quit or reach score of 5

MAX_QUESTION_COUNT = 5
score = 0  # Integer variable for score
question_num = 1  # Integer variable for question count
max_score = 5  # Integer variable for score limit
mistake_count = 0
MAX_MISTAKE_COUNT = 3

while question_num < MAX_QUESTION_COUNT:  # Loop until score reaches 5
    # Generate simple addition question
    num1 = question_num * 2  # Integer for first number
    num2 = question_num * 3  # Integer for second number
    correct_answer = num1 + num2  # Operator for correct answer
    
    # String input from user
    user_input = input(f"🙏 Question {question_num}: What is {num1} + {num2}? (Enter answer or 'q' to quit)({mistake_count}/{MAX_MISTAKE_COUNT}): ")
    
    if user_input.lower() == 'q':  # Check if user wants to quit
        print("👋 You chose to quit!")
        break  # Exit loop immediately
    elif not user_input.isdigit():  # Check if input is not a number
        print("💡 Please enter a number or 'q'.")
        continue  # Skip to next question
    else:
        user_answer = int(user_input)  # Convert string to integer
    
    if user_answer == correct_answer:  # Correct answer
        score += 1  # Operator to increment score
        print(f"🔥 Correct! Score: {score}/{max_score}")
        question_num += 1
    elif user_answer != correct_answer:  # Wrong answer
        print(f"🤔 Wrong! You've tried {mistake_count + 1}/{MAX_MISTAKE_COUNT}. Please try again.")
        mistake_count += 1
        if mistake_count == MAX_MISTAKE_COUNT:
            print(f"🥺 I am sorry but that's not right and we'll advance to the next question.")
            mistake_count = 0
            question_num += 1
else:  # Runs if loop ends naturally (score >= max_score)
    print("\n")
    if score <= 2:
        print(f"💪 Sorry, but your score was {score}. Try again.")
    elif score == 3:
        print(f"👍️ Well done, your score was {score}.")
    else:
        print(f"🎉 Congratulations! You reached a score of {score}/{max_score}!")

print(f"🥳 Quiz ended. Final score: {score}/{max_score}")