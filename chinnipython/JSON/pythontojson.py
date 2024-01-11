import json
x =  { "name":"John", "age":30, "city":"New York"}
z=json.dumps(x)
print(z)
print(type(z))

a=[10,2,31]
b=json.dumps(a)
print(b)
print(type(b))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
