#EX1
x=lambda a:a

#Example
#1
x=lambda a:a+10
print(x(5))

#2
x=lambda a,b,c : a+b+c
print(x(5,6,2))

#3
def func(n):
    return lambda a:a*n
mydoubler=func(2)
mytripler=func(3)

print(mydoubler(11))
print(mytripler(11))