set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
#union andd update exclude the duplicates
s3=set1.union(set2)
print(s3) #{"a", "b" , "c",1, 2, 3}
#intersection_update will give only common item in set
print(set1.intersection_update(set2))
#print(s4) #None

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.intersection(y)) #{'apple'}

#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #{'google', 'cherry', 'microsoft', 'banana'}
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y) 
print(z)    #{'google', 'cherry', 'microsoft', 'banana'}
print(x)  #{'apple', 'banana', 'cherry'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.difference(y)) #{"banana", "cherry"}}
print(x) #{'apple', 'cherry', 'banana'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.difference_update(y)) #None
print(x) #{"banana", "cherry"}}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) #True

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) #True

print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y) #True

print(z)