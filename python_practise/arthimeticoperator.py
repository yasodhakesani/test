def sum(a,b):
    return a+b

sub=lambda a,b:a-b
mul=lambda a,b:a*b

def div(a,b):
    if b>0:
        div=a/b
        floordiv=a//b
        print("Division", div ,"Floor Division", floordiv)
    else:
        print(" b should be greater than 0")
modulas=lambda a,b:a%b
power=lambda a,b:a**b


print(sum(1,20))
print(sub(2,1))
print(mul(2,3))
div(5,2)
print(modulas(10,2))
print(power(2,5))