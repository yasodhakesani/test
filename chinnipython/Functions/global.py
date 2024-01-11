"""Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
use the global keyword if you want to make a change to a global variable inside a function."""
x="global scope in main body of the python code"
def fun():
    print(x)

fun() #global scope in main body of the python code

x="global scope in main body of the python code"   
def fun():
    global x
    x="global scope inside the function"
    print(x)
print(x) #global scope in main body of the python code
fun()     #global scope inside the function 
print(x)    #global scope inside the function


x="global at main body"
def fun():
    global x
    x="redefine global in function"
    print(x," calling in outter function")
    def innerfun():
        global x
        x="redefine global in inner function"
        print(x ," calling in inner funtion")
    innerfun()
print(x ," calling x globally before calling function") #"global at main body calling x globally before calling function"
fun() #redefine global in function calling in outter funtion
#redefine global in inner function calling in inner funtion
print(x,"call the redefined global variable since we have called fun()") #redefine global in inner function call the redefined global variable since we have called fun()


