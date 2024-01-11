x=300
def fun():
    x=200   #variable created inside the function is called local scope of that function
    print(x)
print(x)    #300 x is global scope
fun()       #200 x is local scope


#The local variable can be accessed from a function within the function:
def fun():
    x=20
    print(x)
    def innerfun():
        print(x)
    innerfun()

fun()

x=["global","scope"]
def fun():
    global x
    x=[10,20,30]
    print(x)
    def innerfun():
        x=[10,40]
        print(x)
    innerfun()
print(x) #["global","scope"]
fun() #[10,20,30] #[10,40]
print(x) #[10,20,30]


