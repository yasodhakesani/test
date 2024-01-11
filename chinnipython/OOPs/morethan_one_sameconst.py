class Person:
    def __init__(self):
        print("first constructor")
    def __init__(self):
        print("second constructor")   
st=Person()


"""The object st called the second constructor whereas both have the same configuration. The first method is not accessible by the st object. Internally, 
the object of the class will always call the last constructor if the class has multiple constructors."""