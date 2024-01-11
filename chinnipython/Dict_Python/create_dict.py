#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
d={
    "name":"Raj",
    "age":38,
    "rollnum":1010
}
print(d)
print(type(d))
print(len(d))

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(len(myfamily))
print(type(myfamily))

d2=dict({"key1":"value1","key2":"value2"})
print(d2)
d5=dict(name="john",age=38,year="2023")
print(d5)
thisdict = {
  "brand": ("Ford","KIA"),
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)