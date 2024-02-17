#1
def fun(n):
    for i in range(n+1):
        yield i**2
n=int(input())
sq=fun(n)
for i in  sq:
    print(i)
    
#2
def fun2(m):
    for i in range(n):
        if i%2==0:
            yield i
n=int(input())
even=fun2(n)
for i in even:
    print(i, end=",")
print("\b")

#3
def fun3(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
m=int(input())
d=fun3(m)
for i in d:
    print(i)
    
#4
def fun4(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
po=fun4(a,b)
for i in po:
    print(i)
    
#5
def fun5(n):
    for i in range(n, 0, -1):
        yield i
w=int(input())
down=fun5(w)
for i in down:
    print(i)