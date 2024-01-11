#list comprehension offer shortest syntax for looping through list
#newlist = [expression for item in iterable if condition == True]
list = ["apple", "banana", "cherry"]
[print(x) for x in list]
[print(list[x]) for x in range(len(list))]
[print(list[x]) for x in range(len(list)) if "cherry" in list[x]]
new_list=[x if x!="banana" else "orange" for x in list]
print(new_list)
list1=[x for x in list if "apple" in x]
print(list1)

