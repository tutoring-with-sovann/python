# Exercise: Inheritance with super()
# Description: Create a Student class that inherits from Person and uses super()
#
# Tasks:
# 1. Create a Person class with __init__ constructor
# 2. Person constructor should accept: name, age, city
# 3. Create a Student class that inherits from Person
# 4. Student constructor should accept: name, age, city, student_id, major
# 5. Use super().__init__() to call the Parent constructor
# 6. Add the additional student_id and major properties
# 7. Create both Person and Student objects
#
# Expected Output:
# Person: John Doe, 45 years old, lives in New York
# Student: Alice Smith, 20 years old, lives in Boston
# Student ID: S12345, Major: Computer Science

# Solution:

# Step 1: Create the parent Person class
class Person:
    def __init__(self, name, age, city):
        # Initialize person properties
        self.name = name
        self.age = age
        self.city = city


# Step 2: Create the Student class that inherits from Person
class Student(Person):
    def __init__(self, name, age, city, student_id, major):
        # Use super() to call the parent class's __init__ method
        # This sets name, age, and city using Person's __init__
        super().__init__(name, age, city)

        # Now add the Student-specific properties
        self.student_id = student_id
        self.major = major


# Step 3: Create a Person object
person1 = Person("John Doe", 45, "New York")
print(f"Person: {person1.name}, {person1.age} years old, lives in {person1.city}")

print()  # Empty line for spacing

# Step 4: Create a Student object
student1 = Student("Alice Smith", 20, "Boston", "S12345", "Computer Science")
# Student has all Person properties (name, age, city) plus student_id and major
print(f"Student: {student1.name}, {student1.age} years old, lives in {student1.city}")
print(f"Student ID: {student1.student_id}, Major: {student1.major}")
