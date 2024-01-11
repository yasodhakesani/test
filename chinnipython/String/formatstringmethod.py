name="John"
age=36
print("My name is {} and my age is {}".format(name,age))
x="My name is {} and My age is {}"
print(x.format(name,age))
print(f"my name is {name} and my age is {age}")
print("My name is {0} and my age is {1}".format(name,age))
print("My name is {0} and my age is {1}".format("Radha",35))
print("My name is {} and my age is {}".format("Radha",35))
print("My name is {name} and my age is {age}".format(name="Raj",age=40))


x="ram"
y="sam"
z="{} and {} are brothers"
print("{1} and {0} are brothers".format(x,y) )
print(z.format(y,x))
print("{1} and {0} are big brothers".format("balu","bolu"))
print("{} and {} are big brothers".format("balu","bolu"))
print(f"{x} and {y} are big brothers")

