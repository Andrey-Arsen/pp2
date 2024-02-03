class Shape:
    def __init__ (x, length):
        x.len=length
    def area(x):
        S=x.len*x.len
        print(S)
    
        
class Square(Shape):
    def __init__(x, length):
        super().__init__(length)

x=int(input())
A=Square(x)
A.area()

    