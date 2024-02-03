import math
class point:
    def __init__(a, x, y):
        a.x=x
        a.y=y
    def print(a):
        print(f"{a.x}, {a.y}")
    def change(a):
        x2=int(input())
        y2=int(input())
        a.x=x2
        a.y=y2
    def dis(a, b):
        d=math.dist((a.x, a.y), (b.x, b.y))
        print(d)
        
p1=point(1, 1)
p2=point(2, 2)
p1.print()
p2.print()
p1.change()
p1.dis(p2)
