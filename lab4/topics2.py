#modules
#1
import aaa
aaa.greeting("Arsen")

#2
a=aaa.person["age"]
print(a)

#3
import aaa as bb
a=bb.person["age"]
print(a)

#4
from aaa import person
print(person["name"])

#datetime
import datetime
x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"), x.strftime("%d"), x.strftime("%B"))

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#math
import math
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x, y)

x = abs(-7.25)
print(x)
x = math.sqrt(64)
print(x)
x = math.ceil(1.4)
y = math.floor(1.4)
print(x, y)
x = math.pi
print(x)
x = pow(4, 3)
print(x)