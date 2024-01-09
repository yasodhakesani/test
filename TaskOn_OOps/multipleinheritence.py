from OOPs import multi_level_inheritence as mx

c=mx.Child()
c.common()
class A:
    def methodA(self):
        print(" method in A class")
class B(A):
    def methodB(self):
        print(" method in B class")
    def common(self):
        print("common method on class B")
class C:
    def methodC(self):
        print(" method in C class")
    def common(self):
        print("common method on class C") 
class D(C,B):
    def methodD(self):
        print(" method in D class")

d=D()
d.methodA() #different methods in all the class
d.methodB()
d.methodC()
d.methodD()
d.common() #method resolution same method in both the classes




