#The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#first occurance item will remove
list = ["apple", "banana", "cherry","banana"]
list.remove("banana")
print(list)


#pop() will remove the specified item using index
#if we are giving any index in pop() last item will get remove
list1 = ["apple", "banana", "cherry","banana","kiwi"]
print(list1.pop())
list1.pop(0)

print(list1)


#The del keyword also removes the specified index:
#del the will remove the entire list mean object will delete
dellist = ["apple", "banana", "cherry"]
del dellist[0]
print(dellist)
del dellist

#clear() method empties the list means clear the content list will present as empty
#But in del list will also remove
clearlist=["apple", "banana", "cherry"]

clearlist.clear()
print(clearlist)