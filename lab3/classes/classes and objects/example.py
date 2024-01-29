#1
class myclass:
    x=5
p1=myclass()
print(p1.x)

#2
class person:
    def __init__(x, name, age):
        x.name=name
        x.age=age
p1=person("Jhon", 36)
print(p1.name)
print(p1.age)

#3
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}[{self.age}]"
p1=person("Jhon", 36)
print(p1)

#4
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def func(self):
        print("Hello my name is " + self.name)
p1=person("Jhon", 36)
p1.func()

#5
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
p1.age=40
print(p1.age)
del p1.age
print(p1.age)
del p1
