
class Parent:
    def common(self):
        print("Parent common method")
    def house(self):
        print("Parent class House method calling")
class Child(Parent):
    def common(self):
        print("Child common method")
class GrandChild(Child):
    def common(self):
        print("GrandChild common method")

p=Parent()
p.common()
c=Child()
c.common()
gc=GrandChild()
gc.common()
gc.house()

