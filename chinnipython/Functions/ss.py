def sum(a,b):
    print(a+b)

sum(10,10)

def fun():
    return lambda x,y:x+y
z=fun()

print(z(10,20))