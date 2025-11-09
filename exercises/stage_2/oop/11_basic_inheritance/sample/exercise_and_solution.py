# Exercise: Basic Inheritance
# Description: Create a parent Animal class and a child Dog class that inherits from it
#
# Tasks:
# 1. Create an Animal class with __init__ constructor
# 2. Animal constructor should accept: name, age
# 3. Add a method make_sound() that prints "Some generic animal sound"
# 4. Create a Dog class that inherits from Animal
# 5. Dog should have the same constructor as Animal (no additional properties yet)
# 6. Create both Animal and Dog objects to show inheritance
#
# Expected Output:
# Generic animal named Buddy is 5 years old
# Some generic animal sound
# Dog named Max is 3 years old
# Some generic animal sound

# Solution:

# Step 1: Create the parent Animal class
class Animal:
    def __init__(self, name, age):
        # Initialize animal properties
        self.name = name
        self.age = age

    def make_sound(self):
        # Generic animal sound
        print("Some generic animal sound")


# Step 2: Create the Dog class that inherits from Animal
class Dog(Animal):
    # Dog inherits all properties and methods from Animal
    # We don't need to rewrite __init__ or make_sound() - they're inherited!
    pass  # pass means "do nothing additional"


# Step 3: Create an Animal object
animal1 = Animal("Buddy", 5)
print(f"Generic animal named {animal1.name} is {animal1.age} years old")
animal1.make_sound()

print()  # Empty line for spacing

# Step 4: Create a Dog object
dog1 = Dog("Max", 3)
# Even though we didn't define __init__ in Dog class, it inherits it from Animal
print(f"Dog named {dog1.name} is {dog1.age} years old")
dog1.make_sound()  # This also comes from the Animal class
