class Human:
  name = None
  def __init__(self, name):
    self.name = name
  def greeting(self):
    return f'Hello my name is {self.name}'
  
jake = Human('jake')

print(jake.greeting())

# Above are the same code from previous example

# Okay now let's call `jake` differently, let's call him `joke` lol
# It's as simple as assignment operation
# Write `jake.name` means to call the property `name` of the `jake` object.
# Write `jake.name = 'joke'` means assigns the value `joke` which is a string to the property `name` of the `jake` object.
jake.name = 'joke'

# And you've just modified the object properties value.
# Lets make `jake` object greet us again.

print(jake.greeting())

# Output:
# Hello my name is jake
# Hello my name is joke

# We've just successfully modified the jake object.