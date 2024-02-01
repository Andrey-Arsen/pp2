#1
class person:
    def __init__(x, fname, lname) :
        x.first=fname
        x.last=lname
    def printname(x):
        print(x.first, x.last)
a=person("Jhon", "Doe")
a.printname()

#2
class person:
    def __init__(x,fanme, lname):
        x.first=fanme
        x.last=lname
    def print(x):
        print(x.last, x.first)
class student(person):
    def __init__(y,fname,lname):
        person.__init__(y,fname, lname)
a=student("Mika", "Olsen")
a.print()

#3
class Student(person):
    def __init__(x, fname, lname):
        super(). __init__(fname, lname)
        x.graduationyear=2027
a=Student("Arsen", "Andrey")
a.print()
print(a.graduationyear)

#4
class Student(person):
    def __init__(x, fname, lname, year):
        super(). __init__(fname, lname)
        x.graduationyear=year
a=Student("Arsen", "Andrey", 2027)
a.print()

#5
class firstclass:
    def __init__(x, fname, lname):
        x.first=fname
        x.second=lname
    def printname(x):
        print(x.first, x.second)

class secondclass(firstclass):
    def __init__(y, fname, lname, year):
        super().__init__(fname, lname)
        y.graduationyear=year
    def welcome(y):
        print("Welcome", y.first, y.second,
              "to the clas of", y.graduationyear)

a=secondclass("Arsen", "Andrey", 2027)
a.welcome()
                
