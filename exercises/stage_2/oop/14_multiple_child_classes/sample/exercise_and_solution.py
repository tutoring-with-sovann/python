# Exercise: Multiple Child Classes
# Description: Create one parent class with multiple different child classes
#
# Tasks:
# 1. Create an Employee class (parent) with __init__ constructor
# 2. Employee constructor should accept: name, employee_id, salary
# 3. Add a get_details() method
# 4. Create two child classes:
#    - Manager: adds department property and overrides get_details()
#    - Developer: adds programming_language property and overrides get_details()
# 5. Create objects from all three classes
#
# Expected Output:
# Employee: John Doe, ID: E001, Salary: $50000
# Manager: Sarah Smith, ID: M001, Salary: $80000, Department: Sales
# Developer: Mike Johnson, ID: D001, Salary: $70000, Language: Python

# Solution:

# Step 1: Create the parent Employee class
class Employee:
    def __init__(self, name, employee_id, salary):
        # Initialize employee properties
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        # Return basic employee details
        return f"Employee: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}"


# Step 2: Create the Manager child class
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        # Call parent constructor
        super().__init__(name, employee_id, salary)
        # Add manager-specific property
        self.department = department

    def get_details(self):
        # Override to include department
        return f"Manager: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}, Department: {self.department}"


# Step 3: Create the Developer child class
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        # Call parent constructor
        super().__init__(name, employee_id, salary)
        # Add developer-specific property
        self.programming_language = programming_language

    def get_details(self):
        # Override to include programming language
        return f"Developer: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}, Language: {self.programming_language}"


# Step 4: Create objects from all three classes
employee1 = Employee("John Doe", "E001", 50000)
manager1 = Manager("Sarah Smith", "M001", 80000, "Sales")
developer1 = Developer("Mike Johnson", "D001", 70000, "Python")

# Step 5: Print details for all employees
print(employee1.get_details())
print(manager1.get_details())
print(developer1.get_details())
