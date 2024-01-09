#assign string to varaiable
x="hello world"
y="ram"
print(len(y)) #11
#to get the length of the string
print(len(x)) #3
#Triple double quote to write multi string
multistring=""" Built in funtion in Python:
type
len
id """
#Triple single quote to write multi string
multistring_singlequote=''' Built in funtion in Python:
type
len
id '''

print("multistring" + multistring)
print("multistring in single quotes" + multistring_singlequote)

"""
Slicing: to get the sub list /string from whole string
syntax: x[start_index:ending index],x[start_index],x[:ending_index]
syntax2/:x[start_index:ending_index:step]
step: To skip the num of index positions

"""
x="hello world"
print("print zeroth index" + x[0])   #h
print("print 0th to 5th index" + x[0:6]) #hello  
print("print even positions by step with 2" + x[0:6:2]) #hlo
print("print entire string by giving start index" + x[0:])
print("print entire string by giving length of index" + x[:11])
print("print entire string by giving start negative  index " + x[-11:])
print(x[-9:-6])


x="hello world"
print(x[slice(6,12)])


x = 'GeeksforGeeks'
slice_obj1 = slice(3)
slice_obj2 = slice(1, 5, 2) #ek
print(x[slice_obj1])
print(x[slice_obj2])

