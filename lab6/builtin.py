#1
def fun(l):
    n=1
    for i in l:
        n*=int(i)
    return n
x=list(input().split())
print(fun(x))

import string
#2
def fun2(s):
    n=0
    m=0
    for i in s:
        if i.isupper():
            n+=1
        elif i.islower():
            m+=1
    return n,m
x=input()
print(fun2(x))

#3
def fun3(s):
    r=s[::-1]
    if s==r:
        return True
    return False
x=input()
print(fun3(x))

#4
import math
import time
def fun4(x, t):
    time.sleep(t/1000.)
    return math.sqrt(x)
x=int(input())
t=int(input())
print(fun4(x,t))

#5
def fun5(x):
    return all(x)
t=(False, True, True, True)
print(fun5(t))



    
