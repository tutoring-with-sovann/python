# Class that represent human being
class Human:
  # Name of this human
  name = None
  # Constructor that accept a `name` parameter then set that value to its current object `name` property.
  def __init__(self, name):
    self.name = name
  # A method that return the greeting statement in `string`.
  def greeting(self):
    # This method need access to the self parameter to obtain its `name` property for return value.
    return f'Hello my name is {self.name}'
  
# I instantiate a new object name `jake` from the `Human` class. I also pass in the argument `jake` to the parameter of `name` in the `Human` class's constructor.
jake = Human('jake')

# Now I print the output of the .greeting() method.
# print() function take one parameter of type `string` and `Human.greeting()` return value is string.
print(jake.greeting())