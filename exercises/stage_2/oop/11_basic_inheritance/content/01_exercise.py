# Exercise: Basic Inheritance with Method Overriding
# Description: Create a parent Animal class and child classes (Dog, Cat) that inherit from it
#
# Tasks:
# 1. Create an Animal class with __init__ constructor that accepts name and age
# 2. Add a method make_sound() that prints "Some generic animal sound"
# 3. Create a Dog class that inherits from Animal
# 4. Dog should accept name, age, AND breed in its constructor (use super() to initialize parent)
# 5. Override make_sound() in Dog to print "Woof!"
# 6. Create a Cat class that inherits from Animal
# 7. Cat should have its own make_sound() that prints "Meow!"
# 8. Create instances of all three classes and call make_sound() on each
#
# Expected Output:
# Generic animal named Buddy is 5 years old
# Some generic animal sound
# Dog named Max is 3 years old
# Breed: Golden Retriever
# Woof!
# Cat named Whiskers is 2 years old
# Meow!
#
# Hint: Use super().__init__() in the child class constructor to call the parent's __init__

# Write your code here:
