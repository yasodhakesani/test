#Unpack list and assign it to placeholder
#in the arbitrary arg return list only
list=['apple', 'melon', 'dragon', 'orange', 'kiwi', 'melon', 'mango']
(x,y,z,*p)=list
print(x,y,z,p)

#o/p: apple melon dragon ['orange', 'kiwi', 'melon', 'mango']
print(type(x),type(y),type(z),type(p))
#o/p:<class 'str'> <class 'str'> <class 'str'> <class 'list'>