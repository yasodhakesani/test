s = {"apple", "banana", "cherry"}
s.remove("apple")

#remove will raise an error if item not found
#discard() will not raise the error and return None
print(s.discard("raj"))
#pop() will remove any one item since it is unordered
print(s.pop())


#clear() method empties the set:
print(s.clear)

s1 = {"apple", "banana", "cherry"}

#del will delete the set completely
del s1
