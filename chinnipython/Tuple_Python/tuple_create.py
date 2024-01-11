#Two way of create Tuple
#one way
t1 = ("apple", "banana", "cherry")

#second way by using tuple constructor 
#it is ordered and allow the duplicates
#it is indexed 
#it is unchangeable
t3=tuple(("raj","rama","raj"))
t4=t3
print(t4 is t3)


#Tuple with one item you to mention , 
t2=("carrot",)
t5=("carrot",)
print(t2 is t5) #same object will refer return True
x=y=z=("apple", "banana", "cherry") #one tuple to multiple variables
print(x,y,z)
