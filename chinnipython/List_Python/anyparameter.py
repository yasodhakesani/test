#anything you can send as parameter in the function

def fun(food):
    print(type(food))
    print(food)

fun(["idly","poori"])
fun(("x","y","z"))
fun({"a":1,"b":"john"})
fun({"as","in"})
fun("john")
fun(20)
fun(True)
fun(1)

#return values:
def func(x):
    return 5*x

print(func(5))