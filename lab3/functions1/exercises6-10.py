#6
def reverse(x):
    l=[]
    s = ''
    for j in range(len(x)):
            if x[j]!=' ':
                s+=x[j]
            else:
                l.append(s)
                s=''
    l.append(s)
    rev=' '.join(reversed(l))
    print(rev)
a=input()
reverse(a)

#7
def has(x):
    i=0
    while i<len(x)-1:
        if(x[i]==x[i+1]):
            print("True")
            return 0
        i+=1
    print("False")
has([1, 3, 3])
has([1, 3, 1, 3])
has([3, 1, 3])

#8
def order(x):
    o=0
    for i in range(len(x)):
        if(x[i]==7):
            for j in range(len(x)):
                if(x[j]==0):
                    if j<i:
                        o+=1
    if o>=2:
        print("True")
        return 0
    print("False")
order([1,2,4,0,0,7,5])
order([1,0,2,4,0,5,7])
order([1,7,2,0,4,5,0]) 

#9
def fun(x):
    b=(4/3)*(x**3)
    return b
n=int(input())
v=fun(n)
print(v,'*π')
#10
def fun(x):
    l=[]
    for i in x:
        if i not in l:
            l.append(i)
    return l
l=[1,2,2,3,3,1,4,5,5]
unique=fun(l)
print(unique)
