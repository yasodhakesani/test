def fact(n):
    if n<1:
        return 1
    else:
        return n* fact(n-1)

print(fact(5))
num=int(input("enter number"))
if num<0:
    print("wrong input")
elif num==0:
    print("Factorial of 0! is 1")
else:
    print("Factorial of number {}".format(num),fact(num))

