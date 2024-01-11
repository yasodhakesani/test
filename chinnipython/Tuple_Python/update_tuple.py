#since tuple is immutable we cannot directly add or remove the item in tuple
#we can convert tuple into list and then do the updates and again convert into tuple
t1 = ("apple", "banana", "cherry")
print(id(t1)) #2265810263232 id of tuple
t1=list(t1)
print(id(t1))   #2265810265600 id of list
print("Step1: convert tuple t1 into list" , type(t1))
print("Step2:Do the update opertaions on list as whatever we are doing in the list like append,extend,insert")
t1.append("kiwi")
t1.insert(0,"carrot")
#["carrot","apple", "banana", "cherry","kiwi"]
print(t1)
t1=tuple(t1)
print(id(t1)) #2265810263232 id of tuple
print("Step3: convert list into tuple",type(t1))
#("carrot","apple", "banana", "cherry","kiwi")


#Add two tuple
thistuple= ("apple", "banana", "cherry")
print(id(thistuple))
#2056846868224 mem location of thistuple before addting it with another tuple
y=("orange",)
thistuple +=y
#2056846895248 mem location will be different since tuple is immutable 
print(id(thistuple))


#remove items in tuple
t1 = ("apple", "banana", "cherry","kiwi")
t1=list(t1)
print("Step1: convert tuple t1 into list" , type(t1))
print("Step2:Do the remove opertaions on list as whatever we are doing in the list like remove,pop,del")
t1.remove("kiwi")
t1.pop(0)
del t1[1]
#["carrot","apple", "banana", "cherry","kiwi"]
print(t1)
t1=tuple(t1)

print("Step3: convert list into tuple",type(t1))
#("carrot","apple", "banana", "cherry","kiwi")

#del tuple with delete the entire tuple
t1 = ("apple", "banana", "cherry","kiwi")
del t1
