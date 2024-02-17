#json
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
#pase x
#1
y=json.loads(x)
print(y["age"])

#2
y=json.dumps(x)
print(y)

#3
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
print(json.dumps(x, indent=4))

#4
print(json.dumps(x, indent=4, sort_keys=True))
