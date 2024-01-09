"""
List:
It is used to store multiple items in a single variable
Properties:
it is hetrogenous (all data types may have in single item) eg:["abc", 34, True, 40, "male"]
it is ordered in sequence
it is changeable means mutable
it will allow duplicates
type() will give as <class list>
if we are adding new item it will add end of the list

we can create list in two ways
1.list()
2.myList=["abc", 34, True, 40, "male"]
3.new_list=[]
"""

#three ways of creating list
l=["sanvi","2","daughter"]
list1=["abc", 34, True, 40, "male","male"]
#we can pass list,tuple in list() constructor
list2=list(("apple", "banana", "cherry","apple"))


#Creating new list:

new_list=[]
new_list.append("Apple")
new_list.append("BALL")
l.append("yaso")
l.extend(new_list)
print(l)
print(type(list1))
print(type(list2))
print(type(new_list))

#print each item in list
for x in list1:
    print(x)

#print each item in list by calling index  
for x in range(len(list2)):
    print(list2[x])

#print entire list
print(new_list)
#print in b/w range
#list[start:end:sequence]
print(list1[0:6:2])
print(list2[:5])
print(list2[3:])

#negative index in list
list1=["abc","male","male"]


for x in list1:
    if "abc"  in x:
        continue
    print(x)

