class GrandParent:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print(id,name)
    def common(self):
        print("Grand Parent class calling common method")
class Parent(GrandParent):
    def __init__(self, id, name):
        super().__init__(id, name) #using super keyword calling GrandParent variables
        
    def common(self):
        print("Parent class calling common method")

class Child(Parent):
    def common(self):
        super().common() #using super keyword calling parent class common method

    
c=Child(102,"ram")
c.common() 

gp=GrandParent(101,"Rama")



