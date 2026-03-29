# Exercise: School Grading System (Extended)
# Description: Build a complete school system with teachers, enrollment, attendance, and weighted grades
#
# Tasks:
# 1. Create a Course class with: course_name, course_code, credits, teacher
#    - Add enroll(student) method
#    - Add add_assignment(category, weight, max_score) method
#    - Add get_class_average() method
#    - Add get_class_rankings() method - returns students sorted by grade
# 2. Create an Assignment class with: name, category, weight, max_score
# 3. Create a Submission class with: assignment, student_score
#    - Add get_weighted_score() method
# 4. Create a Student class with: name, student_id
#    - enroll_in(course) method
#    - submit_assignment(course, assignment, score) method
#    - get_course_grade(course) - calculates weighted average
#    - get_gpa() - across all courses (4.0 scale: A=4, B=3, C=2, D=1, F=0)
#    - record_attendance(course, date, present) method
#    - get_attendance_rate(course) method
#    - show_transcript() - shows all courses with grades, attendance
# 5. Create a Teacher class with: name, teacher_id, courses_teaching (list)
#    - Add teach_course(course) method
#    - Add grade_submission(course, student, assignment, score) method
#    - Add calculate_final_grades(course) method
# 6. Demonstrate: Create courses, enroll students, submit assignments, show transcripts
#
# Expected Output:
# Course: Math 101 (MATH101) - 4 credits - Teacher: Dr. Smith
# Enrolled Students: 3
#
# Transcript for Alice Johnson (S001):
# - Math 101 (MATH101): 92% (A) - Attendance: 95%
#   * Homework: 95% weighted, Quiz: 88% weighted, Exam: 92% weighted
# - Science 101 (SCI101): 87% (B+) - Attendance: 90%
#   * Homework: 90% weighted, Lab: 85% weighted
# Overall GPA: 3.50
#
# Class Rankings for Math 101:
# 1. Alice Johnson: 92%
# 2. Bob Wilson: 88%
# 3. Carol Davis: 85%
#
# Hint: Use weighted average: sum(score * weight) / sum(weights). Composition: Student→Submissions→Assignments.

# Solution:

# Step 1: Create Assignment class
class Assignment:
    def __init__(self, name, category, weight, max_score=100):
        self.name = name
        self.category = category
        self.weight = weight
        self.max_score = max_score

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.weight}% weight"


# Step 2: Create Submission class
class Submission:
    def __init__(self, assignment, student_score):
        self.assignment = assignment
        self.student_score = student_score

    def get_weighted_score(self):
        # Calculate percentage then apply weight
        percentage = (self.student_score / self.assignment.max_score) * 100
        return percentage * (self.assignment.weight / 100)

    def __str__(self):
        percentage = (self.student_score / self.assignment.max_score) * 100
        return f"{self.assignment.name}: {percentage:.0f}% (weighted: {self.get_weighted_score():.1f})"


# Step 3: Create Course class
class Course:
    def __init__(self, course_name, course_code, credits, teacher=None):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.teacher = teacher
        self.students = []
        self.assignments = []

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_in(self)

    def add_assignment(self, name, category, weight, max_score=100):
        assignment = Assignment(name, category, weight, max_score)
        self.assignments.append(assignment)
        return assignment

    def get_class_average(self):
        if not self.students:
            return 0
        total = sum(student.get_course_grade(self) for student in self.students)
        return total / len(self.students)

    def get_class_rankings(self):
        rankings = sorted(self.students, key=lambda s: s.get_course_grade(self), reverse=True)
        return rankings

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "TBA"
        return f"{self.course_name} ({self.course_code}) - {self.credits} credits - Teacher: {teacher_name}"


# Step 4: Create Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # List of Course objects
        self.submissions = {}  # {(course, assignment): submission}
        self.attendance = {}  # {course: {"total": N, "present": M}}

    def enroll_in(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.attendance[course] = {"total": 0, "present": 0}

    def submit_assignment(self, course, assignment, score):
        submission = Submission(assignment, score)
        self.submissions[(course, assignment)] = submission

    def get_course_grade(self, course):
        course_submissions = [s for (c, a), s in self.submissions.items() if c == course]
        if not course_submissions:
            return 0
        total_weighted = sum(s.get_weighted_score() for s in course_submissions)
        total_weight = sum(s.assignment.weight for s in course_submissions)
        return total_weighted if total_weight == 0 else total_weighted / total_weight * 100

    def get_letter_grade(self, percentage):
        if percentage >= 93:
            return "A"
        elif percentage >= 90:
            return "A-"
        elif percentage >= 87:
            return "B+"
        elif percentage >= 83:
            return "B"
        elif percentage >= 80:
            return "B-"
        elif percentage >= 77:
            return "C+"
        elif percentage >= 73:
            return "C"
        elif percentage >= 70:
            return "C-"
        elif percentage >= 67:
            return "D+"
        elif percentage >= 63:
            return "D"
        elif percentage >= 60:
            return "D-"
        else:
            return "F"

    def get_gpa_points(self, letter_grade):
        grade_map = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
                     "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0}
        return grade_map.get(letter_grade, 0.0)

    def get_gpa(self):
        if not self.courses:
            return 0.0
        total_points = 0
        total_credits = 0
        for course in self.courses:
            grade_pct = self.get_course_grade(course)
            letter = self.get_letter_grade(grade_pct)
            total_points += self.get_gpa_points(letter) * course.credits
            total_credits += course.credits
        return total_points / total_credits if total_credits > 0 else 0.0

    def record_attendance(self, course, present):
        if course in self.attendance:
            self.attendance[course]["total"] += 1
            if present:
                self.attendance[course]["present"] += 1

    def get_attendance_rate(self, course):
        if course not in self.attendance or self.attendance[course]["total"] == 0:
            return 0
        return (self.attendance[course]["present"] / self.attendance[course]["total"]) * 100

    def show_transcript(self):
        print(f"\nTranscript for {self.name} ({self.student_id}):")
        for course in self.courses:
            grade_pct = self.get_course_grade(course)
            letter = self.get_letter_grade(grade_pct)
            attendance = self.get_attendance_rate(course)
            print(f"- {course}: {grade_pct:.0f}% ({letter}) - Attendance: {attendance:.0f}%")

            # Show assignment breakdown
            course_subs = [(a, s) for (c, a), s in self.submissions.items() if c == course]
            if course_subs:
                for assignment, submission in course_subs:
                    print(f"  * {submission}")

        print(f"Overall GPA: {self.get_gpa():.2f}")


# Step 5: Create Teacher class
class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.courses_teaching = []

    def teach_course(self, course):
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            course.teacher = self

    def grade_submission(self, course, student, assignment, score):
        student.submit_assignment(course, assignment, score)

    def calculate_final_grades(self, course):
        rankings = course.get_class_rankings()
        print(f"\nClass Rankings for {course.course_name}:")
        for i, student in enumerate(rankings, 1):
            grade = student.get_course_grade(course)
            print(f"{i}. {student.name}: {grade:.0f}%")


# Step 6: Demonstration
# Create teacher
teacher = Teacher("Dr. Smith", "T001")

# Create courses
math = Course("Math 101", "MATH101", 4, teacher)
science = Course("Science 101", "SCI101", 3, teacher)

# Add assignments to math
hw1 = math.add_assignment("Homework 1", "Homework", 30, 100)
quiz1 = math.add_assignment("Quiz 1", "Quiz", 20, 100)
exam1 = math.add_assignment("Midterm", "Exam", 50, 100)

# Add assignments to science
lab1 = science.add_assignment("Lab 1", "Lab", 40, 100)
hw2 = science.add_assignment("Homework 1", "Homework", 60, 100)

# Create students
alice = Student("Alice Johnson", "S001")
bob = Student("Bob Wilson", "S002")
carol = Student("Carol Davis", "S003")

# Enroll students
for student in [alice, bob, carol]:
    math.enroll(student)
    science.enroll(alice)  # Only Alice in science

# Record some attendance
for _ in range(20):
    alice.record_attendance(math, True)
    bob.record_attendance(math, True)
    carol.record_attendance(math, True)
    alice.record_attendance(science, True)

# Submit assignments - Alice excels
alice.submit_assignment(math, hw1, 95)
alice.submit_assignment(math, quiz1, 88)
alice.submit_assignment(math, exam1, 92)
alice.submit_assignment(science, lab1, 85)
alice.submit_assignment(science, hw2, 90)

# Bob does well
bob.submit_assignment(math, hw1, 90)
bob.submit_assignment(math, quiz1, 85)
bob.submit_assignment(math, exam1, 88)

# Carol struggles
carol.submit_assignment(math, hw1, 82)
carol.submit_assignment(math, quiz1, 78)
carol.submit_assignment(math, exam1, 90)

# Show results
print(f"Course: {math}")
print(f"Enrolled Students: {len(math.students)}")

alice.show_transcript()
teacher.calculate_final_grades(math)
