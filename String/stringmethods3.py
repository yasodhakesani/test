"""partition Search for the word "apple", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match" 
"""
txt="i am eating apple a day"
print(txt.partition("apple"))


"""partition Search  for the last occurrence of a specified string "apple", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match" 
"""

txt="i am eating apple everyday and remain apple keep in frozen"
print(txt.rpartition("apple"))

#rsplit right split
#['apple, banana', 'cherry']

txt = "apple, banana, cherry"
y=txt.rsplit(",")
x = txt.rsplit(", ", 1)

print(x)
print(y)
#split seperate by give string as tuple and limiter if you give
txt = "apple, banana, cherry"
y=txt.split(",")
x = txt.split(", ", 1)

print(x)
print(y)

#splitlines split into list by  break
#breakline Specifies if the line breaks should be included (True), or not (False). Default value is False
txt = "Thank you for the music\nWelcome to the jungle"
a=txt.splitlines()
print(a)
a=txt.splitlines(True)
print(a)

#startswith(),startswith(value,start,end)
txt="Hello John"
print(txt.startswith("H"))

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)
print(x)

#swapecase convert upper lo lower and lower to upper case in give string
print(txt.swapcase())

#zfill fill the zero with until 10 characters long
#if the value of the parameter is less than length no fill will be done
value="380"
print(value.zfill(10))
print(value.zfill(3))