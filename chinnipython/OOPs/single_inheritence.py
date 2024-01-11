class Parent:
    def __init__(self):
        print("Constructor")
    def display(self):
        print("Parent class Display method calling")
class Child(Parent):
    def person(self):
        print("Child class person method calling")

c=Child()
c.display()
c.person()