def fun(a,b,*c):
    result=a+b
    print(c, "arbirtrary argument returns tuple")
    for x in c:
        result+=x
    print(result)

fun(1,1,5,2,3,4)
