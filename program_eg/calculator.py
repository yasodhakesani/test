def add(a,b):
    result=a+b
    print("sum of a ,b is",result)
def subtract(a,b):
    result=a-b
    print("subtract of a,b",result)
def divide(a,b):
    result=a/b
    print("Divide of a,b",result)
def multiply(a,b):
    result=a*b
    print("multiply of a,b",result)

print("please select choice of operations")
print("a: ADD")
print("b: Subtract")
print("c: Multiply")
print("d: Divide")
choice=input("enter any one opertaions in a,b,c,d: ")
a=int(input("enter first number"))
b=int(input("enter second number"))

if choice=="a":
    add(a,b)
elif choice=="b":
    subtract(a,b)
elif choice=="c":
    multiply(a,b)
elif choice=="d":
    divide(a,b)
else:
    print("enter only operations a,b,c,d")