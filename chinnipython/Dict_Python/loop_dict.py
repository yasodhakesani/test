thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#direct for loop return the key

for x in thisdict:
    print(x) #brand,model,year

#return the values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.keys():
    print("keys",x)
    print("values",thisdict[x])

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print(x,y)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print(id(thisdict))
print(id(mydict))

d=dict(thisdict)
