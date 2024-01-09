s = {"apple", "banana", "cherry"}

s2 = {"pineapple", "mango", "papaya","papaya"}
print(id(s))
#add() to add anyy item to set
s.add("orange")
print(id(s))

#update can add one set to another set not only set it can be any iterable object (tuples, lists, dictionaries etc.).
s.update(s2)
print(s)  #{'cherry', 'orange', 'papaya', 'apple', 'mango', 'banana', 'pineapple'}
print(id(s))
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)