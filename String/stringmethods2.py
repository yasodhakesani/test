#isalnum check given string is alpha numeric or not retur True/False
x="Company12"
print(x.isalnum())

#isalpha check aplhabet 
x="Hello"
print(x.isalpha())
#isascii check given string in ascii characters
x="A"
print(x.isascii())

#isdecimal
x="902"
print(x.isdecimal())
print(x.isdigit())

#isidentifier() return True if it contain alphanumeric or underscore(a-z,0-9,_)
#valid identifier cannot start with number or space
x="hshshj909_h"
print(x.isidentifier())

#islower() return True is str if all the chhars in lower case
x="RAJ"
print(x.islower())

#isprintable() will check if all the chars in string printale or not
print(x.isprintable())
#isspace() will check all are whitespace
x=" "
print(x.isspace())

#istiitle will check all the letters start will upper case and rest lower case
x="Hello Python"
print(x.istitle())

#ljust() left justified version
#ljust(20) left align the string by 20 character long space
#ljust(length,character)
x="john benner"
y=x.ljust(40)
print(y,"banana")
print(x.ljust(20, "O"))

#rjust() right justified version
#rjust(20) right aligh string by 20 chars long space
#rjust(length,character)
x="john benner"
y=x.rjust(40)
print(y,"banana")
print(x.rjust(20, "O"))


#lower() to conver string into lowercase
x="RASDJK dsd"
print(x.lower())

#lstrip() left whitespace trim
#rstrip() right whitespace trim
x="   baba  sdsd "
print(x.lstrip())
print(x.rstrip())
print(x.lstrip(),"hjds")
print(x.rstrip(),"hjds")

#maketrans() Create a mapping table, and use it in the translate() method to replace any character
#you have to give the mapping as str.maketrans("","") in equal length
#Then you can use for translate method x.translate()
x="Hello I as Sony"
y=str.maketrans("S", "I")
print(x.translate(y))

"""
Parameter	Description
x	        Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. 
            If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y	        Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
z	        Optional. A string describing which characters to remove from the original string.
"""
a="synoS"
b="majar"
c="I"


p=str.maketrans(a,b,c)
print(x.translate(p))
