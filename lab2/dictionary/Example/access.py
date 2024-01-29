thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print (x)
x = thisdict.get("model")
print (x)

#key
x = thisdict.keys()
print (x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
"""------"""
#values
x = thisdict.values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before
car["year"] = 2020
print(x) #after

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before
car["color"] = "red"
print(x) #after

#items
x = thisdict.items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")