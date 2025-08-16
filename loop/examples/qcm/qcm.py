from typing import TypedDict, List
import json
import os
import sys

class Option(TypedDict):
    label: str
    text: str

class Question(TypedDict):
    question: str
    options: List[Option]
    correctAnswerIndex: int

RESOURCE_DIR = '/Users/sovannen/personal/tutoring/python/loop/examples/qcm/resources'
files_in_resource_dir = os.listdir(RESOURCE_DIR)

# Function that handling the resource file user input, return the index + 1 value of the files in the resource directory.
def get_user_input_resource():
    selected_resource = input('Select one question resource(q = exit) ')

    # User input 'q', they want to quit the application.
    if(selected_resource.lower() == 'q'):
        print('Exiting the program...')
        sys.exit(0)

    # User input string that isn't number, let them try again.
    if(not selected_resource.isdigit()):
        print('Not a number, please try again.')
        # return statement here is the key.
        # This tell the program to return this function all over again at this condition
        return get_user_input_resource()
    
    # User input is digital(legit answer), we can return this value.
    return int(selected_resource)

def get_user_action_input():
    action = input('N = Next, P = Previous, Q = quit: ')

    if(action.lower() not in ['n', 'p', 'q']):
        print('Invalid input. Enter again...')
        return get_user_action_input()

    return action.lower()


print('\n')
# Uses the enumerate to expose index out
# If we just use the normal for...in, we won't be able to obtain the index of current iteration.
for index, value in enumerate(files_in_resource_dir):
    print(f'{index + 1}. {value}')
print('\n')

# User input their desire file number, we store as index.
selected_resourece_index = get_user_input_resource() - 1


print('load the files...')
# Load the resource from the files
with open(f'{RESOURCE_DIR}/{files_in_resource_dir[selected_resourece_index]}', 'r') as file:
    questions: List[Question] = json.load(file)
print('finished loading the file.')
os.system('clear')
print('\n')


QCM_LETTERS = {
    0: 'A',
    1: 'B',
    2: 'C',
}

print("Welcome to our QCM practice.")

current_question_index: int = 0
while current_question_index < len(questions):
    question: Question = questions[current_question_index]
    print(f"\nQuestion {current_question_index + 1}: {question['question']}")
    for index, option in enumerate(question['options']):
        print(f"{option['label']}: {option['text']}")
    
    # .strip() returns a string that removes leading and trailing whitespace.
    # .upper() returns a string that transforms to uppercase.
    user_answer: str = input("Answer (A, B, C): ").strip().upper()
    
    if user_answer not in QCM_LETTERS.values():
        print("Invalid input. Please enter A, B, or C.")
        continue
    
    # Convert user answer to index
    user_answer_index: int = [k for k, v in QCM_LETTERS.items() if v == user_answer][0]
    
    # Check if the answer is correct
    if user_answer_index == question['correctAnswerIndex']:
        print("Correct!")
    else:
        correct_answer: str = question['options'][question['correctAnswerIndex']]['text']
        print(f"Wrong. The correct answer is {QCM_LETTERS[question['correctAnswerIndex']]}: {correct_answer}")
    
    action = get_user_action_input()

    if(action == 'n'):
        os.system('clear')
        current_question_index += 1
    elif (action == 'p'):
        os.system('clear')
        current_question_index -= 1
    else:
        print('Exiting the application...')
        sys.exit(0)

print("\nQuiz completed! Thank you for participating.")