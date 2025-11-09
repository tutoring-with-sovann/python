# Exercise: Methods and Property Modification
# Description: Create a Student class with methods that modify properties and return values
#
# Tasks:
# 1. Create a Student class with __init__ constructor
# 2. Constructor should accept: name, grade (e.g., "10th"), score (0-100)
# 3. Create a method called study() that increases the score by 5 points
# 4. Create a method called get_letter_grade() that returns:
#    - "A" if score >= 90
#    - "B" if score >= 80
#    - "C" if score >= 70
#    - "D" if score >= 60
#    - "F" if score < 60
# 5. Create a student object, call study() a few times, and print the results
#
# Expected Output:
# Student: Alice Johnson, Grade: 10th, Score: 75, Letter Grade: C
# After studying...
# Student: Alice Johnson, Grade: 10th, Score: 85, Letter Grade: B

# Solution:

# Step 1: Create the Student class
class Student:
    def __init__(self, name, grade, score):
        # Initialize instance properties
        self.name = name
        self.grade = grade
        self.score = score

    # Step 2: Create study method that modifies score
    def study(self):
        # self.score refers to this specific student's score
        self.score = self.score + 5  # Increase score by 5 points
        # Alternative: self.score += 5

    # Step 3: Create get_letter_grade method that returns a value
    def get_letter_grade(self):
        # Use if-elif-else to determine letter grade based on score
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"


# Step 4: Create a student object
student1 = Student("Alice Johnson", "10th", 75)

# Step 5: Print initial information
letter = student1.get_letter_grade()  # Call the method to get the letter grade
print(f"Student: {student1.name}, Grade: {student1.grade}, Score: {student1.score}, Letter Grade: {letter}")

# Step 6: Student studies (call study method twice)
print("After studying...")
student1.study()  # Score goes from 75 to 80
student1.study()  # Score goes from 80 to 85

# Step 7: Print updated information
letter = student1.get_letter_grade()  # Get new letter grade
print(f"Student: {student1.name}, Grade: {student1.grade}, Score: {student1.score}, Letter Grade: {letter}")
