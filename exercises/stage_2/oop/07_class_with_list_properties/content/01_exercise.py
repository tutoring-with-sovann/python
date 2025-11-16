# Exercise: Class with List Properties - Advanced Student Tracking
# Description: Create a Classroom class that manages students with grades and analytics
#
# Tasks:
# 1. Create a Classroom class with __init__ constructor
# 2. Constructor should accept: class_name, teacher, max_capacity
# 3. Initialize an empty dictionary called students in the constructor (key: student_name, value: grade)
# 4. Create the following methods:
#    - add_student(student_name, grade) - adds a student with their grade (0-100)
#      Returns False if class is at max capacity
#    - remove_student(student_name) - removes a student from the class
#    - update_grade(student_name, new_grade) - updates a student's grade
#    - get_student_count() - returns the number of students
#    - get_student_grade(student_name) - returns the grade for a specific student
#    - get_class_average() - calculates and returns average grade for all students
#    - get_honor_students() - returns list of students with grade >= 90
#    - get_students_below(threshold) - returns list of students with grade < threshold
#    - list_all_students() - prints all students with their grades, sorted by name
#    - is_full() - returns True if classroom is at max capacity
# 5. Create a classroom object and test all methods with at least 5 students
#
# Expected Output:
# Math Class taught by Mr. Smith (Max: 5)
# Students in class: 0
# Class is full? False
# Adding students...
# Added Alice with grade 95
# Added Bob with grade 78
# Added Charlie with grade 92
# Added Diana with grade 85
# Added Eve with grade 88
# Students in class: 5
# Class is full? True
# Failed to add Frank (class full)
#
# All students:
# Alice: 95
# Bob: 78
# Charlie: 92
# Diana: 85
# Eve: 88
#
# Class average: 87.6
# Honor students (>=90): Alice, Charlie
# Students below 80: Bob
#
# Updating Bob's grade to 82...
# Bob's new grade: 82
# New class average: 88.4
#
# Removing Diana...
# Students in class: 4
# Class is full? False
#
# Hint: Use self.students = {} to create an empty dictionary
# For class average: sum(self.students.values()) / len(self.students)
# To sort dictionary by keys: sorted(self.students.items())

# Write your code here:
