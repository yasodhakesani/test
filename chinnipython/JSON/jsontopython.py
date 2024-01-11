import json


x =  '{ "name":"John", "age":30, "city":"New York"}'

#convert json into python

y=json.loads(x)
print(type(x))
print(type(y))

a='{"a":"[10,20,20]"}'
print(type(a))
print(json.loads(a))
print(type(a))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(type(x))
a=json.dumps(x,indent=4)
print(a)
print(type(a))