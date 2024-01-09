#it is unordered
#it is unchangable but you can remove and add new item
#set is unindexed
#it will not allow the duplicates means duplicates  will ignore even it you try to add
#it is heterogenous

thisset = {"apple", "banana", "cherry"}
s1=set({"apple", "banana", "cherry"})
s2=set(["apple","banana"])
s3=set({"s":"app","r":"sss"})
print(type(s3))
print(s3) #{"r","s"}
s = {"apple", "banana", "cherry","apple"}
print(s) #{"apple", "banana", "cherry"


#True and 1 is considered the same value:
s1= {"apple", "banana", "cherry", True, 1, 2,False,0}
print(s1) #{False, True, 2, 'apple', 'banana', 'cherry'}

