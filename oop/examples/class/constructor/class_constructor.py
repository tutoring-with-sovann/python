# Whenever a new object is created, you can define an __init__ method that will run.
# By default, every time you create an object, python already coded it into the class definition.

class Animal:
  leg_count = 4
  has_fur = True
  has_tail = True
  # When initalize this object, we use the __init__ to initalized the object property 
  def __init__(self, leg_count = 4):
    print("The line will run when this object is created.")
    self.leg_count = leg_count


# This is when you create an object from a class.
animal = Animal(2)

# This is when you use it, you call the `animal.leg_count`. You want to reference the leg_count value in your print statement. 
# This time the __init__ doesn't get called, it only get called once when it's created at the above line.
print(f"So class most animal has {animal.leg_count} legs")