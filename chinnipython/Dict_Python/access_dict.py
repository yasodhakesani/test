thisdict1={"name": "sanvi",
           "age":29,
           "sname":"pidipatri"
    }
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict1["age"])
print(thisdict1.get("sname"))
x=thisdict1.copy()
print(thisdict1.setdefault("ram","god"))
print(thisdict1)
print(thisdict["brand"]) #Ford
print(thisdict.get("model")) #Mustang
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
print(x)
car["color"]="YOUKA"
print(x) #dict_keys(['brand', 'model', 'year', 'color'])

y=car.values()
print(y) #dict_values(['Ford', 'Mustang', 1964, 'YOUKA'])
car["year"]=2020
print(y) #dict_values(['Ford', 'Mustang', 2020, 'YOUKA'])

#items() method will return each item in a dictionary, as tuples in a list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


#fromkeys:
x = ('key1', 'key2', 'key3')
y = 0
    
thisdict = dict.fromkeys(x, y)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "Bronco")

print(x)
print(car)