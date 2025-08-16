# `Person` is the parent/base class. It provide the base blueprint. 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def greeting(self):
    return f'I am a person. My name is {self.firstname} {self.lastname}.'

# Use the Person class to create an object, and then execute the `greeting` method:
john_doe = Person("John", "Doe")
print(john_doe.greeting())

# `Student` is the child/derived class. It extends the parent class functionalities(Person).
class Student(Person):
  def __init__(self, fname, lname, id_card):
    super().__init__(fname, lname)
    self.id_card = id_card
    
  def greeting(self):
    return f'I am a student. My name is {self.firstname} {self.lastname} and my id card number is {self.id_card}'

# Object that instantiates from `Student` class will have the same properties and methods like the object that instantiates from `Person` class.

# In the example above, we extends the `Student` class functionalities by adding the `id_card` parameter for the `Student` class constructor and assign it to the `id_card` property.

# We also change the behavior of the `greeting` method.

# Here we instantiate an object from the `Student` class. 
student_john_doe = Student('John', 'Doe', '123')

# Let's call its `greeting` method.

print(student_john_doe.greeting())

