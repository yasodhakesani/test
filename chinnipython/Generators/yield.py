def smp():
    for i in range(5):
        return i
print(smp())


#yield can return one value at a time and remember the state of execution
def simple():
    for i in range(5):
        yield i


for i in simple():
    print(i)



    