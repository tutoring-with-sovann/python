# Exercise: Class with List Properties
# Description: Create a Classroom class that manages a list of students
#
# Tasks:
# 1. Create a Classroom class with __init__ constructor
# 2. Constructor should accept: class_name, teacher
# 3. Initialize an empty list called students in the constructor
# 4. Create the following methods:
#    - add_student(student_name) - adds a student to the list
#    - remove_student(student_name) - removes a student from the list
#    - get_student_count() - returns the number of students
#    - list_all_students() - prints all students in the class
# 5. Create a classroom object and test all methods
#
# Expected Output:
# Math Class taught by Mr. Smith
# Students in class: 0
# Adding students...
# Students in class: 3
# All students:
# 1. Alice
# 2. Bob
# 3. Charlie
# Removing Bob...
# Students in class: 2
# All students:
# 1. Alice
# 2. Charlie

# Solution:

class Classroom:
    def __init__(self, class_name, teacher):
        # Initialize basic properties
        self.class_name = class_name
        self.teacher = teacher
        # Initialize an empty list for students
        self.students = []  # This is an empty list that belongs to this classroom

    def add_student(self, student_name):
        # Add a student to the students list
        self.students.append(student_name)

    def remove_student(self, student_name):
        # Remove a student from the students list
        if student_name in self.students:
            self.students.remove(student_name)

    def get_student_count(self):
        # Return the number of students using len()
        return len(self.students)

    def list_all_students(self):
        # Print all students with numbering
        print("All students:")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student}")


# Create a classroom object
math_class = Classroom("Math Class", "Mr. Smith")

# Display initial information
print(f"{math_class.class_name} taught by {math_class.teacher}")
print(f"Students in class: {math_class.get_student_count()}")

# Add students
print("Adding students...")
math_class.add_student("Alice")
math_class.add_student("Bob")
math_class.add_student("Charlie")
print(f"Students in class: {math_class.get_student_count()}")
math_class.list_all_students()

# Remove a student
print("Removing Bob...")
math_class.remove_student("Bob")
print(f"Students in class: {math_class.get_student_count()}")
math_class.list_all_students()
