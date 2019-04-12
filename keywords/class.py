#--- Class: Define a Class----
#--- self parameter is a reference to the class itself----
#--- self is used to access variables that belongs to the class----
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("I am " + self.age + "years old")

p1 = Person("Thomas", "20 ")
p1.myfunc()
