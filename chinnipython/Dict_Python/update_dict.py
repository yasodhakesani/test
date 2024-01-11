#Update we can do using keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"]=2023
print(thisdict)

thisdict.update({"model":"Figo"})
print(thisdict)

#add new key,value to dict
thisdict["color"]="red"
print(thisdict)