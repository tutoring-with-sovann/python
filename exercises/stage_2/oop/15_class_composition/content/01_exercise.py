# Exercise: Class Composition (Extended Has-A Relationships)
# Description: Create classes with multiple composition relationships and nesting
#
# Tasks:
# 1. Create an Address class with: street, city, zip_code, and get_full_address() method
# 2. Create an Employee class with: name, title, salary, address (Address object)
#    - Add get_info() method that returns employee details WITH address
# 3. Create a Department class with: name, manager (Employee object), employees (list of Employee objects)
#    - Add add_employee(employee) method to add an employee to the department
#    - Add get_headcount() method that returns number of employees (excluding manager)
#    - Add get_total_salary() method that sums all salaries (manager + employees)
# 4. Create a Company class with: name, address (Address object), departments (list of Department objects)
#    - Add add_department(department) method
#    - Add display_info() method that prints company name, address, and each department's info
# 5. Create objects demonstrating:
#    - One Address shared between Company and an Employee
#    - Multiple Departments each with a Manager and Employees
#    - Company containing all Departments
#
# Expected Output:
# TechCorp Inc.
# Headquarters: 100 Business Ave, San Francisco, 94105
#
# --- Engineering ---
# Manager: Alice Chen (CTO) - $150000
# Employees: 2
#   - Bob Smith (Developer) - $90000
#   - Carol Lee (Developer) - $95000
# Department Total Salary: $335000
#
# --- Sales ---
# Manager: Dave Wilson (Sales Director) - $120000
# Employees: 1
#   - Eve Brown (Sales Rep) - $70000
# Department Total Salary: $190000
#
# Company Total Employees: 6
# Company Total Payroll: $525000
#
# Hint: Composition can be multi-level (Company→Department→Employee→Address).
#       Objects can be shared (same Address used by Company and Employee).
#       Use loops to iterate through composed collections.

# Write your code here:
