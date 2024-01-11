def fun(x):
    if x>0:
        result = x + fun(x - 1)
    else:
        result=0
    return result
    


print(fun(3))
"""
if(true)
f(3)---result=3+f(2) =3+3=6
f(2)---result=2+f(1) =2+1=3
f(1)---result=1+f(0) =1+0=1
else                  ^
f(0)---result=0-------|


"""

