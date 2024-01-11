#function is a block of code which can run only when it is called
def func():
    a=10
    b=20
    print(a+b)

func()

#parameters or arguments we are passing the function
#A parameter is the variable listed inside the parentheses in the function definition. a,b are parameters
#An argument is the value that is sent to the function when it is called. 1,2 are arguments
def sum(a,b):
    print(a+b)

sum(1,2)
sum(2,3)

#lambda arguments:expression
#lambda function is small anonymous function
#lambda can take any num of arguments but only one expression
#use of lambad function
#The power of lambda is better shown when you use them as an anonymous function inside another function.
def mul(a):
    return lambda x : x*a

result=mul(2)
print(result(2))
print(result(3))

def sum(a):
    return lambda x,y: a+y+x
result1=sum(2)
print(result1(2,3))

