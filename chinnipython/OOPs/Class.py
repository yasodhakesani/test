"""Object Oriented Programming:
Object: Everything in Python is an object, and almost everything has attributes and methods
Methods: method is a function associated with object. Any object type can have methods
Class: classes serve as a template to create objects. It’s a blue print to create object"""

class Person:
    x=0 #class variable
    def __init__(self,name,age): #parameterized constructor
        self.x=name #instance variable
        self.y=age
    def greet(self):
        print("GoodMorning! I am {} and I am {} Years Old".format(self.x,self.y))
        Person.x+=1 # Accessing the class variable using the name of the class 

obj=Person("Raj",25)
obj.greet()
obj1=Person("Ram",35)
obj1.greet()
print(Person.x)

  