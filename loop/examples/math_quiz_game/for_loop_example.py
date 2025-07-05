MAX_QUESTION_COUNT = 5
score = 0  # Integer variable for score
question_num = 1  # Integer variable for question count
max_score = 5  # Integer variable for score limit
mistake_count = 0
MAX_MISTAKE_COUNT = 3

for _ in range(1, MAX_QUESTION_COUNT):  # Loop for up to MAX_QUESTION_COUNT questions
    # Generate simple addition question
    num1 = question_num * 2  # Integer for first number
    num2 = question_num * 3  # Integer for second number
    correct_answer = num1 + num2  # Operator for correct answer

    for attempt in range(MAX_MISTAKE_COUNT):  # Inner loop for up to 3 attempts per question
        # String input from user
        user_input = input(
            f"🙏 Question {question_num}: What is {num1} + {num2}? (Enter answer or 'q' to quit)({mistake_count}/{MAX_MISTAKE_COUNT}): ")

        if user_input.lower() == 'q':  # Check if user wants to quit
            print("👋 You chose to quit!")
            break  # Exit inner loop and outer loop will be broken later
        elif not user_input.isdigit():  # Check if input is not a number
            print("💡 Please enter a number or 'q'.")
            if attempt < MAX_MISTAKE_COUNT - 1:  # Allow retry if not last attempt
                continue  # Retry same question
            else:  # Treat as wrong answer on last attempt
                print(f"🥺 I am sorry but that's not right and we'll advance to the next question.")
                mistake_count = 0
                question_num += 1
                break  # Exit inner loop to move to next question
        else:
            user_answer = int(user_input)  # Convert string to integer

        if user_answer == correct_answer:  # Correct answer
            score += 1  # Operator to increment score
            print(f"🔥 Correct! Score: {score}/{max_score}")
            question_num += 1  # Move to next question
            mistake_count = 0  # Reset mistake count
            break  # Exit inner loop to move to next question
        else:  # Wrong answer
            mistake_count += 1
            print(f"🤔 Wrong! You've tried {mistake_count}/{MAX_MISTAKE_COUNT}. Please try again.")
            if mistake_count == MAX_MISTAKE_COUNT:
                print(f"🥺 I am sorry but that's not right and we'll advance to the next question.")
                mistake_count = 0
                question_num += 1
                break  # Exit inner loop to move to next question
            continue  # Retry same question if attempts remain

    if user_input.lower() == 'q':  # Check if user quit in inner loop
        break  # Exit outer loop

else:  # Runs if outer loop ends naturally (question_num reaches MAX_QUESTION_COUNT)
    print("\n")
    if score <= 2:
        print(f"💪 Sorry, but your score was {score}. Try again.")
    elif score == 3:
        print(f"👍️ Well done, your score was {score}.")
    else:
        print(f"🎉 Congratulations! You reached a score of {score}/{max_score}!")

print(f"🥳 Quiz ended. Final score: {score}/{max_score}")