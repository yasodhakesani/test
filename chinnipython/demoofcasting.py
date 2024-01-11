"""
Casting is to convert one data type to another data type
Casting methods :int,str,float
if you try to convert string to int or float
 r=float(z)
      ValueError: could not convert string to float: 'john'

"""
x=10
y=12.2
z="john"
p=str(x)
q=int(y)
r=float(x)
print(x,y,z)

#type is buit in function and we are using to get the variable data type
print(type(x),type(y),type(z))

#after casting get the variable data type
print(type(p),type(q),type(r))
print(p,q,r)

this_tuple=("1","3","4")
this_list=list(this_tuple)
print(type(this_list))
this_set=set(this_list)