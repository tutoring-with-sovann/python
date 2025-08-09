# Create a new class of 'Animal'
# This class has 3 properties that resemble common animal characteristic
# - legs_count
# - has_fur
# - has_tail

class Animal:
  legs_count = 4
  has_fur = True
  has_tail = True


# Read from right to left
# `Animal()` means `to create an animal`.
# `animal = Animal()` means `assign the created animal to x variable`
# When you reference the `animal` variable, you reference the actual object of the class.
# This process can be call object instatiation.
animal = Animal();