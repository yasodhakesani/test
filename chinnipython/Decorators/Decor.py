#In Decorators, functions are passed as an argument into another function and then called inside the wrapper function.
def dec(fun):
    def inner():
        print("wrapper function called")
        fun()
        print("after function execution")
    return inner

def function_used():
    print("original function")

dec(function_used)
    