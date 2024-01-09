a="python is simple"
#capitalize convert the first character in string in upper and rest lower case
print(a.capitalize())
b="HELLO"
#casefold conver the string to lowercase
print(b.casefold())

"""center will take width as space how much we are passing and it will print string
    string.center(length)
    string.center(length,character)
"""
print(b.center(10))
print(b.center(10,"s"))

"""count number of times character/word repeated in string
    string.count(value)
    string.count(value,start,end) 

"""
x="eat an apple daily  then apple keeps doctor away"
print(x.count("apple"))
print(x.count("apple",0,13))
print(x.encode())

# endswith return True/False for the string ends with that value
print(x.endswith("e"))
print(x.endswith("e",0,13))

"""
expandtabs in the string if you mention \t will default tabsize 8 
if you mention specifically tabsize that will run
"""
x="h\tello"
print(x) #default tabsize as 8
print(x.expandtabs())
print(x.expandtabs(2))
print(x.expandtabs(4))
print(x.expandtabs(6))
print(x.expandtabs(8))
"""
#find() will search value in givn string first occurance
if not found will return -1
if you provide index start,end including value will search in b/w the index
index() also similar to find() but if value not found will raise an exception
Exception has occurred: ValueError
substring not found
  
"""
x="eat an apple daily  then apple keeps doctor away"
print("find", x.find("apple"))
print(x.find("apple",15,40))
print(x.find("rj"))
print(x.index("apple"))

#rfind() will search last occurance
#rindex() also will search for the last occurance
x="eat an apple daily  then apple keeps doctor away"
print(x.rfind("apple"))
print(x.rfind("apple",0,15))
print(x.rfind("rj"))
print(x.rindex("apple"))


