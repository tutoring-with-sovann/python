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

# Write your code here:
