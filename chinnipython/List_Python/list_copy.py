#you cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
#and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
l1=thislist
#object will be same
print(l1 is thislist)

#one way is to use the built-in List method copy().
#object/mem location is different
l2=thislist.copy()
print(l2 is thislist)

#Another way to make a copy is to use the built-in method list()
#object/mem location is different
l3=list(thislist)
print(l3 is thislist)