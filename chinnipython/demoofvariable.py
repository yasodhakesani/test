"""
1.Variable using to store the data type
2.Could not start with number,space b/w,
3.variable is case senstive
4.variable can be camel,pascal,snake case
"""
myVarName="camel case"
my_var_name="snake case"
MyVarName="pascal case"
_my_var_name="under score"
print(myVarName,my_var_name,MyVarName,_my_var_name)
#define variable and assign different data types
x=10
y="john"
z=10.2
print(x,y,z)
#name and Name are two different variable because python is case senstive
name="raj"
Name="sally"


#multiple values to multiple variable
a,b,c="Java","C","python"
print(a,b,c)
#one values to multiple variable
p=q=r="One"
print(p,q,r)
#redefine variable p 
p="Two"
print(p,q,r)


x=y=z="Story"
print( x,y,z)
print(id(x),id(y),id(z))
x="sally"
print(x,y,z)
print(id(x),id(y),id(z))
x,y,z="hello","john","sally"
print(x,y,z)
print(id(x),id(y),id(z))
x="raj"
print(x,y,z)
print(id(x),id(y),id(z))


