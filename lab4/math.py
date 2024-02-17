import math
#1
x=int(input("degree: "))
y=float((x*math.pi)/180)
print(f"radian: {y:.6f}")

#2
x=int(input())
y=int(input())
z=int(input())
print(float((y+z)/2*x))

#3
s=int(input("number of sides: "))
l=int(input("the length of a side: "))
area=float((s*(l**2))/(4*math.tan(math.pi/s)))
print(f"area: {area:.3f}")

#4
b=int(input("Length of base:"))
h=int(input("Height of parallelogram:"))
print(b*h)