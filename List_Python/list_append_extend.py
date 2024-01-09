#append()
#append will add the new items at the end of the list
list=['apple', 'melon', 'dragon', 'orange', 'kiwi', 'melon', 'mango']
list.append("orange")
print(list)

list1=[10,20,30,40,20,50]
list1.append("apple")
list1.append("orange")
print(list1)

#extend()
#To append elements from another list to the current list at the end, use the extend() method.
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list1.extend(list1)
print(list1)

thistuple=("tuple1","tuple2")
thislist=["1","2"]
thislist.extend(thistuple)
print(thislist)

list1.extend(list)
print(list1)


list.extend("hello")
#o/p:['apple', 'melon', 'dragon', 'orange', 'kiwi', 'melon', 'mango', 'orange', 'h', 'e', 'l', 'l', 'o']
print(list)