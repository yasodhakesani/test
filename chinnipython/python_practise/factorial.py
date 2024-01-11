def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
print(fact(5))

for i in range(2,10,2):
    print(i)