class Human:
  name = None
  def __init__(self, name):
    self.name = name
  def greeting(self):
    return f'Hello my name is {self.name}'
  
jake = Human('jake')

print(jake.greeting())

# And what if you want to delete the object properties?
# We can just the `del` keyword

# Let's says we want to delete the property of `name` from the `jake` object
# Here is how we use it:

del jake.name

# Let's call the greeting method again to see the differences

print(jake.greeting())

# Output
# Hello my name is jake
# Hello my name is joke
# Hello my name is None

# When deleting an object value, it's set to None


# Let's guess what will be the output of the greeting if I un-comment these code?
# jake.name = 'Sovann'

# print(jake.greeting())

# What will be the output?
# A. Hello my name is None
# B. Hello my name is Sovann
# C. Error thrown by the program
