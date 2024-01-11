class GrandParent:
    def common(self):
        print("Grand Parent class calling common method")
class Parent(GrandParent):
    def common(self):
        print("Parent class calling common method")
class Child(Parent):
    def common(self):
        print("Child class calling common method")

    


c=Child()
c.common()
p=Parent()
p.common()
GP=GrandParent()
GP.common()

