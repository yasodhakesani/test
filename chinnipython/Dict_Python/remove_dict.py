d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d.pop("year")
print(d)
d.popitem() #will remove last inserted item (in version 3.7 before random item is removing instead)

print(d)

#del keyword removes the item with the specified key name:
#del keyword can also delete the dictionary completely:

d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del d1["year"]
del d1

#clear will empty the dictionary
d1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1.clear()
print(d1)