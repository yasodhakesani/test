import multi_level_inheritence
from OOPs import multi_level_inheritence
class Person:
    def __init__(self): #non parameterised Constructor
        print("This is non parameterised Constructor")
    def display(self,name):
        print("hello",name)
x=multi_level_inheritence.Child()
x.common()
obj=Person()
obj.display("john")
