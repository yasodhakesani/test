import random

print(random.randrange(2,10))
print(random.randrange(2,10,2))

mylist = ["apple", "banana", "cherry"]
#Returns a list with a random selection from the given sequence from choice
print(random.choices(mylist))
#Returns a random element from the given sequence
print(random.choice(mylist))

#Return random number between 0.0 and 1.0:
print(random.random())