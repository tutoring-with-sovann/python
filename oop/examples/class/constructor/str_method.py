# Here we have 2 different classes, one change its default __str__ method and another one we keep the same.

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f'{self.name} has ${self.age} years old.'

p1 = Person1("John", 36)

print(p1)


class Person2:
  def __init__(self, name, age):
    self.name = name;
    self.age = age;

p2 = Person2("Jake", 30)

print(p2)