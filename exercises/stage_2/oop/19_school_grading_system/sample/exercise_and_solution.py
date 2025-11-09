# Exercise: School Grading System
# Description: Build a complete school system with Course, Student, and Grade classes
#
# Tasks:
# 1. Create a Course class with: course_name, course_code
# 2. Create a Grade class with: course (Course object), score
# 3. Add get_letter_grade() method to Grade class
# 4. Create a Student class with:
#    - name, student_id, grades list
#    - add_grade(grade) method
#    - get_gpa() method (calculate average)
#    - show_transcript() method
# 5. Create students, courses, and grades
# 6. Display student transcripts
#
# Expected Output:
# Student: Alice Johnson (ID: S001)
# Transcript:
# - Math (MATH101): 85 (B)
# - Science (SCI101): 92 (A)
# - History (HIST101): 78 (C)
# GPA: 85.00

# Solution:

# Step 1: Create the Course class
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"


# Step 2: Create the Grade class
class Grade:
    def __init__(self, course, score):
        self.course = course  # This is a Course object
        self.score = score

    def get_letter_grade(self):
        # Convert numeric score to letter grade
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

    def __str__(self):
        return f"{self.course}: {self.score} ({self.get_letter_grade()})"


# Step 3: Create the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # List of Grade objects

    def add_grade(self, grade):
        # Add a grade to the student's record
        self.grades.append(grade)

    def get_gpa(self):
        # Calculate average score across all courses
        if len(self.grades) == 0:
            return 0.0
        total = 0
        for grade in self.grades:
            total = total + grade.score
        return total / len(self.grades)

    def show_transcript(self):
        # Display student's full transcript
        print(f"Student: {self.name} (ID: {self.student_id})")
        print("Transcript:")
        for grade in self.grades:
            print(f"- {grade}")
        print(f"GPA: {self.get_gpa():.2f}")


# Step 4: Create courses
math = Course("Math", "MATH101")
science = Course("Science", "SCI101")
history = Course("History", "HIST101")

# Step 5: Create student
student1 = Student("Alice Johnson", "S001")

# Step 6: Create and add grades
grade1 = Grade(math, 85)
grade2 = Grade(science, 92)
grade3 = Grade(history, 78)

student1.add_grade(grade1)
student1.add_grade(grade2)
student1.add_grade(grade3)

# Step 7: Display transcript
student1.show_transcript()
