#ex1
def ounces(x):
    a=float(x/28.3495231)
    print(a)
c=float(input())
ounces(c)
    
#ex2
def tem(x):
    c=float((5/9)*(x-32))
    print(c)
F=float(input())
tem(F)

#ex3
def num(heads, legs):
    r=int((legs-(2*heads))/2)
    c=heads-r
    print("chickens:", c)
    print("rabbits:", r)
head=int(input())
leg=int(input())
num(head, leg)

#ex4
def prime(n):
    if n<2:
        return False
    for i in range(2, int(n)):
        if n%i==0:
            return False
    return True
l=[]
for i in range(6):
    a=int(input())
    l.append(a)
for i in range(len(l)):
    if prime(i)==True:
        print(i, end=' ')
        
#5
from itertools import permutations
def per(string):
    l=[]
    for i in permutations(string):
        s=''
        for j in i:
            s+=j
        l.append(s)
    for i in range(len(l)):
        print(l[i])
a=input()
per(a)
