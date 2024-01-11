def fun(x,y,**z):
    result=x+y
    print(z, "keyword args return dict") # you can use all dictionary methods
    for a in z:
        result+=z[a]
    print(result)
    for a,b in z.items():
        print(a,b)

fun(1,2,a=3,b=4,c=5)