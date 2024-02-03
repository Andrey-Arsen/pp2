def prime(n):
    if n<2:
        return False
    for i in range(2, int(n)):
        if n%i==0:
            return False
    return True
num=[]
x=int(input())
for i in range(x):
    a=int(input())
    num.append(a)
p=list(filter(lambda a:prime(a), num))
print(p)
