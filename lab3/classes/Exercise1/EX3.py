class Shape:
    def __init__ (x, length):
        x.len=length
    def area(x):
        S=x.len*x.len
        print(S)

class Rectangle(Shape):
    def __init__(x, length, width):
        super().__init__(length)
        x.wid=width
    def area(x):
        print(x.len*x.wid)
a=int(input())
b=int(input())
r=Rectangle(a, b)
r.area()