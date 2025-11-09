# Exercise: Object Comparison and Equality
# Description: Create a Person class and compare objects using methods
#
# Tasks:
# 1. Create a Person class with __init__ constructor
# 2. Constructor should accept: name, age, city
# 3. Create a method is_same_age(other_person) that:
#    - Takes another Person object as a parameter
#    - Returns True if both persons have the same age, False otherwise
# 4. Create a method is_from_same_city(other_person) that:
#    - Takes another Person object as a parameter
#    - Returns True if both persons are from the same city, False otherwise
# 5. Create multiple person objects and compare them
#
# Expected Output:
# Alice (25 years old from New York)
# Bob (25 years old from Boston)
# Charlie (30 years old from New York)
#
# Are Alice and Bob the same age? True
# Are Alice and Bob from the same city? False
# Are Alice and Charlie the same age? False
# Are Alice and Charlie from the same city? True

# Solution:

class Person:
    def __init__(self, name, age, city):
        # Initialize person properties
        self.name = name
        self.age = age
        self.city = city

    def is_same_age(self, other_person):
        # Compare this person's age with another person's age
        # self.age is THIS person's age
        # other_person.age is the OTHER person's age
        return self.age == other_person.age

    def is_from_same_city(self, other_person):
        # Compare this person's city with another person's city
        return self.city == other_person.city


# Create person objects
alice = Person("Alice", 25, "New York")
bob = Person("Bob", 25, "Boston")
charlie = Person("Charlie", 30, "New York")

# Print information about each person
print(f"{alice.name} ({alice.age} years old from {alice.city})")
print(f"{bob.name} ({bob.age} years old from {bob.city})")
print(f"{charlie.name} ({charlie.age} years old from {charlie.city})")
print()

# Compare Alice and Bob
print(f"Are {alice.name} and {bob.name} the same age? {alice.is_same_age(bob)}")
print(f"Are {alice.name} and {bob.name} from the same city? {alice.is_from_same_city(bob)}")

# Compare Alice and Charlie
print(f"Are {alice.name} and {charlie.name} the same age? {alice.is_same_age(charlie)}")
print(f"Are {alice.name} and {charlie.name} from the same city? {alice.is_from_same_city(charlie)}")
